""" Control RGBW stripes with 'pigpio' over GPIO pins """

import json
import socket

import requests

from helper.config import c

from shomeserver import PluginError


if 'plugin@pi_rgb' not in c.main.sections():
    c.read(__file__.rsplit('/', 1)[0] + '/config.ini')

try:
    r = c.db.get('/label', name="pi_rgb", group="config")
except requests.exceptions.ConnectionError as ex:
    raise PluginError(f"{ex!r}")

if 'json' in r.headers.get('Content-Type') and r:
    c.read_dict(json.loads(r.text), namespace='pi_rgb')
else:
    raise PluginError(f"{r!r}, {r.text}")

if socket.gethostname() not in c.pi_rgb.sections():
    raise PluginError(f"no config for {socket.gethostname()}")

from .route import api_blueprint

__all__ = ['api_blueprint']
