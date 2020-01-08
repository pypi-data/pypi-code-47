import os
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()


setup(
    name='chaudhary',
    version='1.0',
    packages=['chaudhary'],
    description='farzi vala app',
    long_description=README,
    author='Achintya Ranjan Chaudhary',
    author_email='achintyac77@gmail.com',
    license='MIT',
    install_requires=[
    ]
)
