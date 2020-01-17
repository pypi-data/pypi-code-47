# coding: utf-8
"""
A module for sending monitoring statistics to Prometheus.
"""
import logging
import os
import socket

from cognite_prometheus.cognite_prometheus import CognitePrometheus
from prometheus_client import (
    CollectorRegistry,
    Counter,
    Gauge,
    Info,
    PlatformCollector,
    ProcessCollector,
)

logger = logging.getLogger(__name__)


class Monitor:
    labels = ["project_name"]

    def __init__(
        self, namespace: str, project_name: str, client: CognitePrometheus = None, registry: CollectorRegistry = None,
    ):
        self.namespace = namespace
        self.project_name = project_name
        self.prometheus = _configure_prometheus_client() if client is None else client
        self.registry = CognitePrometheus.registry if registry is None else registry

        self.label_values = {self.project_name}
        self._create_default_metrics()

        self.all_data_points_counter = self._create_metric(
            Counter, "posted_data_points_total", "Number of datapoints posted since the extractor started running",
        )

    def _create_default_metrics(self):
        """Create metrics for process, platform, and host."""
        self.info = Info("host", "Host info", namespace=self.namespace, registry=self.registry)
        self.info.info({"hostname": socket.gethostname(), "fqdn": socket.getfqdn()})
        self.process = ProcessCollector(namespace=self.namespace, registry=self.registry)
        self.platform = PlatformCollector(registry=self.registry)

    def _create_metric(self, metric_class, name, description):
        """Create a new metric of 'metric_class' with 'name' and 'description'."""
        return metric_class(
            name, description, namespace=self.namespace, labelnames=self.labels, registry=self.registry,
        ).labels(*self.label_values)

    def push(self):
        """Push current metrics to the Prometheus server."""
        try:
            self.prometheus.push_to_server()
        except Exception as exc:
            logger.error("Failed to push prometheus data: {!s}".format(exc))


def _configure_prometheus_client(jobname: str = None, username: str = None) -> CognitePrometheus:
    """Configure prometheus object, or return dummy object if not configured."""
    jobname = os.environ.get("COGNITE_PROMETHEUS_JOBNAME") if jobname is None else jobname
    username = os.environ.get("COGNITE_PROMETHEUS_USERNAME") if username is None else username
    password = os.environ.get("COGNITE_PROMETHEUS_PASSWORD")

    if not jobname or not username or not password:
        logger.warning("Prometheus is not configured: {} {}".format(jobname, username))
        unconfigured_dummy = True
    else:
        unconfigured_dummy = False

    try:
        CognitePrometheus(jobname, username, password, unconfigured_dummy=unconfigured_dummy)
    except Exception as exc:
        logger.error("Failed to create Prometheus client: {!s}".format(exc))
    return CognitePrometheus.get_prometheus_object()
