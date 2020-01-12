from flask import Blueprint, jsonify
from flask_security.core import current_user
from flask_security.decorators import login_required, roles_required

from .models import User

blueprint = Blueprint('users', __name__, url_prefix='/api')


@blueprint.route('/user')
@login_required
def get_current_user_route():
    return jsonify(current_user.serialize)


def init_app(app):
    app.register_blueprint(blueprint)
