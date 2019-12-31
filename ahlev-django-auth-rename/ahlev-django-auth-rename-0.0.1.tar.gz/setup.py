# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import auth_rename

setup(
    name='ahlev-django-auth-rename',
    version=auth_rename.__version__,
    description='to rename authentication and authorization',
    long_description='to rename authentication and authorization',
    long_description_content_type='text/x-rst',
    author='ahlev',
    author_email='ohahlev@gmail.com',
    include_package_data=True,
    url='https://github.com/ohahlev/ahlev-django-auth-rename/tree/%s' % auth_rename.__version__,
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    zip_safe=False,
)

# Usage of setup.py:
# $> python setup.py register             # registering package on PYPI
# $> python setup.py build sdist upload   # build, make source dist and upload to PYPI
