import json

from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5

from .exceptions import WatchedError

public_key = """-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDRGLGD6gly5Ut0N34CsLwZJaxG
msFqWH3fnOwJiirzC4mfDyyjXuID3o6oSUiN7BNOz4oyt76ldC/XP3BqBJvhmoo7
wD3jzuxhWM+1zqzhuJKgedoL/slQtPHnpcAaZ2E2hEEyyHALoejyy/6ZxInZdILI
rl2iXzVO8gXUw97fDwIDAQAB
-----END PUBLIC KEY-----"""

rsakey = RSA.importKey(public_key)
signer = PKCS1_v1_5.new(rsakey)


def verify_signature(data):
    """Verifies the WATCHED signature string, and makes
    some basic checks about it's validity.
    """
    if not data:
        raise WatchedError("Missing signature")
    data = data.decode("base64")
    data = json.loads(data)
    digest = SHA256.new()
    digest.update(data["data"])
    if not signer.verify(digest, data["signature"].decode("base64")):
        raise WatchedError("Signature is invalid")

    authdata = json.loads(data["data"])

    # The validity of a signature should not be longer than 15 minutes
    if time.time()*1000 - authdata["time"] > 10*60*1000:
        raise WatchedError("Signature data timed out")

    if authdata["error"]:
        raise WatchedError(authdata["error"])

    if client_ip not in authdata["ips"]:
        raise WatchedError("Client IP is forbidden")

    return authdata
