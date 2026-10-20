#!/usr/bin/env python3
"""Preview or create the complete standalone plugin ZIP from a public allowlist."""
import argparse
import hashlib
import io
import json
import os
from pathlib import Path
import stat
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[1]
FILES = (
    '.codex-plugin/plugin.json',
    'LICENSE',
    'README.md',
    'THIRD_PARTY_NOTICES.md',
    'config/connection.example.json',
    'scripts/package_plugin.py',
    'skills/houston-i-love-kroger/SKILL.md',
    'skills/houston-i-love-kroger/evals/scenarios.json',
    'skills/houston-i-love-kroger/playbooks/choose-store-and-topic.md',
    'skills/houston-i-love-kroger/playbooks/live-shopping.md',
    'skills/houston-i-love-kroger/playbooks/main-procedure.md',
    'skills/houston-i-love-kroger/playbooks/price-check-and-estimate.md',
    'skills/houston-i-love-kroger/playbooks/setup-and-recovery.md',
    'skills/houston-i-love-kroger/playbooks/stored-promotions.md',
    'skills/houston-i-love-kroger/references/api_reference.md',
    'skills/houston-i-love-kroger/references/source-permissions.md',
    'skills/houston-i-love-kroger/references/user-guide.md',
    'skills/houston-i-love-kroger/research/official_docs/exclusions.json',
    'skills/houston-i-love-kroger/research/official_docs/manifest.json',
    'skills/houston-i-love-kroger/research/official_docs/pages/API.md',
    'skills/houston-i-love-kroger/research/official_docs/pages/HISTORY.md',
    'skills/houston-i-love-kroger/research/official_docs/pages/KROGER_PERMISSION_REQUEST.md',
    'skills/houston-i-love-kroger/research/official_docs/pages/PROMOTION_SERVICE.md',
    'skills/houston-i-love-kroger/research/official_docs/pages/SELF_HOSTING.md',
    'skills/houston-i-love-kroger/research/official_docs/pages/USER_GUIDE.md',
    'skills/houston-i-love-kroger/research/research-brief.md',
    'skills/houston-i-love-kroger/research/source-inventory.json',
    'skills/houston-i-love-kroger/schemas/command-rules.md',
    'skills/houston-i-love-kroger/schemas/output-contract.md',
    'skills/houston-i-love-kroger/scripts/README.md',
    'skills/houston-i-love-kroger/scripts/_docs.py',
    'skills/houston-i-love-kroger/scripts/fetch_docs.py',
    'skills/houston-i-love-kroger/scripts/list_skill_steps.py',
    'skills/houston-i-love-kroger/scripts/promotions.py',
    'skills/houston-i-love-kroger/scripts/refresh_docs.py',
    'skills/houston-i-love-kroger/scripts/shopping.py',
    'skills/houston-i-love-kroger/skill-ci/README.md',
    'skills/houston-i-love-kroger/skill-ci/skill-design.md',
    'skills/houston-i-love-kroger/tests/test_discovery.py',
    'skills/houston-i-love-kroger/tests/test_documentation_tools.py',
    'skills/houston-i-love-kroger/tests/test_promotions.py',
    'skills/houston-i-love-kroger/tests/test_shopping.py',
    'skills/houston-i-love-kroger/tests/test_shopping_aliases.py',
    'skills/houston-i-love-kroger/vocabulary.yaml',
    'tests/test_package.py',
)


class PackageError(Exception):
    def __init__(self, code, message, recovery):
        self.code, self.message, self.recovery = code, message, recovery
        super().__init__(message)


def plain(path):
    for current in (path, *path.parents):
        if current.exists() or current.is_symlink():
            info = current.lstat()
            if stat.S_ISLNK(info.st_mode) or getattr(info, 'st_file_attributes', 0) & 0x400 or \
                    stat.S_ISREG(info.st_mode) and info.st_nlink != 1:
                raise PackageError('linked_path', 'A selected path uses a link or junction.', 'Use ordinary plugin files and an ordinary output directory.')


