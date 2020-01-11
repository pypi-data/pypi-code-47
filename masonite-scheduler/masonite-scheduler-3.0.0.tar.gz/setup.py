from setuptools import setup

setup(
    name="masonite-scheduler",
    version='3.0.0',
    package_dir={'': 'src'},
    packages=[
        'masonite.scheduler',
        'masonite.scheduler.commands',
        'masonite.scheduler.providers'
    ],
    author='Joe Mancuso',
    author_email='joe@masoniteproject.com',
    install_requires=[],
    include_package_data=True,
)
