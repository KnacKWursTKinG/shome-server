
import re
import socket
import sys

from typing import Optional

import click
import click_aliases  # type: ignore

from smb.SMBConnection import SMBConnection  # type: ignore

from nmpvc.base import MPV, MPVError

from . import _Cache, _SMB, Cache


@click.group('smb', cls=click_aliases.ClickAliasedGroup)
@click.option('-p', '--path', default='/', show_default=True, help="chang root path")
@click.option('-c', '--credentials', nargs=4,
              metavar="<server> <share> <username> <password>",
              help="samba credentials")
@click.pass_context
def cli_smb(ctx, path: str, credentials: Optional[tuple[str, str, str, str]]):
    """ Sambe Browser """
    if not ctx.obj:
        ctx.obj = Cache

    ctx.obj.logger.name = 'smb'

    if not credentials:
        # @todo: load config credentials
        credentials = ('...', '...', '...', '...')
        ctx.obj.logger.critical("SMB Credentials Missing!")
        sys.exit(1)

    ctx.obj.smb = _SMB(
        *credentials, path=path
    )


@cli_smb.command('list', aliases=['ls'])
@click.argument('path')
@click.pass_obj
def smb_list(obj: _Cache, path: str):
    """ List/Browse samba share """
    #obj.logger.name = 'list'

    if not isinstance(obj.smb, _SMB):
        raise TypeError(f"expect {type(_SMB)} for 'obj.smb', got {type(obj.smb)}")

    with SMBConnection(obj.smb.username, obj.smb.password,
                       obj.smb.server, obj.smb.server) as cli:

        cli.connect(obj.smb.server, obj.smb.port)

        for _file in cli.listPath(obj.smb.share, f"{obj.smb.path.rstrip('/')}/{path.lstrip('/')}"):
            # skip hidden files
            if _file.filename[0] == '.':
                continue

            click.echo(f"{_file.filename}{'/' if _file.isDirectory else ''}")


@cli_smb.group('search', aliases=['s'], invoke_without_command=True)
@click.option('-s', '--sort', type=click.Choice(['write', 'name', 'lazy']), help="sort files")
@click.option('-m', '--max-matches', type=int, help="max number for matches")
@click.argument('file')
@click.pass_obj
def smb_search(obj: _Cache, file: str, max_matches: int, sort: Optional[str]):
    """ Search samba server for file(s) (python regex support) """
    #obj.logger.name = 'search'

    if not isinstance(obj.smb, _SMB):
        raise TypeError(f"expect {type(_SMB)} for 'obj.smb', got {type(obj.smb)}")

    def _add(obj, matches: list):
        for _file in matches[:max_matches]:
            url = obj.smb.url(_file)
            click.echo(_file)
            obj.smb.add(url)

    regex = re.compile(file)
    matches: list = list()

    with SMBConnection(obj.smb.username, obj.smb.password,
                       obj.smb.server, obj.smb.server) as cli:

        cli.connect(obj.smb.server, obj.smb.port)

        # search in path for matching files
        for _file in cli.listPath(obj.smb.share, obj.smb.path):
            # skip hidden files
            if _file.filename[0] == '.' or _file.isDirectory:
                continue

            match = re.match(regex, _file.filename)

            if match:
                matches.append(_file)

    if sort == 'name':
        # sort
        matches = [f.filename for f in matches]
        matches.sort()

        return _add(obj, matches)

    if sort == 'write':
        # sort
        _matches: list = list()

        for _match in matches:
            for idx, _sorted_match in enumerate(_matches):
                if _match.last_write_time > _sorted_match.last_write_time:
                    _matches.insert(idx, _match)
                    break
            else:
                _matches.append(_match)

        matches = _matches
        del _matches

    return _add(obj, [f.filename for f in matches])


@smb_search.command('append')
@click.option('-s', '--server', metavar="<server>", multiple=True,
              help="shomeserver host [multiple: True]")
@click.option('-p', '--port', metavar="<port>", type=int, default=50870, show_default=True,
              help="shomeserver port")
@click.pass_obj
def search_append(obj: _Cache, server: tuple[str], port: int):
    """ Append/Add new file """
    obj.logger.name = 'append'

    if not isinstance(obj.smb, _SMB):
        raise TypeError(f"expect {type(_SMB)} for 'obj.smb', got {type(obj.smb)}")

    if not isinstance(obj.pl.mpv, MPV):
        try:
            # @todo: MPV class changed
            obj.pl.mpv = MPV(*[(_host, port) for _host in server])
        except socket.gaierror as ex:
            obj.logger.error(f"{ex}")
            sys.exit(1)

    try:
        while (file := obj.smb.files.pop(0) if obj.smb.files else None):
            # @todo: will return a list with tuple[addr, return or exception]
            # @todo: create a threaded2 function with on_error handler function (???)
            obj.pl.mpv.run('playlist_append', file)

    # @todo: changed error handling (type check on MPV return data)
    except MPVError as ex:
        obj.logger.error(f"{ex}")
        sys.exit(1)
