import click
import cli.utilities.utils as utils
from requests import ConnectionError, HTTPError

from cli.command_utils import error_message
from disco.core.exceptions import NoCredentials


@click.group()
def cli():
    pass


def setup_cli():
    from cli import auth_commands, cluster_commands, job_commands, version_commands
    cli.add_command(auth_commands.login)
    cli.add_command(auth_commands.logout)
    cli.add_command(cluster_commands.cluster)
    cli.add_command(job_commands.job)
    cli.add_command(version_commands.version)


def check_version():
    if utils.is_update_needed():
        click.echo(click.style("There is a newer version. \nPlease upgrade using: pip install disco --upgrade\n", fg='yellow', bold='True'))


def main():
    check_version()
    try:
        setup_cli()
    except Exception as ex:
        print("Error while setting up cli")

    try:
        cli()
    except HTTPError as ex:
        error_message("Unknown error received from server")
    except ConnectionError as ex:
        error_message("Couldn't establish internet connection. "
                      "Please connect to the internet and try again")
    except NoCredentials as ex:
        error_message("You must be logged in to perform this operation")
    except Exception as ex:
        error_message("Unknown error occurred")


if __name__ == '__main__':
    main()


