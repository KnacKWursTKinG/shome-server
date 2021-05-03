
from flask import Blueprint, request, make_response, jsonify

from test import test


blueprint = Blueprint('Test Api', __name__)


@blueprint.route('/sync')
def test_sync():
    try:
        ts = test.sync(float(request.args['time']))

    except test.SyncError as ex:
        resp = make_response(
            jsonify(message=f"desync: {ex.args[0]}", ts=ex.args[0]), 400
        )
        resp.headers['Content-Type'] = 'application/json'

        return resp

    except ValueError:
        return make_response(
            f"{ex!r}", 400
        )

    return jsonify(ts)
