"""
# CDK Secrets

[![CDK docs](https://img.shields.io/badge/CDK-docs-orange)](https://awscdk.io/packages/cdk-secrets@0.4.0)
[![npm version](https://badge.fury.io/js/cdk-secrets.svg)](https://www.npmjs.com/package/cdk-secrets)
[![PyPI version](https://badge.fury.io/py/cdk-secrets.svg)](https://pypi.org/project/cdk-secrets/)
[![NuGet version](https://badge.fury.io/nu/CDK.Secrets.svg)](https://www.nuget.org/packages/CDK.Secrets/)
[![GitHub](https://img.shields.io/github/license/udondan/cdk-secrets)](https://github.com/udondan/cdk-secrets/blob/master/LICENSE)

> **WORK IN PROGRESS**
>
> While this is generally working, it is not ready for production.

[AWS CDK](https://aws.amazon.com/cdk/) construct to manage secrets. It makes use of a custom resource provider from [binxio/cfn-secret-provider](https://github.com/binxio/cfn-secret-provider).

This package is written in TypeScript and made available via [JSII](https://github.com/aws/jsii) to all other supported languages. Package are available on:

* [npm](https://www.npmjs.com/package/cdk-secrets)
* [PyPI](https://pypi.org/project/cdk-secrets/)
* [NuGet](https://www.nuget.org/packages/CDK.Secrets/)

The secret provider can create RSA keys, DSA keys, EC2 key-pairs, IAM user passwords and access keys and generally secrets stored in parameter store or secret store.

All this functionality is provided by the [binxio/cfn-secret-provider](https://github.com/binxio/cfn-secret-provider) custom resource.

## Examples

There is an example application in [./example](https://github.com/udondan/cdk-secrets/blob/master/example) showing how to create a new EC2 key pair.

When it comes to security, you should not trust anyone. By default the secret provider uses the lambda function stored on `s3://binxio-public-${AWS_REGION}/lambdas/cfn-secret-provider-1.0.0.zip`. You might want to download this file, review its contents and store it in your own bucket or along with your code. You then can create the lambda function from that zip file instead like so:

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
code = lambda.Code.from_asset(path.join(__dirname, "../cfn-secret-provider-1.0.0.zip"))

secret_provider = secret.Provider(self, "SecretProvider",
    code=code
)
```
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
import aws_cdk.aws_iam
import aws_cdk.aws_kms
import aws_cdk.aws_lambda
import aws_cdk.aws_s3
import aws_cdk.core

__jsii_assembly__ = jsii.JSIIAssembly.load("cdk-secrets", "0.4.2", __name__, "cdk-secrets@0.4.2.jsii.tgz")


class AccessKey(aws_cdk.core.Construct, metaclass=jsii.JSIIMeta, jsii_type="cdk-secrets.AccessKey"):
    """
    stability
    :stability: experimental
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, props: "AccessKeyProps", provider: typing.Optional[aws_cdk.aws_lambda.IFunction]=None) -> None:
        """
        :param scope: -
        :param id: -
        :param props: -
        :param provider: -

        stability
        :stability: experimental
        """
        jsii.create(AccessKey, self, [scope, id, props, provider])

    @builtins.property
    @jsii.member(jsii_name="secretAccessKey")
    def secret_access_key(self) -> str:
        """
        stability
        :stability: experimental
        """
        return jsii.get(self, "secretAccessKey")

    @builtins.property
    @jsii.member(jsii_name="smtpPassword")
    def smtp_password(self) -> str:
        """
        stability
        :stability: experimental
        """
        return jsii.get(self, "smtpPassword")


@jsii.data_type(jsii_type="cdk-secrets.CommonProps", jsii_struct_bases=[], name_mapping={'provider': 'provider', 'version': 'version'})
class CommonProps():
    def __init__(self, *, provider: typing.Optional[aws_cdk.aws_lambda.IFunction]=None, version: typing.Optional[str]=None):
        """
        :param provider: The lambda function providing the functionality.
        :param version: Opaque string to force update.

        stability
        :stability: experimental
        """
        self._values = {
        }
        if provider is not None: self._values["provider"] = provider
        if version is not None: self._values["version"] = version

    @builtins.property
    def provider(self) -> typing.Optional[aws_cdk.aws_lambda.IFunction]:
        """The lambda function providing the functionality.

        stability
        :stability: experimental
        attribute:
        :attribute:: true
        """
        return self._values.get('provider')

    @builtins.property
    def version(self) -> typing.Optional[str]:
        """Opaque string to force update.

        stability
        :stability: experimental
        attribute:
        :attribute:: true
        """
        return self._values.get('version')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CommonProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.data_type(jsii_type="cdk-secrets.AccessKeyProps", jsii_struct_bases=[CommonProps], name_mapping={'provider': 'provider', 'version': 'version', 'parameter_path': 'parameterPath', 'user_name': 'userName', 'description': 'description', 'key_alias': 'keyAlias', 'no_echo': 'noEcho', 'refresh_on_update': 'refreshOnUpdate', 'return_password': 'returnPassword', 'return_secret': 'returnSecret', 'serial': 'serial', 'status': 'status'})
