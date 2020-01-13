#!/usr/bin/env python3

import functools
from flask import Flask, Blueprint, flash, g, redirect, render_template, request, session, url_for
import json
import os
import socket
import mixer.redis_store as redis_store
import mixer.utils as utils

app = Flask(__name__)

@app.route('/mixer/<mix>', methods=('GET', 'POST'))
def mixer(mix):

    dataStore = redis_store.data(redis_host=app.config['REDIS_HOST'], redis_port=app.config['REDIS_PORT'])

    rest_ip = socket.gethostbyname(app.config['REST_HOST'])
    # Check that the channel data is already in redis, if not create it.
    # Should probably seperate this out.
    if dataStore.get('channel_data'):
        channelMap = dataStore.get('channel_data')
    else:
        dataStore.set('channel_data', utils._createChannelMap())
    channelMap = dataStore.get('channel_data')

    return render_template('mixer/mixer.html',
                            rest_host=rest_ip,
                            rest_port=app.config['REST_PORT'],
                            mix=mix,
                            channel_map=channelMap,
                            channel_names=app.config['CHANNEL_NAMES'])


def run(port, debug, channel_names,
        ip_addr, redis_host, redis_port,
        rest_host, rest_port):

    app.config['CHANNEL_NAMES'] = channel_names
    app.config['IP_ADDR'] = ip_addr
    app.config['REDIS_HOST'] = redis_host
    app.config['REDIS_PORT'] = redis_port
    app.config['REST_HOST'] = rest_host
    app.config['REST_PORT'] = rest_port
    app.run(debug=debug, host='0.0.0.0', port=port)


if __name__ == '__main__':
    run()
