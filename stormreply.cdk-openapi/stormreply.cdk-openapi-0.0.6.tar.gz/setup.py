import json
import setuptools

kwargs = json.loads("""
{
    "name": "stormreply.cdk-openapi",
    "version": "0.0.6",
    "description": "@stormreply/cdk-openapi",
    "license": "Apache-2.0",
    "url": "https://github.com/stormreply/cdk-openapi.git",
    "long_description_content_type": "text/markdown",
    "author": "Henning Teek<h.teek@reply.com>",
    "project_urls": {
        "Source": "https://github.com/stormreply/cdk-openapi.git"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "stormreply.cdk_openapi",
        "stormreply.cdk_openapi._jsii"
    ],
    "package_data": {
        "stormreply.cdk_openapi._jsii": [
            "cdk-openapi@0.0.6.jsii.tgz"
        ],
        "stormreply.cdk_openapi": [
            "py.typed"
        ]
    },
    "python_requires": ">=3.6",
    "install_requires": [
        "jsii~=0.21.1",
        "publication>=0.0.3",
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
