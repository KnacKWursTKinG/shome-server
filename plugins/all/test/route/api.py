
from flask import Blueprint


blueprint = Blueprint('Test Api', __name__)


@blueprint.route('/sync')
def test_sync():
    # @todo get request params for 'time' (timestamps)
    pass
