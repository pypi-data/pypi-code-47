from setuptools import setup

requires_package = [
    'pandas>=0.25.3',
    'numpy>=1.18.0'
]

classifiers=[
    'Development Status :: 1 - Production/Stable',
    'Intended Audience :: Developers',
    'Natural Language :: English',
    'License :: OSI Approved :: Apache Software License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: Implementation :: CPython',
    'Programming Language :: Python :: Implementation :: PyPy'
]

setup_dict = {
    'name': 'pd-read',
    'version': '0.1.1',
    'author': 'Vikas Shrivastava',
    'author_email': 'vshri119@gmail.com',
    'packages':['pdread'],
    'url':'https://pypi.python.org/pypi/PDRead/',
    'license':'LICENSE.txt',
    'description':'Read csv files with the help of pandas library !!',
    'long_description':open('README.txt').read(),
    'install_requires': requires_package,
    # 'classifiers': classifiers
}

try:
    from distutils.core import setup
except Exception:
    from setuptools import setup

setup(**setup_dict)
