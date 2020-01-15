import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='reproduce_wem_taxonomy',
    version='2020.01.14',
    author='Moritz Renftle',
    author_email='wem-taxonomy@momits.de',
    description='Reproduce the database of use cases for WEMs.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/momits/pubfisher/',
    package_dir={'': 'src'},
    packages=setuptools.find_packages('src'),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    install_requires=[
        # To fish publications
        'pubfisher',

        # To make type checks.
        'typeguard',

        # To store the publications in the database.
        'psycopg2'
    ],
    python_requires='>=3.7',
)
