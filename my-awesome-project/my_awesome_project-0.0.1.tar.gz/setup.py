from setuptools import find_packages, setup

setup(
    name='my_awesome_project',
    version='0.0.1',
    author='PPG',
    author_email='ppg@mail.com',
    packages=find_packages(),
    include_packagae_data=True,
    description='Sample project for pip package'
)