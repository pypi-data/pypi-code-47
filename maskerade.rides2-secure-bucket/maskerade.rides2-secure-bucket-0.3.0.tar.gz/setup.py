import json
import setuptools

kwargs = json.loads("""
{
    "name": "maskerade.rides2-secure-bucket",
    "version": "0.3.0",
    "description": "rides2-secure-bucket",
    "license": "ISC",
    "url": "https://github.com/maskerade/cdk-jsii-demo01.git",
    "long_description_content_type": "text/markdown",
    "author": "Stefan De Figueiredo",
    "project_urls": {
        "Source": "https://github.com/maskerade/cdk-jsii-demo01.git"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "maskerade.rides2_secure_bucket",
        "maskerade.rides2_secure_bucket._jsii"
    ],
    "package_data": {
        "maskerade.rides2_secure_bucket._jsii": [
            "rides2-secure-bucket@0.3.0.jsii.tgz"
        ],
        "maskerade.rides2_secure_bucket": [
            "py.typed"
        ]
    },
    "python_requires": ">=3.6",
    "install_requires": [
        "jsii~=0.21.1",
        "publication>=0.0.3",
        "aws-cdk.aws-s3>=1.20.0, <2.0.0",
        "aws-cdk.core>=1.20.0, <2.0.0"
    ],
    "classifiers": [
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Typing :: Typed",
        "License :: OSI Approved"
    ]
}
""")

with open('README.md') as fp:
    kwargs['long_description'] = fp.read()


setuptools.setup(**kwargs)
