
import dill as pickle
import pprint

import click
import click_aliases

from .help import cli_help


@click.group()
def cli():
    """ Network MPV Client """


cli.add_command(cli_help)
