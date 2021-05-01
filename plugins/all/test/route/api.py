
from flask import Blueprint, request, make_response, jsonify

from test import test


blueprint = Blueprint('Test Api', __name__)


@blueprint.route('/sync')
def test_sync():
    try:
        ts = test.sync(request.args['time'])
    except test.SyncError as ex:
        return make_response(
            jsonify(message=f"desync: {ex.args[0]}", ts=ex.args[0]), 400
        )

    return jsonify(ts)
