from setuptools import setup
from adman.version import __version__ as adman_version

setup(
    name = 'adman',
    version = adman_version,
    description = 'Active Directory Automated Maintenance',
    author = 'Jonathon Reinhart',
    author_email = 'Jonathon.Reinhart@gmail.com',
    url = 'https://gitlab.com/JonathonReinhart/adman',
    python_requires = '>=3.4.0',
    packages = ['adman'],
    install_requires = [
        'python-ldap',      # python3-ldap on Fedora; python3-ldap on Debian Buster
        'dnspython',        # python3-dns on Fedora; python3-dnspython on Debian
        'PyYAML',           # python3-pyyaml on Fedora; python3-yaml on Debian
    ],
    include_package_data = True,
    license = 'MIT',
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Topic :: System :: Systems Administration :: Authentication/Directory',
    ],
    entry_points = {
        'console_scripts': [
            'adman = adman.cli:main',
        ]
    },
)
