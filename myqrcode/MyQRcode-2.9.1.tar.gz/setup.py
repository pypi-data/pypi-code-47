# -*- coding: utf-8 -*-

from distutils.core import setup

setup(
    name = 'MyQRcode',
    version = '2.9.1',
    keywords = ('qr', 'qrcode', 'qr code', 'artistic', 'animated', 'gif'),
    description = 'Generater for amazing QR Codes. Including Common, Artistic and Animated QR Codes.',

    author = 'xyz27900',
    author_email = 'xyz27900@gmail.com',
    url = 'https://github.com/xyz27900/qrcode',
    download_url = 'https://github.com/xyz27900/qrcode',

    install_requires = [
        'imageio >= 1.5',
        'numpy >= 1.11.1',
        'Pillow>=3.3.1'
    ],
    packages = ['MyQRcode', 'MyQRcode.mylibs'],
    
    license = 'GPLv3',
    classifiers = [
        'Programming Language :: Python :: 3',
        'Operating System :: MacOS',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Microsoft :: Windows',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
    ],
    entry_points = {
        'console_scripts': [
            'myqr = MyQRcode.terminal:main',
        ],
    }
)
