import sentry_sdk
from sentry_sdk.integrations.spark import SparkWorkerIntegration
import pyspark.daemon as original_daemon
import os

if __name__ == '__main__' and 'SENTRY_DSN' in os.environ:
    sentry_sdk.init(
        os.environ['SENTRY_DSN'],
        integrations=[SparkWorkerIntegration()]
    )
    original_daemon.manager()
