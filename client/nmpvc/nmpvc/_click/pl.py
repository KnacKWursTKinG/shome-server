
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

    for url in obj.pl.url:
        ...
