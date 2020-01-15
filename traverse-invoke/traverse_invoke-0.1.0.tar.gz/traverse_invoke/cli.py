"""Console script for traverse_invoke."""
import sys
import click
import importlib


@click.command()
@click.argument('modname')
def main(modname):
    """Console script for traverse_invoke."""
    mod = importlib.import_module(modname)
    click.echo(mod.__name__)
    return 0

if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
