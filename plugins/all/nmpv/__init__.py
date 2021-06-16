""" simple mpv plugin to access 'jaseg/python-mpv' from the network

Github: 'https://github.com/jaseg/python-mpv'
"""

import requests
import json

from kwking_helper.config import c  # type: ignore

from shomeserver import PluginError

if 'plugin@nmpv' not in c.main.sections():
    # load default/fallback config
    c.read(__file__.rsplit('/', 1)[0] + '/config.ini')

try:
    r = c.db.get('config', 'nmpv')
except requests.exceptions.ConnectionError as ex:
    raise PluginError(f"{ex!r}")

if 'data/bytes' in r.headers.get('Content-Type') and r:
    c.read_dict(json.loads(r.text), namespace='nmpv')
else:
    raise PluginError(f"{r!r}, {r.text}")

from .route import api_blueprint

__all__ = ['api_blueprint']
