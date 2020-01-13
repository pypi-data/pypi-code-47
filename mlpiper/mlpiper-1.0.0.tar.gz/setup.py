from setuptools import setup, find_packages
import os

# The directory containing this file
ROOT = os.path.dirname(os.path.abspath(__file__))

# The text of the README file
README = open(ROOT + "/README.md").read()

with open('requirements.txt') as f:
    install_requires = f.read().splitlines()

setup(
    name='mlpiper',
    version='1.0.0',
    description="An ML Pipeline to be executed by 'mlpiper' tool",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://mlpiper.github.io/mlpiper/mlcomp/",
    author="DataRobot",
    author_email="zohar.mizrahi@datarobot.com",
    license="Apache License 2.0",
    classifiers=[
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: MacOS",
        "Operating System :: POSIX",
        "Operating System :: Unix",
    ],
    zip_safe=False,
    include_package_data=True,
    package_data={'': ['*.json', '*.jar', '*.egg']},
    packages=find_packages('.'),
    # data_files=[('.', ['__main__.py', 'setup.py'])],
    scripts=["run_pipeline.sh"],
    install_requires=install_requires,
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*',
    # entry_points={
    #     'setuptools.installation': [
    #         ''
    #     ]
    # }
)
