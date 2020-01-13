#!/usr/bin/env python3

import click
import mixer.mixer
import mixer.rest
import netifaces
import os
from mixer.config import ConfigCheck
from rtmidi import midiutil


def print_midiports(ctx, param, value):

    if not value or ctx.resilient_parsing:
        return
    click.echo(midiutil.list_output_ports())
    ctx.exit()


@click.command()
@click.argument('config', type=click.Path(exists=True))
@click.option('--gui', is_flag=True)
@click.option('--restapi', is_flag=True)
@click.option('--port', default=5000, type=int)
@click.option('--debug', is_flag=True)
@click.option('--listmidi', is_flag=True, is_eager=True, expose_value=False, callback=print_midiports)
def start(config, gui, restapi, port, debug):

    """
    Read config and start the app
    """

    c = ConfigCheck(config)
    cfg = c.parse()
    interface = cfg['Network']['interface']
    ip_addr = netifaces.ifaddresses(interface)[2][0]['addr']
    channel_names = cfg['ChannelNames']
    midi_port = cfg['Midi']['port']
    redis_host = cfg['Services']['redis_host']
    redis_port = cfg['Services']['redis_port']
    gui_host = cfg['Services']['gui_host']
    gui_port = cfg['Services']['gui_port']

    # Allow for getting rest_host from env var
    if cfg['Services']['rest_host']:
        rest_host = cfg['Services']['rest_host']
    else:
        print('rest_host not set in config file - this may not be a problem')
        try:
            rest_host = os.environ['REST_HOST']
            print('rest_host not set in config, using REST_HOST environment variable')
        except KeyError as e:
            print(f'Error reading environment variable: {e}')

    rest_port = cfg['Services']['rest_port']

    if gui:
        mixer.mixer.run(port, debug, channel_names, ip_addr, redis_host, redis_port, rest_host, rest_port)
    if restapi:
        mixer.rest.run(port, debug, midi_port, redis_host, redis_port)

if __name__ == '__main__':
    start()
