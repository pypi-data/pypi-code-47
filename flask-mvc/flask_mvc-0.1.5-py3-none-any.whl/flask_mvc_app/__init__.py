from flask import Flask
from flask_mvc_app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__, static_url_path='/static')
app.config.from_object(Config)
app.url_map.strict_slashes = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from flask_mvc_app import routes, models