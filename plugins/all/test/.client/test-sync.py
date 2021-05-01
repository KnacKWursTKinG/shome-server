#!/usr/bin/env python

import click


@click.group()
def cli():
    """ Test Client (shomeserver test plugin) """


@cli.command('sync')
def sync():
    """ Sync (timestamp test) """
    # @todo make 'GET' request to sync path
    # @todo wait for response and handle status_code 400 with contentType json


if __name__ == "__main__":
    cli()
