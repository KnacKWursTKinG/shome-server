
import socket
import sys

import click

from nmpvc.base import MPV

from . import _Cache, _SMB, Cache


@click.command('on-success')
@click.pass_obj
def on_success(obj: _Cache):
    """ @todo ... """
    ...


@click.command('on-error')
@click.pass_obj
def on_error(obj: _Cache):
    """ @todo ... """
    ...


@click.group('append', invoke_without_command=True, chain=True)
@click.option('-s', '--server', metavar="<server>", multiple=True,
              help="shomeserver host [multiple: True]")
@click.option('-p', '--port', metavar="<port>", type=int, default=50870, show_default=True,
              help="shomeserver port")
@click.pass_obj
def smb_append(obj: _Cache, server: tuple[str], port: int):
    """ Append/Add new file """
    obj.logger.name = 'append'

    if not isinstance(obj.smb, _SMB):
        raise TypeError(f"expect {type(_SMB)} for 'obj.smb', got {type(obj.smb)}")

    if not isinstance(obj.pl.mpv, MPV):
        try:
            obj.pl.mpv = MPV(*[(_host, port) for _host in server])
        except socket.gaierror as ex:
            obj.logger.error(f"{ex}")
            sys.exit(1)

    while (file := obj.smb.files.pop(0) if obj.smb.files else None):
        obj.pl.td.append(
            obj.pl.mpv.run('playlist_append', file)
        )

        # @todo: remove (on-error command used instead)
        #for _host, _data in obj.pl.mpv.run('playlist_append', file):
        #    if isinstance(_data, Exception):
        #        obj.logger.name = _host
        #        obj.logger.error(f"{_data!r}")
        #        sys.exit(1)


smb_append.add_command(on_success)
smb_append.add_command(on_error)


@click.group('pl', chain=True)
@click.option('-s', '--server', metavar="<server>", multiple=True,
              help="shomeserver host [multiple: True]")
@click.option('-p', '--port', metavar="<port>", type=int, default=50870, show_default=True,
              help="shomeserver port")
@click.pass_context
def pl(ctx, server: tuple[str], port: int):
    """ Playlist Handler """
    if not ctx.obj:
        ctx.obj = Cache

    ctx.obj.logger.name = 'pl'

    try:
        ctx.obj.pl.mpv = MPV(*[(_host, port) for _host in server])
    except socket.gaierror as ex:
        ctx.obj.logger.error(f"{ex}")
        sys.exit(1)