class AccessKeyProps(CommonProps):
    def __init__(self, *, provider: typing.Optional[aws_cdk.aws_lambda.IFunction]=None, version: typing.Optional[str]=None, parameter_path: str, user_name: str, description: typing.Optional[str]=None, key_alias: typing.Optional[str]=None, no_echo: typing.Optional[bool]=None, refresh_on_update: typing.Optional[bool]=None, return_password: typing.Optional[bool]=None, return_secret: typing.Optional[bool]=None, serial: typing.Optional[jsii.Number]=None, status: typing.Optional["Status"]=None):
        """
        :param provider: The lambda function providing the functionality.
        :param version: Opaque string to force update.
        :param parameter_path: The path for the credentials in the parameter store.
        :param user_name: The user name to create the access key for.
        :param description: The description of the value in the parameter store. Default: - ''
        :param key_alias: The KMS key to use to encrypt the value with. Default: - 'alias/aws/ssm'
        :param no_echo: The secrets as output parameter. Default: - true
        :param refresh_on_update: Generate a new secret on update. Default: - false
        :param return_password: Return access id and SMTP password. Default: - 2048
        :param return_secret: Return access ID and secret. Default: - false
        :param serial: Version to force update. Default: - 1
        :param status: Status of the key. Default: - Active

        stability
        :stability: experimental
        """
        self._values = {
            'parameter_path': parameter_path,
            'user_name': user_name,
        }
        if provider is not None: self._values["provider"] = provider
        if version is not None: self._values["version"] = version
        if description is not None: self._values["description"] = description
        if key_alias is not None: self._values["key_alias"] = key_alias
        if no_echo is not None: self._values["no_echo"] = no_echo
        if refresh_on_update is not None: self._values["refresh_on_update"] = refresh_on_update
        if return_password is not None: self._values["return_password"] = return_password
        if return_secret is not None: self._values["return_secret"] = return_secret
        if serial is not None: self._values["serial"] = serial
        if status is not None: self._values["status"] = status

    @builtins.property
    def provider(self) -> typing.Optional[aws_cdk.aws_lambda.IFunction]:
        """The lambda function providing the functionality.

        stability
        :stability: experimental
        attribute:
        :attribute:: true
        """
        return self._values.get('provider')

    @builtins.property
    def version(self) -> typing.Optional[str]:
        """Opaque string to force update.

        stability
        :stability: experimental
        attribute:
        :attribute:: true
        """
        return self._values.get('version')

    @builtins.property
    def parameter_path(self) -> str:
        """The path for the credentials in the parameter store.

        stability
        :stability: experimental
        """
        return self._values.get('parameter_path')

    @builtins.property
    def user_name(self) -> str:
        """The user name to create the access key for.

        stability
        :stability: experimental
        """
        return self._values.get('user_name')

    @builtins.property
    def description(self) -> typing.Optional[str]:
        """The description of the value in the parameter store.

        default
        :default: - ''

        stability
        :stability: experimental
        """
        return self._values.get('description')

    @builtins.property
    def key_alias(self) -> typing.Optional[str]:
        """The KMS key to use to encrypt the value with.

        default
        :default: - 'alias/aws/ssm'

        stability
        :stability: experimental
        """
        return self._values.get('key_alias')

    @builtins.property
    def no_echo(self) -> typing.Optional[bool]:
        """The secrets as output parameter.

        default
        :default: - true

        stability
        :stability: experimental
        """
        return self._values.get('no_echo')

    @builtins.property
    def refresh_on_update(self) -> typing.Optional[bool]:
        """Generate a new secret on update.

        default
        :default: - false

        stability
        :stability: experimental
        """
        return self._values.get('refresh_on_update')

    @builtins.property
    def return_password(self) -> typing.Optional[bool]:
        """Return access id and SMTP password.

        default
        :default: - 2048

        stability
        :stability: experimental
        """
        return self._values.get('return_password')

    @builtins.property
    def return_secret(self) -> typing.Optional[bool]:
        """Return access ID and secret.

        default
        :default: - false

        stability
        :stability: experimental
        """
        return self._values.get('return_secret')

    @builtins.property
    def serial(self) -> typing.Optional[jsii.Number]:
        """Version to force update.

        default
        :default: - 1

        stability
        :stability: experimental
        """
        return self._values.get('serial')

    @builtins.property
    def status(self) -> typing.Optional["Status"]:
        """Status of the key.

        default
        :default: - Active

        stability
        :stability: experimental
        """
        return self._values.get('status')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'AccessKeyProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


class DSAKey(aws_cdk.core.Construct, metaclass=jsii.JSIIMeta, jsii_type="cdk-secrets.DSAKey"):
    """
    stability
    :stability: experimental
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, props: "DSAKeyProps", provider: typing.Optional[aws_cdk.aws_lambda.IFunction]=None) -> None:
        """
        :param scope: -
        :param id: -
        :param props: -
        :param provider: -

        stability
        :stability: experimental
        """
        jsii.create(DSAKey, self, [scope, id, props, provider])

    @jsii.member(jsii_name="grantRead")
    def grant_read(self, grantee: aws_cdk.aws_iam.IGrantable) -> aws_cdk.aws_iam.Grant:
        """
        :param grantee: -

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "grantRead", [grantee])

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> str:
        """
        stability
        :stability: experimental
        """
        return jsii.get(self, "arn")

    @builtins.property
    @jsii.member(jsii_name="hash")
    def hash(self) -> str:
        """
        stability
        :stability: experimental
        """
        return jsii.get(self, "hash")

    @builtins.property
    @jsii.member(jsii_name="publicKey")
    def public_key(self) -> str:
        """
        stability
        :stability: experimental
        """
        return jsii.get(self, "publicKey")

    @builtins.property
    @jsii.member(jsii_name="publicKeyPEM")
    def public_key_pem(self) -> str:
        """
        stability
        :stability: experimental
        """
        return jsii.get(self, "publicKeyPEM")

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> str:
        """
        stability
        :stability: experimental
        """
        return jsii.get(self, "version")


