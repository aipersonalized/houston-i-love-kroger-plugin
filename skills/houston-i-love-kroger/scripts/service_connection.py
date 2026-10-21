"""Resolve the companion's shared-service connection without a web app install.

The complete skill carries a public default. Operators can explicitly select a
different service with --base-url or HOUSTON_SERVICE_URL. No credentials belong
in this file, the bundled configuration, or command arguments.
"""
from __future__ import annotations

import json
import os
from pathlib import Path

SERVICE_NAME = 'houston-i-love-kroger-shopping'
CONFIG_FILE = Path(__file__).resolve().parents[1] / 'config' / 'connection.json'


class ConnectionError(Exception):
    """A fixed connection error; never includes the supplied configuration."""


def _unique(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError()
        result[key] = value
    return result


def resolve_service_url(explicit=None):
    """Select CLI, environment or the bundled public service, in that order.

    The caller validates the URL transport/path policy. An explicit empty value
    is an error rather than permission to silently use a different installation.
    """
    if explicit is not None:
        selected = explicit
    elif 'HOUSTON_SERVICE_URL' in os.environ:
        selected = os.environ['HOUSTON_SERVICE_URL']
    else:
        try:
            if CONFIG_FILE.stat().st_size > 4096:
                raise ValueError()
            value = json.loads(CONFIG_FILE.read_text(encoding='utf-8'), object_pairs_hook=_unique)
            if (not isinstance(value, dict) or set(value) != {'apiVersion', 'serviceBaseUrl'} or
                    type(value['apiVersion']) is not int or value['apiVersion'] != 1):
                raise ValueError()
            selected = value['serviceBaseUrl']
        except (OSError, ValueError, UnicodeError, RecursionError):
            raise ConnectionError('The shared-service configuration is missing or invalid. Restore the complete plugin or ask its operator to configure the service connection.') from None
    if not isinstance(selected, str) or not selected or len(selected) > 2048:
        raise ConnectionError('The shared-service address is missing or invalid. Ask its operator to check HOUSTON_SERVICE_URL or the explicit service override.')
    return selected
