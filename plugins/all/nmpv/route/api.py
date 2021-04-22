
import pickle

from flask import Blueprint, request, Response

from kwking_helper.config import c

from nmpv.player import Player


blueprint = Blueprint('MPV', __name__)


@blueprint.route('/player', methods=['POST'])
def index():
    response: Response

    if 'data/bytes' in request.headers.get('Content-Type'):
        req_data = pickle.loads(request.data)

        player = Player(req_data[0], *req_data[1], **req_data[2])
        player.start()
        player.join()

        if player._error:
            response = Response(f"{player._error!r}", status=500, mimetype='text/text')
        else:
            response = Response(
                pickle.dumps(player._return),
                mimetype='data/bytes'
            )

        del player

    else:
        response = Response(status=400)

    return response
