from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sspo_db.model.artifact.models import *
from sspo_db.service.base_service import BaseService

class ProductBacklogService(BaseService):
    def __init__(self):
        super(ProductBacklogService,self).__init__(ProductBacklog)

class UserStoryService(BaseService):
    def __init__(self):
        super(UserStoryService,self).__init__(UserStory)

class EpicService(BaseService):
    def __init__(self):
        super(EpicService,self).__init__(Epic)

class AtomicUserStoryService(BaseService):
    def __init__(self):
        super(AtomicUserStoryService,self).__init__(AtomicUserStory)

class SprintBacklogService(BaseService):
    def __init__(self):
        super(SprintBacklogService,self).__init__(SprintBacklog)

class AcceptanceCriterionService(BaseService):
    def __init__(self):
        super(AcceptanceCriterionService,self).__init__(AcceptanceCriterion)

class NonFunctionalAcceptanceCriterionService(BaseService):
    def __init__(self):
        super(NonFunctionalAcceptanceCriterionService,self).__init__(NonFunctionalAcceptanceCriterion)

class FunctionalAcceptanceCriterionService(BaseService):
    def __init__(self):
        super(FunctionalAcceptanceCriterionService,self).__init__(FunctionalAcceptanceCriterion)