@jsii.data_type(jsii_type="cdk-secrets.DSAKeyProps", jsii_struct_bases=[CommonProps], name_mapping={'provider': 'provider', 'version': 'version', 'name': 'name', 'description': 'description', 'key_alias': 'keyAlias', 'key_size': 'keySize', 'refresh_on_update': 'refreshOnUpdate'})
class DSAKeyProps(CommonProps):
    def __init__(self, *, provider: typing.Optional[aws_cdk.aws_lambda.IFunction]=None, version: typing.Optional[str]=None, name: str, description: typing.Optional[str]=None, key_alias: typing.Optional[str]=None, key_size: typing.Optional[jsii.Number]=None, refresh_on_update: typing.Optional[bool]=None):
        """
        :param provider: The lambda function providing the functionality.
        :param version: Opaque string to force update.
        :param name: The name of the private key in the parameter store.
        :param description: The description of the key in the parameter store. Default: - ''
        :param key_alias: The KMS key to use to encrypt the key with. Default: - 'alias/aws/ssm'
        :param key_size: Number of bits in the key. Default: - 2048
        :param refresh_on_update: Generate a new secret on update. Default: - false

        stability
        :stability: experimental
        """
        self._values = {
            'name': name,
        }
        if provider is not None: self._values["provider"] = provider
        if version is not None: self._values["version"] = version
        if description is not None: self._values["description"] = description
        if key_alias is not None: self._values["key_alias"] = key_alias
        if key_size is not None: self._values["key_size"] = key_size
        if refresh_on_update is not None: self._values["refresh_on_update"] = refresh_on_update

    @builtins.property
    def provider(self) -> typing.Optional[aws_cdk.aws_lambda.IFunction]:
        """The lambda function providing the functionality.

        stability
        :stability: experimental
        attribute:
        :attribute:: true
        """
        return self._values.get('provider')

    @builtins.property
    def version(self) -> typing.Optional[str]:
        """Opaque string to force update.

        stability
        :stability: experimental
        attribute:
        :attribute:: true
        """
        return self._values.get('version')

    @builtins.property
    def name(self) -> str:
        """The name of the private key in the parameter store.

        stability
        :stability: experimental
        """
        return self._values.get('name')

    @builtins.property
    def description(self) -> typing.Optional[str]:
        """The description of the key in the parameter store.

        default
        :default: - ''

        stability
        :stability: experimental
        """
        return self._values.get('description')

    @builtins.property
    def key_alias(self) -> typing.Optional[str]:
        """The KMS key to use to encrypt the key with.

        default
        :default: - 'alias/aws/ssm'

        stability
        :stability: experimental
        """
        return self._values.get('key_alias')

    @builtins.property
    def key_size(self) -> typing.Optional[jsii.Number]:
        """Number of bits in the key.

        default
        :default: - 2048

        stability
        :stability: experimental
        """
        return self._values.get('key_size')

    @builtins.property
    def refresh_on_update(self) -> typing.Optional[bool]:
        """Generate a new secret on update.

        default
        :default: - false

        stability
        :stability: experimental
        """
        return self._values.get('refresh_on_update')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'DSAKeyProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.enum(jsii_type="cdk-secrets.KeyFormat")
class KeyFormat(enum.Enum):
    """
    stability
    :stability: experimental
    """
    PKCS8 = "PKCS8"
    """
    stability
    :stability: experimental
    """
    TRADITIONAL_OPEN_SSL = "TRADITIONAL_OPEN_SSL"
    """
    stability
    :stability: experimental
    """

