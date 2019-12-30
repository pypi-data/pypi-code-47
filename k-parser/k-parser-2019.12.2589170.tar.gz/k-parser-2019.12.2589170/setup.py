"""Setup package."""

import distutils
from datetime import datetime


def get_minor_version() -> int:
    """Number of seconds since the beginning of the month."""
    utc_now = \
        datetime.utcnow()
    utc_beginning_of_month = \
        datetime.utcnow().replace(day=1, hour=0, minute=0, second=0)
    return int((utc_now - utc_beginning_of_month).total_seconds())


def get_version():
    return datetime.utcnow().strftime(f'%Y.%m.{get_minor_version()}')


distutils.core.setup(
    name='k-parser',
    version=get_version(),
    packages=[
        'k.parser',
    ],
    install_requires=[
        'lark-parser==0.7.8',
    ],
)
