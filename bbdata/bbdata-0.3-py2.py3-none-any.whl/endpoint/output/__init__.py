from .auth import Auth
from .info import Info
from .units import Units
from .types import Types
from .object_groups import ObjectGroups
from .objects import Objects
from .values import Values
from .user_groups import UserGroups
from .users import Users
from .me import Me
from .comments import Comments


class Output:

    def __init__(self):
        self.auth = Auth()
        self.info = Info(self.auth)
        self.units = Units(self.auth)
        self.types = Types(self.auth)
        self.object_groups = ObjectGroups(self.auth)
        self.objects = Objects(self.auth)
        self.values = Values(self.auth)
        self.user_groups = UserGroups(self.auth)
        self.users = Users(self.auth)
        self.me = Me(self.auth)
        self.comments = Comments(self.auth)

    def login(self):
        return self.auth.login()

    def logout(self):
        return self.auth.logout()


output = Output()
