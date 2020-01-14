from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sspo_db.model.stakeholder.models import *
from sspo_db.service.base_service import BaseService

class PersonService(BaseService):
    def __init__(self):
        super(PersonService,self).__init__(Person)

class TeamMemberService(BaseService):
    def __init__(self):
        super(TeamMemberService,self).__init__(TeamMember)

class TeamMemberService(BaseService):
    def __init__(self):
        super(TeamMemberService,self).__init__(TeamMember)