
import types
import json

from typing import Optional, Any

from flask import Blueprint, request, Response

from nmpv.player import Player


blueprint = Blueprint('MPV', __name__)


@blueprint.route('/player', methods=['POST'])
def index():
    resp: Response
    sync: Optional[float] = float(request.args['sync']) if 'sync' in request.args else None
    ret_data: Any = None

    if 'application/json' in request.headers.get('Content-Type'):
        req_data = request.get_json()
        # req_data == { 'attr': str, 'args': list[Any], 'kwargs': dict[str, Any] }

        if isinstance(req_data, dict):
            if 'attr' not in req_data:
                resp = Response("'attr' missing", status=400)

            else:
                with Player(sync) as player:
                    _attr = player.getattr(req_data['attr'])

                    if isinstance(_attr, types.MethodType):
                        ret_data = player.runattr(
                            _attr,
                            *req_data.get('args', []),
                            **req_data.get('kwargs', {})
                        )

                    else:
                        if req_data.get('args'):
                            player.setattr(req_data['attr'], req_data['args'][0])
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
