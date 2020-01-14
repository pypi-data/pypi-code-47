#!/usr/bin/env python3

import json
import os

import dcyd.utils.constants as constants


def get_project_id():
    with open(os.environ[constants.DCYD_CONFIG_ENV_VAR], 'r') as f:
        key = json.load(f)

    return key['project_id']


def get_client_id():
    with open(os.environ[constants.DCYD_CONFIG_ENV_VAR], 'r') as f:
        key = json.load(f)

    return key['client_id']


def get_pubsub_topic_name():
    with open(os.environ[constants.DCYD_CONFIG_ENV_VAR], 'r') as f:
        key = json.load(f)

    return key['pubsub_topic_name']
