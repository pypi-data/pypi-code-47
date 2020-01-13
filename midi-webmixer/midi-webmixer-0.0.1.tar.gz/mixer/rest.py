from flask import Flask, request
from flask_restful import Api, Resource
import mixer.send_cc as send_cc
import mixer.redis_store as redis_store
import mixer.utils as utils
import json
import os

app = Flask(__name__)
api = Api(app)


class Mixer(Resource):

    def __init__(self):

        self.midi = send_cc.midi(app.config['MIDI_PORT'])
        self.dataStore = redis_store.data(redis_host=app.config['REDIS_HOST'], redis_port=app.config['REDIS_PORT'])

        # Check that the channel data is already in redis, if not create it. This is also used in the mixer app.
        # Should probably seperate this out.
        if self.dataStore.get('channel_data'):
            self.channelMap = self.dataStore.get('channel_data')
        else:
            self.dataStore.set('channel_data', utils._createChannelMap())
        self.channelMap = self.dataStore.get('channel_data')

    def post(self, aux, channel, value):

        cc = self.channelMap[f'aux{aux}'][f'channel{channel}']['cc']
        self.channelMap[f'aux{aux}'][f'channel{channel}']['value'] = value
        self.dataStore.set('channel_data', self.channelMap)
        self.midi.cc_tx(cc, value)

        return {f'aux{aux}':{channel:value}}

    def get(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass

api.add_resource(Mixer, '/mixer/aux<int:aux>/<int:channel>/<int:value>', endpoint = 'mixer')

def run(port, debug, midi_port, redis_host, redis_port):

    app.config['MIDI_PORT'] = midi_port
    app.config['REDIS_HOST'] = redis_host
    app.config['REDIS_PORT'] = redis_port
    app.run(debug=debug, host='0.0.0.0', port=port)

if __name__ == '__main__':
    run()
