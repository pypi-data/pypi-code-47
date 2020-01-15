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

    
    def create_atomic_project (self, name, description, organization, scrum_complex_project=None):
        #Persistindo a classe no banco
        scrum_atomic_project = ScrumAtomicProject()
        scrum_atomic_project.name = name
        scrum_atomic_project.description = description
        scrum_atomic_project.organization = organization
        scrum_atomic_project.scrum_complex_project = scrum_complex_project
        
        #criando o projeto atomico
        self.scrum_atomic_project_service.create(scrum_atomic_project)
        
        return scrum_atomic_project

    def create_atomic_project_process_and_team(self, name, description, organization, scrum_complex_project=None):
        
        #criando o projeto atomico
        scrum_atomic_project = self.create_atomic_project(name, description, organization, scrum_complex_project)
        #Criando o processo
        scrum_process = self.create_scrum_process(name, description,scrum_atomic_project)
        #criando o team
        scrum_team = self.create_scrum_team(name, description, scrum_atomic_project, organization)

        return scrum_atomic_project, scrum_process, scrum_team
    
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
                    
        self.scrum_team_service.create(scrum_team)

        development_team = DevelopmentTeam()
        development_team.name = name
        development_team.description = description
        development_team.scrum_team_id = scrum_team.id
        
        self.development_team_service.create (development_team)
        
        return scrum_team


        


