#!/usr/bin/env python3

import json
from contextlib import contextmanager
from datetime import datetime
from os import environ

import click

from ..main import run as run_smugapi


@click.group()
def cli():
    pass


@cli.command(help="display version and exit")
def version():
    from .. import version
    print("smugapi {}".format(version))


@cli.command(help="start http server")
@click.option('-b', '--bind',
        default='localhost', help="bind to what addr (localhost)")
@click.option('-p', '--port', default=8088,
        help="port for service to bind (8088)")
@click.option('-r', '--prefix', default='', help="prefix all routes with ...")
@click.option('-d', '--debug', is_flag=True, help="enable debug mode")
@click.option('-w', '--weatherbit', default='', help="weatherbit api key")
@click.option('-w', '--worldtradingdata',
        default='', help="worldtradingdata api key")
def run(bind, port, prefix, debug, weatherbit, worldtradingdata):
    print("running smugapi on port:{}{}".format(
        port, " in debug mode" if debug else ''
        ) )
    run_smugapi(
        port=port,
        addr=bind,
        debug=debug,
        prefix=prefix,
        weatherbit_key=weatherbit,
        worldtradingdata_key=worldtradingdata
        )


if __name__ == "__main__":
    cli()

