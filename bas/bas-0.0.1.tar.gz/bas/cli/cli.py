import click
from .g2p import g2p
from .maus import maus
from .subtitle import subtitle


@click.group()
def cli():
    pass


cli.add_command(g2p)
cli.add_command(maus)
cli.add_command(subtitle)