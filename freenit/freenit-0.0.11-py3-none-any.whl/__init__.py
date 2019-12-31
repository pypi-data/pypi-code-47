from importlib import import_module

from flask import Flask, send_file
from flask_collect import Collect
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_security import PeeweeUserDatastore, Security

from . import cli
from .api import create_api
from .db import db
from .utils import sendmail


def create_app(config, app_name, app=None, auth={}):
    if app is None:
        app = Flask(__name__)
        app.config.from_object(config)
    app.models = f'{app_name}.models'

    @app.route('/media/<path:path>')
    def send_media(path):
        fullPath = f"../{app.config['MEDIA_PATH']}/{path}"
        try:
            return send_file(fullPath)
        except FileNotFoundError:
            return 'No such file', 404

    app.sendmail = lambda to, message: sendmail(app.config, to, message)

    app.collect = Collect(app)
    db.init_app(app)
    app.db = db

    user_module = auth.get('user', None)
    if user_module is None:
        from .models.user import User
    else:
        User = import_module(user_module).User

    role_module = auth.get('role', None)
    if role_module is None:
        from .models.role import Role, UserRoles
    else:
        role_module_imported = import_module(role_module)
        Role = role_module_imported.Role
        UserRoles = role_module_imported.UserRoles

    app.user_datastore = PeeweeUserDatastore(
        app.db,
        User,
        Role,
        UserRoles,
    )
    app.security = Security(app, app.user_datastore)
    app.jwt = JWTManager(app)
    create_api(app)
    app.cors = CORS(app, supports_credentials=True)
    cli.register(app)

    return app
