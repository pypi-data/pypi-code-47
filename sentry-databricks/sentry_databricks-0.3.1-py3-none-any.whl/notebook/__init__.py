import sentry_sdk
from sentry_sdk.integrations.spark import SparkIntegration

def initSentry(sentryDsn: str, appEnv: str, appRootNamespaces: list):
    sentry_sdk.init(
        sentryDsn,
        environment=appEnv,
        attach_stacktrace=True,
        in_app_include=appRootNamespaces,
        request_bodies='medium',
        integrations=[SparkIntegration()],
    )
