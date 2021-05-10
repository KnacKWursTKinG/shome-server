
import os
import sys

from flask import Flask, Blueprint

from kwking_helper.config import c
from kwking_helper.logging import CL

from shomeserver import PluginError
from shomeserver.route.base import base_blueprint, api_base_blueprint


__all__ = ['server']

log = CL(
    c.main.get('shomeserver', 'log_level'),
    name="server",
    _file=os.path.expanduser(c.main.get('shomeserver', 'log_file', fallback=None))
)

server = Flask(__name__)

server.register_blueprint(base_blueprint, prefix='/')
server.register_blueprint(api_base_blueprint, prefix='/api')

# load all plugins
plugin_path = os.path.expanduser(c.main.get('shomeserver', 'plugin_path'))

if os.path.isdir(plugin_path):
    sys.path.insert(0, plugin_path)

    for _plugin in os.listdir(plugin_path):
        try:
            _plug = __import__(_plugin)
        except ImportError as ex:
            log.error(f"ImportError while loading plugin '{_plugin}': {ex}")
            continue
        except PluginError as ex:
            log.error(f"[{_plugin}] PluginError: {ex}")
            continue

        try:
            _blueprint = _plug.blueprint if isinstance(_plug.blueprint, Blueprint) else None
        except AttributeError:
            log.warning(f"[{_plugin}] 'blueprint' missing [IGNORE]")
            _blueprint = None

        try:
            _api_blueprint = _plug.api_blueprint if isinstance(_plug.api_blueprint, Blueprint) else None
        except AttributeError:
            log.warning(f"[{_plugin}] 'api_blueprint' missing [IGNORE]")
            _api_blueprint = None

        if _blueprint is not None:
            server.register_blueprint(_blueprint, url_prefix=f'/{_plugin}')
            log.info(f"[{_plugin}] Plugin Blueprint Loaded: '{_blueprint.name}'")

        if _api_blueprint is not None:
            server.register_blueprint(_api_blueprint, url_prefix=f'/api/{_plugin}')
            log.info(f"[{_plugin}] Plugin Blueprint Loaded: '{_api_blueprint.name}'")
else:
    log.warning("No plugins found")

log.debug(f"url map:\n{server.url_map}")
