
import click
import click_aliases

from . import _Cache, Cache
from nmpvc.base import MPV


@click.group('pl', cls=click_aliases.ClickAliasedGroup, chain=True)
@click.pass_context
def cli_pl(ctx):
    """ Playlist Handler """
    if not ctx.obj:
        ctx.obj = Cache

    #ctx.obj.logger.name = 'pl'


@cli_pl.command('append')
@click.pass_obj
def pl_append(obj: _Cache):
    """ Append/Add new file """
    #ctx.obj.logger.name = 'append'
    if not isinstance(obj.pl.mpv, MPV):
        raise TypeError(f"expect {type(MPV)} for 'obj.smb', got {type(obj.pl.mpv)}")

    for url in obj.pl.url:
        obj.pl.mpv.run('playlist_append', url)
