"""TurboGears Setup."""

import sys

# if not (2, 4) <= sys.version_info < (3, 0):
#     raise SystemExit("TurboGears 1.5 requires a Python version"
#         " between 2.4 and 2.7.")

# from ez_setup import use_setuptools
# use_setuptools()
from setuptools import setup, find_packages

version = "0.1.0"
description = "Front-to-back, open-source, rapid web development framework"
long_description = """
Front-to-back rapid web development
===================================

TurboGears brings together four major pieces to create an easy to
install, easy to use web mega-framework. It covers everything from
front end (MochiKit JavaScript for the browser, Genshi / Kid / Mako for
templates in Python) to the controllers (CherryPy) to the
back end (SQLAlchemy).

The TurboGears project is focused on providing documentation and
integration with these tools without losing touch with the communities
that already exist around those tools.

TurboGears is easy to use for a wide range of web applications.

The latest development version is available in the `TurboGears
subversion repository`_.

Our `mailing list`_ is lively and helpful, don't hesitate to send your
questions there, we will try to help you find out a solution to your
problem.

.. _mailing list:
    http://groups.google.com/group/turbogears

.. _TurboGears subversion repository:
    http://svn.turbogears.org/trunk#egg=turbogears-dev
"""

author = "BrightLink"
email = "drocco@thebrightlink.com"
maintainer = "BrightLink"
maintainer_email = "drocco@thebrightlink.com"
url = "https://bitbucket.org/brightlinkinfrastructure/nitrous"
download_url = f"https://bitbucket.org/brightlinkinfrastructure/nitrous/get/{version}.tar.gz"
dependency_links = [download_url]
copyright = "Copyright 2019 BrightLink and contributors"
license = "MIT"


# setup params
install_requires = [
    'future >= 0.17.1',
    'CherryPy >= 3.1.2',
    'ConfigObj >= 4.3.2',
    'FormEncode >= 1.2.1',
    'Genshi >= 0.4.4',
    # 'PEAK-Rules >= 0.5a1.dev-r2555',
    'setuptools >= 0.6c11',
    # 'TurboJson >= 1.3', # implies simplejson for Python < 2.6
    #'tgMochiKit >= 1.4.2',
    'TGScheduler >= 1.6.2',
]

# for when we get rid of Kid & SQLObject dependency
compat = [
    # 'TurboKid >= 1.0.5', # implies Kid
]

future = []

sqlalchemy = [
    # 'Elixir >= 0.6.1',
    'SQLAlchemy >= 0.4.3',
] + compat

toscawidgets = [
    # 'ToscaWidgets >= 0.9.12',
    # 'tw.forms >= 0.9.9',
]

testtools = [
    # 'nose >= 0.9.3',
    # 'WebTest >= 1.2.2',
    # 'python-dateutil >= 1.5, < 2.0a',
]

tgtesttools = testtools


develop_requires = (install_requires
    + future + tgtesttools + sqlalchemy)

setup(
    name='Nitrous',
    description=description,
    long_description=long_description,
    version=version,
    author=author,
    author_email=email,
    maintainer=maintainer,
    maintainer_email=maintainer_email,
    url=url,
    download_url=download_url,
    dependency_links=dependency_links,
    license=license,
    zip_safe=False,
    install_requires=install_requires,
    packages=find_packages(),
    include_package_data=True,
    exclude_package_data={'thirdparty': ['*']},
    entry_points = """
    [console_scripts]
    tg-admin = turbogears.command:main

    [distutils.commands]
    docs = turbogears.docgen:GenSite

    [turbogears.command]
    sql = turbogears.command.base:SQL
    shell = turbogears.command.base:Shell
    toolbox = turbogears.command.base:ToolboxCommand
    i18n = turbogears.command.i18n:InternationalizationTool
    info = turbogears.command.info:InfoCommand
    kid2genshi = turbogears.command.kid2genshi:Kid2Genshi

    [turbogears.identity.provider]
    sqlalchemy= turbogears.identity.saprovider:SqlAlchemyIdentityProvider

    [turbogears.extensions]
    identity = turbogears.identity.visitor
    visit = turbogears.visit

    [turbogears.visit.manager]
    sqlalchemy = turbogears.visit.savisit:SqlAlchemyVisitManager

    [turbogears.toolboxcommand]
    widgets = turbogears.toolbox.base:WidgetBrowser
    shell = turbogears.toolbox.shell:WebConsole
    admi18n = turbogears.toolbox.admi18n:Internationalization
    designer = turbogears.toolbox.designer:Designer
    info = turbogears.toolbox.base:Info
    catwalk = turbogears.toolbox.catwalk:CatWalk

    """,
    extras_require = {
        'compat': compat,
        'sqlalchemy': sqlalchemy,
        'toscawidgets': toscawidgets,
        'future': future,
        'testtools': testtools,
        'tgtesttools': tgtesttools,
        'develop': develop_requires,
    },
    tests_require=develop_requires,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Framework :: TurboGears',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules'],
    test_suite='nose.collector',
)
