
import json
import socket

import requests

from helper.config import c

from shomeserver import PluginError


if 'plugin@pi_pir_motion' not in c.main.sections():
    c.read(__file__.rsplit('/', 1)[0] + '/config.ini')

try:
    r = c.db.get('/label', name='pi_pir_motion', group='config')
except requests.exceptions.ConnectionError as ex:
    raise PluginError(f"{ex!r}")

if 'json' in r.headers.get('Content-Type') and r:
    c.read_dict(json.loads(r.text), namespace='pi_pir_motion')
else:
    c.read_dict({}, namespace='pi_pir_motion')

# start process here
if socket.gethostname() not in c.pi_pir_motion.sections():
    raise PluginError(f"{socket.gethostname()!r} not in config!")

from .main import Motion

if not Motion.P.is_alive():
    Motion().start()
else:
    raise PluginError("Process already running")
