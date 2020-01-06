import json
import sys
import subprocess

from . import Exporter, Metric

from prometheus_client import Gauge

from typing import Any, Iterator


class OpenstackExporter(Exporter):
    def fetch_data(self) -> None:
        """
        Fetch a openstack data from server. ``self.data`` would become a structure like this:

          [{'Name': 'nameOfData', 'Value': 1024}, ...]
        """

        try:
            self.data = json.loads(
                subprocess.check_output(
                    "{0} limits show -f json --absolute --reserved".format(
                        self.get_command_openstack()
                    ),
                    shell=True
                )
            )
        except (subprocess.CalledProcessError, KeyError) as e:
            sys.stderr.write(
                "[ERROR] Phoebe Openstack: Can not fetch Openstack data.\n{0}{1}\n\n".format(type(e), e.args)
            )
            raise

    def get_command_openstack(self) -> str:
        """
        It uses credentials from settings to create an Openstack client command-line.

        :returns: Shell command to login to Openstack
        """
        return """
            openstack --os-auth-url={self.config[client][os_auth_url]} \
                        --os-identity-api-version={self.config[client][os_identity_api_version]} \
                        --os-user-domain-name={self.config[client][os_user_domain_name]} \
                        --os-project-domain-name={self.config[client][os_project_domain_name]} \
                        --os-project-name={self.config[client][os_project_name]} \
                        --os-username={self.config[client][os_username]} \
                        --os-password={self.config[client][os_password]} \
            """.format(self=self)

    def extract_value(self, name: str) -> Any:
        """
        It extract value from a Openstack statistical data.

        :param name str: A name of specific value
        :returns: A value of a given name
        """
        return list(filter(lambda d: d['Name'] == name, self.data))[0]['Value']

    def create_metric(self) -> Iterator[Metric]:
        """
        Generate Prometheus data for metrics. Definition of each metric is read from the configuration
        and yielded to the caller.
        """

        for metric_spes in self.config['metrics']:
            prom_metric = Gauge(
                metric_spes['name'], metric_spes['help'], ['type'],
            )

            for metric_label in metric_spes['labels']:
                prom_metric.labels(type=metric_label['type']).set(
                    self.extract_value(metric_label['os-property'])
                )

            yield prom_metric


def main() -> None:
    """
    Fetches metrics from Openstack and exports them to Prometheus format.
    """

    OpenstackExporter().run()


if __name__ == "__main__":
    main()
