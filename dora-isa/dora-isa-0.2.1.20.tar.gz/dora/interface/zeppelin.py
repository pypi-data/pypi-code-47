import configparser
import os

from ..isa import ISAMagic
from ..ml import MLMagic
from .generic import Generic



ZEPPELIN_HOME = "/usr/lib/zeppelin"


class Zeppelin(Generic):

    def __init__(self, zeppelin, *args, **kargs):
        self.zeppelin = zeppelin
        self.shiro = configparser.ConfigParser()
        self.shiro.read(os.path.join(ZEPPELIN_HOME, "/conf/shiro.ini"))
        super().__init__(*args, **kargs)

    def get_user(self):
        user = self.zeppelin.getInterpreterContext().getAuthenticationInfo().getUser()
        pwd = self.shiro['users'][user].split(",")[0]

        return dict(userName=user, password=pwd)

    def show(self, dataframe):
        self.zeppelin.show(dataframe)

    def command_aux(self, ISAContext):
        ISAMagic(ISAContext)

    def command_ml(self, MLContext):
        MLMagic(MLContext)