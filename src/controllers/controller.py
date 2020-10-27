from flask import Blueprint

controller_blueprint = Blueprint('controller', __name__)


@controller_blueprint.route('/')
def service():
    return 'I am a controller'
