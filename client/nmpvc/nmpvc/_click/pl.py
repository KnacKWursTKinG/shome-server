
import socket
import sys
import pprint

import click

from nmpvc.base import MPV

from . import _Cache, _SMB, Cache


@click.command('on-success')
@click.option('--echo', is_flag=True, default=False, help="print server return")
@click.pass_obj
def on_success(obj: _Cache, **kwargs):
    """ @todo ... """
    to_delete = list()

    obj.logger.debug(f"{pprint.pformat(obj.pl.td)}", name='on-success')

    for part in obj.pl.td:
        for server, data in part:
            if not isinstance(data, Exception):
                to_delete.append(part)

                if kwargs['echo'] and data is not None:
                    obj.logger.info(f"{pprint.pformat(data)}", name=server)

    for part in to_delete:
        obj.pl.td.remove(part)


@click.command('on-error')
@click.option('--echo', is_flag=True, default=False, help="print exception")
@click.option('--exit', is_flag=True, default=False, help="exit if error")
@click.pass_obj
def on_error(obj: _Cache, **kwargs):
    """ @todo ... """
    to_delete = list()

    obj.logger.debug(f"{pprint.pformat(obj.pl.td)}", name='on-error')

    for part in obj.pl.td:
        for server, data in part:
            if isinstance(data, Exception):
                to_delete.append(part)

                if kwargs['echo']:
                    obj.logger.error(f"{data!r}", name=server)

                if kwargs['exit']:
                    sys.exit(1)

    for part in to_delete:
        obj.pl.td.remove(part)


@click.group('append', invoke_without_command=True, chain=True)
@click.option('-s', '--server', metavar="<server>", multiple=True,
              help="shomeserver host [multiple: True]")
@click.option('-p', '--port', metavar="<port>", type=int, default=50870, show_default=True,
              help="shomeserver port")
@click.pass_obj
def smb_append(obj: _Cache, server: tuple[str], port: int):
    """ Append/Add new file """
    if not isinstance(obj.smb, _SMB):
        raise TypeError(f"expect {type(_SMB)} for 'obj.smb', got {type(obj.smb)}")

    if not isinstance(obj.pl.mpv, MPV):
        try:
            obj.pl.mpv = MPV(*[(_host, port) for _host in server])
        except socket.gaierror as ex:
            obj.logger.error(f"{ex}", 'smb append')
            sys.exit(1)

    while (file := obj.smb.files.pop(0) if obj.smb.files else None):
        obj.pl.td.append(
            obj.pl.mpv.run('playlist_append', file)
        )


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

    try:
        ctx.obj.pl.mpv = MPV(*[(_host, port) for _host in server])
    except socket.gaierror as ex:
        ctx.obj.logger.error(f"{ex}", 'pl')
        sys.exit(1)
