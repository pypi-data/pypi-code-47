from sspo_db.service.artifact.service import EpicService

class ApplicationEpic():
    
    def __init__(self):
        self.service = EpicService()
    
    def create (self, epic):
        self.service.create (epic)
        return epic
        