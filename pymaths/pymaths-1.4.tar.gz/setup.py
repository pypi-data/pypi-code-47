from setuptools import setup

setup(name='pymaths',
    version='1.4',
    description='An advanced maths plugin for Python 3.',
    author='Matthew Byrne',
    author_email='matthewlukebyrne19@gmail.com',
    license='MIT',
    url="https://matthew-byrne.co.uk",
    packages=['pymaths.functions', 'pymaths.constants'],
    requires=['sympy'],
    zip_safe=False)