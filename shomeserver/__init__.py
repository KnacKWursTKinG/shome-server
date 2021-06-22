
import json
import os

from helper import rq
from helper.config import c


class PluginError(Exception):
    pass


# load config files (local and dbserver stuff)
c.read([
    __file__.rsplit('/', 1)[0] + '/config.ini',
    os.path.expanduser('~/.config/shomeserver/config.ini')
])

# load config from dbserver if available (store in c.main)
c.db = rq.DBServer(
    c.main.get('dbserver', 'host'),
    c.main.getint('dbserver', 'port')
)

r = c.db.get('/label', name="shomeserver", group="config")

if r:
    c.read_dict(json.loads(r.text))
