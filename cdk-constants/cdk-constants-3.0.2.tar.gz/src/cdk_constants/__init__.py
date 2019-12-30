"""
# CDK Constants

This repository contains constants that make it easier to work with the [aws-cdk](https://github.com/aws/aws-cdk) (CDK).

## Why?

The CDK is awesome but it currently lacks types when initializing constructs such as IAM service principals and managed policies. Finding the right construct names requires diving into AWS documentation. Because there is no verification of these construct initializers, errors are only surfaced after deployment and via a rollback.

This library aims to be an up to date constants library for all things AWS so the above never happens again!

## Quickstart

Install or update from npm

TypeScript/Javascript

```console
npm i cdk-constants

```

Python

```console
pip install cdk-constants
```

## Usage

** TypeScript **

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
from cdk_constants import ServicePrincipals, ManagedPolicies

lambda_role = Role(self, "lambdaDomainChecker",
    assumed_by=ServicePrincipal(ServicePrincipals.LAMBDA),
    managed_policies=[
        ManagedPolicy.from_aws_managed_policy_name(ManagedPolicies.AWS_LAMBDA_BASIC_EXECUTION_ROLE)
    ]
)
```

** Python **

```python
from cdk_constants import ServicePrincipals, ManagedPolicies

lambda_role = Role(self, "lambdaDomainChecker",
    assumed_by=ServicePrincipal(ServicePrincipals.LAMBDA),
    managed_policies=[
        ManagedPolicy.from_aws_managed_policy_name(ManagedPolicies.AWS_LAMBDA_BASIC_EXECUTION_ROLE)
    ]
)
```

## Properties

### [ServicePrincipals](https://github.com/kevinslin/cdk-constants/blob/master/lib/principals.ts)

* AWS services principals

### [ManagedPolicies](https://github.com/kevinslin/cdk-constants/blob/master/lib/policies.ts)

* Managed AWS policies

## Credits

`cdk-constants` wouldn't be possible without modules from the following authors

* [Jared Short](https://gist.github.com/shortjared): initial [gist](https://gist.github.com/shortjared/4c1e3fe52bdfa47522cfe5b41e5d6f22) of all service principals
* [Gene Wood](https://gist.github.com/gene1wood): [gist](https://gist.github.com/gene1wood/55b358748be3c314f956) to pull all aws managed policies

## Contributions

All contributors are welcome. As you are reading this, AWS has probably released a new service. Please see [CONTRIBUTING](CONTRIBUTING.md) for information on how to setup a development environment and submit code.

Some upcoming items on the roadmap:

* list of aws regions and azs, including gov and china
* list of all iam permissions
* [x] jsii compilation into different languages that CDK supports

## License

cdk-constants is distributed under the [Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0).

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

__jsii_assembly__ = jsii.JSIIAssembly.load("cdk-constants", "3.0.2", __name__, "cdk-constants@3.0.2.jsii.tgz")


class FederatedPrincipals(metaclass=jsii.JSIIMeta, jsii_type="cdk-constants.FederatedPrincipals"):
    def __init__(self) -> None:
        jsii.create(FederatedPrincipals, self, [])

    @jsii.python.classproperty
    @jsii.member(jsii_name="COGNITO_IDENTITY")
    def COGNITO_IDENTITY(cls) -> str:
        return jsii.sget(cls, "COGNITO_IDENTITY")


class ManagedPolicies(metaclass=jsii.JSIIMeta, jsii_type="cdk-constants.ManagedPolicies"):
    def __init__(self) -> None:
        jsii.create(ManagedPolicies, self, [])

    @jsii.python.classproperty
    @jsii.member(jsii_name="ACCESS_ANALYZER_SERVICE_ROLE_POLICY")
    def ACCESS_ANALYZER_SERVICE_ROLE_POLICY(cls) -> str:
        return jsii.sget(cls, "ACCESS_ANALYZER_SERVICE_ROLE_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="ADMINISTRATOR_ACCESS")
    def ADMINISTRATOR_ACCESS(cls) -> str:
        return jsii.sget(cls, "ADMINISTRATOR_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="ALEXA_FOR_BUSINESS_DEVICE_SETUP")
    def ALEXA_FOR_BUSINESS_DEVICE_SETUP(cls) -> str:
        return jsii.sget(cls, "ALEXA_FOR_BUSINESS_DEVICE_SETUP")

    @jsii.python.classproperty
    @jsii.member(jsii_name="ALEXA_FOR_BUSINESS_FULL_ACCESS")
    def ALEXA_FOR_BUSINESS_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "ALEXA_FOR_BUSINESS_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="ALEXA_FOR_BUSINESS_GATEWAY_EXECUTION")
    def ALEXA_FOR_BUSINESS_GATEWAY_EXECUTION(cls) -> str:
        return jsii.sget(cls, "ALEXA_FOR_BUSINESS_GATEWAY_EXECUTION")

    @jsii.python.classproperty
    @jsii.member(jsii_name="ALEXA_FOR_BUSINESS_NETWORK_PROFILE_SERVICE_POLICY")
    def ALEXA_FOR_BUSINESS_NETWORK_PROFILE_SERVICE_POLICY(cls) -> str:
        return jsii.sget(cls, "ALEXA_FOR_BUSINESS_NETWORK_PROFILE_SERVICE_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="ALEXA_FOR_BUSINESS_POLY_DELEGATED_ACCESS_POLICY")
    def ALEXA_FOR_BUSINESS_POLY_DELEGATED_ACCESS_POLICY(cls) -> str:
        return jsii.sget(cls, "ALEXA_FOR_BUSINESS_POLY_DELEGATED_ACCESS_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="ALEXA_FOR_BUSINESS_READ_ONLY_ACCESS")
    def ALEXA_FOR_BUSINESS_READ_ONLY_ACCESS(cls) -> str:
        return jsii.sget(cls, "ALEXA_FOR_BUSINESS_READ_ONLY_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_API_GATEWAY_ADMINISTRATOR")
    def AMAZON_API_GATEWAY_ADMINISTRATOR(cls) -> str:
        return jsii.sget(cls, "AMAZON_API_GATEWAY_ADMINISTRATOR")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_API_GATEWAY_INVOKE_FULL_ACCESS")
    def AMAZON_API_GATEWAY_INVOKE_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_API_GATEWAY_INVOKE_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_API_GATEWAY_PUSH_TO_CLOUD_WATCH_LOGS")
    def AMAZON_API_GATEWAY_PUSH_TO_CLOUD_WATCH_LOGS(cls) -> str:
        return jsii.sget(cls, "AMAZON_API_GATEWAY_PUSH_TO_CLOUD_WATCH_LOGS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_APP_STREAM_FULL_ACCESS")
    def AMAZON_APP_STREAM_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_APP_STREAM_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_APP_STREAM_READ_ONLY_ACCESS")
    def AMAZON_APP_STREAM_READ_ONLY_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_APP_STREAM_READ_ONLY_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_APP_STREAM_SERVICE_ACCESS")
    def AMAZON_APP_STREAM_SERVICE_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_APP_STREAM_SERVICE_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_ATHENA_FULL_ACCESS")
    def AMAZON_ATHENA_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_ATHENA_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_AUGMENTED_AI_FULL_ACCESS")
    def AMAZON_AUGMENTED_AI_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_AUGMENTED_AI_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_AUGMENTED_AI_HUMAN_LOOP_FULL_ACCESS")
    def AMAZON_AUGMENTED_AI_HUMAN_LOOP_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_AUGMENTED_AI_HUMAN_LOOP_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_CHIME_FULL_ACCESS")
    def AMAZON_CHIME_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_CHIME_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_CHIME_READ_ONLY")
    def AMAZON_CHIME_READ_ONLY(cls) -> str:
        return jsii.sget(cls, "AMAZON_CHIME_READ_ONLY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_CHIME_SERVICE_ROLE_POLICY")
    def AMAZON_CHIME_SERVICE_ROLE_POLICY(cls) -> str:
        return jsii.sget(cls, "AMAZON_CHIME_SERVICE_ROLE_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_CHIME_USER_MANAGEMENT")
    def AMAZON_CHIME_USER_MANAGEMENT(cls) -> str:
        return jsii.sget(cls, "AMAZON_CHIME_USER_MANAGEMENT")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_CHIME_VOICE_CONNECTOR_SERVICE_LINKED_ROLE_POLICY")
    def AMAZON_CHIME_VOICE_CONNECTOR_SERVICE_LINKED_ROLE_POLICY(cls) -> str:
        return jsii.sget(cls, "AMAZON_CHIME_VOICE_CONNECTOR_SERVICE_LINKED_ROLE_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_CLOUD_DIRECTORY_FULL_ACCESS")
    def AMAZON_CLOUD_DIRECTORY_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_CLOUD_DIRECTORY_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_CLOUD_DIRECTORY_READ_ONLY_ACCESS")
    def AMAZON_CLOUD_DIRECTORY_READ_ONLY_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_CLOUD_DIRECTORY_READ_ONLY_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_CODE_GURU_PROFILER_FULL_ACCESS")
    def AMAZON_CODE_GURU_PROFILER_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_CODE_GURU_PROFILER_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_CODE_GURU_PROFILER_READ_ONLY_ACCESS")
    def AMAZON_CODE_GURU_PROFILER_READ_ONLY_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_CODE_GURU_PROFILER_READ_ONLY_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_CODE_GURU_REVIEWER_FULL_ACCESS")
    def AMAZON_CODE_GURU_REVIEWER_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_CODE_GURU_REVIEWER_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_CODE_GURU_REVIEWER_READ_ONLY_ACCESS")
    def AMAZON_CODE_GURU_REVIEWER_READ_ONLY_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_CODE_GURU_REVIEWER_READ_ONLY_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_CODE_GURU_REVIEWER_SERVICE_ROLE_POLICY")
    def AMAZON_CODE_GURU_REVIEWER_SERVICE_ROLE_POLICY(cls) -> str:
        return jsii.sget(cls, "AMAZON_CODE_GURU_REVIEWER_SERVICE_ROLE_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_COGNITO_DEVELOPER_AUTHENTICATED_IDENTITIES")
    def AMAZON_COGNITO_DEVELOPER_AUTHENTICATED_IDENTITIES(cls) -> str:
        return jsii.sget(cls, "AMAZON_COGNITO_DEVELOPER_AUTHENTICATED_IDENTITIES")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_COGNITO_IDP_EMAIL_SERVICE_ROLE_POLICY")
    def AMAZON_COGNITO_IDP_EMAIL_SERVICE_ROLE_POLICY(cls) -> str:
        return jsii.sget(cls, "AMAZON_COGNITO_IDP_EMAIL_SERVICE_ROLE_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_COGNITO_POWER_USER")
    def AMAZON_COGNITO_POWER_USER(cls) -> str:
        return jsii.sget(cls, "AMAZON_COGNITO_POWER_USER")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_COGNITO_READ_ONLY")
    def AMAZON_COGNITO_READ_ONLY(cls) -> str:
        return jsii.sget(cls, "AMAZON_COGNITO_READ_ONLY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_CONNECT_FULL_ACCESS")
    def AMAZON_CONNECT_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_CONNECT_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_CONNECT_READ_ONLY_ACCESS")
    def AMAZON_CONNECT_READ_ONLY_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_CONNECT_READ_ONLY_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_CONNECT_SERVICE_LINKED_ROLE_POLICY")
    def AMAZON_CONNECT_SERVICE_LINKED_ROLE_POLICY(cls) -> str:
        return jsii.sget(cls, "AMAZON_CONNECT_SERVICE_LINKED_ROLE_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_DMS_CLOUD_WATCH_LOGS_ROLE")
    def AMAZON_DMS_CLOUD_WATCH_LOGS_ROLE(cls) -> str:
        return jsii.sget(cls, "AMAZON_DMS_CLOUD_WATCH_LOGS_ROLE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_DMS_REDSHIFT_S3_ROLE")
    def AMAZON_DMS_REDSHIFT_S3_ROLE(cls) -> str:
        return jsii.sget(cls, "AMAZON_DMS_REDSHIFT_S3_ROLE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_DMSVPC_MANAGEMENT_ROLE")
    def AMAZON_DMSVPC_MANAGEMENT_ROLE(cls) -> str:
        return jsii.sget(cls, "AMAZON_DMSVPC_MANAGEMENT_ROLE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_DOC_DB_CONSOLE_FULL_ACCESS")
    def AMAZON_DOC_DB_CONSOLE_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_DOC_DB_CONSOLE_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_DOC_DB_FULL_ACCESS")
    def AMAZON_DOC_DB_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_DOC_DB_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_DOC_DB_READ_ONLY_ACCESS")
    def AMAZON_DOC_DB_READ_ONLY_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_DOC_DB_READ_ONLY_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_DRSVPC_MANAGEMENT")
    def AMAZON_DRSVPC_MANAGEMENT(cls) -> str:
        return jsii.sget(cls, "AMAZON_DRSVPC_MANAGEMENT")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_DYNAMO_DB_FULL_ACCESS")
    def AMAZON_DYNAMO_DB_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_DYNAMO_DB_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_DYNAMO_DB_FULL_ACCESSWITH_DATA_PIPELINE")
    def AMAZON_DYNAMO_DB_FULL_ACCESSWITH_DATA_PIPELINE(cls) -> str:
        return jsii.sget(cls, "AMAZON_DYNAMO_DB_FULL_ACCESSWITH_DATA_PIPELINE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_DYNAMO_DB_READ_ONLY_ACCESS")
    def AMAZON_DYNAMO_DB_READ_ONLY_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_DYNAMO_DB_READ_ONLY_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_EC2_CONTAINER_REGISTRY_FULL_ACCESS")
    def AMAZON_E_C2_CONTAINER_REGISTRY_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_EC2_CONTAINER_REGISTRY_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_EC2_CONTAINER_REGISTRY_POWER_USER")
    def AMAZON_E_C2_CONTAINER_REGISTRY_POWER_USER(cls) -> str:
        return jsii.sget(cls, "AMAZON_EC2_CONTAINER_REGISTRY_POWER_USER")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_EC2_CONTAINER_REGISTRY_READ_ONLY")
    def AMAZON_E_C2_CONTAINER_REGISTRY_READ_ONLY(cls) -> str:
        return jsii.sget(cls, "AMAZON_EC2_CONTAINER_REGISTRY_READ_ONLY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_EC2_CONTAINER_SERVICE_AUTOSCALE_ROLE")
    def AMAZON_E_C2_CONTAINER_SERVICE_AUTOSCALE_ROLE(cls) -> str:
        return jsii.sget(cls, "AMAZON_EC2_CONTAINER_SERVICE_AUTOSCALE_ROLE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_EC2_CONTAINER_SERVICE_EVENTS_ROLE")
    def AMAZON_E_C2_CONTAINER_SERVICE_EVENTS_ROLE(cls) -> str:
        return jsii.sget(cls, "AMAZON_EC2_CONTAINER_SERVICE_EVENTS_ROLE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_EC2_CONTAINER_SERVICE_FULL_ACCESS")
    def AMAZON_E_C2_CONTAINER_SERVICE_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_EC2_CONTAINER_SERVICE_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_EC2_CONTAINER_SERVICE_ROLE")
    def AMAZON_E_C2_CONTAINER_SERVICE_ROLE(cls) -> str:
        return jsii.sget(cls, "AMAZON_EC2_CONTAINER_SERVICE_ROLE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_EC2_CONTAINER_SERVICEFOR_EC_2_ROLE")
    def AMAZON_E_C2_CONTAINER_SERVICEFOR_EC_2_ROLE(cls) -> str:
        return jsii.sget(cls, "AMAZON_EC2_CONTAINER_SERVICEFOR_EC_2_ROLE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_EC2_FULL_ACCESS")
    def AMAZON_E_C2_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_EC2_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_EC2_READ_ONLY_ACCESS")
    def AMAZON_E_C2_READ_ONLY_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_EC2_READ_ONLY_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_EC2_REPORTS_ACCESS")
    def AMAZON_E_C2_REPORTS_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_EC2_REPORTS_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_EC2_ROLE_POLICY_FOR_LAUNCH_WIZARD")
    def AMAZON_E_C2_ROLE_POLICY_FOR_LAUNCH_WIZARD(cls) -> str:
        return jsii.sget(cls, "AMAZON_EC2_ROLE_POLICY_FOR_LAUNCH_WIZARD")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_EC2_ROLEFOR_AWS_CODE_DEPLOY")
    def AMAZON_E_C2_ROLEFOR_AWS_CODE_DEPLOY(cls) -> str:
        return jsii.sget(cls, "AMAZON_EC2_ROLEFOR_AWS_CODE_DEPLOY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_EC2_ROLEFOR_DATA_PIPELINE_ROLE")
    def AMAZON_E_C2_ROLEFOR_DATA_PIPELINE_ROLE(cls) -> str:
        return jsii.sget(cls, "AMAZON_EC2_ROLEFOR_DATA_PIPELINE_ROLE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_EC2_ROLEFOR_SSM")
    def AMAZON_E_C2_ROLEFOR_SSM(cls) -> str:
        return jsii.sget(cls, "AMAZON_EC2_ROLEFOR_SSM")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_EC2_SPOT_FLEET_AUTOSCALE_ROLE")
    def AMAZON_E_C2_SPOT_FLEET_AUTOSCALE_ROLE(cls) -> str:
        return jsii.sget(cls, "AMAZON_EC2_SPOT_FLEET_AUTOSCALE_ROLE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_EC2_SPOT_FLEET_TAGGING_ROLE")
    def AMAZON_E_C2_SPOT_FLEET_TAGGING_ROLE(cls) -> str:
        return jsii.sget(cls, "AMAZON_EC2_SPOT_FLEET_TAGGING_ROLE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_ECS_FULL_ACCESS")
    def AMAZON_ECS_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_ECS_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_ECS_SERVICE_ROLE_POLICY")
    def AMAZON_ECS_SERVICE_ROLE_POLICY(cls) -> str:
        return jsii.sget(cls, "AMAZON_ECS_SERVICE_ROLE_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_ECS_TASK_EXECUTION_ROLE_POLICY")
    def AMAZON_ECS_TASK_EXECUTION_ROLE_POLICY(cls) -> str:
        return jsii.sget(cls, "AMAZON_ECS_TASK_EXECUTION_ROLE_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_EKS_CLUSTER_POLICY")
    def AMAZON_EKS_CLUSTER_POLICY(cls) -> str:
        return jsii.sget(cls, "AMAZON_EKS_CLUSTER_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_EKS_CNI_POLICY")
    def AMAZON_EKS_CNI_POLICY(cls) -> str:
        return jsii.sget(cls, "AMAZON_EKS_CNI_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_EKS_FARGATE_POD_EXECUTION_ROLE_POLICY")
    def AMAZON_EKS_FARGATE_POD_EXECUTION_ROLE_POLICY(cls) -> str:
        return jsii.sget(cls, "AMAZON_EKS_FARGATE_POD_EXECUTION_ROLE_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_EKS_FOR_FARGATE_SERVICE_ROLE_POLICY")
    def AMAZON_EKS_FOR_FARGATE_SERVICE_ROLE_POLICY(cls) -> str:
        return jsii.sget(cls, "AMAZON_EKS_FOR_FARGATE_SERVICE_ROLE_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_EKS_SERVICE_POLICY")
    def AMAZON_EKS_SERVICE_POLICY(cls) -> str:
        return jsii.sget(cls, "AMAZON_EKS_SERVICE_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_EKS_WORKER_NODE_POLICY")
    def AMAZON_EKS_WORKER_NODE_POLICY(cls) -> str:
        return jsii.sget(cls, "AMAZON_EKS_WORKER_NODE_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_ELASTI_CACHE_FULL_ACCESS")
    def AMAZON_ELASTI_CACHE_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_ELASTI_CACHE_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_ELASTI_CACHE_READ_ONLY_ACCESS")
    def AMAZON_ELASTI_CACHE_READ_ONLY_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_ELASTI_CACHE_READ_ONLY_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_ELASTIC_FILE_SYSTEM_FULL_ACCESS")
    def AMAZON_ELASTIC_FILE_SYSTEM_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_ELASTIC_FILE_SYSTEM_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_ELASTIC_FILE_SYSTEM_READ_ONLY_ACCESS")
    def AMAZON_ELASTIC_FILE_SYSTEM_READ_ONLY_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_ELASTIC_FILE_SYSTEM_READ_ONLY_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_ELASTIC_FILE_SYSTEM_SERVICE_ROLE_POLICY")
    def AMAZON_ELASTIC_FILE_SYSTEM_SERVICE_ROLE_POLICY(cls) -> str:
        return jsii.sget(cls, "AMAZON_ELASTIC_FILE_SYSTEM_SERVICE_ROLE_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_ELASTIC_MAP_REDUCE_EDITORS_ROLE")
    def AMAZON_ELASTIC_MAP_REDUCE_EDITORS_ROLE(cls) -> str:
        return jsii.sget(cls, "AMAZON_ELASTIC_MAP_REDUCE_EDITORS_ROLE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_ELASTIC_MAP_REDUCE_FULL_ACCESS")
    def AMAZON_ELASTIC_MAP_REDUCE_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_ELASTIC_MAP_REDUCE_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_ELASTIC_MAP_REDUCE_READ_ONLY_ACCESS")
    def AMAZON_ELASTIC_MAP_REDUCE_READ_ONLY_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_ELASTIC_MAP_REDUCE_READ_ONLY_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_ELASTIC_MAP_REDUCE_ROLE")
    def AMAZON_ELASTIC_MAP_REDUCE_ROLE(cls) -> str:
        return jsii.sget(cls, "AMAZON_ELASTIC_MAP_REDUCE_ROLE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_ELASTIC_MAP_REDUCEFOR_AUTO_SCALING_ROLE")
    def AMAZON_ELASTIC_MAP_REDUCEFOR_AUTO_SCALING_ROLE(cls) -> str:
        return jsii.sget(cls, "AMAZON_ELASTIC_MAP_REDUCEFOR_AUTO_SCALING_ROLE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_ELASTIC_MAP_REDUCEFOR_EC2_ROLE")
    def AMAZON_ELASTIC_MAP_REDUCEFOR_E_C2_ROLE(cls) -> str:
        return jsii.sget(cls, "AMAZON_ELASTIC_MAP_REDUCEFOR_EC2_ROLE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_ELASTIC_TRANSCODER_FULL_ACCESS")
    def AMAZON_ELASTIC_TRANSCODER_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_ELASTIC_TRANSCODER_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_ELASTIC_TRANSCODER_JOBS_SUBMITTER")
    def AMAZON_ELASTIC_TRANSCODER_JOBS_SUBMITTER(cls) -> str:
        return jsii.sget(cls, "AMAZON_ELASTIC_TRANSCODER_JOBS_SUBMITTER")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_ELASTIC_TRANSCODER_READ_ONLY_ACCESS")
    def AMAZON_ELASTIC_TRANSCODER_READ_ONLY_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_ELASTIC_TRANSCODER_READ_ONLY_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_ELASTIC_TRANSCODER_ROLE")
    def AMAZON_ELASTIC_TRANSCODER_ROLE(cls) -> str:
        return jsii.sget(cls, "AMAZON_ELASTIC_TRANSCODER_ROLE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_ELASTICSEARCH_SERVICE_ROLE_POLICY")
    def AMAZON_ELASTICSEARCH_SERVICE_ROLE_POLICY(cls) -> str:
        return jsii.sget(cls, "AMAZON_ELASTICSEARCH_SERVICE_ROLE_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_EMR_CLEANUP_POLICY")
    def AMAZON_EMR_CLEANUP_POLICY(cls) -> str:
        return jsii.sget(cls, "AMAZON_EMR_CLEANUP_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_ES_COGNITO_ACCESS")
    def AMAZON_ES_COGNITO_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_ES_COGNITO_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_ES_FULL_ACCESS")
    def AMAZON_ES_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_ES_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_ES_READ_ONLY_ACCESS")
    def AMAZON_ES_READ_ONLY_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_ES_READ_ONLY_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_EVENT_BRIDGE_FULL_ACCESS")
    def AMAZON_EVENT_BRIDGE_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_EVENT_BRIDGE_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_EVENT_BRIDGE_READ_ONLY_ACCESS")
    def AMAZON_EVENT_BRIDGE_READ_ONLY_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_EVENT_BRIDGE_READ_ONLY_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_EVENT_BRIDGE_SCHEMAS_FULL_ACCESS")
    def AMAZON_EVENT_BRIDGE_SCHEMAS_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_EVENT_BRIDGE_SCHEMAS_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_EVENT_BRIDGE_SCHEMAS_READ_ONLY_ACCESS")
    def AMAZON_EVENT_BRIDGE_SCHEMAS_READ_ONLY_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_EVENT_BRIDGE_SCHEMAS_READ_ONLY_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_EVENT_BRIDGE_SCHEMAS_SERVICE_ROLE_POLICY")
    def AMAZON_EVENT_BRIDGE_SCHEMAS_SERVICE_ROLE_POLICY(cls) -> str:
        return jsii.sget(cls, "AMAZON_EVENT_BRIDGE_SCHEMAS_SERVICE_ROLE_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_F_SX_CONSOLE_FULL_ACCESS")
    def AMAZON_F_SX_CONSOLE_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_F_SX_CONSOLE_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_F_SX_CONSOLE_READ_ONLY_ACCESS")
    def AMAZON_F_SX_CONSOLE_READ_ONLY_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_F_SX_CONSOLE_READ_ONLY_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_F_SX_FULL_ACCESS")
    def AMAZON_F_SX_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_F_SX_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_F_SX_READ_ONLY_ACCESS")
    def AMAZON_F_SX_READ_ONLY_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_F_SX_READ_ONLY_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_F_SX_SERVICE_ROLE_POLICY")
    def AMAZON_F_SX_SERVICE_ROLE_POLICY(cls) -> str:
        return jsii.sget(cls, "AMAZON_F_SX_SERVICE_ROLE_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_FORECAST_FULL_ACCESS")
    def AMAZON_FORECAST_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_FORECAST_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_FRAUD_DETECTOR_FULL_ACCESS_POLICY")
    def AMAZON_FRAUD_DETECTOR_FULL_ACCESS_POLICY(cls) -> str:
        return jsii.sget(cls, "AMAZON_FRAUD_DETECTOR_FULL_ACCESS_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_FREE_RTOS_FULL_ACCESS")
    def AMAZON_FREE_RTOS_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_FREE_RTOS_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_FREE_RTOSOTA_UPDATE")
    def AMAZON_FREE_RTOSOTA_UPDATE(cls) -> str:
        return jsii.sget(cls, "AMAZON_FREE_RTOSOTA_UPDATE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_GLACIER_FULL_ACCESS")
    def AMAZON_GLACIER_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_GLACIER_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_GLACIER_READ_ONLY_ACCESS")
    def AMAZON_GLACIER_READ_ONLY_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_GLACIER_READ_ONLY_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_GUARD_DUTY_FULL_ACCESS")
    def AMAZON_GUARD_DUTY_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_GUARD_DUTY_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_GUARD_DUTY_READ_ONLY_ACCESS")
    def AMAZON_GUARD_DUTY_READ_ONLY_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_GUARD_DUTY_READ_ONLY_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_GUARD_DUTY_SERVICE_ROLE_POLICY")
    def AMAZON_GUARD_DUTY_SERVICE_ROLE_POLICY(cls) -> str:
        return jsii.sget(cls, "AMAZON_GUARD_DUTY_SERVICE_ROLE_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_INSPECTOR_FULL_ACCESS")
    def AMAZON_INSPECTOR_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_INSPECTOR_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_INSPECTOR_READ_ONLY_ACCESS")
    def AMAZON_INSPECTOR_READ_ONLY_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_INSPECTOR_READ_ONLY_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_INSPECTOR_SERVICE_ROLE_POLICY")
    def AMAZON_INSPECTOR_SERVICE_ROLE_POLICY(cls) -> str:
        return jsii.sget(cls, "AMAZON_INSPECTOR_SERVICE_ROLE_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_KENDRA_FULL_ACCESS")
    def AMAZON_KENDRA_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_KENDRA_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_KENDRA_READ_ONLY_ACCESS")
    def AMAZON_KENDRA_READ_ONLY_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_KENDRA_READ_ONLY_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_KINESIS_ANALYTICS_FULL_ACCESS")
    def AMAZON_KINESIS_ANALYTICS_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_KINESIS_ANALYTICS_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_KINESIS_ANALYTICS_READ_ONLY")
    def AMAZON_KINESIS_ANALYTICS_READ_ONLY(cls) -> str:
        return jsii.sget(cls, "AMAZON_KINESIS_ANALYTICS_READ_ONLY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_KINESIS_FIREHOSE_FULL_ACCESS")
    def AMAZON_KINESIS_FIREHOSE_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_KINESIS_FIREHOSE_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_KINESIS_FIREHOSE_READ_ONLY_ACCESS")
    def AMAZON_KINESIS_FIREHOSE_READ_ONLY_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_KINESIS_FIREHOSE_READ_ONLY_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_KINESIS_FULL_ACCESS")
    def AMAZON_KINESIS_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_KINESIS_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_KINESIS_READ_ONLY_ACCESS")
    def AMAZON_KINESIS_READ_ONLY_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_KINESIS_READ_ONLY_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_KINESIS_VIDEO_STREAMS_FULL_ACCESS")
    def AMAZON_KINESIS_VIDEO_STREAMS_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_KINESIS_VIDEO_STREAMS_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_KINESIS_VIDEO_STREAMS_READ_ONLY_ACCESS")
    def AMAZON_KINESIS_VIDEO_STREAMS_READ_ONLY_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_KINESIS_VIDEO_STREAMS_READ_ONLY_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_LAUNCH_WIZARD_FULLACCESS")
    def AMAZON_LAUNCH_WIZARD_FULLACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_LAUNCH_WIZARD_FULLACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_LEX_FULL_ACCESS")
    def AMAZON_LEX_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_LEX_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_LEX_READ_ONLY")
    def AMAZON_LEX_READ_ONLY(cls) -> str:
        return jsii.sget(cls, "AMAZON_LEX_READ_ONLY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_LEX_RUN_BOTS_ONLY")
    def AMAZON_LEX_RUN_BOTS_ONLY(cls) -> str:
        return jsii.sget(cls, "AMAZON_LEX_RUN_BOTS_ONLY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_MACHINE_LEARNING_BATCH_PREDICTIONS_ACCESS")
    def AMAZON_MACHINE_LEARNING_BATCH_PREDICTIONS_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_MACHINE_LEARNING_BATCH_PREDICTIONS_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_MACHINE_LEARNING_CREATE_ONLY_ACCESS")
    def AMAZON_MACHINE_LEARNING_CREATE_ONLY_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_MACHINE_LEARNING_CREATE_ONLY_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_MACHINE_LEARNING_FULL_ACCESS")
    def AMAZON_MACHINE_LEARNING_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_MACHINE_LEARNING_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_MACHINE_LEARNING_MANAGE_REAL_TIME_ENDPOINT_ONLY_ACCESS")
    def AMAZON_MACHINE_LEARNING_MANAGE_REAL_TIME_ENDPOINT_ONLY_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_MACHINE_LEARNING_MANAGE_REAL_TIME_ENDPOINT_ONLY_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_MACHINE_LEARNING_READ_ONLY_ACCESS")
    def AMAZON_MACHINE_LEARNING_READ_ONLY_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_MACHINE_LEARNING_READ_ONLY_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_MACHINE_LEARNING_REAL_TIME_PREDICTION_ONLY_ACCESS")
    def AMAZON_MACHINE_LEARNING_REAL_TIME_PREDICTION_ONLY_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_MACHINE_LEARNING_REAL_TIME_PREDICTION_ONLY_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_MACHINE_LEARNING_ROLEFOR_REDSHIFT_DATA_SOURCE_V_2")
    def AMAZON_MACHINE_LEARNING_ROLEFOR_REDSHIFT_DATA_SOURCE_V_2(cls) -> str:
        return jsii.sget(cls, "AMAZON_MACHINE_LEARNING_ROLEFOR_REDSHIFT_DATA_SOURCE_V_2")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_MACIE_FULL_ACCESS")
    def AMAZON_MACIE_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_MACIE_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_MACIE_HANDSHAKE_ROLE")
    def AMAZON_MACIE_HANDSHAKE_ROLE(cls) -> str:
        return jsii.sget(cls, "AMAZON_MACIE_HANDSHAKE_ROLE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_MACIE_SERVICE_ROLE")
    def AMAZON_MACIE_SERVICE_ROLE(cls) -> str:
        return jsii.sget(cls, "AMAZON_MACIE_SERVICE_ROLE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_MACIE_SERVICE_ROLE_POLICY")
    def AMAZON_MACIE_SERVICE_ROLE_POLICY(cls) -> str:
        return jsii.sget(cls, "AMAZON_MACIE_SERVICE_ROLE_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_MACIE_SETUP_ROLE")
    def AMAZON_MACIE_SETUP_ROLE(cls) -> str:
        return jsii.sget(cls, "AMAZON_MACIE_SETUP_ROLE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_MANAGED_BLOCKCHAIN_CONSOLE_FULL_ACCESS")
    def AMAZON_MANAGED_BLOCKCHAIN_CONSOLE_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_MANAGED_BLOCKCHAIN_CONSOLE_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_MANAGED_BLOCKCHAIN_FULL_ACCESS")
    def AMAZON_MANAGED_BLOCKCHAIN_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_MANAGED_BLOCKCHAIN_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_MANAGED_BLOCKCHAIN_READ_ONLY_ACCESS")
    def AMAZON_MANAGED_BLOCKCHAIN_READ_ONLY_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_MANAGED_BLOCKCHAIN_READ_ONLY_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_MCS_FULL_ACCESS")
    def AMAZON_MCS_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_MCS_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_MCS_READ_ONLY_ACCESS")
    def AMAZON_MCS_READ_ONLY_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_MCS_READ_ONLY_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_MECHANICAL_TURK_FULL_ACCESS")
    def AMAZON_MECHANICAL_TURK_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_MECHANICAL_TURK_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_MECHANICAL_TURK_READ_ONLY")
    def AMAZON_MECHANICAL_TURK_READ_ONLY(cls) -> str:
        return jsii.sget(cls, "AMAZON_MECHANICAL_TURK_READ_ONLY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_MOBILE_ANALYTICS_FINANCIAL_REPORT_ACCESS")
    def AMAZON_MOBILE_ANALYTICS_FINANCIAL_REPORT_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_MOBILE_ANALYTICS_FINANCIAL_REPORT_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_MOBILE_ANALYTICS_FULL_ACCESS")
    def AMAZON_MOBILE_ANALYTICS_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_MOBILE_ANALYTICS_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_MOBILE_ANALYTICS_NON_FINANCIAL_REPORT_ACCESS")
    def AMAZON_MOBILE_ANALYTICS_NON_FINANCIAL_REPORT_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_MOBILE_ANALYTICS_NON_FINANCIAL_REPORT_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_MOBILE_ANALYTICS_WRITE_ONLY_ACCESS")
    def AMAZON_MOBILE_ANALYTICS_WRITE_ONLY_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_MOBILE_ANALYTICS_WRITE_ONLY_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_MQ_API_FULL_ACCESS")
    def AMAZON_MQ_API_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_MQ_API_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_MQ_API_READ_ONLY_ACCESS")
    def AMAZON_MQ_API_READ_ONLY_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_MQ_API_READ_ONLY_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_MQ_FULL_ACCESS")
    def AMAZON_MQ_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_MQ_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_MQ_READ_ONLY_ACCESS")
    def AMAZON_MQ_READ_ONLY_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_MQ_READ_ONLY_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_MSK_FULL_ACCESS")
    def AMAZON_MSK_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_MSK_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_MSK_READ_ONLY_ACCESS")
    def AMAZON_MSK_READ_ONLY_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_MSK_READ_ONLY_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_PERSONALIZE_FULL_ACCESS")
    def AMAZON_PERSONALIZE_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_PERSONALIZE_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_POLLY_FULL_ACCESS")
    def AMAZON_POLLY_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_POLLY_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_POLLY_READ_ONLY_ACCESS")
    def AMAZON_POLLY_READ_ONLY_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_POLLY_READ_ONLY_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_QLDB_CONSOLE_FULL_ACCESS")
    def AMAZON_QLDB_CONSOLE_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_QLDB_CONSOLE_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_QLDB_FULL_ACCESS")
    def AMAZON_QLDB_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_QLDB_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_QLDB_READ_ONLY")
    def AMAZON_QLDB_READ_ONLY(cls) -> str:
        return jsii.sget(cls, "AMAZON_QLDB_READ_ONLY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_RDS_BETA_SERVICE_ROLE_POLICY")
    def AMAZON_RDS_BETA_SERVICE_ROLE_POLICY(cls) -> str:
        return jsii.sget(cls, "AMAZON_RDS_BETA_SERVICE_ROLE_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_RDS_DATA_FULL_ACCESS")
    def AMAZON_RDS_DATA_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_RDS_DATA_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_RDS_DIRECTORY_SERVICE_ACCESS")
    def AMAZON_RDS_DIRECTORY_SERVICE_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_RDS_DIRECTORY_SERVICE_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_RDS_ENHANCED_MONITORING_ROLE")
    def AMAZON_RDS_ENHANCED_MONITORING_ROLE(cls) -> str:
        return jsii.sget(cls, "AMAZON_RDS_ENHANCED_MONITORING_ROLE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_RDS_FULL_ACCESS")
    def AMAZON_RDS_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_RDS_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_RDS_PREVIEW_SERVICE_ROLE_POLICY")
    def AMAZON_RDS_PREVIEW_SERVICE_ROLE_POLICY(cls) -> str:
        return jsii.sget(cls, "AMAZON_RDS_PREVIEW_SERVICE_ROLE_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_RDS_READ_ONLY_ACCESS")
    def AMAZON_RDS_READ_ONLY_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_RDS_READ_ONLY_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_RDS_SERVICE_ROLE_POLICY")
    def AMAZON_RDS_SERVICE_ROLE_POLICY(cls) -> str:
        return jsii.sget(cls, "AMAZON_RDS_SERVICE_ROLE_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_REDSHIFT_FULL_ACCESS")
    def AMAZON_REDSHIFT_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_REDSHIFT_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_REDSHIFT_QUERY_EDITOR")
    def AMAZON_REDSHIFT_QUERY_EDITOR(cls) -> str:
        return jsii.sget(cls, "AMAZON_REDSHIFT_QUERY_EDITOR")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_REDSHIFT_READ_ONLY_ACCESS")
    def AMAZON_REDSHIFT_READ_ONLY_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_REDSHIFT_READ_ONLY_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_REDSHIFT_SERVICE_LINKED_ROLE_POLICY")
    def AMAZON_REDSHIFT_SERVICE_LINKED_ROLE_POLICY(cls) -> str:
        return jsii.sget(cls, "AMAZON_REDSHIFT_SERVICE_LINKED_ROLE_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_REKOGNITION_FULL_ACCESS")
    def AMAZON_REKOGNITION_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_REKOGNITION_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_REKOGNITION_READ_ONLY_ACCESS")
    def AMAZON_REKOGNITION_READ_ONLY_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_REKOGNITION_READ_ONLY_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_REKOGNITION_SERVICE_ROLE")
    def AMAZON_REKOGNITION_SERVICE_ROLE(cls) -> str:
        return jsii.sget(cls, "AMAZON_REKOGNITION_SERVICE_ROLE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_ROUTE_53_AUTO_NAMING_FULL_ACCESS")
    def AMAZON_ROUTE_53_AUTO_NAMING_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_ROUTE_53_AUTO_NAMING_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_ROUTE_53_AUTO_NAMING_READ_ONLY_ACCESS")
    def AMAZON_ROUTE_53_AUTO_NAMING_READ_ONLY_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_ROUTE_53_AUTO_NAMING_READ_ONLY_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_ROUTE_53_AUTO_NAMING_REGISTRANT_ACCESS")
    def AMAZON_ROUTE_53_AUTO_NAMING_REGISTRANT_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_ROUTE_53_AUTO_NAMING_REGISTRANT_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_ROUTE_53_DOMAINS_FULL_ACCESS")
    def AMAZON_ROUTE_53_DOMAINS_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_ROUTE_53_DOMAINS_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_ROUTE_53_DOMAINS_READ_ONLY_ACCESS")
    def AMAZON_ROUTE_53_DOMAINS_READ_ONLY_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_ROUTE_53_DOMAINS_READ_ONLY_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_ROUTE_53_FULL_ACCESS")
    def AMAZON_ROUTE_53_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_ROUTE_53_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_ROUTE_53_READ_ONLY_ACCESS")
    def AMAZON_ROUTE_53_READ_ONLY_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_ROUTE_53_READ_ONLY_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_ROUTE_53_RESOLVER_FULL_ACCESS")
    def AMAZON_ROUTE_53_RESOLVER_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_ROUTE_53_RESOLVER_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_ROUTE_53_RESOLVER_READ_ONLY_ACCESS")
    def AMAZON_ROUTE_53_RESOLVER_READ_ONLY_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_ROUTE_53_RESOLVER_READ_ONLY_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_S3_FULL_ACCESS")
    def AMAZON_S3_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_S3_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_S3_READ_ONLY_ACCESS")
    def AMAZON_S3_READ_ONLY_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_S3_READ_ONLY_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_SAGE_MAKER_FULL_ACCESS")
    def AMAZON_SAGE_MAKER_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_SAGE_MAKER_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_SAGE_MAKER_MECHANICAL_TURK_ACCESS")
    def AMAZON_SAGE_MAKER_MECHANICAL_TURK_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_SAGE_MAKER_MECHANICAL_TURK_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_SAGE_MAKER_NOTEBOOKS_SERVICE_ROLE_POLICY")
    def AMAZON_SAGE_MAKER_NOTEBOOKS_SERVICE_ROLE_POLICY(cls) -> str:
        return jsii.sget(cls, "AMAZON_SAGE_MAKER_NOTEBOOKS_SERVICE_ROLE_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_SAGE_MAKER_READ_ONLY")
    def AMAZON_SAGE_MAKER_READ_ONLY(cls) -> str:
        return jsii.sget(cls, "AMAZON_SAGE_MAKER_READ_ONLY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_SES_FULL_ACCESS")
    def AMAZON_SES_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_SES_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_SES_READ_ONLY_ACCESS")
    def AMAZON_SES_READ_ONLY_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_SES_READ_ONLY_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_SNS_FULL_ACCESS")
    def AMAZON_SNS_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_SNS_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_SNS_READ_ONLY_ACCESS")
    def AMAZON_SNS_READ_ONLY_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_SNS_READ_ONLY_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_SNS_ROLE")
    def AMAZON_SNS_ROLE(cls) -> str:
        return jsii.sget(cls, "AMAZON_SNS_ROLE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_SQS_FULL_ACCESS")
    def AMAZON_SQS_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_SQS_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_SQS_READ_ONLY_ACCESS")
    def AMAZON_SQS_READ_ONLY_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_SQS_READ_ONLY_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_SSM_AUTOMATION_APPROVER_ACCESS")
    def AMAZON_SSM_AUTOMATION_APPROVER_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_SSM_AUTOMATION_APPROVER_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_SSM_AUTOMATION_ROLE")
    def AMAZON_SSM_AUTOMATION_ROLE(cls) -> str:
        return jsii.sget(cls, "AMAZON_SSM_AUTOMATION_ROLE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_SSM_DIRECTORY_SERVICE_ACCESS")
    def AMAZON_SSM_DIRECTORY_SERVICE_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_SSM_DIRECTORY_SERVICE_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_SSM_FULL_ACCESS")
    def AMAZON_SSM_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_SSM_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_SSM_MAINTENANCE_WINDOW_ROLE")
    def AMAZON_SSM_MAINTENANCE_WINDOW_ROLE(cls) -> str:
        return jsii.sget(cls, "AMAZON_SSM_MAINTENANCE_WINDOW_ROLE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_SSM_MANAGED_INSTANCE_CORE")
    def AMAZON_SSM_MANAGED_INSTANCE_CORE(cls) -> str:
        return jsii.sget(cls, "AMAZON_SSM_MANAGED_INSTANCE_CORE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_SSM_READ_ONLY_ACCESS")
    def AMAZON_SSM_READ_ONLY_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_SSM_READ_ONLY_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_SSM_SERVICE_ROLE_POLICY")
    def AMAZON_SSM_SERVICE_ROLE_POLICY(cls) -> str:
        return jsii.sget(cls, "AMAZON_SSM_SERVICE_ROLE_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_SUMERIAN_FULL_ACCESS")
    def AMAZON_SUMERIAN_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_SUMERIAN_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_TEXTRACT_FULL_ACCESS")
    def AMAZON_TEXTRACT_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_TEXTRACT_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_TEXTRACT_SERVICE_ROLE")
    def AMAZON_TEXTRACT_SERVICE_ROLE(cls) -> str:
        return jsii.sget(cls, "AMAZON_TEXTRACT_SERVICE_ROLE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_TRANSCRIBE_FULL_ACCESS")
    def AMAZON_TRANSCRIBE_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_TRANSCRIBE_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_TRANSCRIBE_READ_ONLY_ACCESS")
    def AMAZON_TRANSCRIBE_READ_ONLY_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_TRANSCRIBE_READ_ONLY_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_VPC_CROSS_ACCOUNT_NETWORK_INTERFACE_OPERATIONS")
    def AMAZON_VPC_CROSS_ACCOUNT_NETWORK_INTERFACE_OPERATIONS(cls) -> str:
        return jsii.sget(cls, "AMAZON_VPC_CROSS_ACCOUNT_NETWORK_INTERFACE_OPERATIONS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_VPC_FULL_ACCESS")
    def AMAZON_VPC_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_VPC_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_VPC_READ_ONLY_ACCESS")
    def AMAZON_VPC_READ_ONLY_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_VPC_READ_ONLY_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_WORK_LINK_FULL_ACCESS")
    def AMAZON_WORK_LINK_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_WORK_LINK_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_WORK_LINK_READ_ONLY")
    def AMAZON_WORK_LINK_READ_ONLY(cls) -> str:
        return jsii.sget(cls, "AMAZON_WORK_LINK_READ_ONLY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_WORK_LINK_SERVICE_ROLE_POLICY")
    def AMAZON_WORK_LINK_SERVICE_ROLE_POLICY(cls) -> str:
        return jsii.sget(cls, "AMAZON_WORK_LINK_SERVICE_ROLE_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_WORK_MAIL_EVENTS_SERVICE_ROLE_POLICY")
    def AMAZON_WORK_MAIL_EVENTS_SERVICE_ROLE_POLICY(cls) -> str:
        return jsii.sget(cls, "AMAZON_WORK_MAIL_EVENTS_SERVICE_ROLE_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_WORK_MAIL_FULL_ACCESS")
    def AMAZON_WORK_MAIL_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_WORK_MAIL_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_WORK_MAIL_READ_ONLY_ACCESS")
    def AMAZON_WORK_MAIL_READ_ONLY_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_WORK_MAIL_READ_ONLY_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_WORK_SPACES_ADMIN")
    def AMAZON_WORK_SPACES_ADMIN(cls) -> str:
        return jsii.sget(cls, "AMAZON_WORK_SPACES_ADMIN")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_WORK_SPACES_APPLICATION_MANAGER_ADMIN_ACCESS")
    def AMAZON_WORK_SPACES_APPLICATION_MANAGER_ADMIN_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_WORK_SPACES_APPLICATION_MANAGER_ADMIN_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_WORK_SPACES_SELF_SERVICE_ACCESS")
    def AMAZON_WORK_SPACES_SELF_SERVICE_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_WORK_SPACES_SELF_SERVICE_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_WORK_SPACES_SERVICE_ACCESS")
    def AMAZON_WORK_SPACES_SERVICE_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_WORK_SPACES_SERVICE_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_ZOCALO_FULL_ACCESS")
    def AMAZON_ZOCALO_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_ZOCALO_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_ZOCALO_READ_ONLY_ACCESS")
    def AMAZON_ZOCALO_READ_ONLY_ACCESS(cls) -> str:
        return jsii.sget(cls, "AMAZON_ZOCALO_READ_ONLY_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="API_GATEWAY_SERVICE_ROLE_POLICY")
    def API_GATEWAY_SERVICE_ROLE_POLICY(cls) -> str:
        return jsii.sget(cls, "API_GATEWAY_SERVICE_ROLE_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="APPLICATION_AUTO_SCALING_FOR_AMAZON_APP_STREAM_ACCESS")
    def APPLICATION_AUTO_SCALING_FOR_AMAZON_APP_STREAM_ACCESS(cls) -> str:
        return jsii.sget(cls, "APPLICATION_AUTO_SCALING_FOR_AMAZON_APP_STREAM_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="APPLICATION_DISCOVERY_SERVICE_CONTINUOUS_EXPORT_SERVICE_ROLE_POLICY")
    def APPLICATION_DISCOVERY_SERVICE_CONTINUOUS_EXPORT_SERVICE_ROLE_POLICY(cls) -> str:
        return jsii.sget(cls, "APPLICATION_DISCOVERY_SERVICE_CONTINUOUS_EXPORT_SERVICE_ROLE_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AUTO_SCALING_CONSOLE_FULL_ACCESS")
    def AUTO_SCALING_CONSOLE_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AUTO_SCALING_CONSOLE_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AUTO_SCALING_CONSOLE_READ_ONLY_ACCESS")
    def AUTO_SCALING_CONSOLE_READ_ONLY_ACCESS(cls) -> str:
        return jsii.sget(cls, "AUTO_SCALING_CONSOLE_READ_ONLY_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AUTO_SCALING_FULL_ACCESS")
    def AUTO_SCALING_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AUTO_SCALING_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AUTO_SCALING_NOTIFICATION_ACCESS_ROLE")
    def AUTO_SCALING_NOTIFICATION_ACCESS_ROLE(cls) -> str:
        return jsii.sget(cls, "AUTO_SCALING_NOTIFICATION_ACCESS_ROLE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AUTO_SCALING_READ_ONLY_ACCESS")
    def AUTO_SCALING_READ_ONLY_ACCESS(cls) -> str:
        return jsii.sget(cls, "AUTO_SCALING_READ_ONLY_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AUTO_SCALING_SERVICE_ROLE_POLICY")
    def AUTO_SCALING_SERVICE_ROLE_POLICY(cls) -> str:
        return jsii.sget(cls, "AUTO_SCALING_SERVICE_ROLE_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_ACCOUNT_ACTIVITY_ACCESS")
    def AWS_ACCOUNT_ACTIVITY_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_ACCOUNT_ACTIVITY_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_ACCOUNT_USAGE_REPORT_ACCESS")
    def AWS_ACCOUNT_USAGE_REPORT_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_ACCOUNT_USAGE_REPORT_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_AGENTLESS_DISCOVERY_SERVICE")
    def AWS_AGENTLESS_DISCOVERY_SERVICE(cls) -> str:
        return jsii.sget(cls, "AWS_AGENTLESS_DISCOVERY_SERVICE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_APP_MESH_ENVOY_ACCESS")
    def AWS_APP_MESH_ENVOY_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_APP_MESH_ENVOY_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_APP_MESH_FULL_ACCESS")
    def AWS_APP_MESH_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_APP_MESH_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_APP_MESH_PREVIEW_ENVOY_ACCESS")
    def AWS_APP_MESH_PREVIEW_ENVOY_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_APP_MESH_PREVIEW_ENVOY_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_APP_MESH_PREVIEW_SERVICE_ROLE_POLICY")
    def AWS_APP_MESH_PREVIEW_SERVICE_ROLE_POLICY(cls) -> str:
        return jsii.sget(cls, "AWS_APP_MESH_PREVIEW_SERVICE_ROLE_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_APP_MESH_READ_ONLY")
    def AWS_APP_MESH_READ_ONLY(cls) -> str:
        return jsii.sget(cls, "AWS_APP_MESH_READ_ONLY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_APP_MESH_SERVICE_ROLE_POLICY")
    def AWS_APP_MESH_SERVICE_ROLE_POLICY(cls) -> str:
        return jsii.sget(cls, "AWS_APP_MESH_SERVICE_ROLE_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_APP_SYNC_ADMINISTRATOR")
    def AWS_APP_SYNC_ADMINISTRATOR(cls) -> str:
        return jsii.sget(cls, "AWS_APP_SYNC_ADMINISTRATOR")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_APP_SYNC_INVOKE_FULL_ACCESS")
    def AWS_APP_SYNC_INVOKE_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_APP_SYNC_INVOKE_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_APP_SYNC_PUSH_TO_CLOUD_WATCH_LOGS")
    def AWS_APP_SYNC_PUSH_TO_CLOUD_WATCH_LOGS(cls) -> str:
        return jsii.sget(cls, "AWS_APP_SYNC_PUSH_TO_CLOUD_WATCH_LOGS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_APP_SYNC_SCHEMA_AUTHOR")
    def AWS_APP_SYNC_SCHEMA_AUTHOR(cls) -> str:
        return jsii.sget(cls, "AWS_APP_SYNC_SCHEMA_AUTHOR")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_APPLICATION_AUTO_SCALING_CUSTOM_RESOURCE_POLICY")
    def AWS_APPLICATION_AUTO_SCALING_CUSTOM_RESOURCE_POLICY(cls) -> str:
        return jsii.sget(cls, "AWS_APPLICATION_AUTO_SCALING_CUSTOM_RESOURCE_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_APPLICATION_AUTOSCALING_APP_STREAM_FLEET_POLICY")
    def AWS_APPLICATION_AUTOSCALING_APP_STREAM_FLEET_POLICY(cls) -> str:
        return jsii.sget(cls, "AWS_APPLICATION_AUTOSCALING_APP_STREAM_FLEET_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_APPLICATION_AUTOSCALING_COMPREHEND_ENDPOINT_POLICY")
    def AWS_APPLICATION_AUTOSCALING_COMPREHEND_ENDPOINT_POLICY(cls) -> str:
        return jsii.sget(cls, "AWS_APPLICATION_AUTOSCALING_COMPREHEND_ENDPOINT_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_APPLICATION_AUTOSCALING_DYNAMO_DB_TABLE_POLICY")
    def AWS_APPLICATION_AUTOSCALING_DYNAMO_DB_TABLE_POLICY(cls) -> str:
        return jsii.sget(cls, "AWS_APPLICATION_AUTOSCALING_DYNAMO_DB_TABLE_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_APPLICATION_AUTOSCALING_EC2_SPOT_FLEET_REQUEST_POLICY")
    def AWS_APPLICATION_AUTOSCALING_E_C2_SPOT_FLEET_REQUEST_POLICY(cls) -> str:
        return jsii.sget(cls, "AWS_APPLICATION_AUTOSCALING_EC2_SPOT_FLEET_REQUEST_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_APPLICATION_AUTOSCALING_ECS_SERVICE_POLICY")
    def AWS_APPLICATION_AUTOSCALING_ECS_SERVICE_POLICY(cls) -> str:
        return jsii.sget(cls, "AWS_APPLICATION_AUTOSCALING_ECS_SERVICE_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_APPLICATION_AUTOSCALING_EMR_INSTANCE_GROUP_POLICY")
    def AWS_APPLICATION_AUTOSCALING_EMR_INSTANCE_GROUP_POLICY(cls) -> str:
        return jsii.sget(cls, "AWS_APPLICATION_AUTOSCALING_EMR_INSTANCE_GROUP_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_APPLICATION_AUTOSCALING_LAMBDA_CONCURRENCY_POLICY")
    def AWS_APPLICATION_AUTOSCALING_LAMBDA_CONCURRENCY_POLICY(cls) -> str:
        return jsii.sget(cls, "AWS_APPLICATION_AUTOSCALING_LAMBDA_CONCURRENCY_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_APPLICATION_AUTOSCALING_RDS_CLUSTER_POLICY")
    def AWS_APPLICATION_AUTOSCALING_RDS_CLUSTER_POLICY(cls) -> str:
        return jsii.sget(cls, "AWS_APPLICATION_AUTOSCALING_RDS_CLUSTER_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_APPLICATION_AUTOSCALING_SAGE_MAKER_ENDPOINT_POLICY")
    def AWS_APPLICATION_AUTOSCALING_SAGE_MAKER_ENDPOINT_POLICY(cls) -> str:
        return jsii.sget(cls, "AWS_APPLICATION_AUTOSCALING_SAGE_MAKER_ENDPOINT_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_APPLICATION_DISCOVERY_AGENT_ACCESS")
    def AWS_APPLICATION_DISCOVERY_AGENT_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_APPLICATION_DISCOVERY_AGENT_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_APPLICATION_DISCOVERY_SERVICE_FULL_ACCESS")
    def AWS_APPLICATION_DISCOVERY_SERVICE_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_APPLICATION_DISCOVERY_SERVICE_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_ARTIFACT_ACCOUNT_SYNC")
    def AWS_ARTIFACT_ACCOUNT_SYNC(cls) -> str:
        return jsii.sget(cls, "AWS_ARTIFACT_ACCOUNT_SYNC")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_AUTO_SCALING_PLANS_EC2_AUTO_SCALING_POLICY")
    def AWS_AUTO_SCALING_PLANS_E_C2_AUTO_SCALING_POLICY(cls) -> str:
        return jsii.sget(cls, "AWS_AUTO_SCALING_PLANS_EC2_AUTO_SCALING_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_BACKUP_FULL_ACCESS")
    def AWS_BACKUP_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_BACKUP_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_BACKUP_OPERATOR_ACCESS")
    def AWS_BACKUP_OPERATOR_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_BACKUP_OPERATOR_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_BACKUP_SERVICE_ROLE_POLICY_FOR_BACKUP")
    def AWS_BACKUP_SERVICE_ROLE_POLICY_FOR_BACKUP(cls) -> str:
        return jsii.sget(cls, "AWS_BACKUP_SERVICE_ROLE_POLICY_FOR_BACKUP")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_BACKUP_SERVICE_ROLE_POLICY_FOR_RESTORES")
    def AWS_BACKUP_SERVICE_ROLE_POLICY_FOR_RESTORES(cls) -> str:
        return jsii.sget(cls, "AWS_BACKUP_SERVICE_ROLE_POLICY_FOR_RESTORES")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_BATCH_FULL_ACCESS")
    def AWS_BATCH_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_BATCH_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_BATCH_SERVICE_EVENT_TARGET_ROLE")
    def AWS_BATCH_SERVICE_EVENT_TARGET_ROLE(cls) -> str:
        return jsii.sget(cls, "AWS_BATCH_SERVICE_EVENT_TARGET_ROLE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_BATCH_SERVICE_ROLE")
    def AWS_BATCH_SERVICE_ROLE(cls) -> str:
        return jsii.sget(cls, "AWS_BATCH_SERVICE_ROLE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CERTIFICATE_MANAGER_FULL_ACCESS")
    def AWS_CERTIFICATE_MANAGER_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_CERTIFICATE_MANAGER_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CERTIFICATE_MANAGER_PRIVATE_CA_AUDITOR")
    def AWS_CERTIFICATE_MANAGER_PRIVATE_CA_AUDITOR(cls) -> str:
        return jsii.sget(cls, "AWS_CERTIFICATE_MANAGER_PRIVATE_CA_AUDITOR")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CERTIFICATE_MANAGER_PRIVATE_CA_FULL_ACCESS")
    def AWS_CERTIFICATE_MANAGER_PRIVATE_CA_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_CERTIFICATE_MANAGER_PRIVATE_CA_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CERTIFICATE_MANAGER_PRIVATE_CA_PRIVILEGED_USER")
    def AWS_CERTIFICATE_MANAGER_PRIVATE_CA_PRIVILEGED_USER(cls) -> str:
        return jsii.sget(cls, "AWS_CERTIFICATE_MANAGER_PRIVATE_CA_PRIVILEGED_USER")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CERTIFICATE_MANAGER_PRIVATE_CA_READ_ONLY")
    def AWS_CERTIFICATE_MANAGER_PRIVATE_CA_READ_ONLY(cls) -> str:
        return jsii.sget(cls, "AWS_CERTIFICATE_MANAGER_PRIVATE_CA_READ_ONLY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CERTIFICATE_MANAGER_PRIVATE_CA_USER")
    def AWS_CERTIFICATE_MANAGER_PRIVATE_CA_USER(cls) -> str:
        return jsii.sget(cls, "AWS_CERTIFICATE_MANAGER_PRIVATE_CA_USER")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CERTIFICATE_MANAGER_READ_ONLY")
    def AWS_CERTIFICATE_MANAGER_READ_ONLY(cls) -> str:
        return jsii.sget(cls, "AWS_CERTIFICATE_MANAGER_READ_ONLY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CHATBOT_SERVICE_LINKED_ROLE_POLICY")
    def AWS_CHATBOT_SERVICE_LINKED_ROLE_POLICY(cls) -> str:
        return jsii.sget(cls, "AWS_CHATBOT_SERVICE_LINKED_ROLE_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CLOUD_9_ADMINISTRATOR")
    def AWS_CLOUD_9_ADMINISTRATOR(cls) -> str:
        return jsii.sget(cls, "AWS_CLOUD_9_ADMINISTRATOR")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CLOUD_9_ENVIRONMENT_MEMBER")
    def AWS_CLOUD_9_ENVIRONMENT_MEMBER(cls) -> str:
        return jsii.sget(cls, "AWS_CLOUD_9_ENVIRONMENT_MEMBER")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CLOUD_9_SERVICE_ROLE_POLICY")
    def AWS_CLOUD_9_SERVICE_ROLE_POLICY(cls) -> str:
        return jsii.sget(cls, "AWS_CLOUD_9_SERVICE_ROLE_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CLOUD_9_USER")
    def AWS_CLOUD_9_USER(cls) -> str:
        return jsii.sget(cls, "AWS_CLOUD_9_USER")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CLOUD_FORMATION_FULL_ACCESS")
    def AWS_CLOUD_FORMATION_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_CLOUD_FORMATION_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CLOUD_FORMATION_READ_ONLY_ACCESS")
    def AWS_CLOUD_FORMATION_READ_ONLY_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_CLOUD_FORMATION_READ_ONLY_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CLOUD_FRONT_LOGGER")
    def AWS_CLOUD_FRONT_LOGGER(cls) -> str:
        return jsii.sget(cls, "AWS_CLOUD_FRONT_LOGGER")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CLOUD_HSM_FULL_ACCESS")
    def AWS_CLOUD_HSM_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_CLOUD_HSM_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CLOUD_HSM_READ_ONLY_ACCESS")
    def AWS_CLOUD_HSM_READ_ONLY_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_CLOUD_HSM_READ_ONLY_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CLOUD_HSM_ROLE")
    def AWS_CLOUD_HSM_ROLE(cls) -> str:
        return jsii.sget(cls, "AWS_CLOUD_HSM_ROLE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CLOUD_MAP_DISCOVER_INSTANCE_ACCESS")
    def AWS_CLOUD_MAP_DISCOVER_INSTANCE_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_CLOUD_MAP_DISCOVER_INSTANCE_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CLOUD_MAP_FULL_ACCESS")
    def AWS_CLOUD_MAP_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_CLOUD_MAP_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CLOUD_MAP_READ_ONLY_ACCESS")
    def AWS_CLOUD_MAP_READ_ONLY_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_CLOUD_MAP_READ_ONLY_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CLOUD_MAP_REGISTER_INSTANCE_ACCESS")
    def AWS_CLOUD_MAP_REGISTER_INSTANCE_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_CLOUD_MAP_REGISTER_INSTANCE_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CLOUD_TRAIL_FULL_ACCESS")
    def AWS_CLOUD_TRAIL_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_CLOUD_TRAIL_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CLOUD_TRAIL_READ_ONLY_ACCESS")
    def AWS_CLOUD_TRAIL_READ_ONLY_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_CLOUD_TRAIL_READ_ONLY_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CODE_BUILD_ADMIN_ACCESS")
    def AWS_CODE_BUILD_ADMIN_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_CODE_BUILD_ADMIN_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CODE_BUILD_DEVELOPER_ACCESS")
    def AWS_CODE_BUILD_DEVELOPER_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_CODE_BUILD_DEVELOPER_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CODE_BUILD_READ_ONLY_ACCESS")
    def AWS_CODE_BUILD_READ_ONLY_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_CODE_BUILD_READ_ONLY_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CODE_COMMIT_FULL_ACCESS")
    def AWS_CODE_COMMIT_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_CODE_COMMIT_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CODE_COMMIT_POWER_USER")
    def AWS_CODE_COMMIT_POWER_USER(cls) -> str:
        return jsii.sget(cls, "AWS_CODE_COMMIT_POWER_USER")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CODE_COMMIT_READ_ONLY")
    def AWS_CODE_COMMIT_READ_ONLY(cls) -> str:
        return jsii.sget(cls, "AWS_CODE_COMMIT_READ_ONLY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CODE_DEPLOY_DEPLOYER_ACCESS")
    def AWS_CODE_DEPLOY_DEPLOYER_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_CODE_DEPLOY_DEPLOYER_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CODE_DEPLOY_FULL_ACCESS")
    def AWS_CODE_DEPLOY_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_CODE_DEPLOY_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CODE_DEPLOY_READ_ONLY_ACCESS")
    def AWS_CODE_DEPLOY_READ_ONLY_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_CODE_DEPLOY_READ_ONLY_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CODE_DEPLOY_ROLE")
    def AWS_CODE_DEPLOY_ROLE(cls) -> str:
        return jsii.sget(cls, "AWS_CODE_DEPLOY_ROLE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CODE_DEPLOY_ROLE_FOR_ECS")
    def AWS_CODE_DEPLOY_ROLE_FOR_ECS(cls) -> str:
        return jsii.sget(cls, "AWS_CODE_DEPLOY_ROLE_FOR_ECS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CODE_DEPLOY_ROLE_FOR_ECS_LIMITED")
    def AWS_CODE_DEPLOY_ROLE_FOR_ECS_LIMITED(cls) -> str:
        return jsii.sget(cls, "AWS_CODE_DEPLOY_ROLE_FOR_ECS_LIMITED")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CODE_DEPLOY_ROLE_FOR_LAMBDA")
    def AWS_CODE_DEPLOY_ROLE_FOR_LAMBDA(cls) -> str:
        return jsii.sget(cls, "AWS_CODE_DEPLOY_ROLE_FOR_LAMBDA")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CODE_PIPELINE_APPROVER_ACCESS")
    def AWS_CODE_PIPELINE_APPROVER_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_CODE_PIPELINE_APPROVER_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CODE_PIPELINE_CUSTOM_ACTION_ACCESS")
    def AWS_CODE_PIPELINE_CUSTOM_ACTION_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_CODE_PIPELINE_CUSTOM_ACTION_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CODE_PIPELINE_FULL_ACCESS")
    def AWS_CODE_PIPELINE_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_CODE_PIPELINE_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CODE_PIPELINE_READ_ONLY_ACCESS")
    def AWS_CODE_PIPELINE_READ_ONLY_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_CODE_PIPELINE_READ_ONLY_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CODE_STAR_FULL_ACCESS")
    def AWS_CODE_STAR_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_CODE_STAR_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CODE_STAR_NOTIFICATIONS_SERVICE_ROLE_POLICY")
    def AWS_CODE_STAR_NOTIFICATIONS_SERVICE_ROLE_POLICY(cls) -> str:
        return jsii.sget(cls, "AWS_CODE_STAR_NOTIFICATIONS_SERVICE_ROLE_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CODE_STAR_SERVICE_ROLE")
    def AWS_CODE_STAR_SERVICE_ROLE(cls) -> str:
        return jsii.sget(cls, "AWS_CODE_STAR_SERVICE_ROLE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CONFIG_MULTI_ACCOUNT_SETUP_POLICY")
    def AWS_CONFIG_MULTI_ACCOUNT_SETUP_POLICY(cls) -> str:
        return jsii.sget(cls, "AWS_CONFIG_MULTI_ACCOUNT_SETUP_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CONFIG_REMEDIATION_SERVICE_ROLE_POLICY")
    def AWS_CONFIG_REMEDIATION_SERVICE_ROLE_POLICY(cls) -> str:
        return jsii.sget(cls, "AWS_CONFIG_REMEDIATION_SERVICE_ROLE_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CONFIG_ROLE")
    def AWS_CONFIG_ROLE(cls) -> str:
        return jsii.sget(cls, "AWS_CONFIG_ROLE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CONFIG_ROLE_FOR_ORGANIZATIONS")
    def AWS_CONFIG_ROLE_FOR_ORGANIZATIONS(cls) -> str:
        return jsii.sget(cls, "AWS_CONFIG_ROLE_FOR_ORGANIZATIONS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CONFIG_RULES_EXECUTION_ROLE")
    def AWS_CONFIG_RULES_EXECUTION_ROLE(cls) -> str:
        return jsii.sget(cls, "AWS_CONFIG_RULES_EXECUTION_ROLE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CONFIG_SERVICE_ROLE_POLICY")
    def AWS_CONFIG_SERVICE_ROLE_POLICY(cls) -> str:
        return jsii.sget(cls, "AWS_CONFIG_SERVICE_ROLE_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CONFIG_USER_ACCESS")
    def AWS_CONFIG_USER_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_CONFIG_USER_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CONNECTOR")
    def AWS_CONNECTOR(cls) -> str:
        return jsii.sget(cls, "AWS_CONNECTOR")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CONTROL_TOWER_SERVICE_ROLE_POLICY")
    def AWS_CONTROL_TOWER_SERVICE_ROLE_POLICY(cls) -> str:
        return jsii.sget(cls, "AWS_CONTROL_TOWER_SERVICE_ROLE_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_DATA_EXCHANGE_FULL_ACCESS")
    def AWS_DATA_EXCHANGE_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_DATA_EXCHANGE_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_DATA_EXCHANGE_PROVIDER_FULL_ACCESS")
    def AWS_DATA_EXCHANGE_PROVIDER_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_DATA_EXCHANGE_PROVIDER_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_DATA_EXCHANGE_READ_ONLY")
    def AWS_DATA_EXCHANGE_READ_ONLY(cls) -> str:
        return jsii.sget(cls, "AWS_DATA_EXCHANGE_READ_ONLY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_DATA_EXCHANGE_SUBSCRIBER_FULL_ACCESS")
    def AWS_DATA_EXCHANGE_SUBSCRIBER_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_DATA_EXCHANGE_SUBSCRIBER_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_DATA_LIFECYCLE_MANAGER_SERVICE_ROLE")
    def AWS_DATA_LIFECYCLE_MANAGER_SERVICE_ROLE(cls) -> str:
        return jsii.sget(cls, "AWS_DATA_LIFECYCLE_MANAGER_SERVICE_ROLE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_DATA_PIPELINE_FULL_ACCESS")
    def AWS_DATA_PIPELINE_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_DATA_PIPELINE_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_DATA_PIPELINE_POWER_USER")
    def AWS_DATA_PIPELINE_POWER_USER(cls) -> str:
        return jsii.sget(cls, "AWS_DATA_PIPELINE_POWER_USER")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_DATA_PIPELINE_ROLE")
    def AWS_DATA_PIPELINE_ROLE(cls) -> str:
        return jsii.sget(cls, "AWS_DATA_PIPELINE_ROLE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_DATA_SYNC_FULL_ACCESS")
    def AWS_DATA_SYNC_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_DATA_SYNC_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_DATA_SYNC_READ_ONLY_ACCESS")
    def AWS_DATA_SYNC_READ_ONLY_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_DATA_SYNC_READ_ONLY_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_DEEP_LENS_LAMBDA_FUNCTION_ACCESS_POLICY")
    def AWS_DEEP_LENS_LAMBDA_FUNCTION_ACCESS_POLICY(cls) -> str:
        return jsii.sget(cls, "AWS_DEEP_LENS_LAMBDA_FUNCTION_ACCESS_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_DEEP_LENS_SERVICE_ROLE_POLICY")
    def AWS_DEEP_LENS_SERVICE_ROLE_POLICY(cls) -> str:
        return jsii.sget(cls, "AWS_DEEP_LENS_SERVICE_ROLE_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_DEEP_RACER_CLOUD_FORMATION_ACCESS_POLICY")
    def AWS_DEEP_RACER_CLOUD_FORMATION_ACCESS_POLICY(cls) -> str:
        return jsii.sget(cls, "AWS_DEEP_RACER_CLOUD_FORMATION_ACCESS_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_DEEP_RACER_ROBO_MAKER_ACCESS_POLICY")
    def AWS_DEEP_RACER_ROBO_MAKER_ACCESS_POLICY(cls) -> str:
        return jsii.sget(cls, "AWS_DEEP_RACER_ROBO_MAKER_ACCESS_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_DEEP_RACER_SERVICE_ROLE_POLICY")
    def AWS_DEEP_RACER_SERVICE_ROLE_POLICY(cls) -> str:
        return jsii.sget(cls, "AWS_DEEP_RACER_SERVICE_ROLE_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_DENY_ALL")
    def AWS_DENY_ALL(cls) -> str:
        return jsii.sget(cls, "AWS_DENY_ALL")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_DEVICE_FARM_FULL_ACCESS")
    def AWS_DEVICE_FARM_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_DEVICE_FARM_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_DIRECT_CONNECT_FULL_ACCESS")
    def AWS_DIRECT_CONNECT_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_DIRECT_CONNECT_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_DIRECT_CONNECT_READ_ONLY_ACCESS")
    def AWS_DIRECT_CONNECT_READ_ONLY_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_DIRECT_CONNECT_READ_ONLY_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_DIRECTORY_SERVICE_FULL_ACCESS")
    def AWS_DIRECTORY_SERVICE_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_DIRECTORY_SERVICE_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_DIRECTORY_SERVICE_READ_ONLY_ACCESS")
    def AWS_DIRECTORY_SERVICE_READ_ONLY_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_DIRECTORY_SERVICE_READ_ONLY_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_DISCOVERY_CONTINUOUS_EXPORT_FIREHOSE_POLICY")
    def AWS_DISCOVERY_CONTINUOUS_EXPORT_FIREHOSE_POLICY(cls) -> str:
        return jsii.sget(cls, "AWS_DISCOVERY_CONTINUOUS_EXPORT_FIREHOSE_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_ELASTIC_BEANSTALK_CUSTOM_PLATFORMFOR_EC2_ROLE")
    def AWS_ELASTIC_BEANSTALK_CUSTOM_PLATFORMFOR_E_C2_ROLE(cls) -> str:
        return jsii.sget(cls, "AWS_ELASTIC_BEANSTALK_CUSTOM_PLATFORMFOR_EC2_ROLE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_ELASTIC_BEANSTALK_ENHANCED_HEALTH")
    def AWS_ELASTIC_BEANSTALK_ENHANCED_HEALTH(cls) -> str:
        return jsii.sget(cls, "AWS_ELASTIC_BEANSTALK_ENHANCED_HEALTH")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_ELASTIC_BEANSTALK_FULL_ACCESS")
    def AWS_ELASTIC_BEANSTALK_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_ELASTIC_BEANSTALK_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_ELASTIC_BEANSTALK_MAINTENANCE")
    def AWS_ELASTIC_BEANSTALK_MAINTENANCE(cls) -> str:
        return jsii.sget(cls, "AWS_ELASTIC_BEANSTALK_MAINTENANCE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_ELASTIC_BEANSTALK_MANAGED_UPDATES_SERVICE_ROLE_POLICY")
    def AWS_ELASTIC_BEANSTALK_MANAGED_UPDATES_SERVICE_ROLE_POLICY(cls) -> str:
        return jsii.sget(cls, "AWS_ELASTIC_BEANSTALK_MANAGED_UPDATES_SERVICE_ROLE_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_ELASTIC_BEANSTALK_MULTICONTAINER_DOCKER")
    def AWS_ELASTIC_BEANSTALK_MULTICONTAINER_DOCKER(cls) -> str:
        return jsii.sget(cls, "AWS_ELASTIC_BEANSTALK_MULTICONTAINER_DOCKER")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_ELASTIC_BEANSTALK_READ_ONLY_ACCESS")
    def AWS_ELASTIC_BEANSTALK_READ_ONLY_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_ELASTIC_BEANSTALK_READ_ONLY_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_ELASTIC_BEANSTALK_SERVICE")
    def AWS_ELASTIC_BEANSTALK_SERVICE(cls) -> str:
        return jsii.sget(cls, "AWS_ELASTIC_BEANSTALK_SERVICE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_ELASTIC_BEANSTALK_SERVICE_ROLE_POLICY")
    def AWS_ELASTIC_BEANSTALK_SERVICE_ROLE_POLICY(cls) -> str:
        return jsii.sget(cls, "AWS_ELASTIC_BEANSTALK_SERVICE_ROLE_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_ELASTIC_BEANSTALK_WEB_TIER")
    def AWS_ELASTIC_BEANSTALK_WEB_TIER(cls) -> str:
        return jsii.sget(cls, "AWS_ELASTIC_BEANSTALK_WEB_TIER")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_ELASTIC_BEANSTALK_WORKER_TIER")
    def AWS_ELASTIC_BEANSTALK_WORKER_TIER(cls) -> str:
        return jsii.sget(cls, "AWS_ELASTIC_BEANSTALK_WORKER_TIER")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_ELASTIC_LOAD_BALANCING_CLASSIC_SERVICE_ROLE_POLICY")
    def AWS_ELASTIC_LOAD_BALANCING_CLASSIC_SERVICE_ROLE_POLICY(cls) -> str:
        return jsii.sget(cls, "AWS_ELASTIC_LOAD_BALANCING_CLASSIC_SERVICE_ROLE_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_ELASTIC_LOAD_BALANCING_SERVICE_ROLE_POLICY")
    def AWS_ELASTIC_LOAD_BALANCING_SERVICE_ROLE_POLICY(cls) -> str:
        return jsii.sget(cls, "AWS_ELASTIC_LOAD_BALANCING_SERVICE_ROLE_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_ELEMENTAL_MEDIA_CONVERT_FULL_ACCESS")
    def AWS_ELEMENTAL_MEDIA_CONVERT_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_ELEMENTAL_MEDIA_CONVERT_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_ELEMENTAL_MEDIA_CONVERT_READ_ONLY")
    def AWS_ELEMENTAL_MEDIA_CONVERT_READ_ONLY(cls) -> str:
        return jsii.sget(cls, "AWS_ELEMENTAL_MEDIA_CONVERT_READ_ONLY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_ELEMENTAL_MEDIA_PACKAGE_FULL_ACCESS")
    def AWS_ELEMENTAL_MEDIA_PACKAGE_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_ELEMENTAL_MEDIA_PACKAGE_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_ELEMENTAL_MEDIA_PACKAGE_READ_ONLY")
    def AWS_ELEMENTAL_MEDIA_PACKAGE_READ_ONLY(cls) -> str:
        return jsii.sget(cls, "AWS_ELEMENTAL_MEDIA_PACKAGE_READ_ONLY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_ELEMENTAL_MEDIA_STORE_FULL_ACCESS")
    def AWS_ELEMENTAL_MEDIA_STORE_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_ELEMENTAL_MEDIA_STORE_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_ELEMENTAL_MEDIA_STORE_READ_ONLY")
    def AWS_ELEMENTAL_MEDIA_STORE_READ_ONLY(cls) -> str:
        return jsii.sget(cls, "AWS_ELEMENTAL_MEDIA_STORE_READ_ONLY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_ENHANCED_CLASSIC_NETWORKING_MANGEMENT_POLICY")
    def AWS_ENHANCED_CLASSIC_NETWORKING_MANGEMENT_POLICY(cls) -> str:
        return jsii.sget(cls, "AWS_ENHANCED_CLASSIC_NETWORKING_MANGEMENT_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_FOR_WORD_PRESS_PLUGIN_POLICY")
    def AWS_FOR_WORD_PRESS_PLUGIN_POLICY(cls) -> str:
        return jsii.sget(cls, "AWS_FOR_WORD_PRESS_PLUGIN_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_GLOBAL_ACCELERATOR_SLR_POLICY")
    def AWS_GLOBAL_ACCELERATOR_SLR_POLICY(cls) -> str:
        return jsii.sget(cls, "AWS_GLOBAL_ACCELERATOR_SLR_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_GLUE_CONSOLE_FULL_ACCESS")
    def AWS_GLUE_CONSOLE_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_GLUE_CONSOLE_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_GLUE_CONSOLE_SAGE_MAKER_NOTEBOOK_FULL_ACCESS")
    def AWS_GLUE_CONSOLE_SAGE_MAKER_NOTEBOOK_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_GLUE_CONSOLE_SAGE_MAKER_NOTEBOOK_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_GLUE_SERVICE_NOTEBOOK_ROLE")
    def AWS_GLUE_SERVICE_NOTEBOOK_ROLE(cls) -> str:
        return jsii.sget(cls, "AWS_GLUE_SERVICE_NOTEBOOK_ROLE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_GLUE_SERVICE_ROLE")
    def AWS_GLUE_SERVICE_ROLE(cls) -> str:
        return jsii.sget(cls, "AWS_GLUE_SERVICE_ROLE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_GREENGRASS_FULL_ACCESS")
    def AWS_GREENGRASS_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_GREENGRASS_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_GREENGRASS_READ_ONLY_ACCESS")
    def AWS_GREENGRASS_READ_ONLY_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_GREENGRASS_READ_ONLY_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_GREENGRASS_RESOURCE_ACCESS_ROLE_POLICY")
    def AWS_GREENGRASS_RESOURCE_ACCESS_ROLE_POLICY(cls) -> str:
        return jsii.sget(cls, "AWS_GREENGRASS_RESOURCE_ACCESS_ROLE_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_HEALTH_FULL_ACCESS")
    def AWS_HEALTH_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_HEALTH_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_IMAGE_BUILDER_READ_ONLY_ACCESS")
    def AWS_IMAGE_BUILDER_READ_ONLY_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_IMAGE_BUILDER_READ_ONLY_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_IMPORT_EXPORT_FULL_ACCESS")
    def AWS_IMPORT_EXPORT_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_IMPORT_EXPORT_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_IMPORT_EXPORT_READ_ONLY_ACCESS")
    def AWS_IMPORT_EXPORT_READ_ONLY_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_IMPORT_EXPORT_READ_ONLY_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_IOT_1_CLICK_FULL_ACCESS")
    def AWS_IOT_1_CLICK_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_IOT_1_CLICK_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_IOT_1_CLICK_READ_ONLY_ACCESS")
    def AWS_IOT_1_CLICK_READ_ONLY_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_IOT_1_CLICK_READ_ONLY_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_IOT_ANALYTICS_FULL_ACCESS")
    def AWS_IOT_ANALYTICS_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_IOT_ANALYTICS_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_IOT_ANALYTICS_READ_ONLY_ACCESS")
    def AWS_IOT_ANALYTICS_READ_ONLY_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_IOT_ANALYTICS_READ_ONLY_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_IOT_CONFIG_ACCESS")
    def AWS_IOT_CONFIG_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_IOT_CONFIG_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_IOT_CONFIG_READ_ONLY_ACCESS")
    def AWS_IOT_CONFIG_READ_ONLY_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_IOT_CONFIG_READ_ONLY_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_IOT_DATA_ACCESS")
    def AWS_IOT_DATA_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_IOT_DATA_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_IOT_DEVICE_DEFENDER_ADD_THINGS_TO_THING_GROUP_MITIGATION_ACTION")
    def AWS_IOT_DEVICE_DEFENDER_ADD_THINGS_TO_THING_GROUP_MITIGATION_ACTION(cls) -> str:
        return jsii.sget(cls, "AWS_IOT_DEVICE_DEFENDER_ADD_THINGS_TO_THING_GROUP_MITIGATION_ACTION")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_IOT_DEVICE_DEFENDER_AUDIT")
    def AWS_IOT_DEVICE_DEFENDER_AUDIT(cls) -> str:
        return jsii.sget(cls, "AWS_IOT_DEVICE_DEFENDER_AUDIT")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_IOT_DEVICE_DEFENDER_ENABLE_IO_T_LOGGING_MITIGATION_ACTION")
    def AWS_IOT_DEVICE_DEFENDER_ENABLE_IO_T_LOGGING_MITIGATION_ACTION(cls) -> str:
        return jsii.sget(cls, "AWS_IOT_DEVICE_DEFENDER_ENABLE_IO_T_LOGGING_MITIGATION_ACTION")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_IOT_DEVICE_DEFENDER_PUBLISH_FINDINGS_TO_SNS_MITIGATION_ACTION")
    def AWS_IOT_DEVICE_DEFENDER_PUBLISH_FINDINGS_TO_SNS_MITIGATION_ACTION(cls) -> str:
        return jsii.sget(cls, "AWS_IOT_DEVICE_DEFENDER_PUBLISH_FINDINGS_TO_SNS_MITIGATION_ACTION")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_IOT_DEVICE_DEFENDER_REPLACE_DEFAULT_POLICY_MITIGATION_ACTION")
    def AWS_IOT_DEVICE_DEFENDER_REPLACE_DEFAULT_POLICY_MITIGATION_ACTION(cls) -> str:
        return jsii.sget(cls, "AWS_IOT_DEVICE_DEFENDER_REPLACE_DEFAULT_POLICY_MITIGATION_ACTION")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_IOT_DEVICE_DEFENDER_UPDATE_CA_CERT_MITIGATION_ACTION")
    def AWS_IOT_DEVICE_DEFENDER_UPDATE_CA_CERT_MITIGATION_ACTION(cls) -> str:
        return jsii.sget(cls, "AWS_IOT_DEVICE_DEFENDER_UPDATE_CA_CERT_MITIGATION_ACTION")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_IOT_DEVICE_DEFENDER_UPDATE_DEVICE_CERT_MITIGATION_ACTION")
    def AWS_IOT_DEVICE_DEFENDER_UPDATE_DEVICE_CERT_MITIGATION_ACTION(cls) -> str:
        return jsii.sget(cls, "AWS_IOT_DEVICE_DEFENDER_UPDATE_DEVICE_CERT_MITIGATION_ACTION")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_IOT_EVENTS_FULL_ACCESS")
    def AWS_IOT_EVENTS_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_IOT_EVENTS_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_IOT_EVENTS_READ_ONLY_ACCESS")
    def AWS_IOT_EVENTS_READ_ONLY_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_IOT_EVENTS_READ_ONLY_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_IOT_FULL_ACCESS")
    def AWS_IOT_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_IOT_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_IOT_LOGGING")
    def AWS_IOT_LOGGING(cls) -> str:
        return jsii.sget(cls, "AWS_IOT_LOGGING")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_IOT_RULE_ACTIONS")
    def AWS_IOT_RULE_ACTIONS(cls) -> str:
        return jsii.sget(cls, "AWS_IOT_RULE_ACTIONS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_IOT_SITE_WISE_CONSOLE_FULL_ACCESS")
    def AWS_IOT_SITE_WISE_CONSOLE_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_IOT_SITE_WISE_CONSOLE_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_IOT_SITE_WISE_FULL_ACCESS")
    def AWS_IOT_SITE_WISE_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_IOT_SITE_WISE_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_IOT_SITE_WISE_MONITOR_SERVICE_ROLE_POLICY")
    def AWS_IOT_SITE_WISE_MONITOR_SERVICE_ROLE_POLICY(cls) -> str:
        return jsii.sget(cls, "AWS_IOT_SITE_WISE_MONITOR_SERVICE_ROLE_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_IOT_SITE_WISE_READ_ONLY_ACCESS")
    def AWS_IOT_SITE_WISE_READ_ONLY_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_IOT_SITE_WISE_READ_ONLY_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_IOT_THINGS_REGISTRATION")
    def AWS_IOT_THINGS_REGISTRATION(cls) -> str:
        return jsii.sget(cls, "AWS_IOT_THINGS_REGISTRATION")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_IOTOTA_UPDATE")
    def AWS_IOTOTA_UPDATE(cls) -> str:
        return jsii.sget(cls, "AWS_IOTOTA_UPDATE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_KEY_MANAGEMENT_SERVICE_CUSTOM_KEY_STORES_SERVICE_ROLE_POLICY")
    def AWS_KEY_MANAGEMENT_SERVICE_CUSTOM_KEY_STORES_SERVICE_ROLE_POLICY(cls) -> str:
        return jsii.sget(cls, "AWS_KEY_MANAGEMENT_SERVICE_CUSTOM_KEY_STORES_SERVICE_ROLE_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_KEY_MANAGEMENT_SERVICE_POWER_USER")
    def AWS_KEY_MANAGEMENT_SERVICE_POWER_USER(cls) -> str:
        return jsii.sget(cls, "AWS_KEY_MANAGEMENT_SERVICE_POWER_USER")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_LAKE_FORMATION_DATA_ADMIN")
    def AWS_LAKE_FORMATION_DATA_ADMIN(cls) -> str:
        return jsii.sget(cls, "AWS_LAKE_FORMATION_DATA_ADMIN")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_LAMBDA_BASIC_EXECUTION_ROLE")
    def AWS_LAMBDA_BASIC_EXECUTION_ROLE(cls) -> str:
        return jsii.sget(cls, "AWS_LAMBDA_BASIC_EXECUTION_ROLE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_LAMBDA_DYNAMO_DB_EXECUTION_ROLE")
    def AWS_LAMBDA_DYNAMO_DB_EXECUTION_ROLE(cls) -> str:
        return jsii.sget(cls, "AWS_LAMBDA_DYNAMO_DB_EXECUTION_ROLE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_LAMBDA_ENI_MANAGEMENT_ACCESS")
    def AWS_LAMBDA_ENI_MANAGEMENT_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_LAMBDA_ENI_MANAGEMENT_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_LAMBDA_EXECUTE")
    def AWS_LAMBDA_EXECUTE(cls) -> str:
        return jsii.sget(cls, "AWS_LAMBDA_EXECUTE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_LAMBDA_FULL_ACCESS")
    def AWS_LAMBDA_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_LAMBDA_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_LAMBDA_INVOCATION_DYNAMO_DB")
    def AWS_LAMBDA_INVOCATION_DYNAMO_DB(cls) -> str:
        return jsii.sget(cls, "AWS_LAMBDA_INVOCATION_DYNAMO_DB")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_LAMBDA_KINESIS_EXECUTION_ROLE")
    def AWS_LAMBDA_KINESIS_EXECUTION_ROLE(cls) -> str:
        return jsii.sget(cls, "AWS_LAMBDA_KINESIS_EXECUTION_ROLE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_LAMBDA_READ_ONLY_ACCESS")
    def AWS_LAMBDA_READ_ONLY_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_LAMBDA_READ_ONLY_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_LAMBDA_REPLICATOR")
    def AWS_LAMBDA_REPLICATOR(cls) -> str:
        return jsii.sget(cls, "AWS_LAMBDA_REPLICATOR")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_LAMBDA_ROLE")
    def AWS_LAMBDA_ROLE(cls) -> str:
        return jsii.sget(cls, "AWS_LAMBDA_ROLE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_LAMBDA_SQS_QUEUE_EXECUTION_ROLE")
    def AWS_LAMBDA_SQS_QUEUE_EXECUTION_ROLE(cls) -> str:
        return jsii.sget(cls, "AWS_LAMBDA_SQS_QUEUE_EXECUTION_ROLE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_LAMBDA_VPC_ACCESS_EXECUTION_ROLE")
    def AWS_LAMBDA_VPC_ACCESS_EXECUTION_ROLE(cls) -> str:
        return jsii.sget(cls, "AWS_LAMBDA_VPC_ACCESS_EXECUTION_ROLE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_LICENSE_MANAGER_MASTER_ACCOUNT_ROLE_POLICY")
    def AWS_LICENSE_MANAGER_MASTER_ACCOUNT_ROLE_POLICY(cls) -> str:
        return jsii.sget(cls, "AWS_LICENSE_MANAGER_MASTER_ACCOUNT_ROLE_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_LICENSE_MANAGER_MEMBER_ACCOUNT_ROLE_POLICY")
    def AWS_LICENSE_MANAGER_MEMBER_ACCOUNT_ROLE_POLICY(cls) -> str:
        return jsii.sget(cls, "AWS_LICENSE_MANAGER_MEMBER_ACCOUNT_ROLE_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_LICENSE_MANAGER_SERVICE_ROLE_POLICY")
    def AWS_LICENSE_MANAGER_SERVICE_ROLE_POLICY(cls) -> str:
        return jsii.sget(cls, "AWS_LICENSE_MANAGER_SERVICE_ROLE_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_MARKETPLACE_FULL_ACCESS")
    def AWS_MARKETPLACE_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_MARKETPLACE_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_MARKETPLACE_GET_ENTITLEMENTS")
    def AWS_MARKETPLACE_GET_ENTITLEMENTS(cls) -> str:
        return jsii.sget(cls, "AWS_MARKETPLACE_GET_ENTITLEMENTS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_MARKETPLACE_IMAGE_BUILD_FULL_ACCESS")
    def AWS_MARKETPLACE_IMAGE_BUILD_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_MARKETPLACE_IMAGE_BUILD_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_MARKETPLACE_MANAGE_SUBSCRIPTIONS")
    def AWS_MARKETPLACE_MANAGE_SUBSCRIPTIONS(cls) -> str:
        return jsii.sget(cls, "AWS_MARKETPLACE_MANAGE_SUBSCRIPTIONS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_MARKETPLACE_METERING_FULL_ACCESS")
    def AWS_MARKETPLACE_METERING_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_MARKETPLACE_METERING_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_MARKETPLACE_METERING_REGISTER_USAGE")
    def AWS_MARKETPLACE_METERING_REGISTER_USAGE(cls) -> str:
        return jsii.sget(cls, "AWS_MARKETPLACE_METERING_REGISTER_USAGE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_MARKETPLACE_PROCUREMENT_SYSTEM_ADMIN_FULL_ACCESS")
    def AWS_MARKETPLACE_PROCUREMENT_SYSTEM_ADMIN_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_MARKETPLACE_PROCUREMENT_SYSTEM_ADMIN_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_MARKETPLACE_READ_ONLY")
    def AWS_MARKETPLACE_READ_ONLY(cls) -> str:
        return jsii.sget(cls, "AWS_MARKETPLACE_READ_ONLY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_MARKETPLACE_SELLER_FULL_ACCESS")
    def AWS_MARKETPLACE_SELLER_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_MARKETPLACE_SELLER_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_MARKETPLACE_SELLER_PRODUCTS_FULL_ACCESS")
    def AWS_MARKETPLACE_SELLER_PRODUCTS_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_MARKETPLACE_SELLER_PRODUCTS_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_MARKETPLACE_SELLER_PRODUCTS_READ_ONLY")
    def AWS_MARKETPLACE_SELLER_PRODUCTS_READ_ONLY(cls) -> str:
        return jsii.sget(cls, "AWS_MARKETPLACE_SELLER_PRODUCTS_READ_ONLY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_MIGRATION_HUB_DISCOVERY_ACCESS")
    def AWS_MIGRATION_HUB_DISCOVERY_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_MIGRATION_HUB_DISCOVERY_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_MIGRATION_HUB_DMS_ACCESS")
    def AWS_MIGRATION_HUB_DMS_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_MIGRATION_HUB_DMS_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_MIGRATION_HUB_FULL_ACCESS")
    def AWS_MIGRATION_HUB_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_MIGRATION_HUB_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_MIGRATION_HUB_SMS_ACCESS")
    def AWS_MIGRATION_HUB_SMS_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_MIGRATION_HUB_SMS_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_MOBILE_HUB_FULL_ACCESS")
    def AWS_MOBILE_HUB_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_MOBILE_HUB_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_MOBILE_HUB_READ_ONLY")
    def AWS_MOBILE_HUB_READ_ONLY(cls) -> str:
        return jsii.sget(cls, "AWS_MOBILE_HUB_READ_ONLY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_NETWORK_MANAGER_FULL_ACCESS")
    def AWS_NETWORK_MANAGER_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_NETWORK_MANAGER_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_NETWORK_MANAGER_READ_ONLY_ACCESS")
    def AWS_NETWORK_MANAGER_READ_ONLY_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_NETWORK_MANAGER_READ_ONLY_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_NETWORK_MANAGER_SERVICE_ROLE_POLICY")
    def AWS_NETWORK_MANAGER_SERVICE_ROLE_POLICY(cls) -> str:
        return jsii.sget(cls, "AWS_NETWORK_MANAGER_SERVICE_ROLE_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_OPS_WORKS_CLOUD_WATCH_LOGS")
    def AWS_OPS_WORKS_CLOUD_WATCH_LOGS(cls) -> str:
        return jsii.sget(cls, "AWS_OPS_WORKS_CLOUD_WATCH_LOGS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_OPS_WORKS_CM_INSTANCE_PROFILE_ROLE")
    def AWS_OPS_WORKS_CM_INSTANCE_PROFILE_ROLE(cls) -> str:
        return jsii.sget(cls, "AWS_OPS_WORKS_CM_INSTANCE_PROFILE_ROLE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_OPS_WORKS_CM_SERVICE_ROLE")
    def AWS_OPS_WORKS_CM_SERVICE_ROLE(cls) -> str:
        return jsii.sget(cls, "AWS_OPS_WORKS_CM_SERVICE_ROLE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_OPS_WORKS_FULL_ACCESS")
    def AWS_OPS_WORKS_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_OPS_WORKS_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_OPS_WORKS_INSTANCE_REGISTRATION")
    def AWS_OPS_WORKS_INSTANCE_REGISTRATION(cls) -> str:
        return jsii.sget(cls, "AWS_OPS_WORKS_INSTANCE_REGISTRATION")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_OPS_WORKS_REGISTER_CLI_EC2")
    def AWS_OPS_WORKS_REGISTER_CLI_E_C2(cls) -> str:
        return jsii.sget(cls, "AWS_OPS_WORKS_REGISTER_CLI_EC2")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_OPS_WORKS_REGISTER_CLI_ON_PREMISES")
    def AWS_OPS_WORKS_REGISTER_CLI_ON_PREMISES(cls) -> str:
        return jsii.sget(cls, "AWS_OPS_WORKS_REGISTER_CLI_ON_PREMISES")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_OPS_WORKS_ROLE")
    def AWS_OPS_WORKS_ROLE(cls) -> str:
        return jsii.sget(cls, "AWS_OPS_WORKS_ROLE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_ORGANIZATIONS_FULL_ACCESS")
    def AWS_ORGANIZATIONS_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_ORGANIZATIONS_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_ORGANIZATIONS_READ_ONLY_ACCESS")
    def AWS_ORGANIZATIONS_READ_ONLY_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_ORGANIZATIONS_READ_ONLY_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_ORGANIZATIONS_SERVICE_TRUST_POLICY")
    def AWS_ORGANIZATIONS_SERVICE_TRUST_POLICY(cls) -> str:
        return jsii.sget(cls, "AWS_ORGANIZATIONS_SERVICE_TRUST_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_PRICE_LIST_SERVICE_FULL_ACCESS")
    def AWS_PRICE_LIST_SERVICE_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_PRICE_LIST_SERVICE_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_PRIVATE_MARKETPLACE_ADMIN_FULL_ACCESS")
    def AWS_PRIVATE_MARKETPLACE_ADMIN_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_PRIVATE_MARKETPLACE_ADMIN_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_PRIVATE_MARKETPLACE_REQUESTS")
    def AWS_PRIVATE_MARKETPLACE_REQUESTS(cls) -> str:
        return jsii.sget(cls, "AWS_PRIVATE_MARKETPLACE_REQUESTS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_QUICK_SIGHT_DESCRIBE_RDS")
    def AWS_QUICK_SIGHT_DESCRIBE_RDS(cls) -> str:
        return jsii.sget(cls, "AWS_QUICK_SIGHT_DESCRIBE_RDS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_QUICK_SIGHT_DESCRIBE_REDSHIFT")
    def AWS_QUICK_SIGHT_DESCRIBE_REDSHIFT(cls) -> str:
        return jsii.sget(cls, "AWS_QUICK_SIGHT_DESCRIBE_REDSHIFT")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_QUICK_SIGHT_IOT_ANALYTICS_ACCESS")
    def AWS_QUICK_SIGHT_IOT_ANALYTICS_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_QUICK_SIGHT_IOT_ANALYTICS_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_QUICK_SIGHT_LIST_IAM")
    def AWS_QUICK_SIGHT_LIST_IAM(cls) -> str:
        return jsii.sget(cls, "AWS_QUICK_SIGHT_LIST_IAM")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_QUICKSIGHT_ATHENA_ACCESS")
    def AWS_QUICKSIGHT_ATHENA_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_QUICKSIGHT_ATHENA_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_RESOURCE_ACCESS_MANAGER_FULL_ACCESS")
    def AWS_RESOURCE_ACCESS_MANAGER_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_RESOURCE_ACCESS_MANAGER_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_RESOURCE_ACCESS_MANAGER_READ_ONLY_ACCESS")
    def AWS_RESOURCE_ACCESS_MANAGER_READ_ONLY_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_RESOURCE_ACCESS_MANAGER_READ_ONLY_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_RESOURCE_ACCESS_MANAGER_RESOURCE_SHARE_PARTICIPANT_ACCESS")
    def AWS_RESOURCE_ACCESS_MANAGER_RESOURCE_SHARE_PARTICIPANT_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_RESOURCE_ACCESS_MANAGER_RESOURCE_SHARE_PARTICIPANT_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_RESOURCE_ACCESS_MANAGER_SERVICE_ROLE_POLICY")
    def AWS_RESOURCE_ACCESS_MANAGER_SERVICE_ROLE_POLICY(cls) -> str:
        return jsii.sget(cls, "AWS_RESOURCE_ACCESS_MANAGER_SERVICE_ROLE_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_RESOURCE_GROUPS_READ_ONLY_ACCESS")
    def AWS_RESOURCE_GROUPS_READ_ONLY_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_RESOURCE_GROUPS_READ_ONLY_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_ROBO_MAKER_FULL_ACCESS")
    def AWS_ROBO_MAKER_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_ROBO_MAKER_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_ROBO_MAKER_READ_ONLY_ACCESS")
    def AWS_ROBO_MAKER_READ_ONLY_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_ROBO_MAKER_READ_ONLY_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_ROBO_MAKER_SERVICE_POLICY")
    def AWS_ROBO_MAKER_SERVICE_POLICY(cls) -> str:
        return jsii.sget(cls, "AWS_ROBO_MAKER_SERVICE_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_ROBO_MAKER_SERVICE_ROLE_POLICY")
    def AWS_ROBO_MAKER_SERVICE_ROLE_POLICY(cls) -> str:
        return jsii.sget(cls, "AWS_ROBO_MAKER_SERVICE_ROLE_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_SAVINGS_PLANS_FULL_ACCESS")
    def AWS_SAVINGS_PLANS_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_SAVINGS_PLANS_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_SAVINGS_PLANS_READ_ONLY_ACCESS")
    def AWS_SAVINGS_PLANS_READ_ONLY_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_SAVINGS_PLANS_READ_ONLY_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_SECURITY_HUB_FULL_ACCESS")
    def AWS_SECURITY_HUB_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_SECURITY_HUB_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_SECURITY_HUB_READ_ONLY_ACCESS")
    def AWS_SECURITY_HUB_READ_ONLY_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_SECURITY_HUB_READ_ONLY_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_SECURITY_HUB_SERVICE_ROLE_POLICY")
    def AWS_SECURITY_HUB_SERVICE_ROLE_POLICY(cls) -> str:
        return jsii.sget(cls, "AWS_SECURITY_HUB_SERVICE_ROLE_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_SERVICE_CATALOG_ADMIN_FULL_ACCESS")
    def AWS_SERVICE_CATALOG_ADMIN_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_SERVICE_CATALOG_ADMIN_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_SERVICE_CATALOG_ADMIN_READ_ONLY_ACCESS")
    def AWS_SERVICE_CATALOG_ADMIN_READ_ONLY_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_SERVICE_CATALOG_ADMIN_READ_ONLY_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_SERVICE_CATALOG_END_USER_FULL_ACCESS")
    def AWS_SERVICE_CATALOG_END_USER_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_SERVICE_CATALOG_END_USER_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_SERVICE_CATALOG_END_USER_READ_ONLY_ACCESS")
    def AWS_SERVICE_CATALOG_END_USER_READ_ONLY_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_SERVICE_CATALOG_END_USER_READ_ONLY_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_SERVICE_ROLE_FOR_AMAZON_EKS_NODEGROUP")
    def AWS_SERVICE_ROLE_FOR_AMAZON_EKS_NODEGROUP(cls) -> str:
        return jsii.sget(cls, "AWS_SERVICE_ROLE_FOR_AMAZON_EKS_NODEGROUP")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_SERVICE_ROLE_FOR_EC2_SCHEDULED_INSTANCES")
    def AWS_SERVICE_ROLE_FOR_E_C2_SCHEDULED_INSTANCES(cls) -> str:
        return jsii.sget(cls, "AWS_SERVICE_ROLE_FOR_EC2_SCHEDULED_INSTANCES")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_SERVICE_ROLE_FOR_IMAGE_BUILDER")
    def AWS_SERVICE_ROLE_FOR_IMAGE_BUILDER(cls) -> str:
        return jsii.sget(cls, "AWS_SERVICE_ROLE_FOR_IMAGE_BUILDER")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_SERVICE_ROLE_FOR_IOT_SITE_WISE")
    def AWS_SERVICE_ROLE_FOR_IOT_SITE_WISE(cls) -> str:
        return jsii.sget(cls, "AWS_SERVICE_ROLE_FOR_IOT_SITE_WISE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_SERVICE_ROLE_FOR_LOG_DELIVERY_POLICY")
    def AWS_SERVICE_ROLE_FOR_LOG_DELIVERY_POLICY(cls) -> str:
        return jsii.sget(cls, "AWS_SERVICE_ROLE_FOR_LOG_DELIVERY_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_SERVICE_ROLE_FOR_SMS")
    def AWS_SERVICE_ROLE_FOR_SMS(cls) -> str:
        return jsii.sget(cls, "AWS_SERVICE_ROLE_FOR_SMS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_SHIELD_DRT_ACCESS_POLICY")
    def AWS_SHIELD_DRT_ACCESS_POLICY(cls) -> str:
        return jsii.sget(cls, "AWS_SHIELD_DRT_ACCESS_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_STEP_FUNCTIONS_CONSOLE_FULL_ACCESS")
    def AWS_STEP_FUNCTIONS_CONSOLE_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_STEP_FUNCTIONS_CONSOLE_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_STEP_FUNCTIONS_FULL_ACCESS")
    def AWS_STEP_FUNCTIONS_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_STEP_FUNCTIONS_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_STEP_FUNCTIONS_READ_ONLY_ACCESS")
    def AWS_STEP_FUNCTIONS_READ_ONLY_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_STEP_FUNCTIONS_READ_ONLY_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_STORAGE_GATEWAY_FULL_ACCESS")
    def AWS_STORAGE_GATEWAY_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_STORAGE_GATEWAY_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_STORAGE_GATEWAY_READ_ONLY_ACCESS")
    def AWS_STORAGE_GATEWAY_READ_ONLY_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_STORAGE_GATEWAY_READ_ONLY_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_SUPPORT_ACCESS")
    def AWS_SUPPORT_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_SUPPORT_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_SUPPORT_SERVICE_ROLE_POLICY")
    def AWS_SUPPORT_SERVICE_ROLE_POLICY(cls) -> str:
        return jsii.sget(cls, "AWS_SUPPORT_SERVICE_ROLE_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_SYSTEMS_MANAGER_ACCOUNT_DISCOVERY_SERVICE_POLICY")
    def AWS_SYSTEMS_MANAGER_ACCOUNT_DISCOVERY_SERVICE_POLICY(cls) -> str:
        return jsii.sget(cls, "AWS_SYSTEMS_MANAGER_ACCOUNT_DISCOVERY_SERVICE_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_TRANSFER_LOGGING_ACCESS")
    def AWS_TRANSFER_LOGGING_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_TRANSFER_LOGGING_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_TRUSTED_ADVISOR_REPORTING_SERVICE_ROLE_POLICY")
    def AWS_TRUSTED_ADVISOR_REPORTING_SERVICE_ROLE_POLICY(cls) -> str:
        return jsii.sget(cls, "AWS_TRUSTED_ADVISOR_REPORTING_SERVICE_ROLE_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_TRUSTED_ADVISOR_SERVICE_ROLE_POLICY")
    def AWS_TRUSTED_ADVISOR_SERVICE_ROLE_POLICY(cls) -> str:
        return jsii.sget(cls, "AWS_TRUSTED_ADVISOR_SERVICE_ROLE_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_XRAY_FULL_ACCESS")
    def AWS_XRAY_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_XRAY_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_XRAY_READ_ONLY_ACCESS")
    def AWS_XRAY_READ_ONLY_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_XRAY_READ_ONLY_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_XRAY_WRITE_ONLY_ACCESS")
    def AWS_XRAY_WRITE_ONLY_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWS_XRAY_WRITE_ONLY_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWSB_9_INTERNAL_SERVICE_POLICY")
    def AWSB_9_INTERNAL_SERVICE_POLICY(cls) -> str:
        return jsii.sget(cls, "AWSB_9_INTERNAL_SERVICE_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWSEC2_FLEET_SERVICE_ROLE_POLICY")
    def AWSE_C2_FLEET_SERVICE_ROLE_POLICY(cls) -> str:
        return jsii.sget(cls, "AWSEC2_FLEET_SERVICE_ROLE_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWSEC2_SPOT_FLEET_SERVICE_ROLE_POLICY")
    def AWSE_C2_SPOT_FLEET_SERVICE_ROLE_POLICY(cls) -> str:
        return jsii.sget(cls, "AWSEC2_SPOT_FLEET_SERVICE_ROLE_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWSEC2_SPOT_SERVICE_ROLE_POLICY")
    def AWSE_C2_SPOT_SERVICE_ROLE_POLICY(cls) -> str:
        return jsii.sget(cls, "AWSEC2_SPOT_SERVICE_ROLE_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWSFM_ADMIN_FULL_ACCESS")
    def AWSFM_ADMIN_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWSFM_ADMIN_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWSFM_ADMIN_READ_ONLY_ACCESS")
    def AWSFM_ADMIN_READ_ONLY_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWSFM_ADMIN_READ_ONLY_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWSFM_MEMBER_READ_ONLY_ACCESS")
    def AWSFM_MEMBER_READ_ONLY_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWSFM_MEMBER_READ_ONLY_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWSIQ_CONTRACT_SERVICE_ROLE_POLICY")
    def AWSIQ_CONTRACT_SERVICE_ROLE_POLICY(cls) -> str:
        return jsii.sget(cls, "AWSIQ_CONTRACT_SERVICE_ROLE_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWSIQ_FULL_ACCESS")
    def AWSIQ_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWSIQ_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWSIQ_PERMISSION_SERVICE_ROLE_POLICY")
    def AWSIQ_PERMISSION_SERVICE_ROLE_POLICY(cls) -> str:
        return jsii.sget(cls, "AWSIQ_PERMISSION_SERVICE_ROLE_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWSSSO_DIRECTORY_ADMINISTRATOR")
    def AWSSSO_DIRECTORY_ADMINISTRATOR(cls) -> str:
        return jsii.sget(cls, "AWSSSO_DIRECTORY_ADMINISTRATOR")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWSSSO_DIRECTORY_READ_ONLY")
    def AWSSSO_DIRECTORY_READ_ONLY(cls) -> str:
        return jsii.sget(cls, "AWSSSO_DIRECTORY_READ_ONLY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWSSSO_MASTER_ACCOUNT_ADMINISTRATOR")
    def AWSSSO_MASTER_ACCOUNT_ADMINISTRATOR(cls) -> str:
        return jsii.sget(cls, "AWSSSO_MASTER_ACCOUNT_ADMINISTRATOR")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWSSSO_MEMBER_ACCOUNT_ADMINISTRATOR")
    def AWSSSO_MEMBER_ACCOUNT_ADMINISTRATOR(cls) -> str:
        return jsii.sget(cls, "AWSSSO_MEMBER_ACCOUNT_ADMINISTRATOR")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWSSSO_READ_ONLY")
    def AWSSSO_READ_ONLY(cls) -> str:
        return jsii.sget(cls, "AWSSSO_READ_ONLY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWSSSO_SERVICE_ROLE_POLICY")
    def AWSSSO_SERVICE_ROLE_POLICY(cls) -> str:
        return jsii.sget(cls, "AWSSSO_SERVICE_ROLE_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWSVPC_TRANSIT_GATEWAY_SERVICE_ROLE_POLICY")
    def AWSVPC_TRANSIT_GATEWAY_SERVICE_ROLE_POLICY(cls) -> str:
        return jsii.sget(cls, "AWSVPC_TRANSIT_GATEWAY_SERVICE_ROLE_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWSVPCS_2_S_VPN_SERVICE_ROLE_POLICY")
    def AWSVPCS_2_S_VPN_SERVICE_ROLE_POLICY(cls) -> str:
        return jsii.sget(cls, "AWSVPCS_2_S_VPN_SERVICE_ROLE_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWSWAF_FULL_ACCESS")
    def AWSWAF_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWSWAF_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWSWAF_READ_ONLY_ACCESS")
    def AWSWAF_READ_ONLY_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWSWAF_READ_ONLY_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWSX_RAY_DAEMON_WRITE_ACCESS")
    def AWSX_RAY_DAEMON_WRITE_ACCESS(cls) -> str:
        return jsii.sget(cls, "AWSX_RAY_DAEMON_WRITE_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="BILLING")
    def BILLING(cls) -> str:
        return jsii.sget(cls, "BILLING")

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLIENT_VPN_SERVICE_ROLE_POLICY")
    def CLIENT_VPN_SERVICE_ROLE_POLICY(cls) -> str:
        return jsii.sget(cls, "CLIENT_VPN_SERVICE_ROLE_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUD_FORMATION_STACK_SETS_ORG_ADMIN_SERVICE_ROLE_POLICY")
    def CLOUD_FORMATION_STACK_SETS_ORG_ADMIN_SERVICE_ROLE_POLICY(cls) -> str:
        return jsii.sget(cls, "CLOUD_FORMATION_STACK_SETS_ORG_ADMIN_SERVICE_ROLE_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUD_FORMATION_STACK_SETS_ORG_MEMBER_SERVICE_ROLE_POLICY")
    def CLOUD_FORMATION_STACK_SETS_ORG_MEMBER_SERVICE_ROLE_POLICY(cls) -> str:
        return jsii.sget(cls, "CLOUD_FORMATION_STACK_SETS_ORG_MEMBER_SERVICE_ROLE_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUD_FRONT_FULL_ACCESS")
    def CLOUD_FRONT_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "CLOUD_FRONT_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUD_FRONT_READ_ONLY_ACCESS")
    def CLOUD_FRONT_READ_ONLY_ACCESS(cls) -> str:
        return jsii.sget(cls, "CLOUD_FRONT_READ_ONLY_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUD_HSM_SERVICE_ROLE_POLICY")
    def CLOUD_HSM_SERVICE_ROLE_POLICY(cls) -> str:
        return jsii.sget(cls, "CLOUD_HSM_SERVICE_ROLE_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUD_SEARCH_FULL_ACCESS")
    def CLOUD_SEARCH_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "CLOUD_SEARCH_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUD_SEARCH_READ_ONLY_ACCESS")
    def CLOUD_SEARCH_READ_ONLY_ACCESS(cls) -> str:
        return jsii.sget(cls, "CLOUD_SEARCH_READ_ONLY_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUD_TRAIL_SERVICE_ROLE_POLICY")
    def CLOUD_TRAIL_SERVICE_ROLE_POLICY(cls) -> str:
        return jsii.sget(cls, "CLOUD_TRAIL_SERVICE_ROLE_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUD_WATCH_ACTIONS_EC2_ACCESS")
    def CLOUD_WATCH_ACTIONS_E_C2_ACCESS(cls) -> str:
        return jsii.sget(cls, "CLOUD_WATCH_ACTIONS_EC2_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUD_WATCH_AGENT_ADMIN_POLICY")
    def CLOUD_WATCH_AGENT_ADMIN_POLICY(cls) -> str:
        return jsii.sget(cls, "CLOUD_WATCH_AGENT_ADMIN_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUD_WATCH_AGENT_SERVER_POLICY")
    def CLOUD_WATCH_AGENT_SERVER_POLICY(cls) -> str:
        return jsii.sget(cls, "CLOUD_WATCH_AGENT_SERVER_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUD_WATCH_AUTOMATIC_DASHBOARDS_ACCESS")
    def CLOUD_WATCH_AUTOMATIC_DASHBOARDS_ACCESS(cls) -> str:
        return jsii.sget(cls, "CLOUD_WATCH_AUTOMATIC_DASHBOARDS_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUD_WATCH_CROSS_ACCOUNT_ACCESS")
    def CLOUD_WATCH_CROSS_ACCOUNT_ACCESS(cls) -> str:
        return jsii.sget(cls, "CLOUD_WATCH_CROSS_ACCOUNT_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUD_WATCH_EVENTS_BUILT_IN_TARGET_EXECUTION_ACCESS")
    def CLOUD_WATCH_EVENTS_BUILT_IN_TARGET_EXECUTION_ACCESS(cls) -> str:
        return jsii.sget(cls, "CLOUD_WATCH_EVENTS_BUILT_IN_TARGET_EXECUTION_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUD_WATCH_EVENTS_FULL_ACCESS")
    def CLOUD_WATCH_EVENTS_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "CLOUD_WATCH_EVENTS_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUD_WATCH_EVENTS_INVOCATION_ACCESS")
    def CLOUD_WATCH_EVENTS_INVOCATION_ACCESS(cls) -> str:
        return jsii.sget(cls, "CLOUD_WATCH_EVENTS_INVOCATION_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUD_WATCH_EVENTS_READ_ONLY_ACCESS")
    def CLOUD_WATCH_EVENTS_READ_ONLY_ACCESS(cls) -> str:
        return jsii.sget(cls, "CLOUD_WATCH_EVENTS_READ_ONLY_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUD_WATCH_EVENTS_SERVICE_ROLE_POLICY")
    def CLOUD_WATCH_EVENTS_SERVICE_ROLE_POLICY(cls) -> str:
        return jsii.sget(cls, "CLOUD_WATCH_EVENTS_SERVICE_ROLE_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUD_WATCH_FULL_ACCESS")
    def CLOUD_WATCH_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "CLOUD_WATCH_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUD_WATCH_LOGS_FULL_ACCESS")
    def CLOUD_WATCH_LOGS_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "CLOUD_WATCH_LOGS_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUD_WATCH_LOGS_READ_ONLY_ACCESS")
    def CLOUD_WATCH_LOGS_READ_ONLY_ACCESS(cls) -> str:
        return jsii.sget(cls, "CLOUD_WATCH_LOGS_READ_ONLY_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUD_WATCH_READ_ONLY_ACCESS")
    def CLOUD_WATCH_READ_ONLY_ACCESS(cls) -> str:
        return jsii.sget(cls, "CLOUD_WATCH_READ_ONLY_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUD_WATCH_SYNTHETICS_FULL_ACCESS")
    def CLOUD_WATCH_SYNTHETICS_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "CLOUD_WATCH_SYNTHETICS_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUD_WATCH_SYNTHETICS_READ_ONLY_ACCESS")
    def CLOUD_WATCH_SYNTHETICS_READ_ONLY_ACCESS(cls) -> str:
        return jsii.sget(cls, "CLOUD_WATCH_SYNTHETICS_READ_ONLY_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUDWATCH_APPLICATION_INSIGHTS_SERVICE_LINKED_ROLE_POLICY")
    def CLOUDWATCH_APPLICATION_INSIGHTS_SERVICE_LINKED_ROLE_POLICY(cls) -> str:
        return jsii.sget(cls, "CLOUDWATCH_APPLICATION_INSIGHTS_SERVICE_LINKED_ROLE_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="COMPREHEND_DATA_ACCESS_ROLE_POLICY")
    def COMPREHEND_DATA_ACCESS_ROLE_POLICY(cls) -> str:
        return jsii.sget(cls, "COMPREHEND_DATA_ACCESS_ROLE_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="COMPREHEND_FULL_ACCESS")
    def COMPREHEND_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "COMPREHEND_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="COMPREHEND_MEDICAL_FULL_ACCESS")
    def COMPREHEND_MEDICAL_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "COMPREHEND_MEDICAL_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="COMPREHEND_READ_ONLY")
    def COMPREHEND_READ_ONLY(cls) -> str:
        return jsii.sget(cls, "COMPREHEND_READ_ONLY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="COMPUTE_OPTIMIZER_SERVICE_ROLE_POLICY")
    def COMPUTE_OPTIMIZER_SERVICE_ROLE_POLICY(cls) -> str:
        return jsii.sget(cls, "COMPUTE_OPTIMIZER_SERVICE_ROLE_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="CONFIG_CONFORMS_SERVICE_ROLE_POLICY")
    def CONFIG_CONFORMS_SERVICE_ROLE_POLICY(cls) -> str:
        return jsii.sget(cls, "CONFIG_CONFORMS_SERVICE_ROLE_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="DATA_SCIENTIST")
    def DATA_SCIENTIST(cls) -> str:
        return jsii.sget(cls, "DATA_SCIENTIST")

    @jsii.python.classproperty
    @jsii.member(jsii_name="DATABASE_ADMINISTRATOR")
    def DATABASE_ADMINISTRATOR(cls) -> str:
        return jsii.sget(cls, "DATABASE_ADMINISTRATOR")

    @jsii.python.classproperty
    @jsii.member(jsii_name="DAX_SERVICE_ROLE_POLICY")
    def DAX_SERVICE_ROLE_POLICY(cls) -> str:
        return jsii.sget(cls, "DAX_SERVICE_ROLE_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="DYNAMO_DB_CLOUD_WATCH_CONTRIBUTOR_INSIGHTS_SERVICE_ROLE_POLICY")
    def DYNAMO_DB_CLOUD_WATCH_CONTRIBUTOR_INSIGHTS_SERVICE_ROLE_POLICY(cls) -> str:
        return jsii.sget(cls, "DYNAMO_DB_CLOUD_WATCH_CONTRIBUTOR_INSIGHTS_SERVICE_ROLE_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="DYNAMO_DB_REPLICATION_SERVICE_ROLE_POLICY")
    def DYNAMO_DB_REPLICATION_SERVICE_ROLE_POLICY(cls) -> str:
        return jsii.sget(cls, "DYNAMO_DB_REPLICATION_SERVICE_ROLE_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="EC2_INSTANCE_CONNECT")
    def E_C2_INSTANCE_CONNECT(cls) -> str:
        return jsii.sget(cls, "EC2_INSTANCE_CONNECT")

    @jsii.python.classproperty
    @jsii.member(jsii_name="EC2_INSTANCE_PROFILE_FOR_IMAGE_BUILDER")
    def E_C2_INSTANCE_PROFILE_FOR_IMAGE_BUILDER(cls) -> str:
        return jsii.sget(cls, "EC2_INSTANCE_PROFILE_FOR_IMAGE_BUILDER")

    @jsii.python.classproperty
    @jsii.member(jsii_name="ELASTI_CACHE_SERVICE_ROLE_POLICY")
    def ELASTI_CACHE_SERVICE_ROLE_POLICY(cls) -> str:
        return jsii.sget(cls, "ELASTI_CACHE_SERVICE_ROLE_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="ELASTIC_LOAD_BALANCING_FULL_ACCESS")
    def ELASTIC_LOAD_BALANCING_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "ELASTIC_LOAD_BALANCING_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="ELASTIC_LOAD_BALANCING_READ_ONLY")
    def ELASTIC_LOAD_BALANCING_READ_ONLY(cls) -> str:
        return jsii.sget(cls, "ELASTIC_LOAD_BALANCING_READ_ONLY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="ELEMENTAL_APPLIANCES_SOFTWARE_FULL_ACCESS")
    def ELEMENTAL_APPLIANCES_SOFTWARE_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "ELEMENTAL_APPLIANCES_SOFTWARE_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="F_SX_DELETE_SERVICE_LINKED_ROLE_ACCESS")
    def F_SX_DELETE_SERVICE_LINKED_ROLE_ACCESS(cls) -> str:
        return jsii.sget(cls, "F_SX_DELETE_SERVICE_LINKED_ROLE_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="FMS_SERVICE_ROLE_POLICY")
    def FMS_SERVICE_ROLE_POLICY(cls) -> str:
        return jsii.sget(cls, "FMS_SERVICE_ROLE_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="GLOBAL_ACCELERATOR_FULL_ACCESS")
    def GLOBAL_ACCELERATOR_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "GLOBAL_ACCELERATOR_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="GLOBAL_ACCELERATOR_READ_ONLY_ACCESS")
    def GLOBAL_ACCELERATOR_READ_ONLY_ACCESS(cls) -> str:
        return jsii.sget(cls, "GLOBAL_ACCELERATOR_READ_ONLY_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="GREENGRASS_OTA_UPDATE_ARTIFACT_ACCESS")
    def GREENGRASS_OTA_UPDATE_ARTIFACT_ACCESS(cls) -> str:
        return jsii.sget(cls, "GREENGRASS_OTA_UPDATE_ARTIFACT_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="HEALTH_ORGANIZATIONS_SERVICE_ROLE_POLICY")
    def HEALTH_ORGANIZATIONS_SERVICE_ROLE_POLICY(cls) -> str:
        return jsii.sget(cls, "HEALTH_ORGANIZATIONS_SERVICE_ROLE_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="IAM_ACCESS_ADVISOR_READ_ONLY")
    def IAM_ACCESS_ADVISOR_READ_ONLY(cls) -> str:
        return jsii.sget(cls, "IAM_ACCESS_ADVISOR_READ_ONLY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="IAM_ACCESS_ANALYZER_FULL_ACCESS")
    def IAM_ACCESS_ANALYZER_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "IAM_ACCESS_ANALYZER_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="IAM_ACCESS_ANALYZER_READ_ONLY_ACCESS")
    def IAM_ACCESS_ANALYZER_READ_ONLY_ACCESS(cls) -> str:
        return jsii.sget(cls, "IAM_ACCESS_ANALYZER_READ_ONLY_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="IAM_FULL_ACCESS")
    def IAM_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "IAM_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="IAM_READ_ONLY_ACCESS")
    def IAM_READ_ONLY_ACCESS(cls) -> str:
        return jsii.sget(cls, "IAM_READ_ONLY_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="IAM_SELF_MANAGE_SERVICE_SPECIFIC_CREDENTIALS")
    def IAM_SELF_MANAGE_SERVICE_SPECIFIC_CREDENTIALS(cls) -> str:
        return jsii.sget(cls, "IAM_SELF_MANAGE_SERVICE_SPECIFIC_CREDENTIALS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="IAM_USER_CHANGE_PASSWORD")
    def IAM_USER_CHANGE_PASSWORD(cls) -> str:
        return jsii.sget(cls, "IAM_USER_CHANGE_PASSWORD")

    @jsii.python.classproperty
    @jsii.member(jsii_name="IAM_USER_SSH_KEYS")
    def IAM_USER_SSH_KEYS(cls) -> str:
        return jsii.sget(cls, "IAM_USER_SSH_KEYS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="KAFKA_SERVICE_ROLE_POLICY")
    def KAFKA_SERVICE_ROLE_POLICY(cls) -> str:
        return jsii.sget(cls, "KAFKA_SERVICE_ROLE_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="LAKE_FORMATION_DATA_ACCESS_SERVICE_ROLE_POLICY")
    def LAKE_FORMATION_DATA_ACCESS_SERVICE_ROLE_POLICY(cls) -> str:
        return jsii.sget(cls, "LAKE_FORMATION_DATA_ACCESS_SERVICE_ROLE_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="LEX_BOT_POLICY")
    def LEX_BOT_POLICY(cls) -> str:
        return jsii.sget(cls, "LEX_BOT_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="LEX_CHANNEL_POLICY")
    def LEX_CHANNEL_POLICY(cls) -> str:
        return jsii.sget(cls, "LEX_CHANNEL_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="LIGHTSAIL_EXPORT_ACCESS")
    def LIGHTSAIL_EXPORT_ACCESS(cls) -> str:
        return jsii.sget(cls, "LIGHTSAIL_EXPORT_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="MIGRATION_HUB_DMS_ACCESS_SERVICE_ROLE_POLICY")
    def MIGRATION_HUB_DMS_ACCESS_SERVICE_ROLE_POLICY(cls) -> str:
        return jsii.sget(cls, "MIGRATION_HUB_DMS_ACCESS_SERVICE_ROLE_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="MIGRATION_HUB_SERVICE_ROLE_POLICY")
    def MIGRATION_HUB_SERVICE_ROLE_POLICY(cls) -> str:
        return jsii.sget(cls, "MIGRATION_HUB_SERVICE_ROLE_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="MIGRATION_HUB_SMS_ACCESS_SERVICE_ROLE_POLICY")
    def MIGRATION_HUB_SMS_ACCESS_SERVICE_ROLE_POLICY(cls) -> str:
        return jsii.sget(cls, "MIGRATION_HUB_SMS_ACCESS_SERVICE_ROLE_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="NEPTUNE_CONSOLE_FULL_ACCESS")
    def NEPTUNE_CONSOLE_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "NEPTUNE_CONSOLE_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="NEPTUNE_FULL_ACCESS")
    def NEPTUNE_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "NEPTUNE_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="NEPTUNE_READ_ONLY_ACCESS")
    def NEPTUNE_READ_ONLY_ACCESS(cls) -> str:
        return jsii.sget(cls, "NEPTUNE_READ_ONLY_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="NETWORK_ADMINISTRATOR")
    def NETWORK_ADMINISTRATOR(cls) -> str:
        return jsii.sget(cls, "NETWORK_ADMINISTRATOR")

    @jsii.python.classproperty
    @jsii.member(jsii_name="POWER_USER_ACCESS")
    def POWER_USER_ACCESS(cls) -> str:
        return jsii.sget(cls, "POWER_USER_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="QUICK_SIGHT_ACCESS_FOR_S3_STORAGE_MANAGEMENT_ANALYTICS_READ_ONLY")
    def QUICK_SIGHT_ACCESS_FOR_S3_STORAGE_MANAGEMENT_ANALYTICS_READ_ONLY(cls) -> str:
        return jsii.sget(cls, "QUICK_SIGHT_ACCESS_FOR_S3_STORAGE_MANAGEMENT_ANALYTICS_READ_ONLY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="RDS_CLOUD_HSM_AUTHORIZATION_ROLE")
    def RDS_CLOUD_HSM_AUTHORIZATION_ROLE(cls) -> str:
        return jsii.sget(cls, "RDS_CLOUD_HSM_AUTHORIZATION_ROLE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="READ_ONLY_ACCESS")
    def READ_ONLY_ACCESS(cls) -> str:
        return jsii.sget(cls, "READ_ONLY_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="RESOURCE_GROUPSAND_TAG_EDITOR_FULL_ACCESS")
    def RESOURCE_GROUPSAND_TAG_EDITOR_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "RESOURCE_GROUPSAND_TAG_EDITOR_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="RESOURCE_GROUPSAND_TAG_EDITOR_READ_ONLY_ACCESS")
    def RESOURCE_GROUPSAND_TAG_EDITOR_READ_ONLY_ACCESS(cls) -> str:
        return jsii.sget(cls, "RESOURCE_GROUPSAND_TAG_EDITOR_READ_ONLY_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="SECRETS_MANAGER_READ_WRITE")
    def SECRETS_MANAGER_READ_WRITE(cls) -> str:
        return jsii.sget(cls, "SECRETS_MANAGER_READ_WRITE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="SECURITY_AUDIT")
    def SECURITY_AUDIT(cls) -> str:
        return jsii.sget(cls, "SECURITY_AUDIT")

    @jsii.python.classproperty
    @jsii.member(jsii_name="SERVER_MIGRATION_CONNECTOR")
    def SERVER_MIGRATION_CONNECTOR(cls) -> str:
        return jsii.sget(cls, "SERVER_MIGRATION_CONNECTOR")

    @jsii.python.classproperty
    @jsii.member(jsii_name="SERVER_MIGRATION_SERVICE_LAUNCH_ROLE")
    def SERVER_MIGRATION_SERVICE_LAUNCH_ROLE(cls) -> str:
        return jsii.sget(cls, "SERVER_MIGRATION_SERVICE_LAUNCH_ROLE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="SERVER_MIGRATION_SERVICE_ROLE")
    def SERVER_MIGRATION_SERVICE_ROLE(cls) -> str:
        return jsii.sget(cls, "SERVER_MIGRATION_SERVICE_ROLE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="SERVICE_QUOTAS_FULL_ACCESS")
    def SERVICE_QUOTAS_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "SERVICE_QUOTAS_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="SERVICE_QUOTAS_READ_ONLY_ACCESS")
    def SERVICE_QUOTAS_READ_ONLY_ACCESS(cls) -> str:
        return jsii.sget(cls, "SERVICE_QUOTAS_READ_ONLY_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="SERVICE_QUOTAS_SERVICE_ROLE_POLICY")
    def SERVICE_QUOTAS_SERVICE_ROLE_POLICY(cls) -> str:
        return jsii.sget(cls, "SERVICE_QUOTAS_SERVICE_ROLE_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="SIMPLE_WORKFLOW_FULL_ACCESS")
    def SIMPLE_WORKFLOW_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "SIMPLE_WORKFLOW_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="SUPPORT_USER")
    def SUPPORT_USER(cls) -> str:
        return jsii.sget(cls, "SUPPORT_USER")

    @jsii.python.classproperty
    @jsii.member(jsii_name="SYSTEM_ADMINISTRATOR")
    def SYSTEM_ADMINISTRATOR(cls) -> str:
        return jsii.sget(cls, "SYSTEM_ADMINISTRATOR")

    @jsii.python.classproperty
    @jsii.member(jsii_name="TAG_POLICIES_SERVICE_ROLE_POLICY")
    def TAG_POLICIES_SERVICE_ROLE_POLICY(cls) -> str:
        return jsii.sget(cls, "TAG_POLICIES_SERVICE_ROLE_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="TRANSLATE_FULL_ACCESS")
    def TRANSLATE_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "TRANSLATE_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="TRANSLATE_READ_ONLY")
    def TRANSLATE_READ_ONLY(cls) -> str:
        return jsii.sget(cls, "TRANSLATE_READ_ONLY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="VIEW_ONLY_ACCESS")
    def VIEW_ONLY_ACCESS(cls) -> str:
        return jsii.sget(cls, "VIEW_ONLY_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="VM_IMPORT_EXPORT_ROLE_FOR_AWS_CONNECTOR")
    def VM_IMPORT_EXPORT_ROLE_FOR_AWS_CONNECTOR(cls) -> str:
        return jsii.sget(cls, "VM_IMPORT_EXPORT_ROLE_FOR_AWS_CONNECTOR")

    @jsii.python.classproperty
    @jsii.member(jsii_name="WAF_LOGGING_SERVICE_ROLE_POLICY")
    def WAF_LOGGING_SERVICE_ROLE_POLICY(cls) -> str:
        return jsii.sget(cls, "WAF_LOGGING_SERVICE_ROLE_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="WAF_REGIONAL_LOGGING_SERVICE_ROLE_POLICY")
    def WAF_REGIONAL_LOGGING_SERVICE_ROLE_POLICY(cls) -> str:
        return jsii.sget(cls, "WAF_REGIONAL_LOGGING_SERVICE_ROLE_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="WAFV_2_LOGGING_SERVICE_ROLE_POLICY")
    def WAFV_2_LOGGING_SERVICE_ROLE_POLICY(cls) -> str:
        return jsii.sget(cls, "WAFV_2_LOGGING_SERVICE_ROLE_POLICY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="WELL_ARCHITECTED_CONSOLE_FULL_ACCESS")
    def WELL_ARCHITECTED_CONSOLE_FULL_ACCESS(cls) -> str:
        return jsii.sget(cls, "WELL_ARCHITECTED_CONSOLE_FULL_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="WELL_ARCHITECTED_CONSOLE_READ_ONLY_ACCESS")
    def WELL_ARCHITECTED_CONSOLE_READ_ONLY_ACCESS(cls) -> str:
        return jsii.sget(cls, "WELL_ARCHITECTED_CONSOLE_READ_ONLY_ACCESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="WORK_LINK_SERVICE_ROLE_POLICY")
    def WORK_LINK_SERVICE_ROLE_POLICY(cls) -> str:
        return jsii.sget(cls, "WORK_LINK_SERVICE_ROLE_POLICY")


class ServiceNames(metaclass=jsii.JSIIMeta, jsii_type="cdk-constants.ServiceNames"):
    def __init__(self) -> None:
        jsii.create(ServiceNames, self, [])

    @jsii.python.classproperty
    @jsii.member(jsii_name="ALEXA_FOR_BUSINESS")
    def ALEXA_FOR_BUSINESS(cls) -> str:
        return jsii.sget(cls, "ALEXA_FOR_BUSINESS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_API_GATEWAY")
    def AMAZON_API_GATEWAY(cls) -> str:
        return jsii.sget(cls, "AMAZON_API_GATEWAY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_APP_STREAM_2_0")
    def AMAZON_APP_STREAM_2_0(cls) -> str:
        return jsii.sget(cls, "AMAZON_APP_STREAM_2_0")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_ATHENA")
    def AMAZON_ATHENA(cls) -> str:
        return jsii.sget(cls, "AMAZON_ATHENA")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_CHIME")
    def AMAZON_CHIME(cls) -> str:
        return jsii.sget(cls, "AMAZON_CHIME")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_CLOUD_DIRECTORY")
    def AMAZON_CLOUD_DIRECTORY(cls) -> str:
        return jsii.sget(cls, "AMAZON_CLOUD_DIRECTORY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_CLOUD_FRONT")
    def AMAZON_CLOUD_FRONT(cls) -> str:
        return jsii.sget(cls, "AMAZON_CLOUD_FRONT")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_CLOUD_SEARCH")
    def AMAZON_CLOUD_SEARCH(cls) -> str:
        return jsii.sget(cls, "AMAZON_CLOUD_SEARCH")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_CLOUD_WATCH")
    def AMAZON_CLOUD_WATCH(cls) -> str:
        return jsii.sget(cls, "AMAZON_CLOUD_WATCH")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_CLOUD_WATCH_LOGS")
    def AMAZON_CLOUD_WATCH_LOGS(cls) -> str:
        return jsii.sget(cls, "AMAZON_CLOUD_WATCH_LOGS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_CLOUD_WATCH_SYNTHETICS")
    def AMAZON_CLOUD_WATCH_SYNTHETICS(cls) -> str:
        return jsii.sget(cls, "AMAZON_CLOUD_WATCH_SYNTHETICS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_COGNITO_IDENTITY")
    def AMAZON_COGNITO_IDENTITY(cls) -> str:
        return jsii.sget(cls, "AMAZON_COGNITO_IDENTITY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_COGNITO_SYNC")
    def AMAZON_COGNITO_SYNC(cls) -> str:
        return jsii.sget(cls, "AMAZON_COGNITO_SYNC")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_COGNITO_USER_POOLS")
    def AMAZON_COGNITO_USER_POOLS(cls) -> str:
        return jsii.sget(cls, "AMAZON_COGNITO_USER_POOLS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_COMPREHEND")
    def AMAZON_COMPREHEND(cls) -> str:
        return jsii.sget(cls, "AMAZON_COMPREHEND")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_CONNECT")
    def AMAZON_CONNECT(cls) -> str:
        return jsii.sget(cls, "AMAZON_CONNECT")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_DATA_LIFECYCLE_MANAGER")
    def AMAZON_DATA_LIFECYCLE_MANAGER(cls) -> str:
        return jsii.sget(cls, "AMAZON_DATA_LIFECYCLE_MANAGER")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_DETECTIVE")
    def AMAZON_DETECTIVE(cls) -> str:
        return jsii.sget(cls, "AMAZON_DETECTIVE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_DYNAMO_DB")
    def AMAZON_DYNAMO_DB(cls) -> str:
        return jsii.sget(cls, "AMAZON_DYNAMO_DB")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_DYNAMO_DB_ACCELERATOR_DAX")
    def AMAZON_DYNAMO_DB_ACCELERATOR_DAX(cls) -> str:
        return jsii.sget(cls, "AMAZON_DYNAMO_DB_ACCELERATOR_DAX")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_EC2")
    def AMAZON_E_C2(cls) -> str:
        return jsii.sget(cls, "AMAZON_EC2")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_EC2_AUTO_SCALING")
    def AMAZON_E_C2_AUTO_SCALING(cls) -> str:
        return jsii.sget(cls, "AMAZON_EC2_AUTO_SCALING")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_EC2_IMAGE_BUILDER")
    def AMAZON_E_C2_IMAGE_BUILDER(cls) -> str:
        return jsii.sget(cls, "AMAZON_EC2_IMAGE_BUILDER")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_EC2_INSTANCE_CONNECT")
    def AMAZON_E_C2_INSTANCE_CONNECT(cls) -> str:
        return jsii.sget(cls, "AMAZON_EC2_INSTANCE_CONNECT")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_ELASTI_CACHE")
    def AMAZON_ELASTI_CACHE(cls) -> str:
        return jsii.sget(cls, "AMAZON_ELASTI_CACHE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_ELASTIC_BLOCK_STORE")
    def AMAZON_ELASTIC_BLOCK_STORE(cls) -> str:
        return jsii.sget(cls, "AMAZON_ELASTIC_BLOCK_STORE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_ELASTIC_CONTAINER_REGISTRY")
    def AMAZON_ELASTIC_CONTAINER_REGISTRY(cls) -> str:
        return jsii.sget(cls, "AMAZON_ELASTIC_CONTAINER_REGISTRY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_ELASTIC_CONTAINER_SERVICE")
    def AMAZON_ELASTIC_CONTAINER_SERVICE(cls) -> str:
        return jsii.sget(cls, "AMAZON_ELASTIC_CONTAINER_SERVICE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_ELASTIC_CONTAINER_SERVICE_FOR_KUBERNETES")
    def AMAZON_ELASTIC_CONTAINER_SERVICE_FOR_KUBERNETES(cls) -> str:
        return jsii.sget(cls, "AMAZON_ELASTIC_CONTAINER_SERVICE_FOR_KUBERNETES")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_ELASTIC_FILE_SYSTEM")
    def AMAZON_ELASTIC_FILE_SYSTEM(cls) -> str:
        return jsii.sget(cls, "AMAZON_ELASTIC_FILE_SYSTEM")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_ELASTIC_INFERENCE")
    def AMAZON_ELASTIC_INFERENCE(cls) -> str:
        return jsii.sget(cls, "AMAZON_ELASTIC_INFERENCE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_ELASTIC_MAP_REDUCE")
    def AMAZON_ELASTIC_MAP_REDUCE(cls) -> str:
        return jsii.sget(cls, "AMAZON_ELASTIC_MAP_REDUCE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_ELASTIC_TRANSCODER")
    def AMAZON_ELASTIC_TRANSCODER(cls) -> str:
        return jsii.sget(cls, "AMAZON_ELASTIC_TRANSCODER")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_ELASTICSEARCH_SERVICE")
    def AMAZON_ELASTICSEARCH_SERVICE(cls) -> str:
        return jsii.sget(cls, "AMAZON_ELASTICSEARCH_SERVICE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_EVENT_BRIDGE")
    def AMAZON_EVENT_BRIDGE(cls) -> str:
        return jsii.sget(cls, "AMAZON_EVENT_BRIDGE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_EVENT_BRIDGE_SCHEMAS")
    def AMAZON_EVENT_BRIDGE_SCHEMAS(cls) -> str:
        return jsii.sget(cls, "AMAZON_EVENT_BRIDGE_SCHEMAS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_FORECAST")
    def AMAZON_FORECAST(cls) -> str:
        return jsii.sget(cls, "AMAZON_FORECAST")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_FRAUD_DETECTOR")
    def AMAZON_FRAUD_DETECTOR(cls) -> str:
        return jsii.sget(cls, "AMAZON_FRAUD_DETECTOR")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_FREE_RTOS")
    def AMAZON_FREE_RTOS(cls) -> str:
        return jsii.sget(cls, "AMAZON_FREE_RTOS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_FSX")
    def AMAZON_FSX(cls) -> str:
        return jsii.sget(cls, "AMAZON_FSX")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_GAME_LIFT")
    def AMAZON_GAME_LIFT(cls) -> str:
        return jsii.sget(cls, "AMAZON_GAME_LIFT")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_GLACIER")
    def AMAZON_GLACIER(cls) -> str:
        return jsii.sget(cls, "AMAZON_GLACIER")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_GROUND_TRUTH_LABELING")
    def AMAZON_GROUND_TRUTH_LABELING(cls) -> str:
        return jsii.sget(cls, "AMAZON_GROUND_TRUTH_LABELING")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_GUARD_DUTY")
    def AMAZON_GUARD_DUTY(cls) -> str:
        return jsii.sget(cls, "AMAZON_GUARD_DUTY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_INSPECTOR")
    def AMAZON_INSPECTOR(cls) -> str:
        return jsii.sget(cls, "AMAZON_INSPECTOR")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_KENDRA")
    def AMAZON_KENDRA(cls) -> str:
        return jsii.sget(cls, "AMAZON_KENDRA")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_KINESIS")
    def AMAZON_KINESIS(cls) -> str:
        return jsii.sget(cls, "AMAZON_KINESIS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_KINESIS_ANALYTICS")
    def AMAZON_KINESIS_ANALYTICS(cls) -> str:
        return jsii.sget(cls, "AMAZON_KINESIS_ANALYTICS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_KINESIS_ANALYTICS_V2")
    def AMAZON_KINESIS_ANALYTICS_V2(cls) -> str:
        return jsii.sget(cls, "AMAZON_KINESIS_ANALYTICS_V2")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_KINESIS_FIREHOSE")
    def AMAZON_KINESIS_FIREHOSE(cls) -> str:
        return jsii.sget(cls, "AMAZON_KINESIS_FIREHOSE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_KINESIS_VIDEO_STREAMS")
    def AMAZON_KINESIS_VIDEO_STREAMS(cls) -> str:
        return jsii.sget(cls, "AMAZON_KINESIS_VIDEO_STREAMS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_LEX")
    def AMAZON_LEX(cls) -> str:
        return jsii.sget(cls, "AMAZON_LEX")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_LIGHTSAIL")
    def AMAZON_LIGHTSAIL(cls) -> str:
        return jsii.sget(cls, "AMAZON_LIGHTSAIL")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_MACHINE_LEARNING")
    def AMAZON_MACHINE_LEARNING(cls) -> str:
        return jsii.sget(cls, "AMAZON_MACHINE_LEARNING")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_MACIE")
    def AMAZON_MACIE(cls) -> str:
        return jsii.sget(cls, "AMAZON_MACIE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_MANAGED_BLOCKCHAIN")
    def AMAZON_MANAGED_BLOCKCHAIN(cls) -> str:
        return jsii.sget(cls, "AMAZON_MANAGED_BLOCKCHAIN")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_MANAGED_STREAMING_FOR_KAFKA")
    def AMAZON_MANAGED_STREAMING_FOR_KAFKA(cls) -> str:
        return jsii.sget(cls, "AMAZON_MANAGED_STREAMING_FOR_KAFKA")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_MECHANICAL_TURK")
    def AMAZON_MECHANICAL_TURK(cls) -> str:
        return jsii.sget(cls, "AMAZON_MECHANICAL_TURK")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_MESSAGE_DELIVERY_SERVICE")
    def AMAZON_MESSAGE_DELIVERY_SERVICE(cls) -> str:
        return jsii.sget(cls, "AMAZON_MESSAGE_DELIVERY_SERVICE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_MOBILE_ANALYTICS")
    def AMAZON_MOBILE_ANALYTICS(cls) -> str:
        return jsii.sget(cls, "AMAZON_MOBILE_ANALYTICS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_MQ")
    def AMAZON_MQ(cls) -> str:
        return jsii.sget(cls, "AMAZON_MQ")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_NEPTUNE")
    def AMAZON_NEPTUNE(cls) -> str:
        return jsii.sget(cls, "AMAZON_NEPTUNE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_PERSONALIZE")
    def AMAZON_PERSONALIZE(cls) -> str:
        return jsii.sget(cls, "AMAZON_PERSONALIZE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_PINPOINT")
    def AMAZON_PINPOINT(cls) -> str:
        return jsii.sget(cls, "AMAZON_PINPOINT")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_PINPOINT_EMAIL_SERVICE")
    def AMAZON_PINPOINT_EMAIL_SERVICE(cls) -> str:
        return jsii.sget(cls, "AMAZON_PINPOINT_EMAIL_SERVICE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_PINPOINT_SMS_AND_VOICE_SERVICE")
    def AMAZON_PINPOINT_SMS_AND_VOICE_SERVICE(cls) -> str:
        return jsii.sget(cls, "AMAZON_PINPOINT_SMS_AND_VOICE_SERVICE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_POLLY")
    def AMAZON_POLLY(cls) -> str:
        return jsii.sget(cls, "AMAZON_POLLY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_QLDB")
    def AMAZON_QLDB(cls) -> str:
        return jsii.sget(cls, "AMAZON_QLDB")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_QUICK_SIGHT")
    def AMAZON_QUICK_SIGHT(cls) -> str:
        return jsii.sget(cls, "AMAZON_QUICK_SIGHT")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_RDS")
    def AMAZON_RDS(cls) -> str:
        return jsii.sget(cls, "AMAZON_RDS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_RDS_DATA_API")
    def AMAZON_RDS_DATA_API(cls) -> str:
        return jsii.sget(cls, "AMAZON_RDS_DATA_API")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_RDS_IAM_AUTHENTICATION")
    def AMAZON_RDS_IAM_AUTHENTICATION(cls) -> str:
        return jsii.sget(cls, "AMAZON_RDS_IAM_AUTHENTICATION")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_REDSHIFT")
    def AMAZON_REDSHIFT(cls) -> str:
        return jsii.sget(cls, "AMAZON_REDSHIFT")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_REKOGNITION")
    def AMAZON_REKOGNITION(cls) -> str:
        return jsii.sget(cls, "AMAZON_REKOGNITION")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_RESOURCE_GROUP_TAGGING_API")
    def AMAZON_RESOURCE_GROUP_TAGGING_API(cls) -> str:
        return jsii.sget(cls, "AMAZON_RESOURCE_GROUP_TAGGING_API")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_ROUTE_53")
    def AMAZON_ROUTE_53(cls) -> str:
        return jsii.sget(cls, "AMAZON_ROUTE_53")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_ROUTE_53_DOMAINS")
    def AMAZON_ROUTE_53_DOMAINS(cls) -> str:
        return jsii.sget(cls, "AMAZON_ROUTE_53_DOMAINS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_ROUTE_53_RESOLVER")
    def AMAZON_ROUTE_53_RESOLVER(cls) -> str:
        return jsii.sget(cls, "AMAZON_ROUTE_53_RESOLVER")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_S3")
    def AMAZON_S3(cls) -> str:
        return jsii.sget(cls, "AMAZON_S3")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_SAGE_MAKER")
    def AMAZON_SAGE_MAKER(cls) -> str:
        return jsii.sget(cls, "AMAZON_SAGE_MAKER")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_SES")
    def AMAZON_SES(cls) -> str:
        return jsii.sget(cls, "AMAZON_SES")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_SESSION_MANAGER_MESSAGE_GATEWAY_SERVICE")
    def AMAZON_SESSION_MANAGER_MESSAGE_GATEWAY_SERVICE(cls) -> str:
        return jsii.sget(cls, "AMAZON_SESSION_MANAGER_MESSAGE_GATEWAY_SERVICE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_SIMPLE_DB")
    def AMAZON_SIMPLE_DB(cls) -> str:
        return jsii.sget(cls, "AMAZON_SIMPLE_DB")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_SIMPLE_WORKFLOW_SERVICE")
    def AMAZON_SIMPLE_WORKFLOW_SERVICE(cls) -> str:
        return jsii.sget(cls, "AMAZON_SIMPLE_WORKFLOW_SERVICE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_SNS")
    def AMAZON_SNS(cls) -> str:
        return jsii.sget(cls, "AMAZON_SNS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_SQS")
    def AMAZON_SQS(cls) -> str:
        return jsii.sget(cls, "AMAZON_SQS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_STORAGE_GATEWAY")
    def AMAZON_STORAGE_GATEWAY(cls) -> str:
        return jsii.sget(cls, "AMAZON_STORAGE_GATEWAY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_SUMERIAN")
    def AMAZON_SUMERIAN(cls) -> str:
        return jsii.sget(cls, "AMAZON_SUMERIAN")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_TEXTRACT")
    def AMAZON_TEXTRACT(cls) -> str:
        return jsii.sget(cls, "AMAZON_TEXTRACT")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_TRANSCRIBE")
    def AMAZON_TRANSCRIBE(cls) -> str:
        return jsii.sget(cls, "AMAZON_TRANSCRIBE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_TRANSLATE")
    def AMAZON_TRANSLATE(cls) -> str:
        return jsii.sget(cls, "AMAZON_TRANSLATE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_WORK_DOCS")
    def AMAZON_WORK_DOCS(cls) -> str:
        return jsii.sget(cls, "AMAZON_WORK_DOCS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_WORK_LINK")
    def AMAZON_WORK_LINK(cls) -> str:
        return jsii.sget(cls, "AMAZON_WORK_LINK")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_WORK_MAIL")
    def AMAZON_WORK_MAIL(cls) -> str:
        return jsii.sget(cls, "AMAZON_WORK_MAIL")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_WORK_MAIL_MESSAGE_FLOW")
    def AMAZON_WORK_MAIL_MESSAGE_FLOW(cls) -> str:
        return jsii.sget(cls, "AMAZON_WORK_MAIL_MESSAGE_FLOW")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_WORK_SPACES")
    def AMAZON_WORK_SPACES(cls) -> str:
        return jsii.sget(cls, "AMAZON_WORK_SPACES")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_WORK_SPACES_APPLICATION_MANAGER")
    def AMAZON_WORK_SPACES_APPLICATION_MANAGER(cls) -> str:
        return jsii.sget(cls, "AMAZON_WORK_SPACES_APPLICATION_MANAGER")

    @jsii.python.classproperty
    @jsii.member(jsii_name="APPLICATION_AUTO_SCALING")
    def APPLICATION_AUTO_SCALING(cls) -> str:
        return jsii.sget(cls, "APPLICATION_AUTO_SCALING")

    @jsii.python.classproperty
    @jsii.member(jsii_name="APPLICATION_DISCOVERY")
    def APPLICATION_DISCOVERY(cls) -> str:
        return jsii.sget(cls, "APPLICATION_DISCOVERY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="APPLICATION_DISCOVERY_ARSENAL")
    def APPLICATION_DISCOVERY_ARSENAL(cls) -> str:
        return jsii.sget(cls, "APPLICATION_DISCOVERY_ARSENAL")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_ACCOUNTS")
    def AWS_ACCOUNTS(cls) -> str:
        return jsii.sget(cls, "AWS_ACCOUNTS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_AMPLIFY")
    def AWS_AMPLIFY(cls) -> str:
        return jsii.sget(cls, "AWS_AMPLIFY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_APP_MESH")
    def AWS_APP_MESH(cls) -> str:
        return jsii.sget(cls, "AWS_APP_MESH")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_APP_MESH_PREVIEW")
    def AWS_APP_MESH_PREVIEW(cls) -> str:
        return jsii.sget(cls, "AWS_APP_MESH_PREVIEW")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_APP_SYNC")
    def AWS_APP_SYNC(cls) -> str:
        return jsii.sget(cls, "AWS_APP_SYNC")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_ARTIFACT")
    def AWS_ARTIFACT(cls) -> str:
        return jsii.sget(cls, "AWS_ARTIFACT")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_AUTO_SCALING")
    def AWS_AUTO_SCALING(cls) -> str:
        return jsii.sget(cls, "AWS_AUTO_SCALING")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_BACKUP")
    def AWS_BACKUP(cls) -> str:
        return jsii.sget(cls, "AWS_BACKUP")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_BACKUP_STORAGE")
    def AWS_BACKUP_STORAGE(cls) -> str:
        return jsii.sget(cls, "AWS_BACKUP_STORAGE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_BATCH")
    def AWS_BATCH(cls) -> str:
        return jsii.sget(cls, "AWS_BATCH")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_BILLING")
    def AWS_BILLING(cls) -> str:
        return jsii.sget(cls, "AWS_BILLING")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_BUDGET_SERVICE")
    def AWS_BUDGET_SERVICE(cls) -> str:
        return jsii.sget(cls, "AWS_BUDGET_SERVICE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CERTIFICATE_MANAGER")
    def AWS_CERTIFICATE_MANAGER(cls) -> str:
        return jsii.sget(cls, "AWS_CERTIFICATE_MANAGER")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CERTIFICATE_MANAGER_PRIVATE_CERTIFICATE_AUTHORITY")
    def AWS_CERTIFICATE_MANAGER_PRIVATE_CERTIFICATE_AUTHORITY(cls) -> str:
        return jsii.sget(cls, "AWS_CERTIFICATE_MANAGER_PRIVATE_CERTIFICATE_AUTHORITY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CHATBOT")
    def AWS_CHATBOT(cls) -> str:
        return jsii.sget(cls, "AWS_CHATBOT")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CLOUD_9")
    def AWS_CLOUD_9(cls) -> str:
        return jsii.sget(cls, "AWS_CLOUD_9")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CLOUD_FORMATION")
    def AWS_CLOUD_FORMATION(cls) -> str:
        return jsii.sget(cls, "AWS_CLOUD_FORMATION")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CLOUD_HSM")
    def AWS_CLOUD_HSM(cls) -> str:
        return jsii.sget(cls, "AWS_CLOUD_HSM")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CLOUD_MAP")
    def AWS_CLOUD_MAP(cls) -> str:
        return jsii.sget(cls, "AWS_CLOUD_MAP")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CLOUD_TRAIL")
    def AWS_CLOUD_TRAIL(cls) -> str:
        return jsii.sget(cls, "AWS_CLOUD_TRAIL")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CODE_BUILD")
    def AWS_CODE_BUILD(cls) -> str:
        return jsii.sget(cls, "AWS_CODE_BUILD")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CODE_COMMIT")
    def AWS_CODE_COMMIT(cls) -> str:
        return jsii.sget(cls, "AWS_CODE_COMMIT")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CODE_DEPLOY")
    def AWS_CODE_DEPLOY(cls) -> str:
        return jsii.sget(cls, "AWS_CODE_DEPLOY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CODE_PIPELINE")
    def AWS_CODE_PIPELINE(cls) -> str:
        return jsii.sget(cls, "AWS_CODE_PIPELINE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CODE_SIGNING_FOR_AMAZON_FREE_RTOS")
    def AWS_CODE_SIGNING_FOR_AMAZON_FREE_RTOS(cls) -> str:
        return jsii.sget(cls, "AWS_CODE_SIGNING_FOR_AMAZON_FREE_RTOS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CODE_STAR")
    def AWS_CODE_STAR(cls) -> str:
        return jsii.sget(cls, "AWS_CODE_STAR")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CODE_STAR_NOTIFICATIONS")
    def AWS_CODE_STAR_NOTIFICATIONS(cls) -> str:
        return jsii.sget(cls, "AWS_CODE_STAR_NOTIFICATIONS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_CONFIG")
    def AWS_CONFIG(cls) -> str:
        return jsii.sget(cls, "AWS_CONFIG")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_COST_AND_USAGE_REPORT")
    def AWS_COST_AND_USAGE_REPORT(cls) -> str:
        return jsii.sget(cls, "AWS_COST_AND_USAGE_REPORT")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_COST_EXPLORER_SERVICE")
    def AWS_COST_EXPLORER_SERVICE(cls) -> str:
        return jsii.sget(cls, "AWS_COST_EXPLORER_SERVICE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_DATA_EXCHANGE")
    def AWS_DATA_EXCHANGE(cls) -> str:
        return jsii.sget(cls, "AWS_DATA_EXCHANGE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_DATABASE_MIGRATION_SERVICE")
    def AWS_DATABASE_MIGRATION_SERVICE(cls) -> str:
        return jsii.sget(cls, "AWS_DATABASE_MIGRATION_SERVICE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_DEEP_LENS")
    def AWS_DEEP_LENS(cls) -> str:
        return jsii.sget(cls, "AWS_DEEP_LENS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_DEEP_RACER")
    def AWS_DEEP_RACER(cls) -> str:
        return jsii.sget(cls, "AWS_DEEP_RACER")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_DEVICE_FARM")
    def AWS_DEVICE_FARM(cls) -> str:
        return jsii.sget(cls, "AWS_DEVICE_FARM")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_DIRECT_CONNECT")
    def AWS_DIRECT_CONNECT(cls) -> str:
        return jsii.sget(cls, "AWS_DIRECT_CONNECT")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_DIRECTORY_SERVICE")
    def AWS_DIRECTORY_SERVICE(cls) -> str:
        return jsii.sget(cls, "AWS_DIRECTORY_SERVICE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_ELASTIC_BEANSTALK")
    def AWS_ELASTIC_BEANSTALK(cls) -> str:
        return jsii.sget(cls, "AWS_ELASTIC_BEANSTALK")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_ELEMENTAL_MEDIA_CONNECT")
    def AWS_ELEMENTAL_MEDIA_CONNECT(cls) -> str:
        return jsii.sget(cls, "AWS_ELEMENTAL_MEDIA_CONNECT")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_ELEMENTAL_MEDIA_CONVERT")
    def AWS_ELEMENTAL_MEDIA_CONVERT(cls) -> str:
        return jsii.sget(cls, "AWS_ELEMENTAL_MEDIA_CONVERT")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_ELEMENTAL_MEDIA_LIVE")
    def AWS_ELEMENTAL_MEDIA_LIVE(cls) -> str:
        return jsii.sget(cls, "AWS_ELEMENTAL_MEDIA_LIVE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_ELEMENTAL_MEDIA_PACKAGE")
    def AWS_ELEMENTAL_MEDIA_PACKAGE(cls) -> str:
        return jsii.sget(cls, "AWS_ELEMENTAL_MEDIA_PACKAGE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_ELEMENTAL_MEDIA_PACKAGE_VOD")
    def AWS_ELEMENTAL_MEDIA_PACKAGE_VOD(cls) -> str:
        return jsii.sget(cls, "AWS_ELEMENTAL_MEDIA_PACKAGE_VOD")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_ELEMENTAL_MEDIA_STORE")
    def AWS_ELEMENTAL_MEDIA_STORE(cls) -> str:
        return jsii.sget(cls, "AWS_ELEMENTAL_MEDIA_STORE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_ELEMENTAL_MEDIA_TAILOR")
    def AWS_ELEMENTAL_MEDIA_TAILOR(cls) -> str:
        return jsii.sget(cls, "AWS_ELEMENTAL_MEDIA_TAILOR")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_FIREWALL_MANAGER")
    def AWS_FIREWALL_MANAGER(cls) -> str:
        return jsii.sget(cls, "AWS_FIREWALL_MANAGER")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_GLOBAL_ACCELERATOR")
    def AWS_GLOBAL_ACCELERATOR(cls) -> str:
        return jsii.sget(cls, "AWS_GLOBAL_ACCELERATOR")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_GLUE")
    def AWS_GLUE(cls) -> str:
        return jsii.sget(cls, "AWS_GLUE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_GROUND_STATION")
    def AWS_GROUND_STATION(cls) -> str:
        return jsii.sget(cls, "AWS_GROUND_STATION")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_HEALTH_APIS_AND_NOTIFICATIONS")
    def AWS_HEALTH_APIS_AND_NOTIFICATIONS(cls) -> str:
        return jsii.sget(cls, "AWS_HEALTH_APIS_AND_NOTIFICATIONS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_IMPORT_EXPORT_DISK_SERVICE")
    def AWS_IMPORT_EXPORT_DISK_SERVICE(cls) -> str:
        return jsii.sget(cls, "AWS_IMPORT_EXPORT_DISK_SERVICE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_IOT")
    def AWS_IOT(cls) -> str:
        return jsii.sget(cls, "AWS_IOT")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_IOT_1_CLICK")
    def AWS_IOT_1_CLICK(cls) -> str:
        return jsii.sget(cls, "AWS_IOT_1_CLICK")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_IOT_ANALYTICS")
    def AWS_IOT_ANALYTICS(cls) -> str:
        return jsii.sget(cls, "AWS_IOT_ANALYTICS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_IOT_EVENTS")
    def AWS_IOT_EVENTS(cls) -> str:
        return jsii.sget(cls, "AWS_IOT_EVENTS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_IOT_GREENGRASS")
    def AWS_IOT_GREENGRASS(cls) -> str:
        return jsii.sget(cls, "AWS_IOT_GREENGRASS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_IOT_SITE_WISE")
    def AWS_IOT_SITE_WISE(cls) -> str:
        return jsii.sget(cls, "AWS_IOT_SITE_WISE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_IOT_THINGS_GRAPH")
    def AWS_IOT_THINGS_GRAPH(cls) -> str:
        return jsii.sget(cls, "AWS_IOT_THINGS_GRAPH")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_IQ")
    def AWS_IQ(cls) -> str:
        return jsii.sget(cls, "AWS_IQ")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_IQ_PERMISSIONS")
    def AWS_IQ_PERMISSIONS(cls) -> str:
        return jsii.sget(cls, "AWS_IQ_PERMISSIONS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_KEY_MANAGEMENT_SERVICE")
    def AWS_KEY_MANAGEMENT_SERVICE(cls) -> str:
        return jsii.sget(cls, "AWS_KEY_MANAGEMENT_SERVICE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_LAKE_FORMATION")
    def AWS_LAKE_FORMATION(cls) -> str:
        return jsii.sget(cls, "AWS_LAKE_FORMATION")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_LAMBDA")
    def AWS_LAMBDA(cls) -> str:
        return jsii.sget(cls, "AWS_LAMBDA")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_LICENSE_MANAGER")
    def AWS_LICENSE_MANAGER(cls) -> str:
        return jsii.sget(cls, "AWS_LICENSE_MANAGER")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_MANAGED_APACHE_CASSANDRA_SERVICE")
    def AWS_MANAGED_APACHE_CASSANDRA_SERVICE(cls) -> str:
        return jsii.sget(cls, "AWS_MANAGED_APACHE_CASSANDRA_SERVICE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_MARKETPLACE")
    def AWS_MARKETPLACE(cls) -> str:
        return jsii.sget(cls, "AWS_MARKETPLACE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_MARKETPLACE_CATALOG")
    def AWS_MARKETPLACE_CATALOG(cls) -> str:
        return jsii.sget(cls, "AWS_MARKETPLACE_CATALOG")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_MARKETPLACE_ENTITLEMENT_SERVICE")
    def AWS_MARKETPLACE_ENTITLEMENT_SERVICE(cls) -> str:
        return jsii.sget(cls, "AWS_MARKETPLACE_ENTITLEMENT_SERVICE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_MARKETPLACE_IMAGE_BUILDING_SERVICE")
    def AWS_MARKETPLACE_IMAGE_BUILDING_SERVICE(cls) -> str:
        return jsii.sget(cls, "AWS_MARKETPLACE_IMAGE_BUILDING_SERVICE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_MARKETPLACE_MANAGEMENT_PORTAL")
    def AWS_MARKETPLACE_MANAGEMENT_PORTAL(cls) -> str:
        return jsii.sget(cls, "AWS_MARKETPLACE_MANAGEMENT_PORTAL")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_MARKETPLACE_METERING_SERVICE")
    def AWS_MARKETPLACE_METERING_SERVICE(cls) -> str:
        return jsii.sget(cls, "AWS_MARKETPLACE_METERING_SERVICE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_MARKETPLACE_PROCUREMENT_SYSTEMS_INTEGRATION")
    def AWS_MARKETPLACE_PROCUREMENT_SYSTEMS_INTEGRATION(cls) -> str:
        return jsii.sget(cls, "AWS_MARKETPLACE_PROCUREMENT_SYSTEMS_INTEGRATION")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_MIGRATION_HUB")
    def AWS_MIGRATION_HUB(cls) -> str:
        return jsii.sget(cls, "AWS_MIGRATION_HUB")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_MOBILE_HUB")
    def AWS_MOBILE_HUB(cls) -> str:
        return jsii.sget(cls, "AWS_MOBILE_HUB")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_OPS_WORKS")
    def AWS_OPS_WORKS(cls) -> str:
        return jsii.sget(cls, "AWS_OPS_WORKS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_OPS_WORKS_CONFIGURATION_MANAGEMENT")
    def AWS_OPS_WORKS_CONFIGURATION_MANAGEMENT(cls) -> str:
        return jsii.sget(cls, "AWS_OPS_WORKS_CONFIGURATION_MANAGEMENT")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_ORGANIZATIONS")
    def AWS_ORGANIZATIONS(cls) -> str:
        return jsii.sget(cls, "AWS_ORGANIZATIONS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_OUTPOSTS")
    def AWS_OUTPOSTS(cls) -> str:
        return jsii.sget(cls, "AWS_OUTPOSTS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_PERFORMANCE_INSIGHTS")
    def AWS_PERFORMANCE_INSIGHTS(cls) -> str:
        return jsii.sget(cls, "AWS_PERFORMANCE_INSIGHTS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_PRICE_LIST")
    def AWS_PRICE_LIST(cls) -> str:
        return jsii.sget(cls, "AWS_PRICE_LIST")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_PRIVATE_MARKETPLACE")
    def AWS_PRIVATE_MARKETPLACE(cls) -> str:
        return jsii.sget(cls, "AWS_PRIVATE_MARKETPLACE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_RESOURCE_ACCESS_MANAGER")
    def AWS_RESOURCE_ACCESS_MANAGER(cls) -> str:
        return jsii.sget(cls, "AWS_RESOURCE_ACCESS_MANAGER")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_RESOURCE_GROUPS")
    def AWS_RESOURCE_GROUPS(cls) -> str:
        return jsii.sget(cls, "AWS_RESOURCE_GROUPS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_ROBO_MAKER")
    def AWS_ROBO_MAKER(cls) -> str:
        return jsii.sget(cls, "AWS_ROBO_MAKER")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_SAVINGS_PLANS")
    def AWS_SAVINGS_PLANS(cls) -> str:
        return jsii.sget(cls, "AWS_SAVINGS_PLANS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_SECRETS_MANAGER")
    def AWS_SECRETS_MANAGER(cls) -> str:
        return jsii.sget(cls, "AWS_SECRETS_MANAGER")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_SECURITY_HUB")
    def AWS_SECURITY_HUB(cls) -> str:
        return jsii.sget(cls, "AWS_SECURITY_HUB")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_SECURITY_TOKEN_SERVICE")
    def AWS_SECURITY_TOKEN_SERVICE(cls) -> str:
        return jsii.sget(cls, "AWS_SECURITY_TOKEN_SERVICE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_SERVER_MIGRATION_SERVICE")
    def AWS_SERVER_MIGRATION_SERVICE(cls) -> str:
        return jsii.sget(cls, "AWS_SERVER_MIGRATION_SERVICE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_SERVERLESS_APPLICATION_REPOSITORY")
    def AWS_SERVERLESS_APPLICATION_REPOSITORY(cls) -> str:
        return jsii.sget(cls, "AWS_SERVERLESS_APPLICATION_REPOSITORY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_SERVICE_CATALOG")
    def AWS_SERVICE_CATALOG(cls) -> str:
        return jsii.sget(cls, "AWS_SERVICE_CATALOG")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_SHIELD")
    def AWS_SHIELD(cls) -> str:
        return jsii.sget(cls, "AWS_SHIELD")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_SNOWBALL")
    def AWS_SNOWBALL(cls) -> str:
        return jsii.sget(cls, "AWS_SNOWBALL")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_SSO")
    def AWS_SSO(cls) -> str:
        return jsii.sget(cls, "AWS_SSO")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_SSO_DIRECTORY")
    def AWS_SSO_DIRECTORY(cls) -> str:
        return jsii.sget(cls, "AWS_SSO_DIRECTORY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_STEP_FUNCTIONS")
    def AWS_STEP_FUNCTIONS(cls) -> str:
        return jsii.sget(cls, "AWS_STEP_FUNCTIONS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_SUPPORT")
    def AWS_SUPPORT(cls) -> str:
        return jsii.sget(cls, "AWS_SUPPORT")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_SYSTEMS_MANAGER")
    def AWS_SYSTEMS_MANAGER(cls) -> str:
        return jsii.sget(cls, "AWS_SYSTEMS_MANAGER")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_TRANSFER_FOR_SFTP")
    def AWS_TRANSFER_FOR_SFTP(cls) -> str:
        return jsii.sget(cls, "AWS_TRANSFER_FOR_SFTP")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_TRUSTED_ADVISOR")
    def AWS_TRUSTED_ADVISOR(cls) -> str:
        return jsii.sget(cls, "AWS_TRUSTED_ADVISOR")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_WAF")
    def AWS_WAF(cls) -> str:
        return jsii.sget(cls, "AWS_WAF")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_WAF_REGIONAL")
    def AWS_WAF_REGIONAL(cls) -> str:
        return jsii.sget(cls, "AWS_WAF_REGIONAL")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_WAF_V2")
    def AWS_WAF_V2(cls) -> str:
        return jsii.sget(cls, "AWS_WAF_V2")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_WELL_ARCHITECTED_TOOL")
    def AWS_WELL_ARCHITECTED_TOOL(cls) -> str:
        return jsii.sget(cls, "AWS_WELL_ARCHITECTED_TOOL")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_X_RAY")
    def AWS_X_RAY(cls) -> str:
        return jsii.sget(cls, "AWS_X_RAY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUD_WATCH_APPLICATION_INSIGHTS")
    def CLOUD_WATCH_APPLICATION_INSIGHTS(cls) -> str:
        return jsii.sget(cls, "CLOUD_WATCH_APPLICATION_INSIGHTS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="COMPREHEND_MEDICAL")
    def COMPREHEND_MEDICAL(cls) -> str:
        return jsii.sget(cls, "COMPREHEND_MEDICAL")

    @jsii.python.classproperty
    @jsii.member(jsii_name="COMPUTE_OPTIMIZER")
    def COMPUTE_OPTIMIZER(cls) -> str:
        return jsii.sget(cls, "COMPUTE_OPTIMIZER")

    @jsii.python.classproperty
    @jsii.member(jsii_name="DATA_PIPELINE")
    def DATA_PIPELINE(cls) -> str:
        return jsii.sget(cls, "DATA_PIPELINE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="DATA_SYNC")
    def DATA_SYNC(cls) -> str:
        return jsii.sget(cls, "DATA_SYNC")

    @jsii.python.classproperty
    @jsii.member(jsii_name="DATABASE_QUERY_METADATA_SERVICE")
    def DATABASE_QUERY_METADATA_SERVICE(cls) -> str:
        return jsii.sget(cls, "DATABASE_QUERY_METADATA_SERVICE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="ELASTIC_LOAD_BALANCING")
    def ELASTIC_LOAD_BALANCING(cls) -> str:
        return jsii.sget(cls, "ELASTIC_LOAD_BALANCING")

    @jsii.python.classproperty
    @jsii.member(jsii_name="ELASTIC_LOAD_BALANCING_V2")
    def ELASTIC_LOAD_BALANCING_V2(cls) -> str:
        return jsii.sget(cls, "ELASTIC_LOAD_BALANCING_V2")

    @jsii.python.classproperty
    @jsii.member(jsii_name="IAM_ACCESS_ANALYZER")
    def IAM_ACCESS_ANALYZER(cls) -> str:
        return jsii.sget(cls, "IAM_ACCESS_ANALYZER")

    @jsii.python.classproperty
    @jsii.member(jsii_name="IDENTITY_AND_ACCESS_MANAGEMENT")
    def IDENTITY_AND_ACCESS_MANAGEMENT(cls) -> str:
        return jsii.sget(cls, "IDENTITY_AND_ACCESS_MANAGEMENT")

    @jsii.python.classproperty
    @jsii.member(jsii_name="LAUNCH_WIZARD")
    def LAUNCH_WIZARD(cls) -> str:
        return jsii.sget(cls, "LAUNCH_WIZARD")

    @jsii.python.classproperty
    @jsii.member(jsii_name="MANAGE_AMAZON_API_GATEWAY")
    def MANAGE_AMAZON_API_GATEWAY(cls) -> str:
        return jsii.sget(cls, "MANAGE_AMAZON_API_GATEWAY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="NETWORK_MANAGER")
    def NETWORK_MANAGER(cls) -> str:
        return jsii.sget(cls, "NETWORK_MANAGER")

    @jsii.python.classproperty
    @jsii.member(jsii_name="SERVICE_QUOTAS")
    def SERVICE_QUOTAS(cls) -> str:
        return jsii.sget(cls, "SERVICE_QUOTAS")


class ServicePrincipals(metaclass=jsii.JSIIMeta, jsii_type="cdk-constants.ServicePrincipals"):
    def __init__(self) -> None:
        jsii.create(ServicePrincipals, self, [])

    @jsii.python.classproperty
    @jsii.member(jsii_name="ACM")
    def ACM(cls) -> str:
        return jsii.sget(cls, "ACM")

    @jsii.python.classproperty
    @jsii.member(jsii_name="ALEXA_APPKIT")
    def ALEXA_APPKIT(cls) -> str:
        return jsii.sget(cls, "ALEXA_APPKIT")

    @jsii.python.classproperty
    @jsii.member(jsii_name="API_GATEWAY")
    def API_GATEWAY(cls) -> str:
        return jsii.sget(cls, "API_GATEWAY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="APP_STREAM")
    def APP_STREAM(cls) -> str:
        return jsii.sget(cls, "APP_STREAM")

    @jsii.python.classproperty
    @jsii.member(jsii_name="APP_SYNC")
    def APP_SYNC(cls) -> str:
        return jsii.sget(cls, "APP_SYNC")

    @jsii.python.classproperty
    @jsii.member(jsii_name="APPLICATION_AUTOSCALING")
    def APPLICATION_AUTOSCALING(cls) -> str:
        return jsii.sget(cls, "APPLICATION_AUTOSCALING")

    @jsii.python.classproperty
    @jsii.member(jsii_name="ATHENA")
    def ATHENA(cls) -> str:
        return jsii.sget(cls, "ATHENA")

    @jsii.python.classproperty
    @jsii.member(jsii_name="AUTO_SCALING")
    def AUTO_SCALING(cls) -> str:
        return jsii.sget(cls, "AUTO_SCALING")

    @jsii.python.classproperty
    @jsii.member(jsii_name="BATCH")
    def BATCH(cls) -> str:
        return jsii.sget(cls, "BATCH")

    @jsii.python.classproperty
    @jsii.member(jsii_name="CHANNELS")
    def CHANNELS(cls) -> str:
        return jsii.sget(cls, "CHANNELS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUD_9")
    def CLOUD_9(cls) -> str:
        return jsii.sget(cls, "CLOUD_9")

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUD_DIRECTORY")
    def CLOUD_DIRECTORY(cls) -> str:
        return jsii.sget(cls, "CLOUD_DIRECTORY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUD_FORMATION")
    def CLOUD_FORMATION(cls) -> str:
        return jsii.sget(cls, "CLOUD_FORMATION")

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUD_FRONT")
    def CLOUD_FRONT(cls) -> str:
        return jsii.sget(cls, "CLOUD_FRONT")

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUD_SEARCH")
    def CLOUD_SEARCH(cls) -> str:
        return jsii.sget(cls, "CLOUD_SEARCH")

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUD_TRAIL")
    def CLOUD_TRAIL(cls) -> str:
        return jsii.sget(cls, "CLOUD_TRAIL")

    @jsii.python.classproperty
    @jsii.member(jsii_name="CODE_BUILD")
    def CODE_BUILD(cls) -> str:
        return jsii.sget(cls, "CODE_BUILD")

    @jsii.python.classproperty
    @jsii.member(jsii_name="CODE_COMMIT")
    def CODE_COMMIT(cls) -> str:
        return jsii.sget(cls, "CODE_COMMIT")

    @jsii.python.classproperty
    @jsii.member(jsii_name="CODE_DEPLOY")
    def CODE_DEPLOY(cls) -> str:
        return jsii.sget(cls, "CODE_DEPLOY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="CODE_PIPELINE")
    def CODE_PIPELINE(cls) -> str:
        return jsii.sget(cls, "CODE_PIPELINE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="CONFIG")
    def CONFIG(cls) -> str:
        return jsii.sget(cls, "CONFIG")

    @jsii.python.classproperty
    @jsii.member(jsii_name="CONTINUOUS_EXPORT")
    def CONTINUOUS_EXPORT(cls) -> str:
        return jsii.sget(cls, "CONTINUOUS_EXPORT")

    @jsii.python.classproperty
    @jsii.member(jsii_name="CUSTOM_RESOURCE")
    def CUSTOM_RESOURCE(cls) -> str:
        return jsii.sget(cls, "CUSTOM_RESOURCE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="DATA_PIPELINE")
    def DATA_PIPELINE(cls) -> str:
        return jsii.sget(cls, "DATA_PIPELINE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="DAX")
    def DAX(cls) -> str:
        return jsii.sget(cls, "DAX")

    @jsii.python.classproperty
    @jsii.member(jsii_name="DEEP_LENS")
    def DEEP_LENS(cls) -> str:
        return jsii.sget(cls, "DEEP_LENS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="DIRECT_CONNECT")
    def DIRECT_CONNECT(cls) -> str:
        return jsii.sget(cls, "DIRECT_CONNECT")

    @jsii.python.classproperty
    @jsii.member(jsii_name="DLM")
    def DLM(cls) -> str:
        return jsii.sget(cls, "DLM")

    @jsii.python.classproperty
    @jsii.member(jsii_name="DMS")
    def DMS(cls) -> str:
        return jsii.sget(cls, "DMS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="DS")
    def DS(cls) -> str:
        return jsii.sget(cls, "DS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="DYNAMO_DB")
    def DYNAMO_DB(cls) -> str:
        return jsii.sget(cls, "DYNAMO_DB")

    @jsii.python.classproperty
    @jsii.member(jsii_name="EC2")
    def E_C2(cls) -> str:
        return jsii.sget(cls, "EC2")

    @jsii.python.classproperty
    @jsii.member(jsii_name="EC2_FLEET")
    def E_C2_FLEET(cls) -> str:
        return jsii.sget(cls, "EC2_FLEET")

    @jsii.python.classproperty
    @jsii.member(jsii_name="EC2_SCHEDULED")
    def E_C2_SCHEDULED(cls) -> str:
        return jsii.sget(cls, "EC2_SCHEDULED")

    @jsii.python.classproperty
    @jsii.member(jsii_name="ECR")
    def ECR(cls) -> str:
        return jsii.sget(cls, "ECR")

    @jsii.python.classproperty
    @jsii.member(jsii_name="ECS")
    def ECS(cls) -> str:
        return jsii.sget(cls, "ECS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="ECS_TASKS")
    def ECS_TASKS(cls) -> str:
        return jsii.sget(cls, "ECS_TASKS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="EDGE_LAMBDA")
    def EDGE_LAMBDA(cls) -> str:
        return jsii.sget(cls, "EDGE_LAMBDA")

    @jsii.python.classproperty
    @jsii.member(jsii_name="EKS")
    def EKS(cls) -> str:
        return jsii.sget(cls, "EKS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="ELASTI_CACHE")
    def ELASTI_CACHE(cls) -> str:
        return jsii.sget(cls, "ELASTI_CACHE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="ELASTIC_BEANSTALK")
    def ELASTIC_BEANSTALK(cls) -> str:
        return jsii.sget(cls, "ELASTIC_BEANSTALK")

    @jsii.python.classproperty
    @jsii.member(jsii_name="ELASTIC_FILE_SYSTEM")
    def ELASTIC_FILE_SYSTEM(cls) -> str:
        return jsii.sget(cls, "ELASTIC_FILE_SYSTEM")

    @jsii.python.classproperty
    @jsii.member(jsii_name="ELASTIC_LOAD_BALANCING")
    def ELASTIC_LOAD_BALANCING(cls) -> str:
        return jsii.sget(cls, "ELASTIC_LOAD_BALANCING")

    @jsii.python.classproperty
    @jsii.member(jsii_name="ELASTIC_MAP_REDUCE")
    def ELASTIC_MAP_REDUCE(cls) -> str:
        return jsii.sget(cls, "ELASTIC_MAP_REDUCE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="ELASTIC_TRANSCODER")
    def ELASTIC_TRANSCODER(cls) -> str:
        return jsii.sget(cls, "ELASTIC_TRANSCODER")

    @jsii.python.classproperty
    @jsii.member(jsii_name="ES")
    def ES(cls) -> str:
        return jsii.sget(cls, "ES")

    @jsii.python.classproperty
    @jsii.member(jsii_name="EVENTS")
    def EVENTS(cls) -> str:
        return jsii.sget(cls, "EVENTS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="FIREHOSE")
    def FIREHOSE(cls) -> str:
        return jsii.sget(cls, "FIREHOSE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="GLUE")
    def GLUE(cls) -> str:
        return jsii.sget(cls, "GLUE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="GREENGRASS")
    def GREENGRASS(cls) -> str:
        return jsii.sget(cls, "GREENGRASS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="GUARDDUTY")
    def GUARDDUTY(cls) -> str:
        return jsii.sget(cls, "GUARDDUTY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="HEALTH")
    def HEALTH(cls) -> str:
        return jsii.sget(cls, "HEALTH")

    @jsii.python.classproperty
    @jsii.member(jsii_name="IAM")
    def IAM(cls) -> str:
        return jsii.sget(cls, "IAM")

    @jsii.python.classproperty
    @jsii.member(jsii_name="INSPECTOR")
    def INSPECTOR(cls) -> str:
        return jsii.sget(cls, "INSPECTOR")

    @jsii.python.classproperty
    @jsii.member(jsii_name="IOT")
    def IOT(cls) -> str:
        return jsii.sget(cls, "IOT")

    @jsii.python.classproperty
    @jsii.member(jsii_name="KINESIS")
    def KINESIS(cls) -> str:
        return jsii.sget(cls, "KINESIS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="KINESIS_ANALYTICS")
    def KINESIS_ANALYTICS(cls) -> str:
        return jsii.sget(cls, "KINESIS_ANALYTICS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="KMS")
    def KMS(cls) -> str:
        return jsii.sget(cls, "KMS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="LAMBDA")
    def LAMBDA_(cls) -> str:
        return jsii.sget(cls, "LAMBDA")

    @jsii.python.classproperty
    @jsii.member(jsii_name="LEX")
    def LEX(cls) -> str:
        return jsii.sget(cls, "LEX")

    @jsii.python.classproperty
    @jsii.member(jsii_name="LIGHTSAIL")
    def LIGHTSAIL(cls) -> str:
        return jsii.sget(cls, "LIGHTSAIL")

    @jsii.python.classproperty
    @jsii.member(jsii_name="LOGS")
    def LOGS(cls) -> str:
        return jsii.sget(cls, "LOGS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="MACHINE_LEARNING")
    def MACHINE_LEARNING(cls) -> str:
        return jsii.sget(cls, "MACHINE_LEARNING")

    @jsii.python.classproperty
    @jsii.member(jsii_name="MACIE")
    def MACIE(cls) -> str:
        return jsii.sget(cls, "MACIE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="MEDIA_CONVERT")
    def MEDIA_CONVERT(cls) -> str:
        return jsii.sget(cls, "MEDIA_CONVERT")

    @jsii.python.classproperty
    @jsii.member(jsii_name="MONITORING")
    def MONITORING(cls) -> str:
        return jsii.sget(cls, "MONITORING")

    @jsii.python.classproperty
    @jsii.member(jsii_name="OPS_WORKS")
    def OPS_WORKS(cls) -> str:
        return jsii.sget(cls, "OPS_WORKS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="ORGANIZATIONS")
    def ORGANIZATIONS(cls) -> str:
        return jsii.sget(cls, "ORGANIZATIONS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="RDS")
    def RDS(cls) -> str:
        return jsii.sget(cls, "RDS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="REDSHIFT")
    def REDSHIFT(cls) -> str:
        return jsii.sget(cls, "REDSHIFT")

    @jsii.python.classproperty
    @jsii.member(jsii_name="REKOGNITION")
    def REKOGNITION(cls) -> str:
        return jsii.sget(cls, "REKOGNITION")

    @jsii.python.classproperty
    @jsii.member(jsii_name="REPLICATION")
    def REPLICATION(cls) -> str:
        return jsii.sget(cls, "REPLICATION")

    @jsii.python.classproperty
    @jsii.member(jsii_name="ROUTE_53")
    def ROUTE_53(cls) -> str:
        return jsii.sget(cls, "ROUTE_53")

    @jsii.python.classproperty
    @jsii.member(jsii_name="S3")
    def S3(cls) -> str:
        return jsii.sget(cls, "S3")

    @jsii.python.classproperty
    @jsii.member(jsii_name="SAGE_MAKER")
    def SAGE_MAKER(cls) -> str:
        return jsii.sget(cls, "SAGE_MAKER")

    @jsii.python.classproperty
    @jsii.member(jsii_name="SECRETS_MANAGER")
    def SECRETS_MANAGER(cls) -> str:
        return jsii.sget(cls, "SECRETS_MANAGER")

    @jsii.python.classproperty
    @jsii.member(jsii_name="SERVICE_CATALOG")
    def SERVICE_CATALOG(cls) -> str:
        return jsii.sget(cls, "SERVICE_CATALOG")

    @jsii.python.classproperty
    @jsii.member(jsii_name="SES")
    def SES(cls) -> str:
        return jsii.sget(cls, "SES")

    @jsii.python.classproperty
    @jsii.member(jsii_name="SIGNIN")
    def SIGNIN(cls) -> str:
        return jsii.sget(cls, "SIGNIN")

    @jsii.python.classproperty
    @jsii.member(jsii_name="SMS")
    def SMS(cls) -> str:
        return jsii.sget(cls, "SMS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="SNS")
    def SNS(cls) -> str:
        return jsii.sget(cls, "SNS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="SPOT_FLEET")
    def SPOT_FLEET(cls) -> str:
        return jsii.sget(cls, "SPOT_FLEET")

    @jsii.python.classproperty
    @jsii.member(jsii_name="SQS")
    def SQS(cls) -> str:
        return jsii.sget(cls, "SQS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="SSM")
    def SSM(cls) -> str:
        return jsii.sget(cls, "SSM")

    @jsii.python.classproperty
    @jsii.member(jsii_name="SSO")
    def SSO(cls) -> str:
        return jsii.sget(cls, "SSO")

    @jsii.python.classproperty
    @jsii.member(jsii_name="STATES")
    def STATES(cls) -> str:
        return jsii.sget(cls, "STATES")

    @jsii.python.classproperty
    @jsii.member(jsii_name="STORAGE_GATEWAY")
    def STORAGE_GATEWAY(cls) -> str:
        return jsii.sget(cls, "STORAGE_GATEWAY")

    @jsii.python.classproperty
    @jsii.member(jsii_name="STS")
    def STS(cls) -> str:
        return jsii.sget(cls, "STS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="SUPPORT")
    def SUPPORT(cls) -> str:
        return jsii.sget(cls, "SUPPORT")

    @jsii.python.classproperty
    @jsii.member(jsii_name="SWF")
    def SWF(cls) -> str:
        return jsii.sget(cls, "SWF")

    @jsii.python.classproperty
    @jsii.member(jsii_name="TRUSTED_ADVISOR")
    def TRUSTED_ADVISOR(cls) -> str:
        return jsii.sget(cls, "TRUSTED_ADVISOR")

    @jsii.python.classproperty
    @jsii.member(jsii_name="VMIE")
    def VMIE(cls) -> str:
        return jsii.sget(cls, "VMIE")

    @jsii.python.classproperty
    @jsii.member(jsii_name="WAF")
    def WAF(cls) -> str:
        return jsii.sget(cls, "WAF")

    @jsii.python.classproperty
    @jsii.member(jsii_name="WORK_DOCS")
    def WORK_DOCS(cls) -> str:
        return jsii.sget(cls, "WORK_DOCS")

    @jsii.python.classproperty
    @jsii.member(jsii_name="WORK_SPACES")
    def WORK_SPACES(cls) -> str:
        return jsii.sget(cls, "WORK_SPACES")


__all__ = ["FederatedPrincipals", "ManagedPolicies", "ServiceNames", "ServicePrincipals", "__jsii_assembly__"]

publication.publish()
