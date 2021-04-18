
import json
import socket

import requests

from kwking_helper import c

from shomeserver import PluginError


if 'plugin@pi_pir_motion' not in c.main.sections():
    c.read(__file__.rsplit('/', 1)[0] + '/config.ini')

try:
    r = c.db.get('config', 'pi_pir_motion')
except requests.exceptions.ConnectionError as ex:
    raise PluginError(f"{ex!r}")

if 'data/bytes' in r.headers.get('Content-Type') and r:
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
