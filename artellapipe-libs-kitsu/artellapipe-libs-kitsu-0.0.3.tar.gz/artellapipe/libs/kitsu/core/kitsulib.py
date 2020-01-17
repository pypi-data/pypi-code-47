#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Utility module that contains useful utilities and classes related with Kitsu
"""

from __future__ import print_function, division, absolute_import

__author__ = "Tomas Poveda"
__license__ = "MIT"
__maintainer__ = "Tomas Poveda"
__email__ = "tpovedatd@gmail.com"

import logging

import gazu

from artellapipe.libs.kitsu.core import kitsuclasses

LOGGER = logging.getLogger()


def set_host(new_host):
    """
    Sets current configured host on which requests are sent
    :param new_host: variant, str or None
    """

    gazu.set_host(new_host)


def host_is_up():
    """
    Returns whether host is up or not
    :return: bool
    """

    return gazu.client.host_is_up()


def log_in(email, password):
    """
    Login to Kitsu with given email and password
    :param email: str
    :param password: str
    :return:
    """

    if not email or not password:
        return False

    return gazu.log_in(email, password)


def get_current_user(as_dict=False):
    """
    Returns user database information for user linked to auth tokens
    :param as_dict: bool
    :return: variant, dict or KitsuUserInfo
    """

    user_data = gazu.client.get_current_user()
    if as_dict:
        return user_data

    return kitsuclasses.KitsuUserInfo(user_data)


def all_assets_for_project(project_id, as_list=False):
    """
    Returns a list with all assets in the given project
    :param project_id: str
    :param as_list: bool
    :return: variant, dict or list
    """

    if type(project_id) != dict:
        project_id = {'id': project_id}

    assets_list = gazu.asset.all_assets_for_project(project_id)
    if as_list:
        return assets_list

    return [kitsuclasses.KitsuAsset(asset) for asset in assets_list]


def all_asset_types_for_project(project_id, as_dict=False):
    """
    Returns asset types from assets listed in the given project
    :param project_id: variant, str or dict
    :param as_dict: bool, Whether to return data as dict or as Kitsu class
    :return: variant, list(dict) or list(KitsuAssetType)
    """

    if type(project_id) != dict:
        project_id = {'id': project_id}

    asset_types = gazu.asset.all_asset_types_for_project(project_id)
    if as_dict:
        return asset_types

    return [kitsuclasses.KitsuAssetType(asset_type) for asset_type in asset_types]


def download_preview_file_thumbnail(preview_id, file_path):
    """
    Downloads given preview file thumbnail and save it at given location
    :param preview_id:  str or dict, The preview file dict or ID.
    :param target_path: str, Location on ahrd drive where to save the file.
    """

    if type(preview_id) != dict:
        preview_id = {'id': preview_id}

    gazu.files.download_preview_file_thumbnail(preview_id, file_path)


def get_project_entity_types():
    """
    Returns all entity types in the project
    :return: list
    """

    return gazu.client.fetch_one('entity-types', '')


def get_all_sequences(project_id, as_dict=False):
    """
    Returns all sequences for the given project
    :param project_id: variant, str or dict
    :param as_dict: bool, Whether to return data as dict or as Kitsu class
    :return: list(dict) or list(KitsuSequence)
    """

    if type(project_id) != dict:
        project_id = {'id': project_id}

    sequences = gazu.shot.all_sequences_for_project(project_id)

    if as_dict:
        return sequences

    return [kitsuclasses.KitsuSequence(sequence) for sequence in sequences]


def get_all_shots(project_id, as_dict=False):
    """
    Returns all shots for the given project
    :param project_id: variant, str or dict
    :param as_dict: bool, Whether to return data as dict or as Kitsu class
    :return: list(dict) or list(KitsuShot)
    """

    if type(project_id) != dict:
        project_id = {'id': project_id}

    shots = gazu.shot.all_shots_for_project(project_id)

    if as_dict:
        return shots

    return [kitsuclasses.KitsuShot(shot) for shot in shots]


def get_shot_sequence(shot_dict, as_dict=False):
    """
    Returns sequence given shot belongs to
    :param shot_dict:
    :param as_dict:  bool, Whether to return data as dict or as Kitsu class
    :return:
    """

    if 'parent_id' not in shot_dict:
        LOGGER.warning('Impossible to retrieve sequence from shot!')
        return None

    shot = gazu.shot.get_sequence_from_shot(shot_dict)

    if as_dict:
        return shot

    return kitsuclasses.KitsuSequence(shot)
