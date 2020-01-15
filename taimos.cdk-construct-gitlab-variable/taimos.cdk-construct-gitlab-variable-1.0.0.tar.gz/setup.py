import json
import setuptools

kwargs = json.loads("""
{
    "name": "taimos.cdk-construct-gitlab-variable",
    "version": "1.0.0",
    "description": "An AWS CDK Construct creates GITLAB CI/CD variables from SecretsManager Secrets",
    "license": "Apache-2.0",
    "url": "https://github.com/taimos/cdk-construct-gitlab-variable",
    "long_description_content_type": "text/markdown",
    "author": "Thorsten Hoeger<thorsten.hoeger@taimos.de>",
    "project_urls": {
        "Source": "https://github.com/taimos/cdk-construct-gitlab-variable"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "taimos.cdk_construct_gitlab_variable",
        "taimos.cdk_construct_gitlab_variable._jsii"
    ],
    "package_data": {
        "taimos.cdk_construct_gitlab_variable._jsii": [
            "cdk-construct-gitlab-variable@1.0.0.jsii.tgz"
        ],
        "taimos.cdk_construct_gitlab_variable": [
            "py.typed"
        ]
    },
    "python_requires": ">=3.6",
    "install_requires": [
        "jsii~=0.21.1",
        "publication>=0.0.3",
        "aws-cdk.aws-cloudformation==1.20.0",
        "aws-cdk.aws-lambda==1.20.0",
        "aws-cdk.aws-secretsmanager==1.20.0",
        "aws-cdk.core==1.20.0",
        "aws-cdk.custom-resources==1.20.0"
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
