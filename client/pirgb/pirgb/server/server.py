
import socket

from flask import Flask, render_template, make_response, jsonify, request

from kwking_helper import ClickLogger, c, thread

from pirgb import config
from pirgb.pirgb import PiRGB
from pirgb.server.cache import Cache


server = Flask(__name__)
logger = ClickLogger(c.main.get('pirgb', 'log_level'), 'server')
config.load_from_db().join(1)
cache = Cache()


# <<- Helper Functions

def cache_reload():
    _t = cache.load()
    _t.join()

    return _t


def get_hosts_for_group(_id) -> list[tuple[str, str]]:
    hosts: list[tuple[str, str]] = list()
    host, section = _id.split('--')

    for _key, _data in cache.cache.items():
        _host, _section = _key.split(':')

        if (host == _host and section == _section) or\
                (host in _data.groups and section == 'group'):

            hosts.append((_host, _section))

    return hosts


def get_all_groups() -> list[str]:
    groups = list()

    for data in cache.cache.values():
        groups.extend(data.groups)

    return list(set(groups))

# ->>


@server.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@server.route('/html/category/<category>', methods=['GET'])
def html_category(category: str):
    # <<- return '.control-element' div elements for host:section or group
    cache_reload()
    logger.debug(f"['/html/category/{category}']")

    template_data: list[tuple[str, str, str]] = list()

    if category == 'sections':
        for key in cache.cache:
            logger.debug(f"['/html/category/{category}'] get data for {key=}")
            template_data.append(
                (
                    str(key).replace(':', '--'),
                    cache.cache[key].name or cache.cache[key].label,
                    category
                )
            )

    elif category == 'groups':
        for group in get_all_groups():
            template_data.append((group + '--group', group, category))

    else:
        return make_response(category, 404)

    return make_response(
        jsonify(render_template('jinja/category.html', data=template_data)), 200
    )
    # ->>


@server.route('/pi/<command>', methods=['POST'])
def pi_command(command: str):
    # <<- pi commands (get, set, on, ...)
    rdata = request.get_json()
    _get_return: list[list[int]] = list()

    @thread(daemon=True, log_level=c.main.get('pirgb', 'log_level'))
    def _t_check(_t):
        _t.join()

        if _t.err:
            return make_response(f"pirgb: {command}: {_t.err!r}", 500)

        if _t.ret and command == 'get':
            _get_return.extend(_t.ret)

        return None

    try:
        hosts = get_hosts_for_group(rdata.pop('id'))
    except KeyError:
        return make_response("missing 'id'", 400)

    threads = list()
    for host, section in hosts:
        try:
            pirgb = PiRGB(host)
        except socket.error:
            logger.warning(f"['/pi/{command}'] {host} offline")
            return make_response(f"'{host}' Offline!", 500)

        try:
            func = pirgb.__getattribute__(command)
        except AttributeError:
            return make_response(f'unknown command: {command}', 400)

        _t = func(**{**dict(sections=[section]), **rdata})
        threads.append(_t_check(_t))

    for _t in threads:
        _t.join()

        if _t.ret:
            return _t.ret

    logger.debug(f"['/pi/{command}'] {_get_return=}")
    return make_response(jsonify(_get_return or None), 200)
    # ->>


@server.route('/cache', methods=['POST', 'GET'])
def cache_handler():
    cache_reload()

    err = (jsonify(None), 200)

    if request.method == 'GET':
        # <<- get data for 'id' from cache
        if not request.args.get('id'):
            err = ("missing 'id' param", 400)
        else:
            try:
                err = (
                    jsonify(
                        {
                            **cache.cache[
                                request.args.get('id').replace('--', ':')
                            ].__dict__,
                            **{'allGroups': get_all_groups()}
                        }

                    ),
                    200
                )
            except KeyError:
                err = (f"'{request.args.get('id')}' not found", 404)
        # ->>

    elif request.method == 'POST':
        # <<- post data to 'id' on cache
        data = request.get_json()

        if 'rgbw' in data:
            data['rgbw'] = list(map(tuple, data.get('rgbw', [])))

        rgb = None

        # NOTE: rgb: convert to rgbw (calc w)
        if data.get('rgb'):
            rgb = data.pop('rgb')

            if len(set(rgb)) == 1:
                rgb.append(max(rgb))

            rgb = rgb[:4]

            data['rgbw'] = data.get('rgbw', []) + [tuple(rgb)]

        if 'id' not in data:
            err = ("missing 'id'", 400)

        else:
            if not isinstance(data, dict):
                err = ("wrong data received", 400)

            else:
                _id = data.pop('id')
                hosts = get_hosts_for_group(_id)

                if not hosts:
                    err = (f"'{_id}' not found", 404)

                else:
                    for host, section in hosts:  # NOTE: final
                        try:
                            cache.update(
                                f"{host}:{section}",
                                append=data.pop('append', True),
                                **dict(data if len(hosts) == 1 else dict(rgbw=data['rgbw']))
                            )

                        except KeyError as key:
                            err = (str(key), 400)

                        if err[1] == 200 and rgb:
                            PiRGB(host).set(sections=[section], rgbw=rgb)
        # ->>

    return make_response(*err)
