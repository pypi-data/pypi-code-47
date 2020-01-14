from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sspo_db.model.activity.models import *
from sspo_db.service.base_service import BaseService

class ScrumDevelopmentTaskService(BaseService):
    def __init__(self):
        super(ScrumDevelopmentTaskService,self).__init__(ScrumDevelopmentTask)

class ScrumIntentedDevelopmentTaskService(BaseService):
    def __init__(self):
        super(ScrumIntentedDevelopmentTaskService,self).__init__(ScrumIntentedDevelopmentTask)

class ScrumPerformedDevelopmentTaskService(BaseService):
    def __init__(self):
        super(ScrumPerformedDevelopmentTaskService,self).__init__(ScrumPerformedDevelopmentTask)

class DevelopmentTaskTypeService(BaseService):
    def __init__(self):
        super(DevelopmentTaskTypeService,self).__init__(DevelopmentTaskType)



