#!/usr/bin/env python
"""
This docstring will appear as epilog of your --help
"""
# Copyright Netflix, 2019
import os

import click

# Implementation libs
import runez
from kaiju_mqtt_py import KaijuMqtt


@runez.click.command()
@runez.click.version()
@click.option(
    "--broker", type=str, required=True, envvar="RAE", help="The broker to connect to. Defaults to the environment variable 'RAE'."
)
@click.option(
    "--port", type=int, default=1883, showDefault=True, help="The port to connect to the broker on.",
)
@click.option("--topic", type=str, help="The topic to request on.")
@click.option(
    "--payload", type=str, help="The payload to deliver with the request. Usually json, but not required.",
)
@click.option("--debug", is_flag=True, help="Show debugging information.")
@runez.click.log()
def make_request(debug, log, broker, port, topic, payload):
    if debug:
        os.environ["DEBUG"] = "1"
    kmp = KaijuMqtt()
    kmp.connect(broker, port)

    # actually we will just forward strings too, but typically this is json in a string
    resp = kmp.request(topic, payload)
    # todo what else
    print(str(resp))
