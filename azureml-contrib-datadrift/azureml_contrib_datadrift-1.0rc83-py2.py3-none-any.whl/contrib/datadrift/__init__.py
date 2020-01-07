# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
"""Deprecated: Please use azureml-datadrift instead. Will be removed soon."""

import logging

from azureml.datadrift.datadriftdetector import DataDriftDetector
from azureml.datadrift.alert_configuration import AlertConfiguration
from azureml.datadrift._datadiff import Metric, MetricType
from azureml.datadrift.model_serving_dataset import ModelServingDataset
from azureml._base_sdk_common import __version__ as VERSION

logger = logging.getLogger(__name__)

__all__ = ["DataDriftDetector", "Metric", "MetricType", "AlertConfiguration", "ModelServingDataset"]
__version__ = VERSION

logger.warning("Deprecated, please use the azureml-datadrift package instead.")
logger.warning("Deprecated, will no longer be updated in upcoming releases.")
