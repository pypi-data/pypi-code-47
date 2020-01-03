# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aleksis',
 'aleksis.core',
 'aleksis.core.migrations',
 'aleksis.core.templatetags',
 'aleksis.core.templatetags.templatetags',
 'aleksis.core.util']

package_data = \
{'': ['*'],
 'aleksis.core': ['dashboard/*',
                  'dashboard/templates/dashboard/*',
                  'dashboard/views/*',
                  'locale/ar/LC_MESSAGES/*',
                  'locale/de_DE/LC_MESSAGES/*',
                  'locale/fr/LC_MESSAGES/*',
                  'locale/nb_NO/LC_MESSAGES/*',
                  'locale/tr_TR/LC_MESSAGES/*',
                  'schoolapps/*',
                  'static/*',
                  'static/common/*',
                  'static/icons/*',
                  'static/img/*',
                  'static/js/*',
                  'templates/*',
                  'templates/common/*',
                  'templates/components/*',
                  'templates/core/*',
                  'templates/impersonate/*',
                  'templates/mail/*',
                  'templates/martor/*',
                  'templates/partials/*',
                  'templates/partials/paper/*',
                  'templates/registration/*',
                  'templates/two_factor/*',
                  'templates/two_factor/core/*',
                  'templates/two_factor/profile/*',
                  'tests/browser/*',
                  'tests/models/*',
                  'tests/templatetags/*',
                  'tests/views/*']}

install_requires = \
['Django>=3.0,<4.0',
 'Pillow>=7.0,<8.0',
 'colour>=0.1.5,<0.2.0',
 'django-any-js>=1.0,<2.0',
 'django-bootstrap4>=1.0,<2.0',
 'django-dbsettings>=1.0.0,<2.0.0',
 'django-debug-toolbar>=2.0,<3.0',
 'django-easy-audit>=1.2rc1,<2.0',
 'django-hattori>=0.2,<0.3',
 'django-image-cropping>=1.2,<2.0',
 'django-impersonate>=1.4,<2.0',
 'django-ipware>=2.1,<3.0',
 'django-maintenance-mode>=0.14.0,<0.15.0',
 'django-material>=1.6.0,<2.0.0',
 'django-menu-generator>=1.0.4,<2.0.0',
 'django-middleware-global-request>=0.1.2,<0.2.0',
 'django-phonenumber-field[phonenumbers]>=3.0,<5.0',
 'django-sass-processor>=0.8,<0.9',
 'django-settings-context-processor>=0.2,<0.3',
 'django-tables2>=2.1,<3.0',
 'django-two-factor-auth[YubiKey,phonenumbers,Call,SMS]>=1.10.0,<2.0.0',
 'django-yarnpkg>=6.0,<7.0',
 'django_select2>=7.1,<8.0',
 'dynaconf[yaml,toml,ini]>=2.0,<3.0',
 'easy-thumbnails>=2.6,<3.0',
 'libsass>=0.19.2,<0.20.0',
 'psycopg2>=2.8,<3.0',
 'python-memcached>=1.59,<2.0',
 'requests>=2.22,<3.0']

extras_require = \
{'ldap': ['django-auth-ldap>=2.0,<3.0']}

setup_kwargs = {
    'name': 'aleksis',
    'version': '1.0a4.dev0',
    'description': 'AlekSIS (School Information System)\u200a—\u200aCore',
    'long_description': 'AlekSIS (School Information System)\u200a—\u200aCore\n==========================================\n\nWarning\n-------\n\n**This is a preview version of AlekSIS. Do not use with sensitive data. Especially, do not grant access to students yet.**\n\n\nWhat AlekSIS is\n----------------\n\nAlekSIS is a web-based school information system (SIS) which can be used to\nmanage and/or publish organisational subjects of educational institutions.\n\nIt was originally developed together with Städt. Leibniz-Gymnasium Remscheid\nas a proprietary product. Five years after the school stole the original\ncode base, as a complete re-implementation as well-designed, free and open\nsource software, BiscuIT-ng was started. In the meantime, students from the\nKatharineum in Lübeck implemented School-Apps with the same goals and tools.\nIn 2020, BiscuIT-ng and School-Apps were combined into AlekSIS.\n\nAlekSIS is a platform based on Django, that provides central funstions\nand data structures that can be used by apps that are developed and provided\nseperately. The core can interact closely with the Debian Edu / Skolelinux\nsystem.\n\nCore features\n--------------\n\nTBA.\n\nLicence\n-------\n\n::\n\n  Copyright © 2019, 2020 Dominik George <dominik.george@teckids.org>\n  Copyright © 2019 Martin Gummi <martin.gummi@teckids.org>\n  Copyright © 2019 Julian Leucker <leuckeju@katharineum.de>\n  Copyright © 2019 mirabilos <thorsten.glaser@teckids.org>\n  Copyright © 2018, 2019 Frank Poetzsch-Heffter <p-h@katharineum.de>\n  Copyright © 2019, 2020 Tom Teichler <tom.teichler@teckids.org>\n  Copyright © 2018, 2019, 2020 Jonathan Weth <wethjo@katharineum.de>\n  Copyright © 2019, 2020 Hangzhi Yu <yuha@katharineum.de>\n\n  Licenced under the EUPL, version 1.2 or later\n\nPlease see the LICENCE file accompanying this distribution for the\nfull licence text or on the `European Union Public Licence`_ website\nhttps://joinup.ec.europa.eu/collection/eupl/guidelines-users-and-developers\n(including all other official language versions).\n\n.. _AlekSIS: https://edugit.org/AlekSIS/AlekSIS\n.. _European Union Public Licence: https://eupl.eu/\n',
    'author': 'Dominik George',
    'author_email': 'dominik.george@teckids.org',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://aleksis.edugit.io/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
