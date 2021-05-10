
import click

from . import Cache
from .help import cli_help
from .pl import cli_pl
from .smb import cli_smb


@click.group()
@click.option('--debug', is_flag=True, default=False, help="enable debug messages")
@click.pass_context
def cli(ctx, debug: bool):
    """ Network MPV Client """
    if not ctx.obj:
        ctx.obj = Cache

    if debug:
        ctx.obj.logger.level = 'debug'


cli.add_command(cli_help)
cli.add_command(cli_pl)
cli.add_command(cli_smb)
