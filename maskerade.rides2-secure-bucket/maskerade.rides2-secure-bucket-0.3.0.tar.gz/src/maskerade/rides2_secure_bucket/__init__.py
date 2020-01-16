"""
# A CDK L3 Construct for a Secure Bucket

This is an AWS CDK L3 Construct used to demonstrate the development and publishing process with the AWS CDK.

## Usage

Just import and use it.

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
import aws_cdk.core as cdk
from secure_bucket import SecureBucket

class SandboxCdkStack(cdk.Stack):
    def __init__(self, scope, id, *, description=None, env=None, stackName=None, tags=None):
        super().__init__(scope, id, description=description, env=env, stackName=stackName, tags=tags)

        SecureBucket(self, "myBucket")
```

## Encryption options

This is just a wrapper around an S3 Bucket and the [props](https://docs.aws.amazon.com/cdk/api/latest/docs/@aws-cdk_aws-s3.BucketProps.html) are shared.

However, you cannot supply an `UNENCRYPTED` option for the `encryption` property. If you do, or don't set it at all, it will use the `BucketEncryption.KMS_MANAGED` value by default.

## Integration Test

If you want to see full usage, you can run

```shell script
$ cdk synth
```

to produce a basic stack with one SecureBucket resource

## License

[MIT License](https://opensource.org/licenses/MIT)
"""
import abc
import builtins
import datetime
import enum
import typing

import jsii
import jsii.compat
import publication

import aws_cdk.aws_s3
import aws_cdk.core

__jsii_assembly__ = jsii.JSIIAssembly.load("rides2-secure-bucket", "0.3.0", __name__, "rides2-secure-bucket@0.3.0.jsii.tgz")


class SecureBucket(aws_cdk.core.Construct, metaclass=jsii.JSIIMeta, jsii_type="rides2-secure-bucket.SecureBucket"):
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, access_control: typing.Optional[aws_cdk.aws_s3.BucketAccessControl]=None, block_public_access: typing.Optional[aws_cdk.aws_s3.BlockPublicAccess]=None, bucket_name: typing.Optional[str]=None, cors: typing.Optional[typing.List[aws_cdk.aws_s3.CorsRule]]=None, encryption: typing.Optional[aws_cdk.aws_s3.BucketEncryption]=None, encryption_key: typing.Optional[aws_cdk.aws_kms.IKey]=None, lifecycle_rules: typing.Optional[typing.List[aws_cdk.aws_s3.LifecycleRule]]=None, metrics: typing.Optional[typing.List[aws_cdk.aws_s3.BucketMetrics]]=None, public_read_access: typing.Optional[bool]=None, removal_policy: typing.Optional[aws_cdk.core.RemovalPolicy]=None, versioned: typing.Optional[bool]=None, website_error_document: typing.Optional[str]=None, website_index_document: typing.Optional[str]=None, website_redirect: typing.Optional[aws_cdk.aws_s3.RedirectTarget]=None, website_routing_rules: typing.Optional[typing.List[aws_cdk.aws_s3.RoutingRule]]=None) -> None:
        """
        :param scope: -
        :param id: -
        :param access_control: Specifies a canned ACL that grants predefined permissions to the bucket. Default: BucketAccessControl.PRIVATE
        :param block_public_access: The block public access configuration of this bucket. Default: false New buckets and objects don't allow public access, but users can modify bucket policies or object permissions to allow public access.
        :param bucket_name: Physical name of this bucket. Default: - Assigned by CloudFormation (recommended).
        :param cors: The CORS configuration of this bucket. Default: - No CORS configuration.
        :param encryption: The kind of server-side encryption to apply to this bucket. If you choose KMS, you can specify a KMS key via ``encryptionKey``. If encryption key is not specified, a key will automatically be created. Default: - ``Kms`` if ``encryptionKey`` is specified, or ``Unencrypted`` otherwise.
        :param encryption_key: External KMS key to use for bucket encryption. The 'encryption' property must be either not specified or set to "Kms". An error will be emitted if encryption is set to "Unencrypted" or "Managed". Default: - If encryption is set to "Kms" and this property is undefined, a new KMS key will be created and associated with this bucket.
        :param lifecycle_rules: Rules that define how Amazon S3 manages objects during their lifetime. Default: - No lifecycle rules.
        :param metrics: The metrics configuration of this bucket. Default: - No metrics configuration.
        :param public_read_access: Grants public read access to all objects in the bucket. Similar to calling ``bucket.grantPublicAccess()`` Default: false
        :param removal_policy: Policy to apply when the bucket is removed from this stack. Default: - The bucket will be orphaned.
        :param versioned: Whether this bucket should have versioning turned on or not. Default: false
        :param website_error_document: The name of the error document (e.g. "404.html") for the website. ``websiteIndexDocument`` must also be set if this is set. Default: - No error document.
        :param website_index_document: The name of the index document (e.g. "index.html") for the website. Enables static website hosting for this bucket. Default: - No index document.
        :param website_redirect: Specifies the redirect behavior of all requests to a website endpoint of a bucket. If you specify this property, you can't specify "websiteIndexDocument", "websiteErrorDocument" nor , "websiteRoutingRules". Default: - No redirection.
        :param website_routing_rules: Rules that define when a redirect is applied and the redirect behavior. Default: - No redirection rules.
        """
        props = aws_cdk.aws_s3.BucketProps(access_control=access_control, block_public_access=block_public_access, bucket_name=bucket_name, cors=cors, encryption=encryption, encryption_key=encryption_key, lifecycle_rules=lifecycle_rules, metrics=metrics, public_read_access=public_read_access, removal_policy=removal_policy, versioned=versioned, website_error_document=website_error_document, website_index_document=website_index_document, website_redirect=website_redirect, website_routing_rules=website_routing_rules)

        jsii.create(SecureBucket, self, [scope, id, props])


__all__ = ["SecureBucket", "__jsii_assembly__"]

publication.publish()
