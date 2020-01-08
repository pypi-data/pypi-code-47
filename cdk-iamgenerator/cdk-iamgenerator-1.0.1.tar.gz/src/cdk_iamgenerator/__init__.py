"""
# CDK IAM Generator

[AWS CDK](https://aws.amazon.com/cdk/) construct helps create IAM Managed Policies and IAM Roles using JSON Configuration

This package is written in TypeScript and made available via [JSII](https://github.com/aws/jsii) to all other supported languages. Package are available on:

* [npm](https://www.npmjs.com/package/cdk-iamgenerator)
* [PyPI] Work in Progress.
* [GitHub packages for Java][Maven] Work in Progress.

## Quickstart

Install or update from npm

TypeScript/Javascript

```console
npm i cdk-iamgenerator

```

## Usage

** TypeScript **

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
from cdk_iam_generator import IamPolicyGenerator, IamRoleGenerator

IamPolicyGenerator(self, "IamPolicyGenerator",
    config_path="config/iam_generator_config.json",
    policy_path="config/policy"
)

IamRoleGenerator(self, "IamRoleGenerator",
    config_path="config/iam_generator_config.json"
)
```

## Prerequsites

Example: Place all the Policy Json files inside config/policy in your project root and policy file would look something like this:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "codecommit:CancelUploadArchive",
        "codecommit:UploadArchive"
      ],
      "Resource": "*"
    }
  ]
}
```

Configure the policies and roles to be created in config/iam_generator_config.json file and would look something like this:

```json
{
    "policies": [
        {
            "policy_name": "CodeCommitArchive",
            "description": "CodeCommitArchive policy",
            "policy_file": "CodeCommitArchive.json"
        },
        {
            "policy_name": "KMSPolicy",
            "description": "KMSPolicy policy",
            "policy_file": "KMSPolicy.json"
        },
        {
            "policy_name": "CreateServiceLinkedRoleECS",
            "description": "CreateServiceLinkedRoleECS policy",
            "policy_file": "CreateServiceLinkedRoleECS.json"
        },
        {
            "policy_name": "DeployService1",
            "description": "DeployService1 policy",
            "policy_file": "DeployService1.json"
        },
        {
            "policy_name": "DeployService2",
            "description": "DeployService2 policy",
            "policy_file": "DeployService2.json"
        }
    ],
    "roles": [
        {
            "role_name": "TestRole1",
            "trust_service_principal": ["apigateway.amazonaws.com","lambda.amazonaws.com"],
            "customer_managed_policies": ["DeployService1","DeployService2","KMSPolicy"],
            "aws_managed_policies": ["service-role/AmazonAPIGatewayPushToCloudWatchLogs"]
        },
        {
            "role_name": "TestRole2",
            "trust_service_principal": ["sns.amazonaws.com"],
            "trust_account_principal": ["748669239283"],
            "customer_managed_policies": ["CreateServiceLinkedRoleECS","CodeCommitArchive","KMSPolicy"],
            "aws_managed_policies": ["service-role/AmazonAPIGatewayPushToCloudWatchLogs"]
        },
        {
            "role_name": "TestRole3",
            "trust_service_principal": ["ec2.amazonaws.com","sns.amazonaws.com"],
            "trust_account_principal": ["748669239283"],
            "customer_managed_policies": ["DeployService2","CodeCommitArchive","KMSPolicy"],
            "aws_managed_policies": ["AWSLambdaFullAccess"]
        }

    ]
}
```

## License

cdk-iamgenerator is distributed under the [Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0).

See [LICENSE](./LICENSE) for more information.
"""
import abc
import builtins
import datetime
import enum
import typing

import jsii
import jsii.compat
import publication

import aws_cdk.aws_iam
import aws_cdk.core

__jsii_assembly__ = jsii.JSIIAssembly.load("cdk-iam-generator", "1.0.1", __name__, "cdk-iam-generator@1.0.1.jsii.tgz")


class IamPolicyGenerator(aws_cdk.core.Construct, metaclass=jsii.JSIIMeta, jsii_type="cdk-iam-generator.IamPolicyGenerator"):
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, config_path: str, policy_path: str, description: typing.Optional[str]=None, env: typing.Optional[aws_cdk.core.Environment]=None, stack_name: typing.Optional[str]=None, tags: typing.Optional[typing.Mapping[str,str]]=None) -> None:
        """
        :param scope: -
        :param id: -
        :param config_path: 
        :param policy_path: 
        :param description: A description of the stack. Default: - No description.
        :param env: The AWS environment (account/region) where this stack will be deployed. Default: - The ``default-account`` and ``default-region`` context parameters will be used. If they are undefined, it will not be possible to deploy the stack.
        :param stack_name: Name to deploy the stack with. Default: - Derived from construct path.
        :param tags: Stack tags that will be applied to all the taggable resources and the stack itself. Default: {}
        """
        props = IamPolicyGeneratorProps(config_path=config_path, policy_path=policy_path, description=description, env=env, stack_name=stack_name, tags=tags)

        jsii.create(IamPolicyGenerator, self, [scope, id, props])


