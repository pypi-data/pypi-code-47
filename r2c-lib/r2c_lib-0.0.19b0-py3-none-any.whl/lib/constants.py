import os

PREFIX: str = os.getenv("PIPELINE_PREFIX", default="test_prefix")
# analyzer related
S3_ANALYSIS_BUCKET_NAME: str = "r2c-pipeline-analysis-output"
S3_ANALYSIS_LOG_BUCKET_NAME: str = "r2c-pipeline-analysis-log"

# registry related
# TODO remove this on API supports manifest

S3_ORG_REGISTRY_BUCKET_NAME: str = f"r2c-{PREFIX}-pipeline-registry"
S3_PUBLIC_REGISTRY_BUCKET_NAME: str = f"r2c-public-pipeline-registry"
S3_REGISTRY_FILENAME: str = "registry.json"

# only for local run
DEFAULT_LOCAL_RUN_DIR_SUFFIX: str = "local-infra"

# TODO remove this on API supports manifest
AWS_ACCOUNT: str = "338683922796"
ECR_URL: str = f"{AWS_ACCOUNT}.dkr.ecr.us-west-2.amazonaws.com"

PLATFORM_ANALYZER_PREFIX = "beta"
PLATFORM_BASE_URL = "https://app.r2c.dev"
