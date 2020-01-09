# -*- coding: utf-8 -*-
"""Installer for the collective.reflex package."""

from setuptools import find_packages
from setuptools import setup


long_description = '\n\n'.join([
    open('README.rst').read(),
    open('CONTRIBUTORS.rst').read(),
    open('CHANGES.rst').read(),
])


setup(
    name='collective.reflex',
    version='2.8',
    description="An add-on for Plone",
    long_description=long_description,
    # Get more from https://pypi.org/classifiers/
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: Addon",
        "Framework :: Plone :: 4.3",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords='Python Plone',
    author='Rob Miller',
    author_email='robmr@openplans.org',
    url='',
    project_urls={
        # 'PyPI': 'https://pypi.python.org/pypi/collective.reflex',
        # 'Source': 'https://github.com/collective/collective.reflex',
        # 'Tracker': 'https://github.com/collective/collective.reflex/issues',
        # 'Documentation': 'https://collective.reflex.readthedocs.io/en/latest/',
    },
    license='GPL version 2',
    packages=find_packages('src', exclude=['ez_setup']),
    namespace_packages=['collective'],
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    python_requires="==2.7",
    install_requires=[
        'setuptools',
        # -*- Extra requirements: -*-
        'z3c.jbot',
        'Products.GenericSetup>=1.8.2',
        'plone.api>=1.8.4',
        'plone.restapi',
        'plone.app.dexterity',
        'plone.app.referenceablebehavior',
        'plone.app.relationfield',
        'plone.app.lockingbehavior',
        'plone.schema',
        'cachetools<4.0.0',
        'cryptography',
        'collective.freeze',
        'PyPDF2',
        'plone.app.registry',
        'plone.memoize',
        'plone.resource',
        'plone.synchronize',
        'python-slugify',
        'requests',
        'openpyxl==2.6.4',
        'collective.z3cform.datagridfield',  # ==1.1',
        'psutil',
        # 'xlrd',
        # 'xlwt',
        # 'pandas==0.24.2',
        # 'numpy==1.16.5',
        # 'matplotlib==2.2.4',
        # 'setuptools'
        # 'plone.behavior==1.3.0',
        # 'jsonschema==2.6.0'
        # 'plone.scale',
        # 'reportlab',
        # 'pdfminer',
        # 'pycrypto',
        # 'filetype',
        # 'collective.documentgenerator',
        # 'collective.taskqueue',
    ],
    extras_require={
        'test': [
            'plone.app.testing',
            # Plone KGS does not use this version, because it would break
            # Remove if your package shall be part of coredev.
            # plone_coredev tests as of 2016-04-01.
            'plone.testing>=5.0.0',
            'plone.app.robotframework[debug]',
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    [console_scripts]
    update_locale = collective.reflex.locales.update:update_locale
    """,
)
