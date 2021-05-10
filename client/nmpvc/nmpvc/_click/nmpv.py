
import dill as pickle
import pprint

import click
import click_aliases

from .help import cli_help
from .pl import cli_pl
from .smb import cli_smb


@click.group()
def cli():
    """ Network MPV Client """


cli.add_command(cli_help)
cli.add_command(cli_pl)
cli.add_command(cli_smb)
