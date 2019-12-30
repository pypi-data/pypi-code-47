"""
``click`` commands the VWS CLI.
"""

import dataclasses
import io
import sys
from pathlib import Path
from typing import Callable, Optional

import click
import yaml
from vws import VWS
from vws.exceptions import TargetProcessingTimeout

from vws_cli.error_handlers import handle_vws_exceptions
from vws_cli.options.credentials import (
    server_access_key_option,
    server_secret_key_option,
)
from vws_cli.options.targets import (
    ActiveFlagChoice,
    active_flag_option,
    application_metadata_option,
    target_id_option,
    target_image_option,
    target_name_option,
    target_width_option,
)


def base_vws_url_option(command: Callable[..., None]) -> Callable[..., None]:
    """
    An option decorator for choosing the base VWS URL.
    """
    click_option_function = click.option(
        '--base-vws-url',
        type=click.STRING,
        default='https://vws.vuforia.com',
        help='The base URL for the VWS API.',
        show_default=True,
    )

    return click_option_function(command)


@click.command(name='get-target-record')
@server_access_key_option
@server_secret_key_option
@target_id_option
@handle_vws_exceptions
@base_vws_url_option
def get_target_record(
    server_access_key: str,
    server_secret_key: str,
    target_id: str,
    base_vws_url: str,
) -> None:
    """
    Get a target record.

    \b
    See
    https://library.vuforia.com/articles/Solution/How-To-Use-the-Vuforia-Web-Services-API.htm#How-To-Retrieve-a-Target-Record.
    """
    vws_client = VWS(
        server_access_key=server_access_key,
        server_secret_key=server_secret_key,
        base_vws_url=base_vws_url,
    )
    record = vws_client.get_target_record(target_id=target_id)

    yaml_record = yaml.dump(dataclasses.asdict(record))
    click.echo(yaml_record)


@click.command(name='list-targets')
@server_access_key_option
@server_secret_key_option
@handle_vws_exceptions
@base_vws_url_option
def list_targets(
    server_access_key: str,
    server_secret_key: str,
    base_vws_url: str,
) -> None:
    """
    List targets.

    \b
    See
    https://library.vuforia.com/articles/Solution/How-To-Use-the-Vuforia-Web-Services-API.htm#How-To-Get-a-Target-List-for-a-Cloud-Database.
    """
    vws_client = VWS(
        server_access_key=server_access_key,
        server_secret_key=server_secret_key,
        base_vws_url=base_vws_url,
    )
    targets = vws_client.list_targets()
    yaml_list = yaml.dump(targets)
    click.echo(yaml_list)


@click.command(name='get-duplicate-targets')
@server_access_key_option
@server_secret_key_option
@target_id_option
@handle_vws_exceptions
@base_vws_url_option
def get_duplicate_targets(
    server_access_key: str,
    server_secret_key: str,
    target_id: str,
    base_vws_url: str,
) -> None:
    """
    Get a list of potential duplicate targets.

    \b
    See
    https://library.vuforia.com/articles/Solution/How-To-Use-the-Vuforia-Web-Services-API.htm#how-to-check-for-similar-targets.
    """
    vws_client = VWS(
        server_access_key=server_access_key,
        server_secret_key=server_secret_key,
        base_vws_url=base_vws_url,
    )
    record = vws_client.get_duplicate_targets(target_id=target_id)

    yaml_record = yaml.dump(record)
    click.echo(yaml_record)


@click.command(name='get-database-summary-report')
@server_access_key_option
@server_secret_key_option
@handle_vws_exceptions
@base_vws_url_option
def get_database_summary_report(
    server_access_key: str,
    server_secret_key: str,
    base_vws_url: str,
) -> None:
    """
    Get a database summary report.

    \b
    See
    https://library.vuforia.com/articles/Solution/How-To-Use-the-Vuforia-Web-Services-API.htm#How-To-Get-a-Database-Summary-Report.
    """
    vws_client = VWS(
        server_access_key=server_access_key,
        server_secret_key=server_secret_key,
        base_vws_url=base_vws_url,
    )
    report = vws_client.get_database_summary_report()
    yaml_report = yaml.dump(dataclasses.asdict(report))
    click.echo(yaml_report)


@click.command(name='get-target-summary-report')
@server_access_key_option
@server_secret_key_option
@target_id_option
@handle_vws_exceptions
@base_vws_url_option
def get_target_summary_report(
    server_access_key: str,
    server_secret_key: str,
    target_id: str,
    base_vws_url: str,
) -> None:
    """
    Get a target summary report.

    \b
    See
    https://library.vuforia.com/articles/Solution/How-To-Use-the-Vuforia-Web-Services-API.htm#How-To-Retrieve-a-Target-Summary-Report.
    """
    vws_client = VWS(
        server_access_key=server_access_key,
        server_secret_key=server_secret_key,
        base_vws_url=base_vws_url,
    )
    report = vws_client.get_target_summary_report(target_id=target_id)
    report_dict = dataclasses.asdict(report)
    report_dict['status'] = report_dict['status'].value
    report_dict['upload_date'] = str(report_dict['upload_date'])
    yaml_summary_report = yaml.dump(report_dict)
    click.echo(yaml_summary_report)


