"""Console script for network_connectivity_tester."""
import sys
import click
import daemon

from network_connectivity_tester.awsclient import AWSConnectivityTestClient


@click.command()
@click.option("--daemonize", is_flag=True, help="Daemonize worker process.")
@click.option("--region", default="us-east-2", help="AWS region.")
@click.option(
    "--registration-queue-name",
    required=True,
    help="Registration queue name that the orchestrator process uses.",
)
def main(daemonize, region, registration_queue_name):
    """Console script for network_connectivity_tester."""

    ct = AWSConnectivityTestClient(
        region=region, registration_queue_name=registration_queue_name
    )
    if daemonize:
        with daemon.DaemonContext():
            ct.loop()
    else:
        ct.loop()

    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
