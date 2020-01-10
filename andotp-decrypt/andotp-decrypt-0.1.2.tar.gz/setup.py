# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['andotp_decrypt', 'generate_code', 'generate_qr_codes']
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
    'version': '0.1.2',
    'description': 'A backup decryptor for the andOTP Android app',
    'long_description': '# andOTP-decrypt\n\nA backup decryptor for the [andOTP](https://github.com/andOTP/andOTP) Android app.\n\nThe tools in this package support the password based backup files of andOTP in both the current (0.6.3) old (0.6.2 and before) format.\n\nTools:\n\n- `andotp_decrypt.py`: A decryption tool for password-secured backups of the [andOTP](https://github.com/flocke/andOTP) two-factor android app.\n  - Output is written to stdout\n- `generate_qr_codes.py`: A tool to generate new, scanable QR code images for every entry of a dump\n  - Images are saved to the current working directory\n- `generate_code.py`: A tool to generate a TOTP token for an account in the backup\n\n## Installation\n\n`pip install andotp-decrypt`\n\nThe tools will be installed as:\n\n- `andotp_decrypt`\n- `andotp_gencode`\n- `andotp_qrcode`\n\n## Development Setup\n\n[Poetry](https://python-poetry.org/) install (recommended)\n\n- Install poetry\n  - `pip install poetry` (or use the recommended way from the website)\n- Install everything else\n  - `poetry install`\n- Launch the virtualenv\n  - `poetry shell`\n\nPip install\n\n- `sudo pip3 install -r requirements.txt` \n\nOn debian/ubuntu this should work:\n\n- `sudo apt-get install python3-pycryptodome python3-pyotp python3-pyqrcode python3-pillow python3-docopt`\n\n## Usage\n\n- Dump JSON to the console:\n  - `./andotp_decrypt.py /path/to/otp_accounts.json.aes`\n- Generate new QR codes:\n  - `./generate_qr_codes.py /path/to/otp_accounts.json.aes`\n- Generate a TOTP code for your google account:\n  - `./generate_code.py /path/to/otp_accounts.json.aes google`\n\n## Thanks\n\nThank you for contributing!\n\n- alkuzad\n- ant9000\n- anthonycicc\n- erik-h\n- romed\n- rubenvdham',
    'author': 'asmw',
    'author_email': 'asmw@asmw.org',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/asmw/andOTP-decrypt',
    'py_modules': modules,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
