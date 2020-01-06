from .box import Box
from .config import sanboxConfig
import os 

class Challenge(object):
    def __init__(self, filename: str, code: str, challenge_input=None, host_path=None, timeout=None, cpu=None, pids_limit=None, memory=None):
        self.filename = filename
        self.code = code
        self.input = challenge_input
        self.host_path = host_path
        self.timeout = timeout
        self.cpu = cpu
        self.pids_limit = pids_limit
        self.memory = memory

    def initBox(self, config=sanboxConfig()):
        config['filename'] = self.filename 
        config['code'] = self.code
        config['input'] = self.input
        if self.host_path:
            config['host_path'] = self.host_path
        if self.cpu:
            config['cpu'] = self.cpu
        if self.timeout:
            config['timeout'] = self.timeout
        if self.pids_limit:
            config['pids_limit'] = self.pids_limit
        if self.memory:
            config['memory'] = self.memory
        # initialize the sandbox
        self.box = Box(config)

    def getDir(self) -> str:
        return self.host_path

    def getName(self) -> str: 
        return self.filename

    def getCode(self) -> str:
        return self.code