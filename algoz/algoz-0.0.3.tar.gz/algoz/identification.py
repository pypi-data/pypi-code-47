

from algoz.location import assert_algorithmia_web
assert_algorithmia_web(message="Intended for use inside Algorithmia Marketplace")

from threeza.crypto.primitives import to_public
import Algorithmia
from Algorithmia.acl import ReadAcl
import json
client = Algorithmia.client()

with open('identification_config.json') as locations_json:
    identification_config = json.load(locations_json)

def save_and_wave(private_key):
    # Save ...
    private_container = client.dir(identification_config["private_container"])
    if not private_container.exists():
        private_container.create()
    private_key_file = client.file(identification_config["private_key_file"])
    private_key_file.putJson({"key":private_key})
    # Wave ...
    public_key = to_public(private_key)
    public_container = client.dir(identification_config["public_container"])
    if not public_container.exists():
        public_container.create(ReadAcl.public)
    public_key_file = client.file(identification_config["public_key_file"])
    public_key_file.putJson({"key":public_key})
    return public_key

def read_private_key():
    return json.loads(client.file(identification_config["private_key_file"]).getString())

def read_public_key():
    return json.loads(client.file(identification_config["public_key_file"]).getString())
