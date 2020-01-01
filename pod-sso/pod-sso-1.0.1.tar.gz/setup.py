from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()
version = {}
with open("sso/version.py") as fp:
    exec(fp.read(), version)

setup(
    name="pod-sso",
    version=version['__version__'],
    url="https://github.com/FanapSoft/pod-sso-python-sdk",
    license="MIT",
    author="ReZa ZaRe",
    author_email="rz.zare@gmail.com",
    description="This package for implementation of POD platform SSO APIs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=["pod", "single sign on", "sso", "pod sdk"],
    packages=find_packages(),
    install_requires=[
        "pod-base>=1,<2",
        "pycrypto>=2.6.1"
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
        'sso': ['*.ini', '*.json']
    },
    project_urls={
        "Documentation": "http://docs.pod.ir/v1.0.0.2/PODSDKs/python/5233/user",
        "Source": "https://github.com/FanapSoft/pod-sso-python-sdk",
        "Tracker": "https://github.com/FanapSoft/pod-sso-python-sdk/issues"
    }
)
