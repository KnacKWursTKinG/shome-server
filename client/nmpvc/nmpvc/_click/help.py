
import dill as pickle
import pprint

import click
import click_aliases


@click.group('help', cls=click_aliases.ClickAliasedGroup)
@click.pass_context
def cli(ctx):
    """ search for methods or attributes in `mpv.MPV` """
    with open(__file__.rsplit('/', 1)[0] + '/mpv-help.pickle', 'rb') as file:
        ctx.obj = pickle.load(file)


@cli.command('search', aliases=['s'])
@click.option('-s', '--short', is_flag=True, default=False, help="only show matching property/method name(s)")
@click.argument('name')
@click.pass_obj
def search(obj, short: bool, name: str):
    """ Search for an attribute """
    matches = list()
    for _key, _value in obj['method'].items():
        if name in _key:
            matches.append((_key, _value))

    for _key, _value in obj['property'].items():
        if name in _key:
            matches.append((_key, _value))

    for idx, (_name, _data) in enumerate(matches):
        if idx > 0 and not short:
            click.echo()

        click.echo(_name)

        if not short:
            click.echo('-' * len(_name))
            click.echo(f"{pprint.pformat(_data)}")


@cli.command('info', aliases=['i'])
@click.argument('name')
@click.pass_obj
def info(obj, name: str):
    """ get info for attribute """
    for _key in obj['method']:
        if _key == name:
            click.echo(_key)
            click.echo('-' * len(_key))
            click.echo(f"{pprint.pformat(obj['method'][_key])}")

    for _key in obj['property']:
        if _key == name:
            click.echo(_key)
            click.echo('-' * len(_key))
            click.echo(f"{pprint.pformat(obj['property'][_key])}")
