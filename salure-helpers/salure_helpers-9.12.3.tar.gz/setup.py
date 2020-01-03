from setuptools import setup

setup(
    name='salure_helpers',
    version='9.12.3',
    description='Files with helpful code, developed by Salure',
    url='https://bitbucket.org/salurebi/salure_helpers/',
    author='Salure',
    author_email='bi@salure.nl',
    license='Salure License',
    packages=['salure_helpers'],
    package_data={'salure_helpers': ['templates/*', 'datasets/*']},
    install_requires=[
        'pandas',
        'mandrill-really-maintained',
        'pymysql',
        'requests',
        'pysftp',
        'twine',
        'clickhouse-driver',
        'fs',
        'gnupg',
        'xmltodict',
        'zeep'
    ],
    zip_safe=False
)
