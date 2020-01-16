"""
[![npm version](https://badge.fury.io/js/%40taimos%2Fcdk-construct-gitlab-variable.svg)](https://badge.fury.io/js/%40taimos%2Fcdk-construct-gitlab-variable)
[![PyPI version](https://badge.fury.io/py/taimos.cdk-construct-gitlab-variable.svg)](https://badge.fury.io/py/taimos.cdk-construct-gitlab-variable)

# A CDK L3 Construct for storing Gitlab CI variables from a SecretsManager secret

## Installation

You can install the library into your project using npm or pip.

```bash
npm install @taimos/cdk-construct-gitlab-variable

pip3 install taimos.cdk-construct-gitlab-variable
```

## Usage

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
secret = Secret(self, "DBSecret",
    description="Some Secret",
    generate_secret_string={
        "secret_string_template": "{\"username\":\"admin2\"}",
        "generate_string_key": "password",
        "password_length": 20
    }
)

gitlab_secret = Secret.from_secret_arn(self, "GitlabToken", "arn:aws:secretsmanager:eu-central-1:123456789012:secret:GitlabToken-abcde")

db_password = GitlabVariable(self, "GitlabVarPassword",
    gitlab_secret=gitlab_secret,
    secret=secret,
    secret_field="password",
    project_id="group/secrets-test",
    variable_name="RDS_PASSWORD"
)
```

# Contributing

We welcome community contributions and pull requests.

# License

The CDK construct library is distributed under the [Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0).

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

import aws_cdk.aws_cloudformation
import aws_cdk.aws_lambda
import aws_cdk.aws_secretsmanager
import aws_cdk.core
import aws_cdk.custom_resources

__jsii_assembly__ = jsii.JSIIAssembly.load("@taimos/cdk-construct-gitlab-variable", "1.0.1", __name__, "cdk-construct-gitlab-variable@1.0.1.jsii.tgz")


class GitlabVariable(aws_cdk.core.Construct, metaclass=jsii.JSIIMeta, jsii_type="@taimos/cdk-construct-gitlab-variable.GitlabVariable"):
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, gitlab_secret: aws_cdk.aws_secretsmanager.ISecret, project_id: str, secret: aws_cdk.aws_secretsmanager.ISecret, variable_name: str, secret_field: typing.Optional[str]=None, server_url: typing.Optional[str]=None) -> None:
        """
        :param scope: -
        :param id: -
        :param gitlab_secret: the secret containing the Gitlab token to access the API.
        :param project_id: the project id within Gitlab ``group/project-name``.
        :param secret: the secret containing teh secret to publish to Gitlab.
        :param variable_name: the name of the variable to set in Gitlab.
        :param secret_field: the field name with the secret to publish. Default: - use the whole SecretString of the secret as value
        :param server_url: the URL of the Gitlab server. Default: https://gitlab.com
        """
        props = GitlabVariableProps(gitlab_secret=gitlab_secret, project_id=project_id, secret=secret, variable_name=variable_name, secret_field=secret_field, server_url=server_url)

        jsii.create(GitlabVariable, self, [scope, id, props])

    @jsii.member(jsii_name="ensureProvider")
    def ensure_provider(self, cr_lambda: aws_cdk.aws_lambda.IFunction) -> aws_cdk.custom_resources.Provider:
        """
        :param cr_lambda: -
        """
        return jsii.invoke(self, "ensureProvider", [cr_lambda])


@jsii.data_type(jsii_type="@taimos/cdk-construct-gitlab-variable.GitlabVariableProps", jsii_struct_bases=[], name_mapping={'gitlab_secret': 'gitlabSecret', 'project_id': 'projectId', 'secret': 'secret', 'variable_name': 'variableName', 'secret_field': 'secretField', 'server_url': 'serverUrl'})
class GitlabVariableProps():
    def __init__(self, *, gitlab_secret: aws_cdk.aws_secretsmanager.ISecret, project_id: str, secret: aws_cdk.aws_secretsmanager.ISecret, variable_name: str, secret_field: typing.Optional[str]=None, server_url: typing.Optional[str]=None):
        """
        :param gitlab_secret: the secret containing the Gitlab token to access the API.
        :param project_id: the project id within Gitlab ``group/project-name``.
        :param secret: the secret containing teh secret to publish to Gitlab.
        :param variable_name: the name of the variable to set in Gitlab.
        :param secret_field: the field name with the secret to publish. Default: - use the whole SecretString of the secret as value
        :param server_url: the URL of the Gitlab server. Default: https://gitlab.com
        """
        self._values = {
            'gitlab_secret': gitlab_secret,
            'project_id': project_id,
            'secret': secret,
            'variable_name': variable_name,
        }
        if secret_field is not None: self._values["secret_field"] = secret_field
        if server_url is not None: self._values["server_url"] = server_url

    @builtins.property
    def gitlab_secret(self) -> aws_cdk.aws_secretsmanager.ISecret:
        """the secret containing the Gitlab token to access the API."""
        return self._values.get('gitlab_secret')

    @builtins.property
    def project_id(self) -> str:
        """the project id within Gitlab ``group/project-name``."""
        return self._values.get('project_id')

    @builtins.property
    def secret(self) -> aws_cdk.aws_secretsmanager.ISecret:
        """the secret containing teh secret to publish to Gitlab."""
        return self._values.get('secret')

    @builtins.property
    def variable_name(self) -> str:
        """the name of the variable to set in Gitlab."""
        return self._values.get('variable_name')

    @builtins.property
    def secret_field(self) -> typing.Optional[str]:
        """the field name with the secret to publish.

        default
        :default: - use the whole SecretString of the secret as value
        """
        return self._values.get('secret_field')

    @builtins.property
    def server_url(self) -> typing.Optional[str]:
        """the URL of the Gitlab server.

        default
        :default: https://gitlab.com
        """
        return self._values.get('server_url')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'GitlabVariableProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


__all__ = ["GitlabVariable", "GitlabVariableProps", "__jsii_assembly__"]

publication.publish()
