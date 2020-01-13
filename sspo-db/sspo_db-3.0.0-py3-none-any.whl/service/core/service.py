from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sspo_db.model.core.models import *
from sspo_db.service.base_service import BaseService

class ApplicationTypeService(BaseService):
    def __init__(self):
        super(ApplicationTypeService,self).__init__(ApplicationType)

class ApplicationService(BaseService):
    def __init__(self):
        super(ApplicationService,self).__init__(Application)

class ConfigurationService(BaseService):
    def __init__(self):
        super(ConfigurationService,self).__init__(Configuration)

class ApplicationReferenceService(BaseService):
    def __init__(self):
        super(ApplicationReferenceService,self).__init__(ApplicationReference)