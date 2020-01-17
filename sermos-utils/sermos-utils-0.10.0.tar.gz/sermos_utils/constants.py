""" Constants used throughout utils.
"""
from urllib.parse import urljoin

ENV_VAR_DEPLOY_KEY = "SERMOS_DEPLOY_KEY"
ENV_VAR_PKG_NAME = "SERMOS_CLIENT_PKG_NAME"
DEFAULT_BASE_URL = "https://admin.sermos.ai/api/v1/"
DEFAULT_DEPLOY_URL = urljoin(DEFAULT_BASE_URL, 'deploy')
DEFAULT_GET_MODEL_URL = urljoin(DEFAULT_BASE_URL, 'models/get-model/')
DEFAULT_STORE_MODEL_URL = urljoin(DEFAULT_BASE_URL, 'models/store-model/')
DEFAULT_YAML_NAME = "sermos.yaml"
S3_MODEL_BUCKET = 'sermos-client-models'