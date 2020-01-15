import json
import setuptools

kwargs = json.loads("""
{
    "name": "cdk-dynamo-table-viewer",
    "version": "3.1.1",
    "description": "cdk-dynamo-table-viewer",
    "license": "Apache-2.0",
    "url": "https://github.com/eladb/cdk-dynamo-table-viewer.git",
    "long_description_content_type": "text/markdown",
    "author": "Elad Ben-Israel<elad.benisrael@gmail.com>",
    "project_urls": {
        "Source": "https://github.com/eladb/cdk-dynamo-table-viewer.git"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "cdk_dynamo_table_viewer",
        "cdk_dynamo_table_viewer._jsii"
    ],
    "package_data": {
        "cdk_dynamo_table_viewer._jsii": [
            "cdk-dynamo-table-viewer@3.1.1.jsii.tgz"
        ],
        "cdk_dynamo_table_viewer": [
            "py.typed"
        ]
    },
    "python_requires": ">=3.6",
    "install_requires": [
        "jsii~=0.21.1",
        "publication>=0.0.3",
        "aws-cdk.aws-apigateway>=1.20.0, <2.0.0",
        "aws-cdk.aws-dynamodb>=1.20.0, <2.0.0",
        "aws-cdk.aws-lambda>=1.20.0, <2.0.0",
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
        "Development Status :: 4 - Beta",
        "License :: OSI Approved"
    ]
}
""")

with open('README.md') as fp:
    kwargs['long_description'] = fp.read()


setuptools.setup(**kwargs)
