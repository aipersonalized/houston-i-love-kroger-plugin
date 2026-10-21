"""Connection and no-web-handoff regressions using only synthetic fixtures."""
import contextlib
import importlib
import io
import json
import os
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
connection = importlib.import_module('service_connection')
shopping = importlib.import_module('shopping')
promotions = importlib.import_module('promotions')
sys.path.pop(0)


class ServiceConnectionTests(unittest.TestCase):
    def test_complete_skill_has_a_real_shared_service_default(self):
        with patch.dict(os.environ, {}, clear=True):
            self.assertEqual(connection.resolve_service_url(),
                             'https://aipersonalized.io/api/houston-i-love-kroger/')
        self.assertNotIn('/apps/', connection.CONFIG_FILE.read_text())

    def test_explicit_then_service_environment_override_and_no_old_app_alias(self):
        with patch.dict(os.environ, {'HOUSTON_SERVICE_URL': 'https://service.example/',
                                     'HOUSTON_APP_URL': 'https://web.example/'}, clear=True):
            self.assertEqual(connection.resolve_service_url('https://explicit.example/'), 'https://explicit.example/')
            self.assertEqual(connection.resolve_service_url(), 'https://service.example/')
        with patch.dict(os.environ, {'HOUSTON_APP_URL': 'https://web.example/'}, clear=True):
            self.assertEqual(connection.resolve_service_url(),
                             'https://aipersonalized.io/api/houston-i-love-kroger/')

    def test_missing_or_malformed_config_is_bounded_and_fails_before_network(self):
        canary = 'private-fixture-value-must-not-leak'
        with tempfile.TemporaryDirectory() as folder:
            target = Path(folder) / 'connection.json'
            for value in (None, canary, '{"apiVersion":1,"apiVersion":1,"serviceBaseUrl":"https://test.example/"}',
                          '{"apiVersion":true,"serviceBaseUrl":"https://test.example/"}',
                          '{"apiVersion":1,"serviceBaseUrl":"https://test.example/","private":"' + canary + '"}'):
                if value is not None:
                    target.write_text(value)
                with patch.dict(os.environ, {}, clear=True), patch.object(connection, 'CONFIG_FILE', target):
                    for client in (shopping, promotions):
                        output = io.StringIO()
                        with patch.object(client, 'request', side_effect=AssertionError('network forbidden')), contextlib.redirect_stdout(output):
                            code = client.main(['status', '--json', '--no-input'])
                        self.assertEqual(code, 3)
                        payload = json.loads(output.getvalue())
                        self.assertEqual(payload['error']['code'], 'service_configuration_invalid')
                        self.assertNotIn(canary, output.getvalue())

    def test_default_connection_is_consumed_by_both_tools_without_shopper_url(self):
        with patch.dict(os.environ, {}, clear=True):
            for client in (shopping, promotions):
                with patch.object(client, 'request', return_value={}) as request, \
                        patch.object(client, 'result_for', return_value=({'ok': True}, 0)):
                    client.run(client.parser().parse_args(['status']))
                    self.assertEqual(request.call_args.args[:2],
                                     ('https://aipersonalized.io/api/houston-i-love-kroger/', 'status'))

    def test_input_errors_emit_one_json_object_without_values(self):
        for client in (shopping, promotions):
            for arguments in (['status', '--timeout', 'private-canary', '--json', '--no-input'],
                              ['status', '--unknown-private-canary', '--json', '--no-input']):
                output, errors = io.StringIO(), io.StringIO()
                with contextlib.redirect_stdout(output), contextlib.redirect_stderr(errors):
                    code = client.main(arguments)
                self.assertEqual(code, 2)
                self.assertEqual(json.loads(output.getvalue())['error']['code'], 'invalid_input')
                self.assertEqual(errors.getvalue(), '')
                self.assertNotIn('private-canary', output.getvalue())


if __name__ == '__main__':
    unittest.main()
