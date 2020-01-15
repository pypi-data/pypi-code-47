from sspo_db.model.process.models import Sprint
from sspo_db.service.process.service import SprintService

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

        return self.sprint_service.create(sprint)