class KeyPair(aws_cdk.core.Construct, metaclass=jsii.JSIIMeta, jsii_type="cdk-secrets.KeyPair"):
    """
    stability
    :stability: experimental
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, props: "KeyPairProps", provider: typing.Optional[aws_cdk.aws_lambda.IFunction]=None) -> None:
        """
        :param scope: -
        :param id: -
        :param props: -
        :param provider: -

        stability
        :stability: experimental
        """
        jsii.create(KeyPair, self, [scope, id, props, provider])

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> str:
        """
        stability
        :stability: experimental
        """
        return jsii.get(self, "arn")

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> str:
        """
        stability
        :stability: experimental
        """
        return jsii.get(self, "name")


@jsii.data_type(jsii_type="cdk-secrets.KeyPairProps", jsii_struct_bases=[CommonProps], name_mapping={'provider': 'provider', 'version': 'version', 'name': 'name', 'public_key_material': 'publicKeyMaterial'})
class KeyPairProps(CommonProps):
    def __init__(self, *, provider: typing.Optional[aws_cdk.aws_lambda.IFunction]=None, version: typing.Optional[str]=None, name: str, public_key_material: str):
        """
        :param provider: The lambda function providing the functionality.
        :param version: Opaque string to force update.
        :param name: The name of the value in the parameters store.
        :param public_key_material: The public key to import.

        stability
        :stability: experimental
        """
        self._values = {
            'name': name,
            'public_key_material': public_key_material,
        }
        if provider is not None: self._values["provider"] = provider
        if version is not None: self._values["version"] = version

    @builtins.property
    def provider(self) -> typing.Optional[aws_cdk.aws_lambda.IFunction]:
        """The lambda function providing the functionality.

        stability
        :stability: experimental
        attribute:
        :attribute:: true
        """
        return self._values.get('provider')

    @builtins.property
    def version(self) -> typing.Optional[str]:
        """Opaque string to force update.

        stability
        :stability: experimental
        attribute:
        :attribute:: true
        """
        return self._values.get('version')

    @builtins.property
    def name(self) -> str:
        """The name of the value in the parameters store.

        stability
        :stability: experimental
        """
        return self._values.get('name')

    @builtins.property
    def public_key_material(self) -> str:
        """The public key to import.

        stability
        :stability: experimental
        """
        return self._values.get('public_key_material')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'KeyPairProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


class Provider(aws_cdk.core.Construct, metaclass=jsii.JSIIMeta, jsii_type="cdk-secrets.Provider"):
    """
    stability
    :stability: experimental
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, code: typing.Optional[aws_cdk.aws_lambda.Code]=None) -> None:
        """
        :param scope: -
        :param id: -
        :param code: Code for the Provider lambda function. Default: - Use code from s3 bucket binxio-public

        stability
        :stability: experimental
        """
        props = ProviderProps(code=code)

        jsii.create(Provider, self, [scope, id, props])

    @jsii.member(jsii_name="accessKey")
    def access_key(self, scope: aws_cdk.core.Construct, id: str, *, parameter_path: str, user_name: str, description: typing.Optional[str]=None, key_alias: typing.Optional[str]=None, no_echo: typing.Optional[bool]=None, refresh_on_update: typing.Optional[bool]=None, return_password: typing.Optional[bool]=None, return_secret: typing.Optional[bool]=None, serial: typing.Optional[jsii.Number]=None, status: typing.Optional["Status"]=None, provider: typing.Optional[aws_cdk.aws_lambda.IFunction]=None, version: typing.Optional[str]=None) -> "AccessKey":
        """
        :param scope: -
        :param id: -
        :param parameter_path: The path for the credentials in the parameter store.
        :param user_name: The user name to create the access key for.
        :param description: The description of the value in the parameter store. Default: - ''
        :param key_alias: The KMS key to use to encrypt the value with. Default: - 'alias/aws/ssm'
        :param no_echo: The secrets as output parameter. Default: - true
        :param refresh_on_update: Generate a new secret on update. Default: - false
        :param return_password: Return access id and SMTP password. Default: - 2048
        :param return_secret: Return access ID and secret. Default: - false
        :param serial: Version to force update. Default: - 1
        :param status: Status of the key. Default: - Active
        :param provider: The lambda function providing the functionality.
        :param version: Opaque string to force update.

        stability
        :stability: experimental
        """
        props = AccessKeyProps(parameter_path=parameter_path, user_name=user_name, description=description, key_alias=key_alias, no_echo=no_echo, refresh_on_update=refresh_on_update, return_password=return_password, return_secret=return_secret, serial=serial, status=status, provider=provider, version=version)

        return jsii.invoke(self, "accessKey", [scope, id, props])

    @jsii.member(jsii_name="dsaKey")
    def dsa_key(self, scope: aws_cdk.core.Construct, id: str, *, name: str, description: typing.Optional[str]=None, key_alias: typing.Optional[str]=None, key_size: typing.Optional[jsii.Number]=None, refresh_on_update: typing.Optional[bool]=None, provider: typing.Optional[aws_cdk.aws_lambda.IFunction]=None, version: typing.Optional[str]=None) -> "DSAKey":
        """
        :param scope: -
        :param id: -
        :param name: The name of the private key in the parameter store.
        :param description: The description of the key in the parameter store. Default: - ''
        :param key_alias: The KMS key to use to encrypt the key with. Default: - 'alias/aws/ssm'
        :param key_size: Number of bits in the key. Default: - 2048
        :param refresh_on_update: Generate a new secret on update. Default: - false
        :param provider: The lambda function providing the functionality.
        :param version: Opaque string to force update.

        stability
        :stability: experimental
        """
        props = DSAKeyProps(name=name, description=description, key_alias=key_alias, key_size=key_size, refresh_on_update=refresh_on_update, provider=provider, version=version)

        return jsii.invoke(self, "dsaKey", [scope, id, props])

    @jsii.member(jsii_name="keyPair")
    def key_pair(self, scope: aws_cdk.core.Construct, id: str, *, name: str, public_key_material: str, provider: typing.Optional[aws_cdk.aws_lambda.IFunction]=None, version: typing.Optional[str]=None) -> "KeyPair":
        """
        :param scope: -
        :param id: -
        :param name: The name of the value in the parameters store.
        :param public_key_material: The public key to import.
        :param provider: The lambda function providing the functionality.
        :param version: Opaque string to force update.

        stability
        :stability: experimental
        """
        props = KeyPairProps(name=name, public_key_material=public_key_material, provider=provider, version=version)

        return jsii.invoke(self, "keyPair", [scope, id, props])

    @jsii.member(jsii_name="rsaKey")
    def rsa_key(self, scope: aws_cdk.core.Construct, id: str, *, key_format: typing.Optional["KeyFormat"]=None, name: str, description: typing.Optional[str]=None, key_alias: typing.Optional[str]=None, key_size: typing.Optional[jsii.Number]=None, refresh_on_update: typing.Optional[bool]=None, provider: typing.Optional[aws_cdk.aws_lambda.IFunction]=None, version: typing.Optional[str]=None) -> "RSAKey":
        """
        :param scope: -
        :param id: -
        :param key_format: Encoding type of the private key. Default: - 2048
        :param name: The name of the private key in the parameter store.
        :param description: The description of the key in the parameter store. Default: - ''
        :param key_alias: The KMS key to use to encrypt the key with. Default: - 'alias/aws/ssm'
        :param key_size: Number of bits in the key. Default: - 2048
        :param refresh_on_update: Generate a new secret on update. Default: - false
        :param provider: The lambda function providing the functionality.
        :param version: Opaque string to force update.

        stability
        :stability: experimental
        """
        props = RSAKeyProps(key_format=key_format, name=name, description=description, key_alias=key_alias, key_size=key_size, refresh_on_update=refresh_on_update, provider=provider, version=version)

        return jsii.invoke(self, "rsaKey", [scope, id, props])

    @jsii.member(jsii_name="secret")
    def secret(self, scope: aws_cdk.core.Construct, id: str, *, name: str, alphabet: typing.Optional[str]=None, content: typing.Optional[str]=None, description: typing.Optional[str]=None, encrypted_content: typing.Optional[str]=None, key_alias: typing.Optional[str]=None, length: typing.Optional[jsii.Number]=None, no_echo: typing.Optional[bool]=None, refresh_on_update: typing.Optional[bool]=None, return_secret: typing.Optional[bool]=None, provider: typing.Optional[aws_cdk.aws_lambda.IFunction]=None, version: typing.Optional[str]=None) -> "Secret":
        """
        :param scope: -
        :param id: -
        :param name: The name of the secret in the parameter store.
        :param alphabet: The alphabet of characters from which to generate a secret. Default: - Defaults to ASCII letters, digits and punctuation characters
        :param content: Plain text secret to be stored. Default: - ''
        :param description: The description of the secret in the parameter store. Default: - ''
        :param encrypted_content: Base64 encoded KMS encoded secret, to be decrypted before stored. Default: - ''
        :param key_alias: The KMS key to use to encrypt the secret with. Default: - 'alias/aws/ssm'
        :param length: The length of the secret. Default: - 30
        :param no_echo: Indicates whether output of the return values is replaced by *****. Default: - true
        :param refresh_on_update: Generate a new secret on update. Default: - false
        :param return_secret: Return the secret as an attribute. Default: - false
        :param provider: The lambda function providing the functionality.
        :param version: Opaque string to force update.

        stability
        :stability: experimental
        """
        props = SecretProps(name=name, alphabet=alphabet, content=content, description=description, encrypted_content=encrypted_content, key_alias=key_alias, length=length, no_echo=no_echo, refresh_on_update=refresh_on_update, return_secret=return_secret, provider=provider, version=version)

        return jsii.invoke(self, "secret", [scope, id, props])

    @jsii.member(jsii_name="secretManagerSecret")
    def secret_manager_secret(self, scope: aws_cdk.core.Construct, id: str, *, name: str, client_request_token: typing.Optional[str]=None, description: typing.Optional[str]=None, kms_key_id: typing.Optional[str]=None, no_echo: typing.Optional[bool]=None, recovery_window_in_days: typing.Optional[jsii.Number]=None, secret_binary: typing.Optional[str]=None, secret_string: typing.Any=None, tags: typing.Optional[typing.Mapping[typing.Any, typing.Any]]=None, provider: typing.Optional[aws_cdk.aws_lambda.IFunction]=None, version: typing.Optional[str]=None) -> "SecretManagerSecret":
        """
        :param scope: -
        :param id: -
        :param name: The name of the secret.
        :param client_request_token: A unique identifier for the new version to ensure idempotency. Default: - ''
        :param description: The description of the secret in the parameter store. Default: - ''
        :param kms_key_id: The KMS key to use to encrypt the secret with. Default: - 'alias/aws/secretsmanager'
        :param no_echo: The secret as output parameter. Default: - true
        :param recovery_window_in_days: Number of days a deleted secret can be restored. Default: - 30
        :param secret_binary: Base64 encoded secret. Default: - ''
        :param secret_string: Secret string or json object or array to be converted to string. Default: - ''
        :param tags: Array of tags for the secret. Default: - []
        :param provider: The lambda function providing the functionality.
        :param version: Opaque string to force update.

        stability
        :stability: experimental
        """
        props = SecretManagerSecretProps(name=name, client_request_token=client_request_token, description=description, kms_key_id=kms_key_id, no_echo=no_echo, recovery_window_in_days=recovery_window_in_days, secret_binary=secret_binary, secret_string=secret_string, tags=tags, provider=provider, version=version)

        return jsii.invoke(self, "secretManagerSecret", [scope, id, props])

    @builtins.property
    @jsii.member(jsii_name="fn")
    def fn(self) -> aws_cdk.aws_lambda.SingletonFunction:
        """
        stability
        :stability: experimental
        """
        return jsii.get(self, "fn")

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> aws_cdk.aws_kms.Key:
        """
        stability
        :stability: experimental
        """
        return jsii.get(self, "key")


