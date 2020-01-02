import os

from django.conf import settings
from django.core.management.base import BaseCommand
from django.core.management.base import CommandError

from aorta.client import AortaClient


class Command(BaseCommand):

    def add_arguments(self, parser):
        """Adds the arguments for the Aorta client to the management
        command.
        """
        parser.add_argument('--container-id', type=str)

    def handle(self, *args, **kwargs):
        if not kwargs.get('host'):
            kwargs['host'] = settings.AORTA_INGRESS_HOST
        if not kwargs.get('port'):
            kwargs['port'] = settings.AORTA_INGRESS_PORT
        if not kwargs.get('channel'):
            kwargs['channel'] = settings.AORTA_INGRESS_CHANNEL
        try:
            AortaClient.run(**kwargs)
        except KeyboardInterrupt:
            return
