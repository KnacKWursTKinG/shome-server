
import click
import click_aliases


@click.group('help', cls=click_aliases.ClickAliasedGroup)
def cli():
    """ Get help for mpv attributes (properties/methods) """


@cli.command('property', aliases=['prop', 'p'])
def cli_property():
    """ Get Property Default """
    import mpv


@cli.command('search', aliases=['s'])
def cli_search():
    """ Search in Properties and Methods """
    import mpv


@cli.command('method', aliases=['m'])
def cli_method():
    """ Get Method info (parameter) """
    import mpv
