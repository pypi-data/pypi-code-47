from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sspo_db.model.core.models import ApplicationType, Application
from sspo_db.service.base_service import BaseService

class ApplicationTypeService(BaseService):
    def __init__(self):
        super(ApplicationTypeService,self).__init__(ApplicationType)

class ApplicationService(BaseService):
    def __init__(self):
        super(ApplicationService,self).__init__(Application)