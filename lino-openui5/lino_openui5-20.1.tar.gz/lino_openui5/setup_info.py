# -*- coding: UTF-8 -*-
# Copyright 2015-2020 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)

from __future__ import unicode_literals

SETUP_INFO = dict(
    name='lino_openui5',
    version='20.1',
    install_requires=['lino', 'lino_noi'],
    tests_require=[],
    test_suite='tests',
    description="The SAP Open Ui5 user interface for Lino",
    license='BSD-2-Clause',
    include_package_data=False,
    zip_safe=False,
    author='Luc Saffre',
    author_email='luc.saffre@gmail.com',
    url="http://www.lino-framework.org",
    classifiers="""\
  Programming Language :: Python
  Programming Language :: Python :: 3
  Development Status :: 5 - Production/Stable
  Environment :: Web Environment
  Framework :: Django
  Intended Audience :: Developers
  Intended Audience :: System Administrators
  License :: OSI Approved :: BSD License
  Natural Language :: English
  Natural Language :: French
  Natural Language :: German
  Operating System :: OS Independent
  Topic :: Database :: Front-Ends
  Topic :: Home Automation
  Topic :: Office/Business
  Topic :: Software Development :: Libraries :: Application Frameworks""".splitlines())

SETUP_INFO.update(long_description="""\

The SAP Open Ui5 user interface for Lino

The central project homepage is http://openui5.lino-framework.org/


""")

SETUP_INFO.update(packages=[str(n) for n in """
lino_openui5
lino_openui5.openui5
lino_openui5.projects
lino_openui5.projects.teamUi5
lino_openui5.projects.teamUi5.settings
lino_openui5.projects.teamUi5.tests
lino_openui5.projects.lydiaUi5
lino_openui5.projects.lydiaUi5.settings
lino_openui5.projects.lydiaUi5.tests
""".splitlines() if n])
