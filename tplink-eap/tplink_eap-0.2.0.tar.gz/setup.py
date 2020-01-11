from setuptools import setup

setup(
    name = 'tplink_eap',
    packages = ['tplink_eap'],
    install_requires=['requests>=2.18.4','aiohttp>=3.6.2'],
    version = '0.2.0',
    description = 'A library to communicate with the TP link EAP access point.',
    author='Ruud van der Horst',
    author_email='ik@ruudvdhorst.nl',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ' +
            'GNU Lesser General Public License v3 or later (LGPLv3+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Topic :: Home Automation',
        'Topic :: Software Development :: Libraries :: Python Modules'
        ]
)