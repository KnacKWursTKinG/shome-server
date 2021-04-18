
import os

from flask import Blueprint, request, make_response, jsonify

from kwking_helper import ClickLogger, c

from pi_rgb.pigpio import PigpioHandler


api_blueprint = Blueprint('Pi RGB API', __name__)
pig = PigpioHandler()
log = ClickLogger(
    c.main.get('plugin@pi_rgb', 'log_level'),
    name="Pi_RGB: Api Blueprint",
    _file=os.path.expanduser(c.main.get('plugin@pi_rgb', 'log_file', fallback=None))
)


@api_blueprint.route('/set', methods=["POST"])
def rgbw_set():
    log.info("[/set] Got connection from: {}".format(request.remote_addr))
    cli_data = request.get_json()

    if not isinstance(cli_data, dict):
        return make_response(
            "Wrong Json Data", 400
        )

    sections: list = cli_data.get('sections') or [cli_data.get('section')] or []
    rgbw: list = cli_data.get('rgbw') or cli_data.get('rgbw') or []

    log.debug(f"[/set] {sections=}, {rgbw=}")

    if sections and isinstance(sections, list):
        if rgbw and isinstance(rgbw, list):
            rgbw = list(rgbw + [0, 0, 0, 0])[:4]
            _threads = list()

            for section in sections:
                _threads.append(pig.set_dutycycle(section, rgbw))

            for t in _threads:
                t.join()

                if t.err:
                    log.critical(f"[/get] Thread: {t.name}, Exception: {t.err!r}")
                    return make_response(f"Exception: {t.err!r}", 500)

        return make_response(jsonify(None), 200)

    return make_response("Missing: 'sections'", 400)


@api_blueprint.route('/get', methods=["POST"])
def rgbw_get():
    log.info("[/get] Got connection from: {}".format(request.remote_addr))

    cli_data = request.get_json()

    if not isinstance(cli_data, dict):
        return make_response(
            "Wrong Json Data", 400
        )

    sections: list = cli_data.get('sections') or [cli_data.get('section')] or []

    if sections and isinstance(sections, list) and sections:
        _threads = [pig.get_dutycycle(section) for section in sections]

        for t in _threads:
            t.join()

            if t.err:
                log.critical(f"[/get] Thread: {t.name}, Exception: {t.err!r}")
                return make_response(f"Exception: {t.err!r}", 500)

        return make_response(
            jsonify([t.ret for t in _threads]), 200
        )

    return make_response("Missing: 'sections'", 400)


@api_blueprint.route('/on', methods=["POST"])
def rgbw_on():
    log.info("[/on] Got connection from: {}".format(request.remote_addr))

    cli_data = request.get_json()

    if not isinstance(cli_data, dict):
        return make_response(
            "Wrong Json Data", 400
        )

    sections: list = cli_data.get('sections') or [cli_data.get('section')] or []

    if sections and isinstance(sections, list):
        _threads = list()

        for section in sections:
            _threads.append(pig.set_dutycycle(section, pig.rgbw(section)))

        for t in _threads:
            t.join()

            if t.err:
                log.critical(f"[/get] Thread: {t.name}, Exception: {t.err!r}")
                return make_response(f"Exception: {t.err!r}", 500)

        return make_response(jsonify(None), 200)

    return make_response("Missing: 'sections'", 400)


@api_blueprint.route('/off', methods=["POST"])
def rgbw_off():
    log.info("[/off] Got connection from: {}".format(request.remote_addr))

    cli_data = request.get_json()

    if not isinstance(cli_data, dict):
        return make_response(
            "Wrong Json Data", 400
        )

    sections: list = cli_data.get('sections') or [cli_data.get('section')] or []

    if sections and isinstance(sections, list):
        _threads = list()

        for section in sections:
            _threads.append(pig.set_dutycycle(section, [0, 0, 0, 0]))

        for t in _threads:
            t.join()

            if t.err:
                log.critical(f"[/get] Thread: {t.name}, Exception: {t.err!r}")
                return make_response(f"Exception: {t.err!r}", 500)

        return make_response(jsonify(None), 200)

    return make_response("Missing: 'sections'", 400)
