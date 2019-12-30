"""Console script for zeroae-cli."""

import sys
import click
from click_plugins import with_plugins
from entrypoints import get_group_named


@with_plugins(get_group_named("zeroae.cli").values())
@click.group()
def cli(args=None):
    """zeroae command-line-interface"""
    return 0


if __name__ == "__main__":
    sys.exit(cli)  # pragma: no cover
