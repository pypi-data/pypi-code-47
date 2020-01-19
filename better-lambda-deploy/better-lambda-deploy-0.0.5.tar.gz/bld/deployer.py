from .lambda_function import LambdaFunction
from .api_function import APIFunction
from jinja2 import Environment, FileSystemLoader
import os
import subprocess
import boto3


class Deployer(object):
    def __init__(self, dir, environment="prod"):
        self.dir = dir
        script_dir = os.path.dirname(os.path.realpath(__file__))
        self.jinja = Environment(loader=FileSystemLoader(script_dir))
        self.project_name = "legoon"
        self.environment = environment

    def deploy(self):
        # Running files to create subclasses.
        # TODO: Change these from hardcoded to dynamic.
        exec(open("function.py").read())
        exec(open("api.py").read())

        # Get all Lambda Functions.
        # TODO: Check to make sure ignoring the first one is safe.
        lambda_functions = []
        lambda_classes = LambdaFunction.__subclasses__()
        lambda_classes = lambda_classes[1:]
        for lambda_class in lambda_classes:
            # inst = lambda_class()
            lambda_functions.append({"name": lambda_class.__name__})

        # Get all APIFunctions.
        api_functions = []
        api_classes = APIFunction.__subclasses__()
        for api in api_classes:
            inst = api({}, {})
            methods = inst.get_methods()
            for method in methods:
                api_functions.append(
                    {"name": api.__name__, "endpoint": api.endpoint, "method": method}
                )

        # Creating SAM template.
        template = self.jinja.get_template("sam.j2")

        rendered = template.render(
            description="Test",
            functions=lambda_functions,
            api_functions=api_functions,
            environment_variables=[],
            dynamo_tables=[],
            subdomain=self.project_name,
        )
        f = open("template.yml", "w")
        f.write(rendered)
        f.close()

        # Creating S3 bucket for SAM.
        # TODO: Set this to create a random bucket if the name is taken or something.
        s3 = boto3.client("s3")
        s3.create_bucket(
            ACL="private", Bucket=f"{self.project_name}-{self.environment}"
        )

        # Run the SAM CLI to build and deploy.
        subprocess.run(
            ["sam", "build", "--use-container", "--debug"], cwd=self.dir, check=True
        )
        subprocess.run(
            [
                "sam",
                "package",
                "--s3-bucket",
                f"{self.project_name}-{self.environment}",
            ],
            cwd=self.dir,
        )
        subprocess.run(
            [
                "sam",
                "deploy",
                "--stack-name",
                f"{self.project_name}-{self.environment}",
                "--capabilities",
                "CAPABILITY_NAMED_IAM",
                "--s3-bucket",
                f"{self.project_name}-{self.environment}",
                "--parameter-overrides",
                f"ENVIRONMENT={self.environment}",
            ],
            cwd=self.dir,
            check=True,
        )

        print("Deployed successfully.")