@click.command(name='delete-target')
@server_access_key_option
@server_secret_key_option
@target_id_option
@handle_vws_exceptions
@base_vws_url_option
def delete_target(
    server_access_key: str,
    server_secret_key: str,
    target_id: str,
    base_vws_url: str,
) -> None:
    """
    Delete a target.

    \b
    See
    https://library.vuforia.com/articles/Solution/How-To-Use-the-Vuforia-Web-Services-API.htm#How-To-Delete-a-Target.
    """
    vws_client = VWS(
        server_access_key=server_access_key,
        server_secret_key=server_secret_key,
        base_vws_url=base_vws_url,
    )

    vws_client.delete_target(target_id=target_id)


@click.command(name='add-target')
@server_access_key_option
@server_secret_key_option
@target_name_option
@target_width_option
@target_image_option(required=True)
@application_metadata_option
@active_flag_option
@handle_vws_exceptions
@base_vws_url_option
def add_target(
    server_access_key: str,
    server_secret_key: str,
    name: str,
    width: float,
    image_file_path: Path,
    active_flag_choice: ActiveFlagChoice,
    base_vws_url: str,
    application_metadata: Optional[str] = None,
) -> None:
    """
    Add a target.

    \b
    See
    https://library.vuforia.com/articles/Solution/How-To-Use-the-Vuforia-Web-Services-API#How-To-Add-a-Target
    """
    vws_client = VWS(
        server_access_key=server_access_key,
        server_secret_key=server_secret_key,
        base_vws_url=base_vws_url,
    )

    image_bytes = image_file_path.read_bytes()
    image = io.BytesIO(image_bytes)

    active_flag = {
        ActiveFlagChoice.TRUE: True,
        ActiveFlagChoice.FALSE: False,
    }[active_flag_choice]

    target_id = vws_client.add_target(
        name=name,
        width=width,
        image=image,
        active_flag=active_flag,
        application_metadata=application_metadata,
    )

    click.echo(target_id)


@click.command(name='update-target')
@server_access_key_option
@server_secret_key_option
@target_name_option(required=False)
@target_image_option(required=False)
@target_width_option(required=False)
@application_metadata_option
@active_flag_option(allow_none=True)
@target_id_option
@handle_vws_exceptions
@base_vws_url_option
def update_target(
    server_access_key: str,
    server_secret_key: str,
    target_id: str,
    image_file_path: Optional[Path],
    base_vws_url: str,
    name: Optional[str] = None,
    application_metadata: Optional[str] = None,
    active_flag_choice: Optional[ActiveFlagChoice] = None,
    width: Optional[float] = None,
) -> None:
    """
    Update a target.

    \b
    See
    https://library.vuforia.com/articles/Solution/How-To-Use-the-Vuforia-Web-Services-API#How-To-Update-a-Target
    """
    vws_client = VWS(
        server_access_key=server_access_key,
        server_secret_key=server_secret_key,
        base_vws_url=base_vws_url,
    )

    if image_file_path is None:
        image = None
    else:
        image_bytes = image_file_path.read_bytes()
        image = io.BytesIO(image_bytes)

    active_flag = {
        ActiveFlagChoice.TRUE: True,
        ActiveFlagChoice.FALSE: False,
        None: None,
    }[active_flag_choice]

    vws_client.update_target(
        name=name,
        target_id=target_id,
        image=image,
        application_metadata=application_metadata,
        active_flag=active_flag,
        width=width,
    )


_SECONDS_BETWEEN_REQUESTS_DEFAULT = 0.2

_SECONDS_BETWEEN_REQUESTS_HELP = (
    'The number of seconds to wait between requests made while polling the '
    'target status. '
    f'We wait {_SECONDS_BETWEEN_REQUESTS_DEFAULT} seconds by default, rather '
    'than less, than that to decrease the number of calls made to the API, to '
    'decrease the likelihood of hitting the request quota.'
)

_TIMEOUT_SECONDS_HELP = (
    'The maximum number of seconds to wait for the target to be processed.'
)


@click.command(name='wait-for-target-processed')
@click.option(
    '--seconds-between-requests',
    type=click.FloatRange(min=0.05),
    default=_SECONDS_BETWEEN_REQUESTS_DEFAULT,
    help=_SECONDS_BETWEEN_REQUESTS_HELP,
    show_default=True,
)
@click.option(
    '--timeout-seconds',
    type=click.FloatRange(min=0.05),
    default=300,
    help=_TIMEOUT_SECONDS_HELP,
    show_default=True,
)
@server_access_key_option
@server_secret_key_option
@target_id_option
@handle_vws_exceptions
@base_vws_url_option
def wait_for_target_processed(
    server_access_key: str,
    server_secret_key: str,
    target_id: str,
    seconds_between_requests: float,
    base_vws_url: str,
    timeout_seconds: float,
) -> None:
    """
    Wait for a target to be "processed". This is done by polling the VWS API.
    """
    vws_client = VWS(
        server_access_key=server_access_key,
        server_secret_key=server_secret_key,
        base_vws_url=base_vws_url,
    )

    try:
        vws_client.wait_for_target_processed(
            target_id=target_id,
            seconds_between_requests=seconds_between_requests,
            timeout_seconds=timeout_seconds,
        )
    except TargetProcessingTimeout:
        click.echo(f'Timeout of {timeout_seconds} seconds reached.', err=True)
        sys.exit(1)
