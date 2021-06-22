
import types
import json

from typing import Any

from flask import Blueprint, request, Response

from nmpv.player import Player

from helper.config import c
from helper.logging import CL


blueprint = Blueprint('MPV', __name__)
logger = CL(
    c.main.get('plugin@nmpv', 'log_level'), 'nmpv',
    _file=c.main.get('plugin@nmpv', 'log_file', fallback=None)
)


@blueprint.route('/player', methods=['POST'])
def index():
    resp: Response
    ret_data: Any = None

    if 'application/json' in request.headers.get('Content-Type'):
        req_data = request.get_json()
        # req_data == { 'attr': str, 'args': list[Any], 'kwargs': dict[str, Any] }

        logger.debug(f"{req_data=}")

        if isinstance(req_data, dict):
            if 'attr' not in req_data:
                resp = Response("'attr' missing", status=400)

            else:
                with Player(req_data.get('sync', None)) as player:
                    _attr = player.getattr(req_data['attr'])

                    if isinstance(_attr, types.MethodType):
                        ret_data = player.runattr(
                            _attr,
                            *req_data.get('args', []),
                            **req_data.get('kwargs', {})
                        )

                    else:
                        if 'value' in req_data:
                            player.setattr(req_data['attr'], req_data['value'])
                        else:
                            ret_data = _attr

                resp = Response(json.dumps(ret_data), status=200, mimetype='application/json')

        else:
            resp = Response(
                f"wrong data: expect '{type(dict())}' but got '{type(req_data)}'",
                status=400
            )

    else:
        resp = Response("missing json data", status=400)

    return resp
