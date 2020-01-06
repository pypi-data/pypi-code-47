import os
from collections.abc import Mapping
from pathlib import Path


def read_environment_settings() -> Mapping:
    vault_address = _vault_address()
    app_name = _app_name()
    namespace = _namespace()

    return {
        "token": _token(),
        "app_name": app_name,
        "vault_address": vault_address,
        "namespace": namespace,
        "auth_url": _auth_url(vault_address),
        "secrets_url": _secrets_url(vault_address, app_name, namespace)
    }


def _app_name():
    try:
        app_name = os.environ["APPLICATION_NAME"]
    except KeyError:
        raise EnvironmentError("APPLICATION_NAME env is not set")
    else:
        return app_name


def _token():
    try:
        token_path = os.environ["K8S_SERVICEACCOUNT_PATH"]
    except KeyError:
        raise EnvironmentError("K8S_SERVICEACCOUNT_PATH env is not set")
    else:
        with Path(token_path).joinpath("token").open("r") as token_file:
            return token_file.read()


def _vault_address():
    try:
        address = os.environ["VKS_VAULT_ADDR"]
    except KeyError:
        raise EnvironmentError("VKS_VAULT_ADDR env is not set")
    else:
        return address


def _namespace():
    try:
        namespace_path = os.environ["K8S_SERVICEACCOUNT_PATH"]
    except KeyError:
        raise EnvironmentError("K8S_SERVICEACCOUNT_PATH env is not set")
    else:
        with Path(namespace_path).joinpath("namespace").open("r") as namespace_file:
            return namespace_file.read()


def _auth_url(vault_address):
    try:
        vault_auth_path = os.environ["VKS_AUTH_PATH"]
    except KeyError:
        raise EnvironmentError("VKS_AUTH_PATH env is not set")
    else:
        return f"{vault_address}/v1/{vault_auth_path}"


def _secrets_url(vault_address, app_name, namespace):
    try:
        vault_kv_path = os.environ["VKS_KV_PATH"]
    except KeyError:
        raise EnvironmentError("VKS_KV_PATH env is not set")
    else:
        return f"{vault_address}/v1/{vault_kv_path}/{app_name}/{namespace}"
