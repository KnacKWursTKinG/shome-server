
import click
import click_aliases

from . import _Cache, Cache


@click.group('pl', cls=click_aliases.ClickAliasedGroup, chain=True)
@click.pass_context
def cli_pl(ctx):
    """ Playlist Handler """
    if not ctx.obj:
        ctx.obj = Cache


@cli_pl.command('append')
@click.pass_obj
def pl_append(obj: _Cache):
    """ Append/Add new file """
