from distutils.core import setup
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='cthulhu-cult.database',
    packages=setuptools.find_packages(),
    version='0.1',
    license='Proprietary',
    description='SQL Alchemy entities for Cthulhu Cult project',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Przemyslaw Michalak',
    author_email='przemichalak@gmail.com',
    url='https://github.com/derzahal/cthulhu-cult-database',
    download_url='https://github.com/derzahal/cthulhu-cult-database/archive/v0.1.tar.gz',
    keywords=['CTHULHU', 'CULT', 'ENTITIES'],
    install_requires=[
        'sqlalchemy>=1.3.12'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: Other/Proprietary License',
        'Programming Language :: Python :: 3.6',
    ],
)
