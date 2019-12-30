import os

from django.core.management.base import BaseCommand
from django.core.management.base import CommandError

from aorta.client import AortaClient


class Command(BaseCommand):

    def add_arguments(self, parser):
        """Adds the arguments for the Aorta client to the management
        command.
        """
        parser.add_argument('--host', default=os.getenv('AORTA_INGRESS_HOST'))
        parser.add_argument('--port', type=int,
            default=os.getenv('AORTA_INGRESS_PORT') or 5672)
        parser.add_argument('--channel', type=str,
            default=os.getenv('AORTA_INGRESS_CHANNEL'))
        parser.add_argument('--container-id', type=str,
            default=os.getenv('AORTA_CONTAINER_ID'))

    def handle(self, *args, **kwargs):
        kwargs.setdefault('host', os.getenv('AORTA_HOST'))
        kwargs.setdefault('port', os.getenv('AORTA_PORT'))
        try:
            AortaClient.run(**kwargs)
        except KeyboardInterrupt:
            return