@jsii.data_type(jsii_type="cdk-secrets.ProviderProps", jsii_struct_bases=[], name_mapping={'code': 'code'})
class ProviderProps():
    def __init__(self, *, code: typing.Optional[aws_cdk.aws_lambda.Code]=None):
        """
        :param code: Code for the Provider lambda function. Default: - Use code from s3 bucket binxio-public

        stability
        :stability: experimental
        """
        self._values = {
        }
        if code is not None: self._values["code"] = code

    @builtins.property
    def code(self) -> typing.Optional[aws_cdk.aws_lambda.Code]:
        """Code for the Provider lambda function.

        default
        :default: - Use code from s3 bucket binxio-public

        stability
        :stability: experimental
        """
        return self._values.get('code')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'ProviderProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


class RSAKey(aws_cdk.core.Construct, metaclass=jsii.JSIIMeta, jsii_type="cdk-secrets.RSAKey"):
    """
    stability
    :stability: experimental
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, props: "RSAKeyProps", provider: typing.Optional[aws_cdk.aws_lambda.IFunction]=None) -> None:
        """
        :param scope: -
        :param id: -
        :param props: -
        :param provider: -

        stability
        :stability: experimental
        """
        jsii.create(RSAKey, self, [scope, id, props, provider])

    @jsii.member(jsii_name="grantRead")
    def grant_read(self, grantee: aws_cdk.aws_iam.IGrantable) -> aws_cdk.aws_iam.Grant:
        """
        :param grantee: -

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "grantRead", [grantee])

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> str:
        """
        stability
        :stability: experimental
        """
        return jsii.get(self, "arn")

    @builtins.property
    @jsii.member(jsii_name="hash")
    def hash(self) -> str:
        """
        stability
        :stability: experimental
        """
        return jsii.get(self, "hash")

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> str:
        """
        stability
        :stability: experimental
        """
        return jsii.get(self, "name")

    @builtins.property
    @jsii.member(jsii_name="publicKey")
    def public_key(self) -> str:
        """
        stability
        :stability: experimental
        """
        return jsii.get(self, "publicKey")

    @builtins.property
    @jsii.member(jsii_name="publicKeyPEM")
    def public_key_pem(self) -> str:
        """
        stability
        :stability: experimental
        """
        return jsii.get(self, "publicKeyPEM")

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> str:
        """
        stability
        :stability: experimental
        """
        return jsii.get(self, "version")


