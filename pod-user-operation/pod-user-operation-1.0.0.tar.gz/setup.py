from setuptools import setup, find_packages
from user_operation import __version__


with open("README.md", "r") as fh:
    long_description = fh.read()

requires = ["pod-base>=1,<2"]

setup(
    name="pod-user-operation",
    version=__version__,
    url="https://github.com/FanapSoft/pod-user-operation-python-sdk",
    license="MIT",
    author="ReZa ZaRe",
    author_email="rz.zare@gmail.com",
    description="This package for implementation of POD platform User Operation APIs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=["pod", "user operation", "pod sdk"],
    packages=find_packages(),
    install_requires=requires,
    zip_safe=False,
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
        'user_operation': ['*.ini', '*.json']
    },
    project_urls={
        "Documentation": "http://docs.pod.ir/v1.0.0.2/PODSDKs/python/5202/user-operation",
        "Source": "https://github.com/FanapSoft/pod-user-operation-python-sdk",
        "Tracker": "https://github.com/FanapSoft/pod-user-operation-python-sdk/issues"
    }
)
