import os
from setuptools import setup

# read the contents of your README file
this_dir = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_dir, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

install_requires = [
    'confluent-kafka >= 0.11.5'
]

setup(
    name = 'cronut',
    version = '0.0.1',
    description = 'Tasty event processing with Kafka',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url = 'https://gitlab.com/myNameIsPatrick/cronut',
    author = 'Patrick Godwin',
    author_email = 'patrick.godwin@psu.edu',
    license = 'BSD 3-Clause',

    packages = ['cronut'],

    install_requires = install_requires,

    classifiers = [
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Astronomy',
        'Topic :: Scientific/Engineering :: Physics',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Operating System :: MacOS',
        'License :: OSI Approved :: BSD License',
    ],

)
