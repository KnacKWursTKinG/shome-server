
import os
import sys

import click

module_path = os.path.abspath(__file__).rsplit('/', 2)[0]
sys.path.insert(0, module_path)

from nmpvc._click.help import cli as cli_help


@click.group()
def cli():
    """ Network MPV Client """


cli.add_command(cli_help)


cli()
