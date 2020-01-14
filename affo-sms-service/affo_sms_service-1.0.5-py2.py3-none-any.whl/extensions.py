import os

from flask_migrate import Migrate

from flask_sqlalchemy import SQLAlchemy


__all__ = ["db", "migrate"]

db = SQLAlchemy()

migrate = Migrate(directory=os.path.join(os.path.dirname(os.path.abspath(__file__)), "migrations"))
