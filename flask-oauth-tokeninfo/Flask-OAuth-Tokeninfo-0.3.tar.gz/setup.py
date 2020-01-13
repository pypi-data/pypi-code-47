"""
Flask-OAuth-Tokeninfo
-------------

This is the description for that library
"""
from setuptools import setup


setup(
    name='Flask-OAuth-Tokeninfo',
    version='0.3',
    url='https://cerebra.tech',
    license='proprietary',
    author='Cerebra',
    author_email='info@cerebra.tech',
    description='A library that authenticates using token info',
    long_description="todo",
    packages=['flask_oauth_tokeninfo'],
    # if you would be using a package instead use packages instead
    # of py_modules:
    # packages=['flask_sqlite3'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask',
        'requests'
    ],
    classifiers=[]
)