
import socket
import json
import sys

import click

from pygments import highlight  # type: ignore
from pygments.lexers import JsonLexer  # type: ignore
from pygments.formatters import TerminalFormatter  # type: ignore

from nmpvc.base import MPV
from nmpvc._click._thread import on_success, on_error

from . import _Cache, _SMB, Cache


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


@pl.command('list')
@click.option('-l', '--length', is_flag=True, default=False, help="only print list length")
@click.pass_obj
def pl_list(obj: _Cache, length: bool):
    """ show playlist """
    _error = False

    for server, data in obj.pl.mpv.get('playlist'):
        if isinstance(data, Exception):
            obj.logger.error(f"{data!r}", name=server)
            _error = True

        elif data is not None:
            if length:
                obj.logger.info(f"{len(data)}", name=server)

            else:
                message = highlight(
                    json.dumps(data, indent=2),
                    JsonLexer(), TerminalFormatter()
                )

                obj.logger.info(f"\n{message}", name=server)


    if _error:
        sys.exit(1)


@pl.command('append')
@click.argument('file', type=click.Path())
@click.pass_obj
def pl_append(obj: _Cache, file: str):
    """ append a file to playlist """
    _error = False

    for server, data in obj.pl.mpv.run('playlist_append', file):
        if isinstance(data, Exception):
            obj.logger.error(f"{data!r}", name=server)
            _error = True

    if _error:
        sys.exit(1)


@pl.command('remove')
@click.option('-i', '--index', type=int,
              help="remove from playlist [default: 'current']")
@click.pass_obj
def pl_remove(obj: _Cache, index):
    """ remove from playlist """
    _error = False

    for server, data in obj.pl.mpv.run('playlist_remove', index or 'current'):
        if isinstance(data, Exception):
            obj.logger.error(f"{data!r}", name=server)
            _error = True

    if _error:
        sys.exit(1)


@pl.command('pos')
@click.option('-i', '--index', type=int, default=None, show_default=True,
              help="change playlist position")
@click.pass_obj
def pl_pos(obj: _Cache, index: int):
    """ current playlist position """
    _error = False

    if index:
        for server, data in obj.pl.mpv.set('playlist_pos', index):
            if isinstance(data, Exception):
                obj.logger.error(f"{data!r}", name=server)
                _error = True

    else:
        for server, data in obj.pl.mpv.get('playlist_pos'):
            if isinstance(data, Exception):
                obj.logger.error(f"{data!r}", name=server)
                _error = True

            elif data is not None:
                obj.logger.info(f"{data!r}", name=server)

    if _error:
        sys.exit(1)


@pl.command('pause')
@click.argument('state', type=click.BOOL)
@click.pass_obj
def pl_pause(obj: _Cache, state: bool):
    """ pause true/false """
    _error = False

    for server, data in obj.pl.mpv.set('pause', state):
        if isinstance(data, Exception):
            obj.logger.error(f"{data!r}", name=server)
            _error = True

    if _error:
        sys.exit(1)


@pl.command('time-pos')
@click.pass_obj
def pl_time_pos(obj: _Cache):
    """ pause true/false """
    _error = False

    for server, data in obj.pl.mpv.get('time_pos'):
        if isinstance(data, Exception):
            obj.logger.error(f"{data!r}", name=server)
            _error = True

        elif data is not None:
            obj.logger.info(f"{data!r}", name=server)

    if _error:
        sys.exit(1)


@pl.command('seek')
@click.option('-i', '--increase', is_flag=True, default=False, help="seek forward")
@click.option('-d', '--decrease', is_flag=True, default=False, help="seek backwards")
@click.argument('value', type=float)
@click.pass_obj
def pl_seek(obj: _Cache, increase: bool, decrease: bool, value: float):
    """ pause true/false """
    _error = False

    if increase or decrease:
        for server, data in obj.pl.mpv.run('seek', f"{'+' if increase else '-'}{value}"):
            if isinstance(data, Exception):
                obj.logger.error(f"{data!r}", name=server)
                _error = True

    else:
        for server, data in obj.pl.mpv.set('time_pos', value):
            if isinstance(data, Exception):
                obj.logger.error(f"{data!r}", name=server)
                _error = True

    if _error:
        sys.exit(1)
