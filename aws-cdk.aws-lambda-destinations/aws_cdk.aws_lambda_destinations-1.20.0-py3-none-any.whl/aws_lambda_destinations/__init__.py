"""
## Amazon Lambda Destinations Library

<!--BEGIN STABILITY BANNER-->---


![Stability: Stable](https://img.shields.io/badge/stability-Stable-success.svg?style=for-the-badge)

---
<!--END STABILITY BANNER-->

This library provides constructs for adding destinations to a Lambda function.
Destinations can be added by specifying the `onFailure` or `onSuccess` props when creating a function or alias.

## Destinations

The following destinations are supported

* Lambda function
* SQS queue
* SNS topic
* EventBridge event bus

Example with a SNS topic for sucessful invocations:

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_lambda as lambda
import aws_cdk.aws_lambda_destinations as destinations
import aws_cdk.aws_sns as sns

my_topic = sns.Topic(self, "Topic")

my_fn = lambda.Function(self, "Fn",
    # other props
    on_success=destinations.SnsDestionation(my_topic)
)
```

See also [Configuring Destinations for Asynchronous Invocation](https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html#invocation-async-destinations).
"""
import abc
import builtins
import datetime
import enum
import typing

import jsii
import jsii.compat
import publication

import aws_cdk.aws_events
import aws_cdk.aws_lambda
import aws_cdk.aws_sns
import aws_cdk.aws_sqs
import aws_cdk.core

__jsii_assembly__ = jsii.JSIIAssembly.load("@aws-cdk/aws-lambda-destinations", "1.20.0", __name__, "aws-lambda-destinations@1.20.0.jsii.tgz")


@jsii.implements(aws_cdk.aws_lambda.IDestination)
class EventBridgeDestination(metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-lambda-destinations.EventBridgeDestination"):
    """Use an Event Bridge event bus as a Lambda destination.

    If no event bus is specified, the default event bus is used.
    """
    def __init__(self, event_bus: typing.Optional[aws_cdk.aws_events.IEventBus]=None) -> None:
        """
        :param event_bus: -

        default
        :default: - use the default event bus
        """
        jsii.create(EventBridgeDestination, self, [event_bus])

    @jsii.member(jsii_name="bind")
    def bind(self, _scope: aws_cdk.core.Construct, fn: aws_cdk.aws_lambda.IFunction) -> aws_cdk.aws_lambda.DestinationConfig:
        """Returns a destination configuration.

        :param _scope: -
        :param fn: -
        """
        return jsii.invoke(self, "bind", [_scope, fn])


@jsii.implements(aws_cdk.aws_lambda.IDestination)
class LambdaDestination(metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-lambda-destinations.LambdaDestination"):
    """Use a Lambda function as a Lambda destination."""
    def __init__(self, fn: aws_cdk.aws_lambda.IFunction) -> None:
        """
        :param fn: -
        """
        jsii.create(LambdaDestination, self, [fn])

    @jsii.member(jsii_name="bind")
    def bind(self, _scope: aws_cdk.core.Construct, fn: aws_cdk.aws_lambda.IFunction) -> aws_cdk.aws_lambda.DestinationConfig:
        """Returns a destination configuration.

        :param _scope: -
        :param fn: -
        """
        return jsii.invoke(self, "bind", [_scope, fn])


@jsii.implements(aws_cdk.aws_lambda.IDestination)
class SnsDestination(metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-lambda-destinations.SnsDestination"):
    """Use a SNS topic as a Lambda destination."""
    def __init__(self, topic: aws_cdk.aws_sns.ITopic) -> None:
        """
        :param topic: -
        """
        jsii.create(SnsDestination, self, [topic])

    @jsii.member(jsii_name="bind")
    def bind(self, _scope: aws_cdk.core.Construct, fn: aws_cdk.aws_lambda.IFunction) -> aws_cdk.aws_lambda.DestinationConfig:
        """Returns a destination configuration.

        :param _scope: -
        :param fn: -
        """
        return jsii.invoke(self, "bind", [_scope, fn])


@jsii.implements(aws_cdk.aws_lambda.IDestination)
class SqsDestination(metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-lambda-destinations.SqsDestination"):
    """Use a SQS queue as a Lambda destination."""
    def __init__(self, queue: aws_cdk.aws_sqs.IQueue) -> None:
        """
        :param queue: -
        """
        jsii.create(SqsDestination, self, [queue])

    @jsii.member(jsii_name="bind")
    def bind(self, _scope: aws_cdk.core.Construct, fn: aws_cdk.aws_lambda.IFunction) -> aws_cdk.aws_lambda.DestinationConfig:
        """Returns a destination configuration.

        :param _scope: -
        :param fn: -
        """
        return jsii.invoke(self, "bind", [_scope, fn])


__all__ = ["EventBridgeDestination", "LambdaDestination", "SnsDestination", "SqsDestination", "__jsii_assembly__"]

publication.publish()
