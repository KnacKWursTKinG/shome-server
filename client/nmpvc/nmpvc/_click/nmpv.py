
import sys
import socket

import click

from . import Cache
from .help import cli_help
from .pl import cli_pl
from .smb import cli_smb

from nmpvc.base import MPV


@click.group()
@click.option('--debug', is_flag=True, default=False, help="enable debug messages")
@click.option('-s', '--server', metavar="<server>", multiple=True,
              help="shomeserver host [multiple: True]")
@click.option('-p', '--port', metavar="<port>", type=int, default=50870, show_default=True,
              help="shomeserver port")
@click.pass_context
def cli(ctx, server: tuple[str], port: int, debug: bool):
    """ Network MPV Client """
    if not ctx.obj:
        ctx.obj = Cache

    if debug:
        ctx.obj.logger.level = 'debug'

    ctx.obj.logger.name = 'nmpvc'

    try:
        ctx.obj.pl.mpv = MPV(*[(_host, port) for _host in server])
    except socket.gaierror as ex:
        ctx.obj.logger.error(f"{ex}")
        sys.exit(1)


cli.add_command(cli_help)
cli.add_command(cli_pl)
cli.add_command(cli_smb)
