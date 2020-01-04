import argparse
import collections
import dataclasses
import re

import bs4
import requests
from prometheus_client import Gauge

from . import Exporter, Metric

from typing import cast, Any, Counter, Dict, Iterator, List

JSONType = Dict[str, Any]


@dataclasses.dataclass
class JenkinsConnection:
    url: str
    username: str
    password: str


@dataclasses.dataclass
class NodeInfo:
    api: Dict[str, Any]
    config: bs4.Tag


@dataclasses.dataclass
class NodesInfo:
    api: List[Dict[str, Any]]
    nodes: Dict[str, NodeInfo]


class JenkinsExporter(Exporter):
    def parse_args(self) -> argparse.Namespace:
        options = super(JenkinsExporter, self).parse_args()

        self.jenkins = JenkinsConnection(
            url=self.config['jenkins']['master_url'],
            username=self.config['jenkins']['username'],
            password=self.config['jenkins']['password']
        )

        return options

    def _fetch_json(self, url: str) -> JSONType:
        return cast(
            JSONType,
            requests.get(
                '{}/{}'.format(self.jenkins.url, url),
                auth=(self.jenkins.username, self.jenkins.password)
            ).json()
        )

    def _fetch_xml(self, url: str) -> bs4.BeautifulSoup:
        return bs4.BeautifulSoup(
            requests.get(
                '{}/{}'.format(self.jenkins.url, url),
                auth=(self.jenkins.username, self.jenkins.password)
            ).content,
            'xml'
        )

    def fetch_data(self) -> None:
        self.data_nodes = NodesInfo(
            api=[],
            nodes={}
        )

        # Fetch summary data we can get for all nodes via JSON API.
        self.data_nodes.api = cast(
            List[Dict[str, Any]],
            self._fetch_json('/computer/api/json?depth=1')['computer']
        )

        # For each node, fetch its configuration, and extract its JSON API data from the global structure.
        for node_info in self.data_nodes.api:
            display_name = node_info['displayName']

            if display_name == 'master':
                continue

            self.data_nodes.nodes[display_name] = NodeInfo(
                api=node_info,
                config=self._fetch_xml('/computer/{}/config.xml'.format(display_name))
            )

        self.data_queue = self._fetch_json('/queue/api/json')

    def _create_label_count_metric(self) -> Metric:
        labels: Counter[str] = collections.Counter()

        for display_name, node in self.data_nodes.nodes.items():
            node_labels = node.config.find('label').text.split(' ')

            for label in node_labels:
                labels[label] += 1

        metric = Gauge(
            'node_labels',
            'Number of executors having a given label',
            ['label']
        )

        for node_label, count in labels.items():
            metric.labels(
                label=node_label
            ).set(count)

        return metric

    def _create_build_count_metric(self) -> Metric:
        running_jobs: Counter[str] = collections.Counter()
        queued_jobs: Counter[str] = collections.Counter()

        # Running builds first
        for _, node in self.data_nodes.nodes.items():
            for executor in node.api['executors']:
                if executor['currentExecutable'] is None:
                    continue

                match = re.match(r'{}/job/(.+?)/\d+/'.format(self.jenkins.url), executor['currentExecutable']['url'])
                if match:
                    running_jobs[match.group(1)] += 1

        # Queued builds next
        for queue_item in self.data_queue['items']:
            if queue_item['_class'] != 'hudson.model.Queue$BuildableItem':
                continue

            queued_jobs[queue_item['task']['name']] += 1

        metric = Gauge(
            'build_count',
            'Number of builds of a given job',
            ['job', 'state']
        )

        for job_name, count in running_jobs.items():
            metric.labels(
                job=job_name,
                state='running'
            ).set(count)

        for job_name, count in queued_jobs.items():
            metric.labels(
                job=job_name,
                state='queued'
            ).set(count)

        return metric

    def create_metric(self) -> Iterator[Metric]:
        yield self._create_label_count_metric()
        yield self._create_build_count_metric()


def main() -> None:
    """
    Fetches metrics from Jenkins and exports them to Prometheus format.
    """

    JenkinsExporter().run()


if __name__ == "__main__":
    main()
