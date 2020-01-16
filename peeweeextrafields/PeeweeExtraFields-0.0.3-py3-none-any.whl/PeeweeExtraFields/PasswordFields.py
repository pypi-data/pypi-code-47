import hashlib
import random
import unicodedata

from peewee import *


def normalize_string(data: str) -> str:
    return unicodedata.normalize('NFKD', data)


def get_hexdigest(algorithm, salt, raw_password):
    """
    Returns a string of the hexdigest of the given plaintext password and salt
    using the given algorithm ('md5', 'sha1').
    """
    salt, raw_password = normalize_string(salt).encode(), normalize_string(raw_password).encode()
    if algorithm == 'md5':
        hash_maker = hashlib.md5()
        hash_maker.update(salt + raw_password)
        return hash_maker.hexdigest()
    elif algorithm == 'sha1':
        hash_maker = hashlib.sha1()
        hash_maker.update(salt + raw_password)
        return hash_maker.hexdigest()
    else:
        raise ValueError("Got unknown password algorithm type in password.")


def check_password(encrypted: str, raw_password: str) -> bool:
    algorithm, salt, hsh = encrypted.split('$')
    return hsh == get_hexdigest(algorithm, salt, raw_password)


class PasswordMD5Field(CharField):
    """
    Custom Field for Passwords in MD5 encryption.
    """

    def db_value(self, value: str) -> str:
        """
        Encode raw password with salt and MD5 algorithm.
        :param value: raw password
        :return: encoded password
        """
        if value is not None:
            algorithm = 'md5'
            salt = get_hexdigest(algorithm, str(random.random()), str(random.random()))[:5]
            hsh = get_hexdigest(algorithm, salt, value)
            return '%s$%s$%s' % (algorithm, salt, hsh)


class PasswordSHA1Field(CharField):
    """
    Custom Field for Passwords in SHA1 encryption.
    """

    def db_value(self, value: str) -> str:
        """
        Encode raw password with salt and MD5 algorithm.
        :param value: raw password
        :return: encoded password
        """
        if value is not None:
            algorithm = 'sha1'
            salt = get_hexdigest(algorithm, str(random.random()), str(random.random()))[:5]
            hsh = get_hexdigest(algorithm, salt, value)
            return '%s$%s$%s' % (algorithm, salt, hsh)
