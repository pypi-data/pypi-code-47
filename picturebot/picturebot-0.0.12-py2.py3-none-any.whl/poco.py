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


@dataclass
class Context:
    '''POCO class for context data'''
    
    Config: str = ""
    WorkspaceObj: object = None
