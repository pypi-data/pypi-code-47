"""Base with a `model_id` property for SQLAlchemy models"""

from sqlalchemy.inspection import inspect


class ModelIdBase():
    @property
    def model_id(self):
        """ID for distinguishing models"""
        id = inspect(self).identity
        id = '-'.join([str(key) for key in id]) if id is not None else ''
        return type(self).__name__+'-'+str(id)