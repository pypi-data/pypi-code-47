# -*- coding: utf-8 -*-
"""Setup module for flask taxonomy."""
import os

from setuptools import setup

readme = open('README.rst').read()
OAREPO_VERSION = os.environ.get('OAREPO_VERSION', '3.1.1')

install_requires = [
]

tests_require = [
    'pytest>=4.6.3',
]

extras_require = {
    'postgresql': [
        'invenio-db[postgresql]>=1.0.0b3',
    ],
    'mysql': [
        'invenio-db[mysql]>=1.0.0b3',
    ],
    'sqlite': [
        'invenio-db>=1.0.0b3',
    ],
    'tests': [
        *tests_require,
        'oarepo[tests]~={version}'.format(
            version=OAREPO_VERSION)],
    'tests-es7': [
        *tests_require,
        'oarepo[tests-es7]~={version}'.format(
            version=OAREPO_VERSION)],
}

setup_requires = [
    'pytest-runner>=2.7',
]

g = {}
with open(os.path.join('invenio_oarepo_multilingual', 'version.py'), 'rt') as fp:
    exec(fp.read(), g)
    version = g['__version__']

setup(
    name="invenio_oarepo_multilingual",
    version=version,
    url="https://github.com/oarepo/invenio-oarepo-multilingual",
    license="MIT",
    author="Miroslav Simek",
    author_email="miroslav.simek@vscht.cz",
    description="Multilingual support for OARepo",
    zip_safe=False,
    packages=['invenio_oarepo_multilingual'],
    entry_points={
        'invenio_oarepo_mapping_includes': [
            'invenio_oarepo_multilingual=invenio_oarepo_multilingual.included_mappings'
        ],
        'invenio_jsonschemas.schemas': [
            'invenio_oarepo_multilingual = invenio_oarepo_multilingual.jsonschemas'
        ],
    },
    include_package_data=True,
    setup_requires=setup_requires,
    extras_require=extras_require,
    install_requires=install_requires,
    tests_require=tests_require,
    platforms='any',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Development Status :: 4 - Beta',
    ],
)
