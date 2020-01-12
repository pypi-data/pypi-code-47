"""
[![npm version](https://badge.fury.io/js/@taimos/cdk-construct-hosting.svg)](https://badge.fury.io/js/@taimos/cdk-construct-hosting)
[![PyPI version](https://badge.fury.io/py/taimos.cdk-construct-hosting.svg)](https://badge.fury.io/py/taimos.cdk-construct-hosting)

# A CDK L3 Construct for web hosting

## Installation

You can install the library into your project using npm or pip.

```bash
npm install @taimos/cdk-construct-hosting

pip3 install taimos-cdk
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

import aws_cdk.aws_certificatemanager
import aws_cdk.aws_cloudfront
import aws_cdk.aws_route53
import aws_cdk.aws_route53_targets
import aws_cdk.aws_s3
import aws_cdk.aws_s3_deployment
import aws_cdk.core

__jsii_assembly__ = jsii.JSIIAssembly.load("@taimos/cdk-construct-hosting", "1.0.0", __name__, "cdk-construct-hosting@1.0.0.jsii.tgz")


class SinglePageAppHosting(aws_cdk.core.Construct, metaclass=jsii.JSIIMeta, jsii_type="@taimos/cdk-construct-hosting.SinglePageAppHosting"):
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, domain_name: str, cert_arn: typing.Optional[str]=None, index_file: typing.Optional[str]=None, web_folder: typing.Optional[str]=None, zone_id: typing.Optional[str]=None, zone_name: typing.Optional[str]=None) -> None:
        """
        :param scope: -
        :param id: -
        :param domain_name: Name of the domain to deploy.
        :param cert_arn: The ARN of the certificate; Has to be in us-east-1 Default: - create a new certificate in us-east-1
        :param index_file: Name of the index document. Default: index.html
        :param web_folder: local folder with contents for the website bucket. Default: - no file deployment
        :param zone_id: ID of the HostedZone of the domain. Default: - lookup zone from context using the zone name
        :param zone_name: Name of the HostedZone of the domain. Default: - same a the domain name
        """
        props = SinglePageAppHostingProps(domain_name=domain_name, cert_arn=cert_arn, index_file=index_file, web_folder=web_folder, zone_id=zone_id, zone_name=zone_name)

        jsii.create(SinglePageAppHosting, self, [scope, id, props])

    @builtins.property
    @jsii.member(jsii_name="distribution")
    def distribution(self) -> aws_cdk.aws_cloudfront.CloudFrontWebDistribution:
        return jsii.get(self, "distribution")

    @builtins.property
    @jsii.member(jsii_name="webBucket")
    def web_bucket(self) -> aws_cdk.aws_s3.Bucket:
        return jsii.get(self, "webBucket")


@jsii.data_type(jsii_type="@taimos/cdk-construct-hosting.SinglePageAppHostingProps", jsii_struct_bases=[], name_mapping={'domain_name': 'domainName', 'cert_arn': 'certArn', 'index_file': 'indexFile', 'web_folder': 'webFolder', 'zone_id': 'zoneId', 'zone_name': 'zoneName'})
class SinglePageAppHostingProps():
    def __init__(self, *, domain_name: str, cert_arn: typing.Optional[str]=None, index_file: typing.Optional[str]=None, web_folder: typing.Optional[str]=None, zone_id: typing.Optional[str]=None, zone_name: typing.Optional[str]=None):
        """
        :param domain_name: Name of the domain to deploy.
        :param cert_arn: The ARN of the certificate; Has to be in us-east-1 Default: - create a new certificate in us-east-1
        :param index_file: Name of the index document. Default: index.html
        :param web_folder: local folder with contents for the website bucket. Default: - no file deployment
        :param zone_id: ID of the HostedZone of the domain. Default: - lookup zone from context using the zone name
        :param zone_name: Name of the HostedZone of the domain. Default: - same a the domain name
        """
        self._values = {
            'domain_name': domain_name,
        }
        if cert_arn is not None: self._values["cert_arn"] = cert_arn
        if index_file is not None: self._values["index_file"] = index_file
        if web_folder is not None: self._values["web_folder"] = web_folder
        if zone_id is not None: self._values["zone_id"] = zone_id
        if zone_name is not None: self._values["zone_name"] = zone_name

    @builtins.property
    def domain_name(self) -> str:
        """Name of the domain to deploy."""
        return self._values.get('domain_name')

    @builtins.property
    def cert_arn(self) -> typing.Optional[str]:
        """The ARN of the certificate;

        Has to be in us-east-1

        default
        :default: - create a new certificate in us-east-1
        """
        return self._values.get('cert_arn')

    @builtins.property
    def index_file(self) -> typing.Optional[str]:
        """Name of the index document.

        default
        :default: index.html
        """
        return self._values.get('index_file')

    @builtins.property
    def web_folder(self) -> typing.Optional[str]:
        """local folder with contents for the website bucket.

        default
        :default: - no file deployment
        """
        return self._values.get('web_folder')

    @builtins.property
    def zone_id(self) -> typing.Optional[str]:
        """ID of the HostedZone of the domain.

        default
        :default: - lookup zone from context using the zone name
        """
        return self._values.get('zone_id')

    @builtins.property
    def zone_name(self) -> typing.Optional[str]:
        """Name of the HostedZone of the domain.

        default
        :default: - same a the domain name
        """
        return self._values.get('zone_name')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'SinglePageAppHostingProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


__all__ = ["SinglePageAppHosting", "SinglePageAppHostingProps", "__jsii_assembly__"]

publication.publish()
