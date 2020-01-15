#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path
from pathlib import Path

from setuptools import setup


def readme_text() -> str:
    projet_root_path = os.path.abspath(os.path.dirname(__file__))
    return Path(projet_root_path, 'README.md').read_text()


setup(
    name='bulk-mail-sender',
    version='0.1.1',
    description='Send emails in bulk with a CSV listing and a email template.',
    author='Clément Martinez',
    author_email='clementmartinezdev@gmail.com',
    url='https://github.com/moverest/bulk-mail-sender',
    long_description=readme_text(),
    long_description_content_type='text/markdown',
    install_requires=('click', 'mako'),
    packages=('bulk_mail_sender', ),
    entry_points={
        'console_scripts': [
            'bulk-mail-sender=bulk_mail_sender.main:main',
        ]
    },
)
