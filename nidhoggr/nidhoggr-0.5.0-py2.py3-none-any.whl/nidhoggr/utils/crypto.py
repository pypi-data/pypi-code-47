from base64 import b64encode, b64decode
from typing import NamedTuple
from uuid import uuid4

from M2Crypto import EVP, RSA, BIO

from nidhoggr.models.session import UserProperty, SignedUserProperty


class KeyPair(NamedTuple):
    private: bytes
    public: bytes

    @classmethod
    def generate(cls, *, bits: int = 4096) -> "KeyPair":
        """
        Generate an RSA keypair with an exponent of 65537 in PEM format

        :param: bits The key length in bits
        :return: Key pair with private and public keys
        """
        key = RSA.gen_key(bits, 65537)

        with BIO.MemoryBuffer() as buffer:
            key.save_key_bio(buffer, cipher=None)
            private_key = buffer.getvalue()

        with BIO.MemoryBuffer() as buffer:
            key.save_pub_key_bio(buffer)
            public_key = buffer.getvalue()

        del key
        return KeyPair(private=private_key, public=public_key)


def sign_property(*, private_key: bytes, prop: UserProperty) -> SignedUserProperty:
    key = EVP.load_key_string(private_key)
    key.reset_context(md="sha1")
    key.sign_init()
    key.sign_update(prop.value.encode("ascii"))
    signature = b64encode(key.sign_final()).decode("ascii")
    return SignedUserProperty(name=prop.name, value=prop.value, signature=signature)


def verify_property(*, public_key: bytes, prop: SignedUserProperty) -> bool:
    with BIO.MemoryBuffer(public_key) as buffer:
        key = EVP.load_key_bio_pubkey(buffer)
    key.reset_context(md="sha1")
    key.verify_init()
    key.verify_update(prop.value.encode("ascii"))
    result = (key.verify_final(b64decode(prop.signature)) == 1)
    del key
    return result


def generate_uuid() -> str:
    """Generate random UUID token like Java's UUID.toString()"""
    return uuid4().hex
