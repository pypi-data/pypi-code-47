"""
Getting application settings from settings.py
"""
from django.conf import settings  # noqa

from appconf import AppConf

from django_magnificent_messages import constants


class MessageConfig(AppConf):
    LEVELS = constants.DEFAULT_LEVELS
    LEVEL_TAGS = constants.DEFAULT_TAGS
    MINIMAL_LEVEL = constants.INFO
    MESSAGE_FILES_UPLOAD_TO = constants.MESSAGE_FILES_UPLOAD_TO
    NOTIFICATION_STORAGE = constants.DEFAULT_NOTIFICATION_STORAGE
    MESSAGE_STORAGE = constants.DEFAULT_MESSAGE_STORAGE

    class Meta:
        prefix = 'DMM'


config = MessageConfig()
