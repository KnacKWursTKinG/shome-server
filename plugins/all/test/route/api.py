
from flask import Blueprint


blueprint = Blueprint('Test Api', __name__)


@blueprint.route('/sync')
def test_sync():
    # TODO get request params for 'time' to get timestamp
    pass
