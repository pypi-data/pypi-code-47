from requests.exceptions import ConnectionError
from botocore.errorfactory import ClientError
from IPython.core import magic_arguments
from IPython.core.magic import register_cell_magic
from .interface.Interfaces import Interface, Interfaces
from IPython import get_ipython

import subprocess
import shutil
import base64
import docker
import boto3
import uuid
import os
import re

client_docker = docker.from_env()
cli_docker = docker.APIClient()
ipython = get_ipython()


class MLContext:

    def __init__(self, interface_type=Interfaces.GENERIC, interface=None, debug=False, **kwargs):
        self.region_name = os.environ.get('AWS_DEFAULT_REGION', 'us-east-1')
        self.user = os.environ.get('DORA_USER')
        self.variable = kwargs.get("variable")
        self.interface = Interface.get_interface(interface_type, interface, region_name=self.region_name)
        self.interface.command_ml(self)
        self.debug = debug

    def printd(self, *messages):
        """
        Utility used to display messages when debug mode is enabled
        ----------
        messages : list
            List of all messages to be painted
        """

        if self.debug:
            for message in messages:
                print(message)

    def new_model(self, name, code, artefacts, args):
        """
        Function that creates the model that can be done to deploy or versioning in ML
        ----------
        name : string
            Name to be given to the ML model
        code : string
            ML code which will be implemented
        artefacts : list
            Name to be given to the ML model
        args : argparse.Namespace
            Attribute that is passed when it is instantiated in the ML model.
        """

        self.debug = args.verbose
        self.printd(args)

        if (re.search(r"def[\s]+score[\s]*\(.*?\):", code) is None):
            raise SyntaxError("is missing a \"score\" function.")

        model = Model(name, code, artefacts, self.user, self.region_name, self.debug, args.tag)
        setattr(self, name, model)

        if self.variable:
            print("saved in variable '{}.{}'".format(self.variable, name))
        else:
            print("saved in variable '<this class>.{}'".format(name))


