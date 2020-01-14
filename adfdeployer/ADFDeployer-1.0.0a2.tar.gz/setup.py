from setuptools import (
    find_packages,
    setup,
)

version = '1.0.0a2'

with open('README.md', 'r') as readme_file:
    long_description = readme_file.read()

setup(
    name='ADFDeployer',
    description='Continuously deploy an Azure Data Factory repository.',
    version=version,
    packages=find_packages(),
    author='ProRail DataTeam',
    author_email='d&a_datateam@prorail.nl',
    url='https://github.com/ProRailBDAP/adf-deployer',
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=[
        'azure-common >= 1.1.24',
        'requests >= 2.22.0',
    ],
    entry_points={
        'console_scripts': [
            'adf-deployer = ADFDeployer.runner:main'
        ]
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Version Control :: Git',
    ]
)
