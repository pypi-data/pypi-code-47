from sspo_db.model.stakeholder.models import Person, Developer
from sspo_db.service.stakeholder.service import PersonService, DeveloperService
from sspo_db.service.core.service import ApplicationReferenceService

class ApplicationPerson():
    
    def __init__(self):
        self.person_service = PersonService()
        self.application_reference_service = ApplicationReferenceService()
    
    def retrive_by_uuid(self, uuid):
        return self.person_service.get_by_uuid(uuid)
    

    def retrive_person_by_external_uuid (self, external_uuid):
        application_reference = self.application_reference_service.get_by_external_uuid(external_uuid)
        return self.person_service.get_by_uuid(application_reference.internal_uuid)

    def create_person(self, name, email, organization, description = ""):
        
        person = Person()
        person.name = name
        person.description = description
        person.email = email 
        person.organization = organization

        self.person_service.create(person)

        return person
        

class ApplicationStakeholder():

    def __ini__(self):
        self.develope_service = DeveloperService()
    
    def create_developer(self, person, team, team_role = ""):
        
        developer = Developer()
        developer.person = person
        developer.team = team 
        developer.team_role = team_role

        self.develope_service(developer)

    
    