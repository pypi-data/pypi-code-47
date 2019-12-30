# -*- coding: UTF-8 -*-
#
# Copyright 2015-2020 Flavio Garcia
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import string
import sys


# Used implementations described on: http://bit.ly/2gHlH9z
# Recommended here: http://bit.ly/2fm97H3
# Confirmed here:
# https://docs.python.org/2/library/random.html#random.SystemRandom
# TODO: Use that after 3.6 https://bit.ly/2wvubJ6
def random_string(length=5, upper_chars=True, punctuation=False):
    """
    Generate a random string with the size equal to the given length.

    The string is based on random choices from a sequence of ascii lower case
    characters and digits.

    If length is not informed the string size will be 5.
    """
    chars = string.ascii_lowercase + string.digits
    if upper_chars:
        chars += string.ascii_uppercase
    if punctuation:
        chars += string.punctuation
    if sys.version_info < (3, 6):
        import random
        return ''.join(
            random.SystemRandom().choice(chars) for _ in range(length)
        )
    else:
        import secrets
        return ''.join(secrets.choice(chars) for _ in range(length))


class KeyManager(object):

    SALT_SIZE = 24

    def generate(self, password):
        # First is hash second is salt
        # Salt is generated randomly
        return None

    def create_hash(self, password, salt):
        return None

    def validate_password(self, password, correct_hash):
        return False


class Sha512KeyManager(KeyManager):
    # following: https://crackstation.net/hashing-security.htm

    def generate(self, password):
        salt = os.urandom(self.SALT_SIZE).encode('hex')
        return "%s:%s" % (self.create_hash(password, salt), salt)

    def create_hash(self, password, salt):
        import hashlib
        salted_password = "%s%s" % (password, salt)
        return hashlib.sha512(salted_password).hexdigest()

    def validate_password(self, password, correct_hash):
        correct_hashX = correct_hash.split(':')
        canditate_hash = "%s:%s" % (
            self.create_hash(password, correct_hashX[1]), correct_hashX[1])
        return canditate_hash == correct_hash
