from django.core.management.base import BaseCommand

from django_init.db.mysql import DatabaseMySQL
from django_init.db.postgresql import DatabasePostgreSQL
from django_init.management import add_arguments


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        add_arguments(parser)

    def handle(self, *args, **options):
        bd = DatabaseMySQL()
        bd.show_dbs()
        bd.create_db('tttttttt')
        bd.drop_db('tttttttt')

        bd = DatabasePostgreSQL()
        bd.show_dbs()
        bd.create_db('tttttttt')
        bd.drop_db('tttttttt')