@jsii.data_type(jsii_type="cdk-iam-generator.IamPolicyGeneratorProps", jsii_struct_bases=[aws_cdk.core.StackProps], name_mapping={'description': 'description', 'env': 'env', 'stack_name': 'stackName', 'tags': 'tags', 'config_path': 'configPath', 'policy_path': 'policyPath'})
class IamPolicyGeneratorProps(aws_cdk.core.StackProps):
    def __init__(self, *, description: typing.Optional[str]=None, env: typing.Optional[aws_cdk.core.Environment]=None, stack_name: typing.Optional[str]=None, tags: typing.Optional[typing.Mapping[str,str]]=None, config_path: str, policy_path: str):
        """
        :param description: A description of the stack. Default: - No description.
        :param env: The AWS environment (account/region) where this stack will be deployed. Default: - The ``default-account`` and ``default-region`` context parameters will be used. If they are undefined, it will not be possible to deploy the stack.
        :param stack_name: Name to deploy the stack with. Default: - Derived from construct path.
        :param tags: Stack tags that will be applied to all the taggable resources and the stack itself. Default: {}
        :param config_path: 
        :param policy_path: 
        """
        if isinstance(env, dict): env = aws_cdk.core.Environment(**env)
        self._values = {
            'config_path': config_path,
            'policy_path': policy_path,
        }
        if description is not None: self._values["description"] = description
        if env is not None: self._values["env"] = env
        if stack_name is not None: self._values["stack_name"] = stack_name
        if tags is not None: self._values["tags"] = tags

    @builtins.property
    def description(self) -> typing.Optional[str]:
        """A description of the stack.

        default
        :default: - No description.
        """
        return self._values.get('description')

    @builtins.property
    def env(self) -> typing.Optional[aws_cdk.core.Environment]:
        """The AWS environment (account/region) where this stack will be deployed.

        default
        :default:

        - The ``default-account`` and ``default-region`` context parameters will be
          used. If they are undefined, it will not be possible to deploy the stack.
        """
        return self._values.get('env')

    @builtins.property
    def stack_name(self) -> typing.Optional[str]:
        """Name to deploy the stack with.

        default
        :default: - Derived from construct path.
        """
        return self._values.get('stack_name')

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[str,str]]:
        """Stack tags that will be applied to all the taggable resources and the stack itself.

        default
        :default: {}
        """
        return self._values.get('tags')

    @builtins.property
    def config_path(self) -> str:
        return self._values.get('config_path')

    @builtins.property
    def policy_path(self) -> str:
        return self._values.get('policy_path')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'IamPolicyGeneratorProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


class IamRoleGenerator(aws_cdk.core.Construct, metaclass=jsii.JSIIMeta, jsii_type="cdk-iam-generator.IamRoleGenerator"):
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, config_path: str, description: typing.Optional[str]=None, env: typing.Optional[aws_cdk.core.Environment]=None, stack_name: typing.Optional[str]=None, tags: typing.Optional[typing.Mapping[str,str]]=None) -> None:
        """
        :param scope: -
        :param id: -
        :param config_path: 
        :param description: A description of the stack. Default: - No description.
        :param env: The AWS environment (account/region) where this stack will be deployed. Default: - The ``default-account`` and ``default-region`` context parameters will be used. If they are undefined, it will not be possible to deploy the stack.
        :param stack_name: Name to deploy the stack with. Default: - Derived from construct path.
        :param tags: Stack tags that will be applied to all the taggable resources and the stack itself. Default: {}
        """
        props = IamRoleGeneratorProps(config_path=config_path, description=description, env=env, stack_name=stack_name, tags=tags)

        jsii.create(IamRoleGenerator, self, [scope, id, props])


@jsii.data_type(jsii_type="cdk-iam-generator.IamRoleGeneratorProps", jsii_struct_bases=[aws_cdk.core.StackProps], name_mapping={'description': 'description', 'env': 'env', 'stack_name': 'stackName', 'tags': 'tags', 'config_path': 'configPath'})
class IamRoleGeneratorProps(aws_cdk.core.StackProps):
    def __init__(self, *, description: typing.Optional[str]=None, env: typing.Optional[aws_cdk.core.Environment]=None, stack_name: typing.Optional[str]=None, tags: typing.Optional[typing.Mapping[str,str]]=None, config_path: str):
        """
        :param description: A description of the stack. Default: - No description.
        :param env: The AWS environment (account/region) where this stack will be deployed. Default: - The ``default-account`` and ``default-region`` context parameters will be used. If they are undefined, it will not be possible to deploy the stack.
        :param stack_name: Name to deploy the stack with. Default: - Derived from construct path.
        :param tags: Stack tags that will be applied to all the taggable resources and the stack itself. Default: {}
        :param config_path: 
        """
        if isinstance(env, dict): env = aws_cdk.core.Environment(**env)
        self._values = {
            'config_path': config_path,
        }
        if description is not None: self._values["description"] = description
        if env is not None: self._values["env"] = env
        if stack_name is not None: self._values["stack_name"] = stack_name
        if tags is not None: self._values["tags"] = tags

    @builtins.property
    def description(self) -> typing.Optional[str]:
        """A description of the stack.

        default
        :default: - No description.
        """
        return self._values.get('description')

    @builtins.property
    def env(self) -> typing.Optional[aws_cdk.core.Environment]:
        """The AWS environment (account/region) where this stack will be deployed.

        default
        :default:

        - The ``default-account`` and ``default-region`` context parameters will be
          used. If they are undefined, it will not be possible to deploy the stack.
        """
        return self._values.get('env')

    @builtins.property
    def stack_name(self) -> typing.Optional[str]:
        """Name to deploy the stack with.

        default
        :default: - Derived from construct path.
        """
        return self._values.get('stack_name')

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[str,str]]:
        """Stack tags that will be applied to all the taggable resources and the stack itself.

        default
        :default: {}
        """
        return self._values.get('tags')

    @builtins.property
    def config_path(self) -> str:
        return self._values.get('config_path')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'IamRoleGeneratorProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


__all__ = ["IamPolicyGenerator", "IamPolicyGeneratorProps", "IamRoleGenerator", "IamRoleGeneratorProps", "__jsii_assembly__"]

publication.publish()
