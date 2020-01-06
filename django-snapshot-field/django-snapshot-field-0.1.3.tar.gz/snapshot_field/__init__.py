# -*- coding: utf-8 -*-
from .fields import SnapshotModelField
from . import monkey  # noqa

__all__ = ['SnapshotModelField']

__version__ = '0.1.3'

default_app_config = 'snapshot_field.apps.SnapshotFieldConfig'
