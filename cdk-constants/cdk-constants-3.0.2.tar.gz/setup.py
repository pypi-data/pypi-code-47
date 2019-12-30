import json
import setuptools

kwargs = json.loads("""
{
    "name": "cdk-constants",
    "version": "3.0.2",
    "description": "Library of helpful constants to work with the CDK",
    "license": "Apache-2.0",
    "url": "https://github.com/kevinslin/cdk-constants",
    "long_description_content_type": "text/markdown",
    "author": "Kevin S Lin<kevin@thence.io>",
    "project_urls": {
        "Source": "https://github.com/kevinslin/cdk-constants"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "cdk_constants",
        "cdk_constants._jsii"
    ],
    "package_data": {
        "cdk_constants._jsii": [
            "cdk-constants@3.0.2.jsii.tgz"
        ],
        "cdk_constants": [
            "py.typed"
        ]
    },
    "python_requires": ">=3.6",
    "install_requires": [
        "jsii~=0.20.11",
        "publication>=0.0.3"
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
