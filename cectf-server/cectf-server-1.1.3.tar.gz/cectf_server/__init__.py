import os

from flask import Flask, Response
from flask_security import Security


def create_app(test_config=None):

    if 'FLASK_INSTANCE_DIRECTORY' in os.environ:
        # The instance directory was overwritten
        app = Flask(__name__, os.environ['FLASK_INSTANCE_DIRECTORY'])
    else:
        # Use the default relative instance path
        app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        SECURITY_TRACKABLE=True,
        SECURITY_REGISTERABLE=True,
        SECURITY_SEND_REGISTER_EMAIL=False,
        SECURITY_LOGIN_URL='/api/login',
        # the default logout returns a 302, so we define our own logout method
        SECURITY_LOGOUT_URL='/logout',
        SECURITY_REGISTER_URL='/api/register',
        SECURITY_POST_LOGIN_VIEW='/',
        SECURITY_POST_LOGOUT_VIEW='/',
        CECTF_FILE_LOCATION='/tmp/ctf/dev',
        CECTF_PRODUCTION=True
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance and ctf folders exists
    try:
        os.makedirs(app.instance_path)
        os.makedirs(app.config['CECTF_FILE_LOCATION'])
    except OSError:
        pass

    from . import database
    database.init_app(app)

    from . import models

    from . import commands
    commands.init_app(app)

    # Setup Flask-Security
    security = Security(app, models.user_datastore,
                        register_blueprint=False)
    security.unauthorized_handler(
        lambda: Response('Unauthorized', 400))
    app.login_manager.unauthorized_handler(
        lambda: Response('Unauthorized', 400))

    from . import users
    users.init_app(app)

    from . import challenges
    challenges.init_app(app)

    from . import challenges_admin
    challenges_admin.init_app(app)

    from . import challenges_files
    challenges_files.init_app(app)

    from . import authentication
    authentication.init_app(app)

    from . import reset
    reset.init_app(app)

    from . import jsconfig
    jsconfig.init_app(app)

    return app
