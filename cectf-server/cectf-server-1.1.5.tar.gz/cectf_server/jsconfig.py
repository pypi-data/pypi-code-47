from flask import Blueprint, jsonify, current_app

blueprint = Blueprint('jsconfig', __name__, url_prefix='/api/config')


@blueprint.route('/config.json')
def config():
    return jsonify({'production': current_app.config['CECTF_PRODUCTION']})



def init_app(app):
    app.register_blueprint(blueprint)