class Model:

    def __init__(self, name, code, artefacts, user, region_name=None, debug=False, tag=None):

        self.region_name = region_name
        self.client_ecr = boto3.client('ecr', region_name=self.region_name)
        self.code = code
        self.name = name
        self.artefacts = artefacts
        self.repository = None
        self.user = user
        self.debug = debug
        self.tag = tag

    def printd(self, *messages):
        """
        Utility used to display messages when debug mode is enabled
        ----------
        messages : list
            List of all messages to be painted
        """

        if self.debug:
            for message in messages:
                print(message)

    def create_template(self):
        """
        Create a build template by placing the code, process libs and attributes.
        ----------
        return : string
            returns where are the files for the build
        """

        tmp_name = str(uuid.uuid4())
        tmp_directory = os.path.join("/tmp", "ml", tmp_name + "/")
        directory = os.path.dirname(os.path.abspath(__file__))
        template_directory = os.path.join(directory, "template")

        shutil.copytree(template_directory, tmp_directory)
        try:
            with open(os.path.join(tmp_directory, "cp", "score", "code_score.py"), "ab") as file:
                file.write(self.code.encode('utf-8'))

            with open(os.path.join(tmp_directory, "cp", "requirements.txt"), "w") as file:
                libraries = subprocess.run(['pip', 'freeze'], stdout=subprocess.PIPE).stdout.decode("utf-8")
                file.write(libraries)

            for artifact in self.artefacts:
                absolute = os.path.abspath(artifact)
                destiny = os.path.join(tmp_directory, "cp", "score", artifact)

                try:
                    os.makedirs(os.path.dirname(destiny))
                except FileExistsError as e:
                    pass

                shutil.copy2(absolute, destiny)
        except Exception as e:
            shutil.rmtree(tmp_directory)
            raise Exception("Error: " + str(e))

        return tmp_directory

    def to_version(self):
        """
        Put the files in the notebook folder to versioning
        ----------
        """

        if self.tag is not None:
            notebooks_directory = os.path.join("./", self.name + "-" + self.tag + "/")
            self.printd(notebooks_directory)
        else:
            notebooks_directory = os.path.join("./", self.name + "/")
            self.printd(notebooks_directory)

        tmp_directory = self.create_template()
        self.printd(tmp_directory)
        shutil.copytree(tmp_directory, notebooks_directory)
        shutil.rmtree(tmp_directory)

    def build(self, args=None):
        """
        To build the model that was generated and coded, a repository will be created in the ECR with the model name and in the local docker plus the tag
        ----------
        args : dict
            A dictionary with the attributes to perform the build, such as name of the default image and user name, "IMAGE_BASE", "DORA_BUCKET", "DORA_USER".
        """

        tmp_directory = self.create_template()
        self.printd(tmp_directory)

        if tmp_directory is None:
            raise Exception("There was an error creating the directory for the code.")

        if args is None:
            args = dict()

        args["IMAGE_BASE"] = args["IMAGE_BASE"] if "IMAGE_BASE" in args else os.environ.get('IMAGE_BASE')
        args["DORA_BUCKET"] = args["DORA_BUCKET"] if "DORA_BUCKET" in args else os.environ.get('DORA_BUCKET', 'autonomous-sandbox')
        args["DORA_USER"] = args["DORA_USER"] if "DORA_USER" in args else self.user

        if self.name is not None:
            try:
                response_repository = self.client_ecr.create_repository(repositoryName="dora-" + str(self.name))
                self.repository = response_repository["repository"]["repositoryUri"]
                self.registry_id = response_repository["repository"]["registryId"]
            except ClientError as e:
                self.registry_id = re.findall(r"""(?:"|')(.+?)(?:'|")""", e.response["Error"]["Message"])[1]
                self.repository = "{registry_id}.dkr.ecr.{region_name}.amazonaws.com/{repository_name}".format(
                    registry_id=self.registry_id, region_name=self.region_name, repository_name="dora-" + str(self.name))
        else:
            raise Exception("Code name must not be null.")

        response_authorization = self.client_ecr.get_authorization_token()
        password = base64.b64decode(response_authorization['authorizationData'][0]['authorizationToken']).decode("utf-8").split(":")[1]
        client_docker.login(username="AWS", password=password, registry=response_authorization["authorizationData"][0]["proxyEndpoint"])

        if self.tag is not None:
            client_docker.images.build(path=tmp_directory, tag=self.repository + ":" + self.tag, forcerm=True, buildargs=args)
            self.printd(self.repository + ":" + self.tag)
        else:
            client_docker.images.build(path=tmp_directory, tag=self.repository, forcerm=True, buildargs=args)
            self.printd(self.repository)

        shutil.rmtree(tmp_directory)

    def run(self, command=None, wait=True, auto_remove=False):
        """
        Used to run the docker container and see the result of the model
        ----------
        command : string
            Command used to run the docker
        wait : boolean
            To wait for the default result True
        auto_remove : boolean
            To auto remove the docker container
        """

        self.printd(command)

        if self.tag is not None:
            self.printd("run-> " + self.repository + ":" + self.tag)
            container = client_docker.containers.run(image=self.repository + ":" + self.tag, detach=True, command=command, auto_remove=auto_remove)
        else:
            self.printd("run-> " + self.repository)
            container = client_docker.containers.run(image=self.repository, detach=True, command=command, auto_remove=auto_remove)

        if wait:
            container.wait()
            return container.logs().decode("utf-8")
        else:
            return container

    def deploy(self):
        """
        Used to make the model of the ECR deploy AWS, according to the model name and the tag
        ----------
        """

        if self.repository is not None:

            response_authorization = self.client_ecr.get_authorization_token(registryIds=[self.registry_id])
            password = base64.b64decode(response_authorization['authorizationData'][0]['authorizationToken']).decode("utf-8").split(":")[1]
            cli_docker.login(username="AWS", password=password, registry=response_authorization["authorizationData"][0]["proxyEndpoint"])

            try:
                if self.tag is not None:
                    self.printd(self.repository + ":" + self.tag)
                    cli_docker.push(self.repository + ":" + self.tag)
                else:
                    self.printd(self.repository)
                    cli_docker.push(self.repository)

            except ConnectionError as e:
                raise "Error: " + str(e)
        else:
            print("No repository found, please execute the method 'build()'")


class MLMagic:

    def __init__(self, MLContext):
        self.MLContext = MLContext
        ipython.register_magic_function(self.ml, 'cell')

    @magic_arguments.magic_arguments()
    @magic_arguments.argument('name', help='Nome da modulo autonomo.')
    @magic_arguments.argument('--verbose', '-v', action='store_true', help='Print Debug messages')
    @magic_arguments.argument('--tag', '-t', default=None, help='Tag para dockerfile')
    def ml(self, line, code=None):
        """
        Execute Machine Learning with Dora
        ----------
        code: string
            ML code which will be implemented

        Dora Version (2.0)
        -------
        ML 0.2.0
        """

        _code = re.sub(r"""%%ml[\s]+.+""", "", code)
        artefacts = re.findall(r"""%artefacts((?:[\s]+".+?")+)""", _code)
        args = magic_arguments.parse_argstring(self.ml, line)

        if (len(artefacts) != 0):
            _code = re.sub(r"""%artefacts((?:[\s]+".+?")+)""", "#%artefacts{}".format(artefacts[0]), _code)
            artefacts = re.findall(r"""(?:")(.+?)(?:")""", artefacts[0])

        else:
            print("Warning: No artifacts were added, to add use the \"%artefacts\" command.")

        self.MLContext.new_model(args.name, _code, artefacts, args)