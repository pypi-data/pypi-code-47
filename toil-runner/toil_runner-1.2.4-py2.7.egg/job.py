from toil.job import Job
import os
from abc import ABCMeta, abstractmethod
import docker
import logging
import pwd
import getpass
import grp
import time
import socket
from sarge import run, Capture

job_exclude_list = [
    'image', 'volumes', 'network_mode', 'ipc', 'image_master_check'
]


class JobProcess(Job):
    __metaclass__ = ABCMeta

    def __init__(self, *args, **kwargs):
        self._jobName = "toil"
        self.debug = os.getenv('TOIL_DEBUG', False)

        for exclude_item in job_exclude_list:
            if exclude_item in kwargs.keys():
                kwargs.pop(exclude_item)
        print(kwargs)
        super(JobProcess, self).__init__(*args, **kwargs)

    @abstractmethod
    def pre_process(self):
        return True

    @abstractmethod
    def post_process(self):
        return True

    @abstractmethod
    def execute_command(self):
        pass

    @abstractmethod
    def get_command_line(self):
        pass

    @property
    def jobname(self):
        return self._jobName

    @jobname.setter
    def jobname(self, value):
        self._jobName = value

    @abstractmethod
    def _pre_process(self):
        pass

    @abstractmethod
    def _post_process(self):
        pass

    def run(self, fileStore):
        self.log("Runtime.{jobname}.Start={time}".format(jobname=self._jobName,
                                                         time=time.time()))
        self._pre_process()
        self.execute_command()
        self._post_process()
        self.log("Runtime.{jobname}.End={time}".format(jobname=self._jobName,
                                                       time=time.time()))


class JobShellProcess(JobProcess):
    def __init__(self, *args, **kwargs):
        super(JobShellProcess, self).__init__(*args, **kwargs)

    def execute_command(self):
        process = run(self.get_command_line(),
                      async_=False,
                      stdout=Capture(),
                      stderr=Capture())
        ret_code = any(process.returncodes)
        if ret_code:
            self.log(process.stderr.text, logging.ERROR)

        if self.debug:
            self.log(process.stderr.text, logging.INFO)

    def _post_process(self):
        return self.post_process()

    def _pre_process(self):
        return self.pre_process()


class JobDockerProcess(JobProcess):
    def __init__(self, *args, **kwargs):
        self._image = kwargs.get('image')
        self._volumes = kwargs.get('volumes')
        self.network_mode = kwargs.get('network_mode', None)
        self.ipc = kwargs.get('ipc', None)
        self.image_master_check = kwargs.get('image_master_check', False)
        self.timeout = os.getenv('DOCKER_TIMEOUT', 1000)
        if self._check_images() and self.image_master_check:
            raise ValueError("{Node}:{image} not found".format(
                node=socket.gethostname, image=self._image))
        super(JobDockerProcess, self).__init__(*args, **kwargs)

    def _check_volumes(self):
        for key in self._volumes.keys():
            if not os.path.exists(key):
                self.log("path {} not exist".format(key))
                raise ValueError("path {} not exist".format(key))

    def _check_images(self):
        client = docker.from_env(timeout=self.timeout)
        try:
            client.images.get(self._image)
        except docker.errors.ImageNotFound as E:
            self.log(
                "{Node}:{image} not found".format(node=socket.gethostname,
                                                  image=self._image),
                logging.ERROR)
            raise ValueError("IMAGE")

    def _check_commandline(self):
        if not (isinstance(self.get_command_line(), str)
                and isinstance(self.get_command_line(), list)):
            self.log("get_command_line() return type is list or str",
                     logging.ERROR)

        if isinstance(self.get_command_line(), list):
            for arg in self.get_command_line():
                if not isinstance(arg, str):
                    self.log(
                        "get_command_line() return type is list,but element is not str",
                        logging.ERROR)

    def execute_command(self):
        client = docker.from_env(timeout=self.timeout)
        group_add = [
            g.gr_gid for g in grp.getgrall() if getpass.getuser() in g.gr_mem
        ]
        gid = pwd.getpwnam(getpass.getuser()).pw_gid
        group_add.append(gid)

        commmandsrt = self.get_command_line()
        if not self.ipc:
            container = client.containers.run(self._image,
                                              self.get_command_line(),
                                              volumes=self._volumes,
                                              network_mode=self.network_mode,
                                              user=pwd.getpwnam(
                                                  getpass.getuser()).pw_uid,
                                              group_add=group_add,
                                              detach=True)
        else:
            container = client.containers.run(self._image,
                                              self.get_command_line(),
                                              volumes=self._volumes,
                                              network_mode=self.network_mode,
                                              user=pwd.getpwnam(
                                                  getpass.getuser()).pw_uid,
                                              group_add=group_add,
                                              detach=True)
        stream = container.logs(stream=True)
        logs = ''
        for item in stream:
            logs += item
        if container.wait() != 0:
            self.log(str(self._volumes), logging.ERROR)
            self.log(logs, level=logging.ERROR)
            raise ValueError("EXIT Non-Zero")

        if self.debug:
            self.log(logs, logging.INFO)
        container.remove(v=True)

    def _post_process(self):
        return self.post_process()

    def _pre_process(self):
        self._check_images()
        self._check_volumes()
        self.pre_process()
        return True


class JobFactory(type):
    def __new__(cls, name, bases, dct):
        if os.getenv('TOIL_RUN_AS', 'docker') == 'docker':
            bases_ = (JobDockerProcess, )
        elif os.getenv('TOIL_RUN_AS') == 'shell':
            bases_ = (JobShellProcess, )
        return type(name, bases_, dct)