# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['andotp_decrypt']
install_requires = \
['docopt>=0.6.2,<0.7.0',
 'pillow>=7.0.0,<8.0.0',
 'pycryptodome>=3.9.4,<4.0.0',
 'pyotp>=2.3.0,<3.0.0',
 'pyqrcode>=1.2.1,<2.0.0']

entry_points = \
{'console_scripts': ['andotp_decrypt = andotp_decrypt:main',
                     'andotp_gencode = generate_code:main',
                     'andotp_qrcode = generate_qr_codes:main']}

setup_kwargs = {
    'name': 'andotp-decrypt',
    'version': '0.1.0',
    'description': 'A backup decryptor for the andOTP Android app',
    'long_description': None,
    'author': 'asmw',
    'author_email': 'asmw@asmw.org',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'py_modules': modules,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
