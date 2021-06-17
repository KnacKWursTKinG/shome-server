
import socket
import json
import sys

import click

from pygments import highlight  # type: ignore
from pygments.lexers import JsonLexer  # type: ignore
from pygments.formatters import TerminalFormatter  # type: ignore

from nmpv_client.base import MPV

from . import _Cache, Cache


# @todo: add commands for set/get property


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

    if not isinstance(ctx.obj.pl.mpv, MPV) or server:
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
@click.option('--sync', is_flag=True, default=False, help="enable sync")
@click.argument('state', type=click.BOOL)
@click.pass_obj
def pl_pause(obj: _Cache, sync: bool, state: bool):
    """ pause true/false """
    _error = False

    for server, data in obj.pl.mpv.set('pause', state, _sync=sync):
        if isinstance(data, Exception):
            obj.logger.error(f"{data!r}", name=server)
            _error = True

    if _error:
        sys.exit(1)


@pl.command('time-pos')
@click.pass_obj
def pl_time_pos(obj: _Cache):
    """ get time-pos prop """
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
    """ seek position """
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


@pl.command('prop')
@click.option('-s', '--set', '_set', help="Set a property")
@click.option('--sync', is_flag=True, default=False, help="enable sync")
@click.argument('prop')
@click.pass_obj
def pl_prop(obj: _Cache, prop: str, _set: str, sync: bool):
    """ Get or set a mpv property """
    obj.logger.debug(f"{prop=}, {_set=}", name="pl_prop")

    if _set:
        server_return = obj.pl.mpv.set(prop, _set, _sync=sync)
    else:
        server_return = obj.pl.mpv.get(prop, _sync=sync)

    _err = False
    for server, ret in server_return:
        if isinstance(ret, Exception):
            obj.logger.error(f"{ret!r}", name=server)
            _err = True
        else:
            obj.logger.info("\n{}".format(
                highlight(
                    json.dumps(ret, indent=2),
                    JsonLexer(), TerminalFormatter()
                )
            ), name=f"property: {server}")

    if _err:
        sys.exit(1)


@pl.command('quit')
@click.pass_obj
def pl_cmd(obj: _Cache):
    """ run mpv command """
    _err = False
    for server, ret in obj.pl.mpv.run('quit'):
        if isinstance(ret, Exception):
            obj.logger.error(f"{ret!r}", name=server)
            _err = True

    if _err:
        sys.exit(1)
