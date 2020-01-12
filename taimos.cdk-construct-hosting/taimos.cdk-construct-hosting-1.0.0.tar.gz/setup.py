import json
import setuptools

kwargs = json.loads("""
{
    "name": "taimos.cdk-construct-hosting",
    "version": "1.0.0",
    "description": "An AWS CDK Construct that provides website hosting",
    "license": "Apache-2.0",
    "url": "https://github.com/taimos/cdk-construct-sample",
    "long_description_content_type": "text/markdown",
    "author": "Thorsten Hoeger<thorsten.hoeger@taimos.de>",
    "project_urls": {
        "Source": "https://github.com/taimos/cdk-construct-sample"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "taimos.cdk_construct_hosting",
        "taimos.cdk_construct_hosting._jsii"
    ],
    "package_data": {
        "taimos.cdk_construct_hosting._jsii": [
            "cdk-construct-hosting@1.0.0.jsii.tgz"
        ],
        "taimos.cdk_construct_hosting": [
            "py.typed"
        ]
    },
    "python_requires": ">=3.6",
    "install_requires": [
        "jsii~=0.21.1",
        "publication>=0.0.3",
        "aws-cdk.aws-certificatemanager==1.20.0",
        "aws-cdk.aws-cloudfront==1.20.0",
        "aws-cdk.aws-route53==1.20.0",
        "aws-cdk.aws-route53-targets==1.20.0",
        "aws-cdk.aws-s3==1.20.0",
        "aws-cdk.aws-s3-deployment==1.20.0",
        "aws-cdk.core==1.20.0"
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