@jsii.data_type(jsii_type="cdk-secrets.RSAKeyProps", jsii_struct_bases=[DSAKeyProps], name_mapping={'provider': 'provider', 'version': 'version', 'name': 'name', 'description': 'description', 'key_alias': 'keyAlias', 'key_size': 'keySize', 'refresh_on_update': 'refreshOnUpdate', 'key_format': 'keyFormat'})
class RSAKeyProps(DSAKeyProps):
    def __init__(self, *, provider: typing.Optional[aws_cdk.aws_lambda.IFunction]=None, version: typing.Optional[str]=None, name: str, description: typing.Optional[str]=None, key_alias: typing.Optional[str]=None, key_size: typing.Optional[jsii.Number]=None, refresh_on_update: typing.Optional[bool]=None, key_format: typing.Optional["KeyFormat"]=None):
        """
        :param provider: The lambda function providing the functionality.
        :param version: Opaque string to force update.
        :param name: The name of the private key in the parameter store.
        :param description: The description of the key in the parameter store. Default: - ''
        :param key_alias: The KMS key to use to encrypt the key with. Default: - 'alias/aws/ssm'
        :param key_size: Number of bits in the key. Default: - 2048
        :param refresh_on_update: Generate a new secret on update. Default: - false
        :param key_format: Encoding type of the private key. Default: - 2048

        stability
        :stability: experimental
        """
        self._values = {
            'name': name,
        }
        if provider is not None: self._values["provider"] = provider
        if version is not None: self._values["version"] = version
        if description is not None: self._values["description"] = description
        if key_alias is not None: self._values["key_alias"] = key_alias
        if key_size is not None: self._values["key_size"] = key_size
        if refresh_on_update is not None: self._values["refresh_on_update"] = refresh_on_update
        if key_format is not None: self._values["key_format"] = key_format

    @builtins.property
    def provider(self) -> typing.Optional[aws_cdk.aws_lambda.IFunction]:
        """The lambda function providing the functionality.

        stability
        :stability: experimental
        attribute:
        :attribute:: true
        """
        return self._values.get('provider')

    @builtins.property
    def version(self) -> typing.Optional[str]:
        """Opaque string to force update.

        stability
        :stability: experimental
        attribute:
        :attribute:: true
        """
        return self._values.get('version')

    @builtins.property
    def name(self) -> str:
        """The name of the private key in the parameter store.

        stability
        :stability: experimental
        """
        return self._values.get('name')

    @builtins.property
    def description(self) -> typing.Optional[str]:
        """The description of the key in the parameter store.

        default
        :default: - ''

        stability
        :stability: experimental
        """
        return self._values.get('description')

    @builtins.property
    def key_alias(self) -> typing.Optional[str]:
        """The KMS key to use to encrypt the key with.

        default
        :default: - 'alias/aws/ssm'

        stability
        :stability: experimental
        """
        return self._values.get('key_alias')

    @builtins.property
    def key_size(self) -> typing.Optional[jsii.Number]:
        """Number of bits in the key.

        default
        :default: - 2048

        stability
        :stability: experimental
        """
        return self._values.get('key_size')

    @builtins.property
    def refresh_on_update(self) -> typing.Optional[bool]:
        """Generate a new secret on update.

        default
        :default: - false

        stability
        :stability: experimental
        """
        return self._values.get('refresh_on_update')

    @builtins.property
    def key_format(self) -> typing.Optional["KeyFormat"]:
        """Encoding type of the private key.

        default
        :default: - 2048

        stability
        :stability: experimental
        """
        return self._values.get('key_format')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'RSAKeyProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


class Secret(aws_cdk.core.Construct, metaclass=jsii.JSIIMeta, jsii_type="cdk-secrets.Secret"):
    """
    stability
    :stability: experimental
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, props: "SecretProps", provider: typing.Optional[aws_cdk.aws_lambda.IFunction]=None) -> None:
        """
        :param scope: -
        :param id: -
        :param props: -
        :param provider: -

        stability
        :stability: experimental
        """
        jsii.create(Secret, self, [scope, id, props, provider])

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> str:
        """
        stability
        :stability: experimental
        """
        return jsii.get(self, "arn")

    @builtins.property
    @jsii.member(jsii_name="hash")
    def hash(self) -> str:
        """
        stability
        :stability: experimental
        """
        return jsii.get(self, "hash")

    @builtins.property
    @jsii.member(jsii_name="secret")
    def secret(self) -> str:
        """
        stability
        :stability: experimental
        """
        return jsii.get(self, "secret")

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> str:
        """
        stability
        :stability: experimental
        """
        return jsii.get(self, "version")


class SecretManagerSecret(aws_cdk.core.Construct, metaclass=jsii.JSIIMeta, jsii_type="cdk-secrets.SecretManagerSecret"):
    """
    stability
    :stability: experimental
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, props: "SecretManagerSecretProps", provider: typing.Optional[aws_cdk.aws_lambda.IFunction]=None) -> None:
        """
        :param scope: -
        :param id: -
        :param props: -
        :param provider: -

        stability
        :stability: experimental
        """
        jsii.create(SecretManagerSecret, self, [scope, id, props, provider])

    @builtins.property
    @jsii.member(jsii_name="versionId")
    def version_id(self) -> str:
        """
        stability
        :stability: experimental
        """
        return jsii.get(self, "versionId")


