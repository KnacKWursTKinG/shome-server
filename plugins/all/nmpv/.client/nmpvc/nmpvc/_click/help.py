
import pprint

import dill as pickle  # type: ignore

import click
import click_aliases  # type: ignore


@click.group('help', cls=click_aliases.ClickAliasedGroup)
@click.pass_context
def cli_help(ctx):
    """ search for methods or attributes in `mpv.MPV` """
    with open(__file__.rsplit('/', 1)[0] + '/mpv-help.pickle', 'rb') as file:
        ctx.obj.help = pickle.load(file)


@cli_help.command('search', aliases=['s'])
@click.option('-s', '--short', is_flag=True, default=False, help="only show matching property/method name(s)")
@click.argument('name')
@click.pass_obj
def help_search(obj, short: bool, name: str):
    """ Search for an attribute """
    matches = list()
    for _key, _value in obj.help['method'].items():
        if name in _key:
            matches.append((_key, _value))

    for _key, _value in obj.help['property'].items():
        if name in _key:
            matches.append((_key, _value))

    for idx, (_name, _data) in enumerate(matches):
        if idx > 0 and not short:
            click.echo()

        click.echo(_name)

        if not short:
            click.echo('-' * len(_name))
            click.echo(f"{pprint.pformat(_data)}")


@cli_help.command('info', aliases=['i'])
@click.argument('name')
@click.pass_obj
def help_info(obj, name: str):
    """ get info for attribute """
    for _key in obj.help['method']:
        if _key == name:
            click.echo(_key)
            click.echo('-' * len(_key))
            click.echo(f"{pprint.pformat(obj.help['method'][_key])}")

    for _key in obj.help['property']:
        if _key == name:
            click.echo(_key)
            click.echo('-' * len(_key))
            click.echo(f"{pprint.pformat(obj.help['property'][_key])}")
