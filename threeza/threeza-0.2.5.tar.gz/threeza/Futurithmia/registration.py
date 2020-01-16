#
from threeza.location import assert_algorithmia_web
assert_algorithmia_web(message="Intended for use inside Algorithmia Marketplace")


from threeza.crypto.primitives import to_public
import Algorithmia
from Algorithmia.acl import ReadAcl
client = Algorithmia.client()

def save_and_wave(private_key):
    # Save ...
    private_container = client.dir("data://.my/threeza_private")
    if not private_container.exists():
        private_container.create()
    private_key_file = client.file("data://.my/threeza_private/private_key.json")
    private_key_file.putJson({"key":private_key})
    # Wave ...
    public_key = to_public(private_key)
    public_container = client.dir("data://.my/threeza_public")
    if not public_container.exists():
        public_container.create(ReadAcl.public)
    public_key_file = client.file("data://.my/threeza_public/public_key.json")
    public_key_file.putJson({"key":public_key})
    return "https://algorithmia.com/v1/data/<YOUR USER NAME>/threeza_public/public_key.json"
