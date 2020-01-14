from sspo_db.model.organization.models import Organization, ScrumTeam, DevelopmentTeam
from sspo_db.service.organization.service import OrganizationService, ScrumTeamService, DevelopmentTeamService

from sspo_db.model.process.models import ScrumAtomicProject, ScrumComplexProject, ScrumProject
from sspo_db.service.process.service import ScrumAtomicProjectService, ScrumComplexProjectService, ScrumProjectService

from sspo_db.model.process.models import ScrumProcess, ProductBacklogDefinition
from sspo_db.service.process.service import ScrumProcessService, ProductBacklogDefinitionService

from sspo_db.model.artifact.models import ProductBacklog
from sspo_db.service.artifact.service import ProductBacklogService

class ApplicationScrumProject():

    def __init__(self):

        self.scrum_project_service = ScrumProjectService()
        self.scrum_process_service = ScrumProcessService()
        self.scrum_atomic_project_service = ScrumAtomicProjectService()
        
        self.product_backlog_definition_service = ProductBacklogDefinitionService()
        self.product_backlog_service = ProductBacklogService()
        
        self.scrum_team_service = ScrumTeamService()
        self.development_team_service = DevelopmentTeamService()
    
    def create_scrum_process(self, name, description, scrum_project):
        
        scrum_process = ScrumProcess()
        
        scrum_process.name = name
        scrum_process.description = description
        scrum_process.scrum_project = scrum_project
        self.scrum_process_service.create(scrum_project)

        #Criando o product backlog definition
        product_backlog_definition = ProductBacklogDefinition()
        product_backlog_definition.name = name
        product_backlog_definition.description = description
        product_backlog_definition.scrum_process = scrum_process
                    
        self.product_backlog_definition_service.create(product_backlog_definition)
                    
        # Criando o backlog do projeto
        product_backlog = ProductBacklog()
        product_backlog.name = name
        product_backlog.description = description
        product_backlog.product_backlog_definition = product_backlog_definition.id
                    
        self.product_backlog_service.create(product_backlog)

        return scrum_process
    
    def create_scrum_team(self, name, description, scrum_project, organization):
        #criando o scrum team
        scrum_team = ScrumTeam()
        scrum_team.name = name
        scrum_team.description = description
        scrum_team.organization = organization
        scrum_team.scrum_project = scrum_project.id
                    
        self.scrum_team_service.create (scrum_team)

        development_team = DevelopmentTeam()
        development_team.name = name
        development_team.description = description
        #development_team.complex_team = scrum_team

        self.development_team_service.create (development_team)


        


