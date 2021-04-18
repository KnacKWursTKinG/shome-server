
from flask import Blueprint


blueprint = Blueprint('MPV', __name__)


@blueprint.route('/', methods=['POST'])
def index():
    ...
