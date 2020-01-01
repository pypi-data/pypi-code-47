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
        kwargs.setdefault('host', settings.AORTA_INGRESS_HOST)
        kwargs.setdefault('port', settings.AORTA_INGRESS_PORT)
        kwargs.setdefault('channel', settings.AORTA_INGRESS_CHANNEL)
        try:
            AortaClient.run(**kwargs)
        except KeyboardInterrupt:
            return
