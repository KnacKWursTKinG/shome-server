
import sys
import pprint

import click

from nmpvc._click import pl

from . import _Cache


@click.group('on-success')
@click.option('--echo', is_flag=True, default=False, help="print server return")
@click.option('--exit', is_flag=True, default=False, help="exit if error")
@click.pass_obj
def on_success(obj: _Cache, **kwargs):
    """ (Experimental) """
    to_delete = list()

    obj.logger.debug(f"{pprint.pformat(obj.pl.td)}", name='on-success')

    for part in obj.pl.td:
        for server, data in part:
            if not isinstance(data, Exception):
                to_delete.append(part)

                if kwargs['echo'] and data is not None:
                    obj.logger.info(f"{pprint.pformat(data)}", name=server)

            else:
                to_delete.append(part)

                if kwargs['echo']:
                    obj.logger.error(f"{data!r}", name=server)

                if kwargs['exit']:
                    sys.exit(1)

    for part in to_delete:
        obj.pl.td.remove(part)


on_success.add_command(pl.pl)


#@click.command('on-error')
#@click.option('--echo', is_flag=True, default=False, help="print exception")
#@click.option('--exit', is_flag=True, default=False, help="exit if error")
#@click.pass_obj
#def on_error(obj: _Cache, **kwargs):
#    """ (Experimental) """
#    to_delete = list()
#
#    obj.logger.debug(f"{pprint.pformat(obj.pl.td)}", name='on-error')
#
#    for part in obj.pl.td:
#        for server, data in part:
#            if isinstance(data, Exception):
#                to_delete.append(part)
#
#                if kwargs['echo']:
#                    obj.logger.error(f"{data!r}", name=server)
#
#                if kwargs['exit']:
#                    sys.exit(1)
#
#    for part in to_delete:
#        obj.pl.td.remove(part)
