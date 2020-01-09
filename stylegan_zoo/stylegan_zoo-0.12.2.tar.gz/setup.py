import setuptools
import yaml

meta = yaml.load(open('./meta.yaml'), Loader=yaml.FullLoader)

setuptools.setup(
    name=meta['package']['name'],
    author='aster',
    author_email='galaster@foxmail.com',
    url=meta['source']['url'],
    version=meta['package']['version'],
    description='',

    packages=['sgan'],
    package_data={
        'sgan': ['license.txt', 'meta.yaml', 'License', 'Readme.md']
    },
    install_requires=[
        # no pytorch
        'matplotlib',
        'numpy',
        'wolframclient'
    ],
)
