from setuptools import setup

setup(
    name='dsls',
    version='0.0.4',
    description='DSLs parent package',
    long_description=open('README.md').read(),
    url='https://github.com/python-memes-for-dsl-teens',
    author='python-memes-for-dsl-teens',
    author_email='david@daviddworken.com',
    packages=[],
    classifiers=['Development Status :: 1 - Planning'],
    extras_require={
        'results': 'magicresult'
    }
)
