"""Isolated public ZIP tests; existing CLI tests use synthetic injected transports."""
import importlib.util
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('plugin_packager', ROOT / 'scripts/package_plugin.py')
tool = importlib.util.module_from_spec(spec);spec.loader.exec_module(tool)


class PackageTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory();self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name);self.zip = self.root / 'plugin.zip'

    def command(self, *arguments, cwd=None):
        environment = {key: value for key, value in os.environ.items() if key.upper() in
            {'PATH', 'SYSTEMROOT', 'WINDIR', 'TEMP', 'TMP', 'USERPROFILE', 'HOME', 'APPDATA', 'LOCALAPPDATA', 'COMSPEC', 'PATHEXT', 'PROGRAMFILES'}}
        return subprocess.run([sys.executable, '-s', '-E', '-B', *map(str, arguments)], cwd=cwd or self.root,
            env=environment, capture_output=True, text=True, timeout=90, shell=False)

    def test_deterministic_zip_extracts_without_app_or_private_skill(self):
        preview = tool.package();self.assertFalse(preview['writes']);self.assertFalse(self.zip.exists())
        result = tool.package(output=self.zip);self.assertEqual(preview['sha256'], result['sha256'])
        with zipfile.ZipFile(self.zip) as archive:
            self.assertEqual(set(archive.namelist()), {'houston-i-love-kroger-plugin/' + name for name in tool.FILES})
            self.assertNotIn('houston-i-love-kroger-plugin/.gitignore', archive.namelist())
            archive.extractall(self.root / 'extracted')
        plugin = self.root / 'extracted/houston-i-love-kroger-plugin';skill = plugin / 'skills/houston-i-love-kroger'
        self.assertFalse((plugin / 'package.json').exists());self.assertFalse((plugin / 'skills/kroger-api').exists())
        manifest = json.loads((plugin / '.codex-plugin/plugin.json').read_text())
        self.assertEqual(manifest['skills'], './skills/');self.assertTrue((plugin / manifest['skills'] / 'houston-i-love-kroger/SKILL.md').is_file())
        for script in ('shopping.py', 'promotions.py'):
            check = self.command(skill / 'scripts' / script, '--help');self.assertEqual(check.returncode, 0, check.stderr)
        for script, args in (('shopping.py', ['products', '--store', 'TEST0001', '--term', 'apples']),
                ('promotions.py', ['latest', '--store', 'TEST0001', '--topic', 'milk'])):
            check = self.command(skill / 'scripts' / script, *args, '--summary-only', '--dry-run', '--json', '--no-input')
            self.assertEqual(check.returncode, 0, check.stderr);payload = json.loads(check.stdout)
            self.assertTrue(payload['ok']);self.assertEqual(payload['status'], 'preview')
            self.assertFalse(payload['network']);self.assertFalse(payload['writes'])
        check = self.command(skill / 'scripts/refresh_docs.py', '--check', '--json', '--no-input')
        self.assertEqual(check.returncode, 0, check.stderr);self.assertEqual(json.loads(check.stdout)['result']['counts']['saved'], 6)
        check = self.command(skill / 'scripts/refresh_docs.py', '--refresh', '--json', '--no-input')
        self.assertEqual(check.returncode, 2);self.assertEqual(json.loads(check.stdout)['error']['code'], 'repository_required')
        check = self.command('-m', 'unittest', 'discover', '-s', skill / 'tests', cwd=plugin)
        self.assertEqual(check.returncode, 0, check.stdout + check.stderr)

    def test_unknown_private_canaries_are_never_packaged(self):
        plugin = self.root / 'plugin'
        canary = b'private-fixture-' + os.urandom(16)
        for name in tool.FILES:
            target = plugin / name;target.parent.mkdir(parents=True, exist_ok=True);shutil.copyfile(ROOT / name, target)
        for name in ('.env', 'skills/kroger-api/SKILL.md', 'skills/houston-i-love-kroger/references/project-record.md',
                'skills/houston-i-love-kroger/research/sources/capture.txt'):
            target = plugin / name;target.parent.mkdir(parents=True, exist_ok=True);target.write_bytes(canary)
        tool.package(plugin, self.zip)
        with zipfile.ZipFile(self.zip) as archive:
            self.assertTrue(all(canary not in archive.read(name) for name in archive.namelist()))

    def test_existing_output_missing_input_and_hardlinks_are_refused(self):
        self.zip.write_bytes(b'keep existing artifact')
        with self.assertRaises(tool.PackageError):tool.package(output=self.zip)
        self.assertEqual(self.zip.read_bytes(), b'keep existing artifact')
        with self.assertRaises(tool.PackageError):tool.package(self.root / 'missing')
        plugin = self.root / 'linked';plugin.mkdir()
        target = plugin / tool.FILES[0];target.parent.mkdir(parents=True, exist_ok=True)
        source = self.root / 'ordinary';source.write_bytes(b'synthetic linked file');os.link(source, target)
        with self.assertRaises(tool.PackageError) as caught:tool.package(plugin)
        self.assertEqual(caught.exception.code, 'linked_path')


if __name__ == '__main__':unittest.main()
