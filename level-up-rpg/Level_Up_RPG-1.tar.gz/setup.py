from setuptools import setup


def readme():
    with open("README.md", "r") as fh:
        long_description = fh.read()
        return long_description


setup(
    name='Level_Up_RPG',
    version='1',
    packages=['Level_Up_RPG'],
    url='https://github.com/DtjiAppDev/LEVEL_UP_RPG',
    license='MIT',
    author='Dtji AppDev',
    author_email='dtjiappdev1999@gmail.com',
    description='This package contains implementation of the game "Level_Up_RPG".',
    long_description=readme(),
    long_description_content_type="text/markdown",
    include_package_data=True,
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7"
    ],
    entry_points={
        "console_scripts": [
            "Level_Up_RPG=Level_Up_RPG.level_up_rpg:main",
        ]
    }
)
