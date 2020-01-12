from setuptools import setup

# Use README for the PyPI page
with open('README.md') as f:
    long_description = f.read()

setup(
    name='gistolog',
    version='0.1',
    packages=['gistolog'],
    url='https://github.com/ivanjermakov/gistolog',
    license='MIT',
    author='Ivan Ermakov',
    author_email='ivanjermakov1@gmail.com',
    description='Use GitHub Gists for logging',
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=['PyGithub']
)
