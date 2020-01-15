from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sspo_db.model.stakeholder.models import *
from sspo_db.service.base_service import BaseService

class PersonService(BaseService):
    
    def __init__(self):
        super(PersonService,self).__init__(Person)
    
    def retrive_person_by_external_id(self, external_id):
        pass

class TeamMemberService(BaseService):
    def __init__(self):
        super(TeamMemberService,self).__init__(TeamMember)

class DeveloperService(BaseService):
    def __init__(self):
        super(DeveloperService,self).__init__(Developer)

class ScrumMasterService(BaseService):
    def __init__(self):
        super(ScrumMasterService,self).__init__(ScrumMaster)

class ProductOwnerService(BaseService):
    def __init__(self):
        super(ProductOwnerService,self).__init__(ProductOwner)

class ClientService(BaseService):
    def __init__(self):
        super(ClientService,self).__init__(Client)