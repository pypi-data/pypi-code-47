from flask import Flask 
from .config import Config 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate 
from flask_login import LoginManager
import os

app = Flask(__name__)

app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'
APP_URL = Config.APP_URL
basedir = os.path.abspath(os.path.dirname(__file__))


from app.api import bp as api_bp
app.register_blueprint(api_bp, url_prefix='/api')

from app import routes, models