@jsii.data_type(jsii_type="cdk-secrets.SecretManagerSecretProps", jsii_struct_bases=[CommonProps], name_mapping={'provider': 'provider', 'version': 'version', 'name': 'name', 'client_request_token': 'clientRequestToken', 'description': 'description', 'kms_key_id': 'kmsKeyId', 'no_echo': 'noEcho', 'recovery_window_in_days': 'recoveryWindowInDays', 'secret_binary': 'secretBinary', 'secret_string': 'secretString', 'tags': 'tags'})
class SecretManagerSecretProps(CommonProps):
    def __init__(self, *, provider: typing.Optional[aws_cdk.aws_lambda.IFunction]=None, version: typing.Optional[str]=None, name: str, client_request_token: typing.Optional[str]=None, description: typing.Optional[str]=None, kms_key_id: typing.Optional[str]=None, no_echo: typing.Optional[bool]=None, recovery_window_in_days: typing.Optional[jsii.Number]=None, secret_binary: typing.Optional[str]=None, secret_string: typing.Any=None, tags: typing.Optional[typing.Mapping[typing.Any, typing.Any]]=None):
        """
        :param provider: The lambda function providing the functionality.
        :param version: Opaque string to force update.
        :param name: The name of the secret.
        :param client_request_token: A unique identifier for the new version to ensure idempotency. Default: - ''
        :param description: The description of the secret in the parameter store. Default: - ''
        :param kms_key_id: The KMS key to use to encrypt the secret with. Default: - 'alias/aws/secretsmanager'
        :param no_echo: The secret as output parameter. Default: - true
        :param recovery_window_in_days: Number of days a deleted secret can be restored. Default: - 30
        :param secret_binary: Base64 encoded secret. Default: - ''
        :param secret_string: Secret string or json object or array to be converted to string. Default: - ''
        :param tags: Array of tags for the secret. Default: - []

        stability
        :stability: experimental
        """
        self._values = {
            'name': name,
        }
        if provider is not None: self._values["provider"] = provider
        if version is not None: self._values["version"] = version
        if client_request_token is not None: self._values["client_request_token"] = client_request_token
        if description is not None: self._values["description"] = description
        if kms_key_id is not None: self._values["kms_key_id"] = kms_key_id
        if no_echo is not None: self._values["no_echo"] = no_echo
        if recovery_window_in_days is not None: self._values["recovery_window_in_days"] = recovery_window_in_days
        if secret_binary is not None: self._values["secret_binary"] = secret_binary
        if secret_string is not None: self._values["secret_string"] = secret_string
        if tags is not None: self._values["tags"] = tags

    @builtins.property
    def provider(self) -> typing.Optional[aws_cdk.aws_lambda.IFunction]:
        """The lambda function providing the functionality.

        stability
        :stability: experimental
        attribute:
        :attribute:: true
        """
        return self._values.get('provider')

    @builtins.property
    def version(self) -> typing.Optional[str]:
        """Opaque string to force update.

        stability
        :stability: experimental
        attribute:
        :attribute:: true
        """
        return self._values.get('version')

    @builtins.property
    def name(self) -> str:
        """The name of the secret.

        stability
        :stability: experimental
        """
        return self._values.get('name')

    @builtins.property
    def client_request_token(self) -> typing.Optional[str]:
        """A unique identifier for the new version to ensure idempotency.

        default
        :default: - ''

        stability
        :stability: experimental
        """
        return self._values.get('client_request_token')

    @builtins.property
    def description(self) -> typing.Optional[str]:
        """The description of the secret in the parameter store.

        default
        :default: - ''

        stability
        :stability: experimental
        """
        return self._values.get('description')

    @builtins.property
    def kms_key_id(self) -> typing.Optional[str]:
        """The KMS key to use to encrypt the secret with.

        default
        :default: - 'alias/aws/secretsmanager'

        stability
        :stability: experimental
        """
        return self._values.get('kms_key_id')

    @builtins.property
    def no_echo(self) -> typing.Optional[bool]:
        """The secret as output parameter.

        default
        :default: - true

        stability
        :stability: experimental
        """
        return self._values.get('no_echo')

    @builtins.property
    def recovery_window_in_days(self) -> typing.Optional[jsii.Number]:
        """Number of days a deleted secret can be restored.

        default
        :default: - 30

        stability
        :stability: experimental
        """
        return self._values.get('recovery_window_in_days')

    @builtins.property
    def secret_binary(self) -> typing.Optional[str]:
        """Base64 encoded secret.

        default
        :default: - ''

        stability
        :stability: experimental
        """
        return self._values.get('secret_binary')

    @builtins.property
    def secret_string(self) -> typing.Any:
        """Secret string or json object or array to be converted to string.

        default
        :default: - ''

        stability
        :stability: experimental
        """
        return self._values.get('secret_string')

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[typing.Any, typing.Any]]:
        """Array of tags for the secret.

        default
        :default: - []

        stability
        :stability: experimental
        """
        return self._values.get('tags')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'SecretManagerSecretProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.data_type(jsii_type="cdk-secrets.SecretProps", jsii_struct_bases=[CommonProps], name_mapping={'provider': 'provider', 'version': 'version', 'name': 'name', 'alphabet': 'alphabet', 'content': 'content', 'description': 'description', 'encrypted_content': 'encryptedContent', 'key_alias': 'keyAlias', 'length': 'length', 'no_echo': 'noEcho', 'refresh_on_update': 'refreshOnUpdate', 'return_secret': 'returnSecret'})
