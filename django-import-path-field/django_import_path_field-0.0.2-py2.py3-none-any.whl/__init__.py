# -*- coding: utf-8 -*-

from .db import ImportPathField
from .choices import ImportPathChoices

__all__ = ['ImportPathField', 'ImportPathChoices']

__version__ = '0.0.2'

default_app_config = 'importpath_field.apps.ImportpathFieldConfig'
