from setuptools import find_packages, setup

setup(
    name='diva-boiler',
    version='0.0.1',
    author='Kitware, Inc.',
    author_email='kitware@kitware.com',
    packages=find_packages(include=['boiler']),
    include_package_data=True,
    install_requires=['attrs', 'boto3', 'click>=7.0', 'requests', 'requests-toolbelt', 'pyyaml'],
    entry_points={'console_scripts': ['boiler=boiler:cli']},
    license='Apache Software License 2.0',
)
