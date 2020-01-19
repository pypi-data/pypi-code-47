"""
# CDK CodePipeline Stack (pre-release)

The purpose of this Construct is to build a CodePipeline stack that builds and deploys a CDK Stack.

This construct is still in development and as such you should use with caution.

# What it creates

This will create a CodePipeline pipeline that builds a CDK module and then deploys it to CloudFormation as a Stack.

## Usage

Refer to the [bin/automation.ts](bin/automation.ts) for an example.

## Properties [lib/cdk-cicd.ts](lib/cdk-cicd.ts)

| prop | description | usage
| --- | --- | ---
| stackName | The CloudFormation Stack to create/update | must be a valid CFN stack name (e.g. some-stack-name)
| sourceAction | The Source IAction for CodePipeline | Rather than try to account for all source situations, you just provide your own. The factory function is given the Artifact to use as the output target in your Action. If you don't use this artifact, the construct will fail construction.
| createBuildSpec | A Factory that returns a BuildSpec object to use | Refer to the [lib/buildspec-factory.ts](lib/buildspec-factory.ts) for creating these. You can create your own buildspec if you'd like but there are certain requirements; you have to have artifacts setup properly.
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

__jsii_assembly__ = jsii.JSIIAssembly.load("cdk-cicd", "0.1.3", __name__, "cdk-cicd@0.1.3.jsii.tgz")


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
        """The name of the Stack to create/update with the pipeline."""
        ...

    @builtins.property
    @jsii.member(jsii_name="additionalPolicyStatements")
    def additional_policy_statements(self) -> typing.Optional[typing.List[aws_cdk.aws_iam.PolicyStatement]]:
        """Additional PolicyStatement you'd like applied to the CodeBuild project role.

        This comes in useful if your CDK module will need to make API calls to the AWS SDK
        """
        ...

    @additional_policy_statements.setter
    def additional_policy_statements(self, value: typing.Optional[typing.List[aws_cdk.aws_iam.PolicyStatement]]):
        ...

    @builtins.property
    @jsii.member(jsii_name="hasLambdas")
    def has_lambdas(self) -> typing.Optional[bool]:
        """If your CDK module will be using assets, like Lambdas, then enable this to get a bucket name passed to the CodeBuild runtime as the S3_LAMBDA_BUCKET environment variable."""
        ...

    @has_lambdas.setter
    def has_lambdas(self, value: typing.Optional[bool]):
        ...

    @jsii.member(jsii_name="createBuildSpec")
    def create_build_spec(self) -> typing.Any:
        """A BuildSpec object factory to use in the CodeBuild pipeline.

        You can use the `BuildSpecFactory <./buildspec-factory.ts>`_
        """
        ...

    @jsii.member(jsii_name="sourceAction")
    def source_action(self, source_artifact: aws_cdk.aws_codepipeline.Artifact) -> aws_cdk.aws_codepipeline.IAction:
        """A source action factory.

        This is the first step in the pipeline.

        :param source_artifact: - the artifact that source pipeline should put output artifacts.
        """
        ...


class _ICdkCicdPropsProxy():
    __jsii_type__ = "cdk-cicd.ICdkCicdProps"
    @builtins.property
    @jsii.member(jsii_name="stackName")
    def stack_name(self) -> str:
        """The name of the Stack to create/update with the pipeline."""
        return jsii.get(self, "stackName")

    @builtins.property
    @jsii.member(jsii_name="additionalPolicyStatements")
    def additional_policy_statements(self) -> typing.Optional[typing.List[aws_cdk.aws_iam.PolicyStatement]]:
        """Additional PolicyStatement you'd like applied to the CodeBuild project role.

        This comes in useful if your CDK module will need to make API calls to the AWS SDK
        """
        return jsii.get(self, "additionalPolicyStatements")

    @additional_policy_statements.setter
    def additional_policy_statements(self, value: typing.Optional[typing.List[aws_cdk.aws_iam.PolicyStatement]]):
        jsii.set(self, "additionalPolicyStatements", value)

    @builtins.property
    @jsii.member(jsii_name="hasLambdas")
    def has_lambdas(self) -> typing.Optional[bool]:
        """If your CDK module will be using assets, like Lambdas, then enable this to get a bucket name passed to the CodeBuild runtime as the S3_LAMBDA_BUCKET environment variable."""
        return jsii.get(self, "hasLambdas")

    @has_lambdas.setter
    def has_lambdas(self, value: typing.Optional[bool]):
        jsii.set(self, "hasLambdas", value)

    @jsii.member(jsii_name="createBuildSpec")
    def create_build_spec(self) -> typing.Any:
        """A BuildSpec object factory to use in the CodeBuild pipeline.

        You can use the `BuildSpecFactory <./buildspec-factory.ts>`_
        """
        return jsii.invoke(self, "createBuildSpec", [])

    @jsii.member(jsii_name="sourceAction")
    def source_action(self, source_artifact: aws_cdk.aws_codepipeline.Artifact) -> aws_cdk.aws_codepipeline.IAction:
        """A source action factory.

        This is the first step in the pipeline.

        :param source_artifact: - the artifact that source pipeline should put output artifacts.
        """
        return jsii.invoke(self, "sourceAction", [source_artifact])


__all__ = ["CdkCicd", "ICdkCicdProps", "__jsii_assembly__"]

publication.publish()