def package(root=ROOT, output=None, dry_run=False):
    root = Path(root).absolute();plain(root)
    if not FILES or len(FILES) != len(set(FILES)):
        raise PackageError('invalid_inventory', 'The public inventory is incomplete or duplicated.', 'Restore the reviewed package builder.')
    entries = [];total = 0
    for name in FILES:
        relative = Path(name)
        if relative.is_absolute() or '..' in relative.parts or '\\' in name:
            raise PackageError('invalid_inventory', 'A package entry leaves the plugin.', 'Restore the reviewed public inventory.')
        path = root / relative;plain(path)
        if not path.is_file() or not 1 <= path.stat().st_size <= 1_000_000:
            raise PackageError('missing_file', 'A required public plugin file is absent, empty or oversized.', 'Restore the complete reviewed plugin before packaging.')
        raw = path.read_bytes();total += len(raw)
        if total > 4_000_000:
            raise PackageError('package_too_large', 'The public plugin exceeds the package limit.', 'Review its allowlist and intended source files.')
        entries.append((name, raw))
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, 'w', compression=zipfile.ZIP_STORED) as archive:
        for name, raw in sorted(entries):
            entry = zipfile.ZipInfo('houston-i-love-kroger-plugin/' + name, date_time=(1980, 1, 1, 0, 0, 0))
            entry.create_system = 3;entry.external_attr = (stat.S_IFREG | 0o644) << 16
            archive.writestr(entry, raw)
    content = buffer.getvalue();fingerprint = hashlib.sha256(content).hexdigest()
    writes = output is not None and not dry_run
    if output is not None:
        target = Path(output).expanduser().absolute();plain(target)
        if target.suffix.lower() != '.zip' or not target.parent.is_dir():
            raise PackageError('invalid_output', 'The output must be a ZIP in an existing directory.', 'Supply --output PATH_TO_NEW_ZIP with a .zip ending.')
        if target.exists():
            raise PackageError('output_exists', 'The requested ZIP already exists.', 'Keep the existing artifact and choose a new output filename.')
        if writes:
            with target.open('xb') as stream:
                stream.write(content);stream.flush();os.fsync(stream.fileno())
            if hashlib.sha256(target.read_bytes()).hexdigest() != fingerprint:
                raise PackageError('write_unverified', 'The new ZIP could not be verified.', 'Preserve it for inspection; do not overwrite or publish it.')
    return {'ok': True, 'status': 'created' if writes else 'preview', 'files': len(entries), 'sourceBytes': total,
            'archiveBytes': len(content), 'sha256': fingerprint, 'writes': writes, 'networkRequests': 0}


class Parser(argparse.ArgumentParser):
    def error(self, _message):
        raise PackageError('invalid_arguments', 'The command arguments are unsupported.', 'Run package_plugin.py --help for supported flags and examples.')


def main(arguments=None):
    parser = Parser(description=__doc__, allow_abbrev=False, epilog='Examples: package_plugin.py --json; package_plugin.py --output plugin.zip --dry-run --json; package_plugin.py --output plugin.zip --json --no-input')
    parser.add_argument('--output', help='New .zip filename; omit to preview without writing.')
    parser.add_argument('-n', '--dry-run', action='store_true', help='Validate and preview without writing.')
    for flag in ('--json', '--no-input', '--no-color', '--quiet', '--verbose'):parser.add_argument(flag, action='store_true')
    supplied = list(sys.argv[1:] if arguments is None else arguments);machine = '--json' in supplied
    try:
        args = parser.parse_args(supplied)
        if sys.stdout.isatty() and not (args.json or args.quiet):print('Package Houston I Love Kroger — public files only')
        result = package(output=args.output, dry_run=args.dry_run);code = 0
        if args.verbose:result['entries'] = list(FILES)
    except PackageError as error:
        result = {'ok': False, 'error': {'code': error.code, 'message': error.message, 'recovery': error.recovery}};code = 2
    except (OSError, ValueError, zipfile.BadZipFile, KeyboardInterrupt):
        result = {'ok': False, 'error': {'code': 'package_io', 'message': 'The package could not be completed.',
            'recovery': 'Check ordinary file permissions. Preserve any partial output and choose a new target.'}};code = 1
    try:
        if machine:print(json.dumps(result, allow_nan=False))
        elif result['ok']:print(f"{result['status'].capitalize()}: {result['files']} public files; SHA256 {result['sha256']}")
        else:print(f"Error: {result['error']['message']}\nFix: {result['error']['recovery']}", file=sys.stderr)
    except BrokenPipeError:return 1
    return code


if __name__ == '__main__':raise SystemExit(main())
