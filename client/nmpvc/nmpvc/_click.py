""" click stuff for client(s)

Notes:
    * client for get help
        - list/search properties/methods and defaults/parameters (inspect.getfull...)
          only works with if python-mpv is installed (pip install python-mpv)

    * some basic stuff to play things and control

"""

import click
import click_aliases


@click.group(cls=click_aliases.ClickAliasedGroup)
def cli_mpv_help():
    """ Get help for `mpv.MPV` class attributes """


@cli_mpv_help.command('property', aliases=['prop', 'p'])
def cli_mpv_help_property():
    """ get property info, default, ... """


@cli_mpv_help.command('search', aliases=['s'])
def cli_mpv_help_search():
    """ search for property or method, show full name and type """


@cli_mpv_help.command('method', aliases=['m'])
def cli_mpv_help_method():
    """ Get method params, defaults, ... """
