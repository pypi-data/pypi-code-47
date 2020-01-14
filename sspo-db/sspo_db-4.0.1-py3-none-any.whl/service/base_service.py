from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sspo_db.config.config import session
from sspo_db.model.core.models import ApplicationReference
class BaseService():
    
    def __init__(self, object):
        self.session = session
        self.object = object
    
    def get_all(self):
        return self.session.query(self.object).order_by(self.object.id)
    
    def get_by_uuid(self, uuid):
        return self.session.query(self.object).filter(self.object.uuid == uuid).first()
    
    def get_by_external_uuid(self,external_id):
        return self.session.query(self.object).join(ApplicationReference, ApplicationReference.internal_uuid == self.object.uuid).filter(ApplicationReference.external_id == external_id).first()
        
    def create(self, object):
        self.session.add(object)
        self.session.commit()

    def delete(self, object):
        self.session.delete(object)
        self.session.commit()

    def update(self, object):
        self.session.update(object)
        self.session.commit()