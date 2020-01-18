from dataclasses import dataclass

@dataclass
class Config:
    '''POCO class for config data'''

    Workspace: str = ""
    Workflow: str = ""
    Baseflow: str = ""
    Backup: str = ""
    Selection: str = ""
    Edited: str = ""
    Preview: str = ""
    Editing: str = ""
    Instagram: str = ""

    def __str__(self):
        '''Overide the __str__ class
        
        Returns:
            (string): Returns the overrode string
        '''
        
        return f"""
                Workspace: {self.Workspace}
                Workflow: {self.Workflow}
                Baseflow: {self.Baseflow}
                Backup: {self.Backup}
                Selection: {self.Selection}
                Edited: {self.Edited}
                Preview: {self.Preview}
                Editing: {self.Editing}
                Instagram: {self.Instagram}
                """

@dataclass
class Context:
    '''POCO class for context data'''
    
    Config: str = ""
    WorkspaceObj: object = None
