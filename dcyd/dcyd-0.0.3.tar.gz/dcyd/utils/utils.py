#!/usr/bin/env python3

import json
import os
import pkg_resources

import dcyd.utils.constants as constants


def get_project_id():
    with open(os.environ[constants.DCYD_CONFIG_ENV_VAR], 'r') as f:
        key = json.load(f)

    return key.get('project_id')


def get_account_data():
    with open(os.environ[constants.DCYD_CONFIG_ENV_VAR], 'r') as f:
        key = json.load(f)

    return {
        'account_id': key.get('client_id'),
        'account_email': key.get('client_email')
    }


def get_pubsub_topic_name():
    with open(os.environ[constants.DCYD_CONFIG_ENV_VAR], 'r') as f:
        key = json.load(f)

    return key.get('pubsub_topic_name')


def get_mpm_client_data():
    dist = pkg_resources.get_distribution('dcyd')

    return {
        'mpm_client_name': dist.key,
        'mpm_client_version': dist.version,
    }
