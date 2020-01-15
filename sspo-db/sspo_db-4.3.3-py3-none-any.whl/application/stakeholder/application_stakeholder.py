from sspo_db.model.stakeholder.models import Person, Developer, ScrumMaster
from sspo_db.service.stakeholder.service import PersonService, DeveloperService, ScrumMasterService
from sspo_db.application.core.application_application_reference import ApplicationApplicationReference

class ApplicationPerson():
    
    def __init__(self):
        self.person_service = PersonService()
        self.application_reference_service = ApplicationApplicationReference()
    
    def retrive_by_uuid(self, uuid):
        return self.person_service.get_by_uuid(uuid)
    
    def retrive_person_by_external_uuid (self, external_uuid):
        
        application_reference = self.application_reference_service.get_by_external_uuid(external_uuid)
        if application_reference:
            return self.person_service.get_by_uuid(application_reference.internal_uuid)
        return None

    def create_person(self, name, email, organization, description = ""):
        
        person = Person()
        person.name = name
        person.description = description
        person.email = email 
        person.organization = organization

        self.person_service.create(person)

        return person
        

class ApplicationStakeholder():

    def __init__(self):
        self.developer_service = DeveloperService()
        self.scrum_master_service = ScrumMasterService()
    
    def create_developer(self, person, team, team_role = ""):
        
        developer = Developer()
        developer.name = team.name+" - "+person.name
        developer.description = person.description
        developer.person = person
        developer.team = team 
        developer.team_role = team_role

        self.developer_service.create(developer)

    def create_scrum_master(self, person, team, team_role = ""):
        
        scrum_master = ScrumMaster()
        scrum_master.name = team.name+" - "+person.name
        scrum_master.description = person.description
        scrum_master.person = person
        scrum_master.team = team 
        scrum_master.team_role = team_role

        self.scrum_master_service.create(scrum_master)
    
    