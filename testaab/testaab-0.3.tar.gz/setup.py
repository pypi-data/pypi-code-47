from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='testaab',
    packages=['testaab'],
    version='0.3',
    entry_points = {"console_scripts": ["solver=testaab.__init__:main"]},
)
