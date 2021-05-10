
import json
import os

from kwking_helper import rq
from kwking_helper.config import c
from kwking_helper.thread import threaded2


path = {
    'Linux': {
        'config': os.path.expanduser('~/.config/pirgb'),
        'cache': os.path.expanduser('~/.cache/pirgb')
    },
    'ubuntu-phablet': {
        'config': os.path.expanduser('~/.config/pirgb.knackwurstking'),
        'cache': os.path.expanduser('~/.cache/pirgb.knackwurstking')
    }
}


def platform():
    platform = None
    sysname, nodename, _, _, _ = os.uname()

    if nodename == 'ubuntu-phablet':
        platform = nodename
    elif sysname == 'Linux':
        platform = sysname

    return platform


if platform() == 'ubuntu-phablet':
    default_config_path = os.path.abspath(__file__).rsplit('/', 2)[0] + '/config.ini'
else:
    default_config_path = os.path.abspath(__file__).rsplit('/', 1)[0] + '/config.ini'

c.read([
    default_config_path,
    path[platform()]['config'] + '/config.ini'
])


@threaded2(daemon=True)
def load_from_db():
    if not c.main.getboolean('pirgb', 'use_db_config'):
        return

    if not c.db:
        c.db = rq.DBServer(
            c.main.get('dbserver', 'credentials'),
            c.main.get('dbserver', 'host'),
            c.main.getint('dbserver', 'port')
        )

    if c.db:
        r = c.db.get('config', 'pi_rgb')

        if r:
            c.read_dict(json.loads(r.text), 'pi_rgb')

    if 'pi_rgb' not in dir(c):
        c.read_dict({}, 'pi_rgb')
