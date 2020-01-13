import setuptools

with open('README.rst') as file:

    readme = file.read()

name = 'locopt'

version = '0.0.0'

author = 'Exahilosys'

url = f'https://github.com/{author}/{name}'

setuptools.setup(
    name = name,
    version = version,
    author = author,
    url = url,
    license = 'MIT',
    description = 'Localized template access and format.',
    long_description = readme,
    py_modules = [
        name
    ]
)
