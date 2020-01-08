import json
import setuptools

kwargs = json.loads("""
{
    "name": "cdk-iamgenerator",
    "version": "1.0.1",
    "description": "This CDK Construct helps create IAM Managed Policies and IAM Roles using JSON Configuration",
    "license": "Apache-2.0",
    "url": "https://github.com/srihariph/cdk-iam-generator.git",
    "long_description_content_type": "text/markdown",
    "author": "Srihari Prabaharan<srihariph@gmail.com>",
    "project_urls": {
        "Source": "https://github.com/srihariph/cdk-iam-generator.git"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "cdk_iamgenerator",
        "cdk_iamgenerator._jsii"
    ],
    "package_data": {
        "cdk_iamgenerator._jsii": [
            "cdk-iam-generator@1.0.1.jsii.tgz"
        ],
        "cdk_iamgenerator": [
            "py.typed"
        ]
    },
    "python_requires": ">=3.6",
    "install_requires": [
        "jsii~=0.20.11",
        "publication>=0.0.3",
        "aws-cdk.aws-iam~=1.19,>=1.19.0",
        "aws-cdk.core~=1.19,>=1.19.0"
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
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved"
    ]
}
""")

with open('README.md') as fp:
    kwargs['long_description'] = fp.read()


setuptools.setup(**kwargs)
