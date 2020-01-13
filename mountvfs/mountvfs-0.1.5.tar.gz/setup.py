import setuptools


PACKAGE_NAME='mountvfs'
PACKAGE_AUTHOR='Annaz'
PACKAGE_AUTHOR_EMAIL='annazabn@gmail.com'
PACKAGE_DESCR='SSHFS, NFS clients.'


try:
   from pip._internal.req import parse_requirements
except ImportError:
   from pip.req import parse_requirements

try:
   from version import __version__ as version
except ImportError:
   exec(f'from {PACKAGE_NAME}.version import __version__ as version')


with open('README.md', 'r') as f: long_description=f.read()

setuptools.setup(
   name=PACKAGE_NAME,
   version=version,
   author=PACKAGE_AUTHOR,
   author_email=PACKAGE_AUTHOR_EMAIL,
   description=PACKAGE_DESCR,
   long_description=long_description,
   long_description_content_type='text/markdown',
   packages=setuptools.find_packages(),
   install_requires=[str(s.req) for s in parse_requirements('requirements.txt', session='hack')],
   python_requires='>=3.6',
)
