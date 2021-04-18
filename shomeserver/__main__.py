
import os
import sys

import click

from kwking_helper import c, ClickLogger

_path = os.path.abspath(__file__).split('/', 2)[0]
sys.path.insert(0, _path)
import shomeserver  # NOTE: this will load the configuration


@click.command()
@click.option('--host', type=str, default='0.0.0.0', show_default=True)
@click.option('--port', type=int, default=c.main.get('shomeserver', 'port'), show_default=True)
@click.option('--log-level', type=click.Choice(ClickLogger.LEVELS),
              default=c.main.get('shomeserver', 'log_level'))
def cli(**kwargs):
    """ DBServer for storing data for network. """
    c.main.set('shomeserver', 'log_level', kwargs['log_level'])

    from shomeserver.server import server
    sys.path.remove(_path)

    server.run(
        host=kwargs['host'],
        port=kwargs['port']
    )


cli()
