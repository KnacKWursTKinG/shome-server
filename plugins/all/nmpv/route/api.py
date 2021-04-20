
from flask import Blueprint, request, make_response, Response

from kwking_helper import c

from nmpv.player import player


blueprint = Blueprint('MPV', __name__)


@blueprint.route('/', methods=['POST'])
def index():
    _return: Response

    if 'data/bytes' in request.headers.get('Content-Type'):
        _t = player(request.data)
        _t.join()

        if _t.err:
            # TODO find the correct status code here (500?)
            _return = make_response(f"{_t.err!r}", 500)
        else:
            _return = make_response(
                _t.ret, 200,
                {'Content-Type': 'data/bytes'}
            )
    else:
        _return = make_response("no data", 400)

    return _return