class SecretProps(CommonProps):
    def __init__(self, *, provider: typing.Optional[aws_cdk.aws_lambda.IFunction]=None, version: typing.Optional[str]=None, name: str, alphabet: typing.Optional[str]=None, content: typing.Optional[str]=None, description: typing.Optional[str]=None, encrypted_content: typing.Optional[str]=None, key_alias: typing.Optional[str]=None, length: typing.Optional[jsii.Number]=None, no_echo: typing.Optional[bool]=None, refresh_on_update: typing.Optional[bool]=None, return_secret: typing.Optional[bool]=None):
        """
        :param provider: The lambda function providing the functionality.
        :param version: Opaque string to force update.
        :param name: The name of the secret in the parameter store.
        :param alphabet: The alphabet of characters from which to generate a secret. Default: - Defaults to ASCII letters, digits and punctuation characters
        :param content: Plain text secret to be stored. Default: - ''
        :param description: The description of the secret in the parameter store. Default: - ''
        :param encrypted_content: Base64 encoded KMS encoded secret, to be decrypted before stored. Default: - ''
        :param key_alias: The KMS key to use to encrypt the secret with. Default: - 'alias/aws/ssm'
        :param length: The length of the secret. Default: - 30
        :param no_echo: Indicates whether output of the return values is replaced by *****. Default: - true
        :param refresh_on_update: Generate a new secret on update. Default: - false
        :param return_secret: Return the secret as an attribute. Default: - false

        stability
        :stability: experimental
        """
        self._values = {
            'name': name,
        }
        if provider is not None: self._values["provider"] = provider
        if version is not None: self._values["version"] = version
        if alphabet is not None: self._values["alphabet"] = alphabet
        if content is not None: self._values["content"] = content
        if description is not None: self._values["description"] = description
        if encrypted_content is not None: self._values["encrypted_content"] = encrypted_content
        if key_alias is not None: self._values["key_alias"] = key_alias
        if length is not None: self._values["length"] = length
        if no_echo is not None: self._values["no_echo"] = no_echo
        if refresh_on_update is not None: self._values["refresh_on_update"] = refresh_on_update
        if return_secret is not None: self._values["return_secret"] = return_secret

    @builtins.property
    def provider(self) -> typing.Optional[aws_cdk.aws_lambda.IFunction]:
        """The lambda function providing the functionality.

        stability
        :stability: experimental
        attribute:
        :attribute:: true
        """
        return self._values.get('provider')

    @builtins.property
    def version(self) -> typing.Optional[str]:
        """Opaque string to force update.

        stability
        :stability: experimental
        attribute:
        :attribute:: true
        """
        return self._values.get('version')

    @builtins.property
    def name(self) -> str:
        """The name of the secret in the parameter store.

        stability
        :stability: experimental
        """
        return self._values.get('name')

    @builtins.property
    def alphabet(self) -> typing.Optional[str]:
        """The alphabet of characters from which to generate a secret.

        default
        :default: - Defaults to ASCII letters, digits and punctuation characters

        stability
        :stability: experimental
        """
        return self._values.get('alphabet')

    @builtins.property
    def content(self) -> typing.Optional[str]:
        """Plain text secret to be stored.

        default
        :default: - ''

        stability
        :stability: experimental
        """
        return self._values.get('content')

    @builtins.property
    def description(self) -> typing.Optional[str]:
        """The description of the secret in the parameter store.

        default
        :default: - ''

        stability
        :stability: experimental
        """
        return self._values.get('description')

    @builtins.property
    def encrypted_content(self) -> typing.Optional[str]:
        """Base64 encoded KMS encoded secret, to be decrypted before stored.

        default
        :default: - ''

        stability
        :stability: experimental
        """
        return self._values.get('encrypted_content')

    @builtins.property
    def key_alias(self) -> typing.Optional[str]:
        """The KMS key to use to encrypt the secret with.

        default
        :default: - 'alias/aws/ssm'

        stability
        :stability: experimental
        """
        return self._values.get('key_alias')

    @builtins.property
    def length(self) -> typing.Optional[jsii.Number]:
        """The length of the secret.

        default
        :default: - 30

        stability
        :stability: experimental
        """
        return self._values.get('length')

    @builtins.property
    def no_echo(self) -> typing.Optional[bool]:
        """Indicates whether output of the return values is replaced by *****.

        default
        :default: - true

        stability
        :stability: experimental
        """
        return self._values.get('no_echo')

    @builtins.property
    def refresh_on_update(self) -> typing.Optional[bool]:
        """Generate a new secret on update.

        default
        :default: - false

        stability
        :stability: experimental
        """
        return self._values.get('refresh_on_update')

    @builtins.property
    def return_secret(self) -> typing.Optional[bool]:
        """Return the secret as an attribute.

        default
        :default: - false

        stability
        :stability: experimental
        """
        return self._values.get('return_secret')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'SecretProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.enum(jsii_type="cdk-secrets.Status")
class Status(enum.Enum):
    """
    stability
    :stability: experimental
    """
    ACTIVE = "ACTIVE"
    """
    stability
    :stability: experimental
    """
    INACTIVE = "INACTIVE"
    """
    stability
    :stability: experimental
    """

@jsii.data_type(jsii_type="cdk-secrets.Tag", jsii_struct_bases=[], name_mapping={'key': 'key', 'value': 'value'})
class Tag():
    def __init__(self, *, key: str, value: str):
        """
        :param key: 
        :param value: 

        stability
        :stability: experimental
        """
        self._values = {
            'key': key,
            'value': value,
        }

    @builtins.property
    def key(self) -> str:
        """
        stability
        :stability: experimental
        """
        return self._values.get('key')

    @builtins.property
    def value(self) -> str:
        """
        stability
        :stability: experimental
        """
        return self._values.get('value')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'Tag(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


__all__ = ["AccessKey", "AccessKeyProps", "CommonProps", "DSAKey", "DSAKeyProps", "KeyFormat", "KeyPair", "KeyPairProps", "Provider", "ProviderProps", "RSAKey", "RSAKeyProps", "Secret", "SecretManagerSecret", "SecretManagerSecretProps", "SecretProps", "Status", "Tag", "__jsii_assembly__"]

publication.publish()
