
import pickle

from flask import Blueprint, request, Response

from kwking_helper.config import c

from nmpv.player import Player


blueprint = Blueprint('MPV', __name__)


@blueprint.route('/player', methods=['POST'])
def index():
    response: Response

    if 'data/bytes' in request.headers.get('Content-Type'):
        # @todo add sync (timestamp & optional)
        # @todo change to json {'sync': ...'attr': '...', 'args': [...], 'kwargs': {...: ...}}
        req_data = pickle.loads(request.data)
        with Player(None, req_data[0], *req_data[1], **req_data[2]) as player:
            player.join()

            if player._error:
                response = Response(player._error, status=400)
            else:
                response = Response(
                    pickle.dumps(player._return),
                    mimetype='data/bytes'
                )

        print(Player.Queue)

    else:
        response = Response(status=400)

    return response
