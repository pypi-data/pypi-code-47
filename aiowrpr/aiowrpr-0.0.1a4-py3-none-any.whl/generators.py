# -*- coding: utf-8 -*-
# Copyright 2019 Ildar.Shirshov <ildar-shirshov@ya.ru>
#  
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import random
import string


def make_random_string(pack: str = None, n: int = 15) -> str:
    """
    Function generates random string which
    specific string cases.
    :param pack: alphabet
    :param n: length of generated string
    :return: as is
    """
    if not pack:
        pack = string.ascii_uppercase + string.digits + string.ascii_lowercase

    for _ in range(n):
        yield random.SystemRandom().choice(pack)
