from .deployer import Deployer
import click


@click.command()
@click.option("--dir", default="./", help="The directory to deploy as a Gamma project.")
def deploy(dir):
    deployer = Deployer(dir)
    deployer.deploy()


if __name__ == "__main__":
    deploy()
