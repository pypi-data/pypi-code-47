from typing import List

import pgpy
from django.contrib.auth.hashers import PBKDF2PasswordHasher
from django.contrib.auth.models import AbstractUser
from django.db.models import QuerySet
from pgpy import PGPKey, PGPMessage
from pgpy.constants import SymmetricKeyAlgorithm, HashAlgorithm, PubKeyAlgorithm
from pgpy.errors import PGPError
from typing import List, Union

from django_pgpy import settings


def create_identity(name, email, password=None, restorer_public_keys: List[PGPKey] = []):
    key = create_key_pair(name, email)
    restorer_public_keys.append(key.pubkey)
    secret_blob = None
    hash_info = None

    if password:
        hash_info, password_hash = hash_password(password)
        # public_keys = [r.public_key for r in restorers]

        if restorer_public_keys:
            secret_blob = encrypt(password_hash, restorer_public_keys)
        encrypt_private_key_by_password(key, password_hash)

    return key, hash_info, secret_blob


def create_key_pair(name: str, email: str) -> PGPKey:
    key = pgpy.PGPKey.new(PubKeyAlgorithm.RSAEncryptOrSign, 4096)
    uid = pgpy.PGPUID.new(name, email=email)

    key.add_uid(uid,
                usage=settings.DJANGO_PGPY_KEY_USAGE,
                hashes=settings.DJANGO_PGPY_KEY_HASHES,
                ciphers=settings.DJANGO_PGPY_KEY_CIPHERS,
                compression=settings.DJANGO_PGPY_KEY_COMPRESSION)

    return key


def hash_password(password, hash_info=None):
    hasher = PBKDF2PasswordHasher()
    if hash_info:
        algo, iterations, salt = hash_info.split('$')
        return hasher.encode(password,
                             salt=salt,
                             iterations=int(iterations)).rsplit('$', 1)
    return hasher.encode(password, hasher.salt()).rsplit('$', 1)


def encrypt_private_key_by_password(key: PGPKey, password: str) -> PGPKey:
    assert key.is_unlocked

    key.protect(password, SymmetricKeyAlgorithm.AES256, HashAlgorithm.SHA256)
    return key


def create_session_key():
    cipher = pgpy.constants.SymmetricKeyAlgorithm.AES256
    sessionkey = cipher.gen_key()
    return cipher, sessionkey


def encrypt(text: str, public_keys: List[PGPKey]):
    cipher, sessionkey = create_session_key()

    msg = PGPMessage.new(text)
    for key in public_keys:
        msg = key.encrypt(msg, cipher=cipher, sessionkey=sessionkey)

    del sessionkey
    return msg


def add_encrypters(text, uid, password, encrypters):
    message = PGPMessage.from_blob(text)

    if not message.is_encrypted:
        raise PGPError("This message is not encrypted")

    if uid.private_key.fingerprint.keyid not in message.encrypters:
        raise PGPError("Cannot decrypt the provided message with this key")

    pkesk = next(pk for pk in message._sessionkeys if pk.pkalg == uid.private_key.key_algorithm and pk.encrypter == uid.private_key.fingerprint.keyid)
    with uid.unlock(password):
        cipher, sessionkey = pkesk.decrypt_sk(uid.private_key._key)

    for encrypter in encrypters:
        message = encrypter.public_key.encrypt(message, cipher=cipher, sessionkey=sessionkey)

    del sessionkey

    return message