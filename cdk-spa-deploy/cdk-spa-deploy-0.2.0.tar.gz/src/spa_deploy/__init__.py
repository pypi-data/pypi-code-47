"""
# CDK-SPA-Deploy

This is an AWS CDK Construct to make deploying a single page website (Angular/React/Vue) to AWS S3 behind SSL/Cloudfront easier

## Installation and Usage

### Typescript

npm install --save cdk-spa-deploy

![cdk-spa-deploy example](https://raw.githubusercontent.com/nideveloper/cdk-spa-deploy/master/img/spadeploy.png)

### Python

pip install cdk-spa-deploy

![cdk-spa-deploy python example](https://raw.githubusercontent.com/nideveloper/cdk-spa-deploy/master/img/python.png)

## Advanced Usage

You can also pass the ARN for an SSL certification and your alias routes to cloudfront

![cdk-spa-deploy alias](https://raw.githubusercontent.com/nideveloper/cdk-spa-deploy/master/img/cdkdeploy-alias.png)

## Issues / Feature Requests

https://github.com/nideveloper/CDK-SPA-Deploy
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
import aws_cdk.aws_s3
import aws_cdk.aws_s3_deployment
import aws_cdk.core

__jsii_assembly__ = jsii.JSIIAssembly.load("cdk-spa-deploy", "0.2.0", __name__, "cdk-spa-deploy@0.2.0.jsii.tgz")


class SPADeploy(aws_cdk.core.Construct, metaclass=jsii.JSIIMeta, jsii_type="cdk-spa-deploy.SPADeploy"):
    def __init__(self, scope: aws_cdk.core.Construct, id: str) -> None:
        """
        :param scope: -
        :param id: -
        """
        jsii.create(SPADeploy, self, [scope, id])

    @jsii.member(jsii_name="createBasicSite")
    def create_basic_site(self, *, index_doc: str, website_folder: str, certificate_arn: typing.Optional[str]=None, cf_aliases: typing.Optional[typing.List[str]]=None) -> None:
        """Basic setup needed for a non-ssl, non vanity url, non cached s3 website.

        :param index_doc: -
        :param website_folder: -
        :param certificate_arn: -
        :param cf_aliases: -
        """
        config = SPADeployConfig(index_doc=index_doc, website_folder=website_folder, certificate_arn=certificate_arn, cf_aliases=cf_aliases)

        return jsii.invoke(self, "createBasicSite", [config])

    @jsii.member(jsii_name="createSiteWithCloudfront")
    def create_site_with_cloudfront(self, *, index_doc: str, website_folder: str, certificate_arn: typing.Optional[str]=None, cf_aliases: typing.Optional[typing.List[str]]=None) -> None:
        """This will create an s3 deployment fronted by a cloudfront distribution It will also setup error forwarding and unauth forwarding back to indexDoc.

        :param index_doc: -
        :param website_folder: -
        :param certificate_arn: -
        :param cf_aliases: -
        """
        config = SPADeployConfig(index_doc=index_doc, website_folder=website_folder, certificate_arn=certificate_arn, cf_aliases=cf_aliases)

        return jsii.invoke(self, "createSiteWithCloudfront", [config])


@jsii.data_type(jsii_type="cdk-spa-deploy.SPADeployConfig", jsii_struct_bases=[], name_mapping={'index_doc': 'indexDoc', 'website_folder': 'websiteFolder', 'certificate_arn': 'certificateARN', 'cf_aliases': 'cfAliases'})
class SPADeployConfig():
    def __init__(self, *, index_doc: str, website_folder: str, certificate_arn: typing.Optional[str]=None, cf_aliases: typing.Optional[typing.List[str]]=None):
        """
        :param index_doc: -
        :param website_folder: -
        :param certificate_arn: -
        :param cf_aliases: -
        """
        self._values = {
            'index_doc': index_doc,
            'website_folder': website_folder,
        }
        if certificate_arn is not None: self._values["certificate_arn"] = certificate_arn
        if cf_aliases is not None: self._values["cf_aliases"] = cf_aliases

    @builtins.property
    def index_doc(self) -> str:
        return self._values.get('index_doc')

    @builtins.property
    def website_folder(self) -> str:
        return self._values.get('website_folder')

    @builtins.property
    def certificate_arn(self) -> typing.Optional[str]:
        return self._values.get('certificate_arn')

    @builtins.property
    def cf_aliases(self) -> typing.Optional[typing.List[str]]:
        return self._values.get('cf_aliases')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'SPADeployConfig(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


__all__ = ["SPADeploy", "SPADeployConfig", "__jsii_assembly__"]

publication.publish()
