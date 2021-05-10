
import socket
import sys

import click
import click_aliases  # type: ignore

from nmpvc.base import MPV

from . import _Cache, Cache


@click.group('pl', cls=click_aliases.ClickAliasedGroup, chain=True)
@click.option('-s', '--server', metavar="<server>", multiple=True,
              help="shomeserver host [multiple: True]")
@click.option('-p', '--port', metavar="<port>", type=int, default=50870, show_default=True,
              help="shomeserver port")
@click.pass_context
def cli_pl(ctx, server: tuple[str], port: int):
    """ Playlist Handler """
    if not ctx.obj:
        ctx.obj = Cache

    ctx.obj.logger.name = 'pl'

    try:
        ctx.obj.pl.mpv = MPV(*[(_host, port) for _host in server])
    except socket.gaierror as ex:
        ctx.obj.logger.error(f"{ex}")
        sys.exit(1)


@cli_pl.command('append')
@click.pass_obj
def pl_append(obj: _Cache):
    """ Append/Add new file """
    #ctx.obj.logger.name = 'append'
    if not isinstance(obj.pl.mpv, MPV):
        raise TypeError(f"expect {type(MPV)} for 'obj.smb', got {type(obj.pl.mpv)}")

    ...
