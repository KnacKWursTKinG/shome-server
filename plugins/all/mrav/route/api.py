
from flask import Blueprint


blueprint = Blueprint('MRAV', __name__)


@blueprint.route('/', methods=['POST'])
def index():
    ...
