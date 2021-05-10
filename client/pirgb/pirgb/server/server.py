
import socket

from flask import Flask, render_template, make_response, jsonify, request

from kwking_helper.config import c
from kwking_helper.logging import CL
from kwking_helper.thread import threaded2

from pirgb import config
from pirgb.pirgb import PiRGB
from pirgb.server.cache import Cache


server = Flask(__name__)
logger = CL(c.main.get('pirgb', 'log_level'), 'server')
config.load_from_db().join(1)
cache = Cache()


# <<- Helper Functions

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
    cache.load().thread.join()
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
    get_ret: list[list[int]] = list()

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

        threads.append(
            func(**{**dict(sections=[section]), **rdata})
        )

    for _t in threads:
        try:
            ret = _t.join()

            if ret:
                get_ret.extend(ret)

        except Exception as ex:
            return make_response(f"pirgb: {command}: {ex!r}", 500)

        del _t

    logger.debug(f"['/pi/{command}'] {get_ret=}")

    return make_response(
        jsonify(get_ret or None), 200, {'Content-Type': 'application/json'}
    )
    # ->>


@server.route('/cache', methods=['POST', 'GET'])
def cache_handler():
    cache.load().thread.join()

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
