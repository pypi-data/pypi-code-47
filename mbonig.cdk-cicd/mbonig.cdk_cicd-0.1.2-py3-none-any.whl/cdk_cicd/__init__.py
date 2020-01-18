"""
# CDK CodePipeline Stack (pre-release)

The purpose of this Construct is to build a CodePipeline stack that builds and deploys a CDK Stack.

This construct is still in development and as such you should use with caution.

# What it creates

This will create a CodePipeline pipeline that builds a CDK module and then deploys it to CloudFormation as a Stack.

## Usage

Refer to the [bin/automation.ts](bin/automation.ts) for an example.

## Properties [lib/cdk-cicd-props.ts](lib/cdk-cicd-props.ts)

| prop | description | usage
| --- | --- | ---
| stackName | The CloudFormation Stack to create/update | must be a valid CFN stack name (e.g. some-stack-name)
| sourceAction | The Source IAction for CodePipeline | Rather than try to account for all source situations, you just provide your own. The factory function is given the Artifact to use as the output target in your Action. If you don't use this artifact, the construct will fail construction.
| createBuildSpec | A Factory that returns a BuildSpec object to use | Refer to the [lib/buildspec-factory.ts] for creating these. You can create your own buildspec if you'd like but there are certain requirements.
| additionalPolicyStatements | Any additional PolicyStatements you'd like to add to the CodeBuild project Role | Useful if you're going to be making AWS API calls from within your CDK 'synth' process during the build.

## Contribute

Always open to any suggestions or help in making this better. Open an Issue.

## License

MIT
"""
import abc
import builtins
import datetime
import enum
import typing

import jsii
import jsii.compat
import publication

import aws_cdk.aws_codebuild
import aws_cdk.aws_codepipeline
import aws_cdk.aws_codepipeline_actions
import aws_cdk.aws_events
import aws_cdk.aws_events_targets
import aws_cdk.aws_s3
import aws_cdk.core

__jsii_assembly__ = jsii.JSIIAssembly.load("cdk-cicd", "0.1.2", __name__, "cdk-cicd@0.1.2.jsii.tgz")


class CdkCicd(aws_cdk.core.Construct, metaclass=jsii.JSIIMeta, jsii_type="cdk-cicd.CdkCicd"):
    def __init__(self, scope: aws_cdk.core.Construct, id: str, props: "ICdkCicdProps") -> None:
        """
        :param scope: -
        :param id: -
        :param props: -
        """
        jsii.create(CdkCicd, self, [scope, id, props])

    @builtins.property
    @jsii.member(jsii_name="codePipeline")
    def code_pipeline(self) -> typing.Optional[aws_cdk.aws_codepipeline.Pipeline]:
        return jsii.get(self, "codePipeline")

    @code_pipeline.setter
    def code_pipeline(self, value: typing.Optional[aws_cdk.aws_codepipeline.Pipeline]):
        jsii.set(self, "codePipeline", value)


@jsii.interface(jsii_type="cdk-cicd.ICdkCicdProps")
class ICdkCicdProps(jsii.compat.Protocol):
    @builtins.staticmethod
    def __jsii_proxy_class__():
        return _ICdkCicdPropsProxy

    @builtins.property
    @jsii.member(jsii_name="stackName")
    def stack_name(self) -> str:
        ...

    @builtins.property
    @jsii.member(jsii_name="buildspec")
    def buildspec(self) -> typing.Any:
        ...

    @builtins.property
    @jsii.member(jsii_name="additionalPolicyStatements")
    def additional_policy_statements(self) -> typing.Optional[typing.List[aws_cdk.aws_iam.PolicyStatement]]:
        ...

    @additional_policy_statements.setter
    def additional_policy_statements(self, value: typing.Optional[typing.List[aws_cdk.aws_iam.PolicyStatement]]):
        ...

    @builtins.property
    @jsii.member(jsii_name="hasLambdas")
    def has_lambdas(self) -> typing.Optional[bool]:
        ...

    @has_lambdas.setter
    def has_lambdas(self, value: typing.Optional[bool]):
        ...

    @jsii.member(jsii_name="createBuildSpec")
    def create_build_spec(self) -> typing.Any:
        ...

    @jsii.member(jsii_name="sourceAction")
    def source_action(self, source_artifact: aws_cdk.aws_codepipeline.Artifact) -> aws_cdk.aws_codepipeline.IAction:
        """
        :param source_artifact: -
        """
        ...


class _ICdkCicdPropsProxy():
    __jsii_type__ = "cdk-cicd.ICdkCicdProps"
    @builtins.property
    @jsii.member(jsii_name="stackName")
    def stack_name(self) -> str:
        return jsii.get(self, "stackName")

    @builtins.property
    @jsii.member(jsii_name="buildspec")
    def buildspec(self) -> typing.Any:
        return jsii.get(self, "buildspec")

    @builtins.property
    @jsii.member(jsii_name="additionalPolicyStatements")
    def additional_policy_statements(self) -> typing.Optional[typing.List[aws_cdk.aws_iam.PolicyStatement]]:
        return jsii.get(self, "additionalPolicyStatements")

    @additional_policy_statements.setter
    def additional_policy_statements(self, value: typing.Optional[typing.List[aws_cdk.aws_iam.PolicyStatement]]):
        jsii.set(self, "additionalPolicyStatements", value)

    @builtins.property
    @jsii.member(jsii_name="hasLambdas")
    def has_lambdas(self) -> typing.Optional[bool]:
        return jsii.get(self, "hasLambdas")

    @has_lambdas.setter
    def has_lambdas(self, value: typing.Optional[bool]):
        jsii.set(self, "hasLambdas", value)

    @jsii.member(jsii_name="createBuildSpec")
    def create_build_spec(self) -> typing.Any:
        return jsii.invoke(self, "createBuildSpec", [])

    @jsii.member(jsii_name="sourceAction")
    def source_action(self, source_artifact: aws_cdk.aws_codepipeline.Artifact) -> aws_cdk.aws_codepipeline.IAction:
        """
        :param source_artifact: -
        """
        return jsii.invoke(self, "sourceAction", [source_artifact])


__all__ = ["CdkCicd", "ICdkCicdProps", "__jsii_assembly__"]

publication.publish()
