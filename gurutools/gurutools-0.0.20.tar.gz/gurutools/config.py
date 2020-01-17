from enum import Enum

class PERMISSION_GROUPS(Enum):
    OWNER = ['Owner']
    ADMIN_AND_UP = ['Owner', 'Admin']
    ADMIN = ['Admin']
    MEMBER_AND_UP = ['Owner', 'Admin', 'Member']
    MEMBER = ['Member']

class SPACE_ROLES(Enum):
    OWNER = 'Owner'
    ADMIN = 'Admin'
    MEMBER = 'Member'

class FEED_GROUPS(Enum):
    USER = 'user'
    SPACE = 'space'
    RECORD = 'record'
    INVOICE = 'invoice'
    APPOINTMENT = 'appointment'
    PRACTITIONER = 'practitioner'
    SYSTEM = 'system'
    TODO = 'todo'
    COMMUNICATION = 'communication'
    RELATIONSHIP = 'relationship'
    NOTE = 'note'
    STTEMENT = 'statement'
    APPOINTMENTGURU = 'appointmentguru'
    APPOINTMENTVIEW = 'appointmentview'
