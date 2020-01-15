import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="dockship",
    version="0.1.4",
    description="Run AI models in Docker containers",
    long_description=README,
    long_description_content_type="text/markdown",
    author_email='deepak@unrealai.xyz',
    author='Unreal AI Technologies Pvt. Ltd.',
    url='https://github.com/dockship/dockship',
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Operating System :: OS Independent",
    ],
    packages=["dockship"],
    install_requires=["fire", "requests", "tqdm", "alive-progress"],
    entry_points={
        "console_scripts": [
            "dockship=dockship.__main__:main",
        ]
    },
)
