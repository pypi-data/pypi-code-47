from sspo_db.model.process.models import Sprint
from sspo_db.service.process.service import SprintService, ScrumAtomicProjectService
from sspo_db.application.core.application_application_reference import ApplicationApplicationReference

class ApplicationSprint():

    def __init__(self):
        self.sprint_service = SprintService()
    
    def create (self, name, start_date, end_date, scrum_process):
        
        sprint = Sprint()
        sprint.name = name
        sprint.description = name
        sprint.startDate = start_date
        sprint.endDate = end_date
        sprint.scrum_process = scrum_process
        
        self.sprint_service.create(sprint)
        
        return sprint

class ApplicationScrumAtomic():
    
    def __init__(self):
        self.scrum_atomic_project_service = ScrumAtomicProjectService()
        self.application_application_reference = ApplicationApplicationReference()
    
    def retrive_by_external_uuid(self, external_uuid):
        application_reference = self.application_application_reference.get_by_external_uuid_and_seon_entity_name(external_uuid, "scrum_atomic_project")
        if application_reference:
            return self.scrum_atomic_project_service.get_by_uuid(application_reference.internal_uuid)
        return None
