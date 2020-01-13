from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sspo_db.config.config import session
class BaseService():
    
    def __init__(self, object):
        self.session = session
        self.object = object
    
    def get_all(self):
        return self.session.query(self.object).order_by(self.object.id)
    
    def create(self, object):
        self.session.add(object)
        self.session.commit()

    def delete(self, object):
        self.session.delete(object)
        self.session.commit()

    def update(self, object):
        self.session.update(object)
        self.session.commit()