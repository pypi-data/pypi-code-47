from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sspo_db.model.organization.models import Organization
from sspo_db.service.base_service import BaseService

class OrganizationService(BaseService):
    def __init__(self):
        super(OrganizationService,self).__init__(Organization)
