from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open("README.md", "r") as fh:
    long_description = fh.read()

version = {}
with open("pod_base/version.py") as fp:
    exec(fp.read(), version)

setup(
    name="pod-base",
    version=version['__version__'],
    url="https://github.com/FanapSoft/pod-base-python-sdk",
    license="MIT",
    author="ReZa ZaRe",
    author_email="rz.zare@gmail.com",
    description="Base package for implementation of POD platform APIs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=["pod", "pod sdk"],
    packages=find_packages(),
    install_requires=[
        "requests>=2.22",
        "jsonschema>=3.2"
    ],
    classifiers=[
        "Natural Language :: Persian",
        "Natural Language :: English",
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
    python_requires='>=2.7',
    package_data={
        'pod_base': ['*.ini']
    },
    project_urls={
        'Documentation': 'http://docs.pod.ir/v1.0.0.2/PODSDKs/python/5200/prerequisite',
        'Source': 'https://github.com/FanapSoft/pod-base-python-sdk',
        'Tracker': 'https://github.com/FanapSoft/pod-base-python-sdk/issues',
    }
)
