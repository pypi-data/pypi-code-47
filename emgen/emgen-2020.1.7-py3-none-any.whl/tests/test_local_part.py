# -*- coding:utf-8 -*-

import random

from emgen.common import fake
from emgen.core import local_part


def test_local_part(trials: int = 99_999) -> None:
    """Test generation of random email address local-parts.

    Args:
        trials (int, optional): Number of tests to perform. Defaults to 99_999.

    """
    for _ in range(trials):
        length = random.randint(4, 64)
        username = random.choice([fake.username(), None])
        separator = random.choice("-+")

        local = local_part(
            length=length, username=username, separator=separator
        )
        assert 1 <= len(local) <= 64
