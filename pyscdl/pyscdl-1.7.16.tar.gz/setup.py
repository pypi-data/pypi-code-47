from setuptools import setup, find_packages
import scdl

setup(
    name='pyscdl',
    version=scdl.__version__,
    packages=find_packages(),
    author='DarkArtek',
    author_email='luca@ahd-creative.com',
    description='Download Music from SoundCloud',
    install_requires=[
        'docopt',
        'mutagen',
        'termcolor',
        'requests',
        'clint'
    ],
    url='https://github.com/AHDCreative/pyscdl',
    classifiers=[
        'Programming Language :: Python',
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet',
        'Topic :: Multimedia :: Sound/Audio',
    ],
    entry_points={
        'console_scripts': [
            'scdl = scdl.scdl:main'
        ],
    },
)
