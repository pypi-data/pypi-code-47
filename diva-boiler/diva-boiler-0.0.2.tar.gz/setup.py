from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='diva-boiler',
    version='0.0.2',
    author='Kitware, Inc.',
    author_email='kitware@kitware.com',
    description="a cli for interacting with stumpf server",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(include=['boiler']),
    include_package_data=True,
    install_requires=['attrs', 'boto3', 'click>=7.0', 'requests', 'requests-toolbelt', 'pyyaml'],
    entry_points={'console_scripts': ['boiler=boiler:cli']},
    license='Apache Software License 2.0',
)
