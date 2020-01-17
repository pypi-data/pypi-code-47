#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module that contains Kitsu tracking class for Artella projects
"""

from __future__ import print_function, division, absolute_import

__author__ = "Tomas Poveda"
__license__ = "MIT"
__maintainer__ = "Tomas Poveda"
__email__ = "tpovedatd@gmail.com"

import os
import logging

from tpPyUtils import decorators
from tpQtLib.core import qtutils

import artellapipe.register
from artellapipe.managers import tracking
import artellapipe.libs.kitsu as kitsu_lib
from artellapipe.libs.kitsu.core import kitsulib, kitsuclasses

LOGGER = logging.getLogger()


@decorators.Singleton
class KitsuTrackingManager(tracking.TrackingManager, object):
    def __init__(self):
        tracking.TrackingManager.__init__(self)

        self._email = None
        self._password = None
        self._store_credentials = False
        self._user_data = dict()
        self._entity_types = list()

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, new_email):
        self._email = new_email

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, new_password):
        self._password = new_password

    @property
    def store_credentials(self):
        return self._store_credentials

    @store_credentials.setter
    def store_credentials(self, new_store_credentials):
        self._store_credentials = new_store_credentials

    @property
    def user_data(self):
        return self._user_data

    def needs_login(self):
        """
        Returns whether or not production trackign needs log to work or not
        """

        return True

    def reset_user_info(self):
        """
        Function that resets the information stored of the user
        """

        self._email = None
        self._password = None
        self._store_credentials = False
        self._user_data = None

    def set_project(self, project):
        """
        Overrides base TrackingManager
        :param project: ArtellaProject
        """

        tracking.TrackingManager.set_project(self, project)
        self._load_user_settings()

    def update_tracking_info(self):
        print('Updating tracking info ...')

    def is_tracking_available(self):
        """
        Returns whether tracking service is available or not
        :return: bool
        """

        return kitsulib.host_is_up()

    def login(self, *args, **kwargs):
        """
        Login into tracking service with given user and password
        :return: bool
        """

        email = kwargs.get('email', self._email)
        password = kwargs.get('password', self._password)
        store_credentials = kwargs.get('store_credentials', self._store_credentials)

        if not email or not password:
            LOGGER.warning('Impossible to login into Kitsu because username or password are not valid!')
            return False

        gazup_api = kitsu_lib.config.get('gazu_api', default=None)
        if not gazup_api:
            LOGGER.warning('Impossible to login into Kitsu because Gazu API is not available!')
            return False

        kitsulib.set_host(gazup_api)
        if not kitsulib.host_is_up():
            LOGGER.warning('Impossible to login into Kitsu because Gazu API is not available: "{}"'.format(gazup_api))
            qtutils.show_warning(
                None, 'Kitsu server is down!',
                'Was not possible to retrieve Gazu API. '
                'This usually happens when Kitsu server is down. Please contact TD!')
            return False

        try:
            valid_login = kitsulib.log_in(email, password)
            self._logged = bool(valid_login)
            self._user_data = kitsulib.get_current_user()
            self._project.settings.set('kitsu_store_credentials', store_credentials)
            if store_credentials:
                self._project.settings.set('kitsu_email', email)
                self._project.settings.set('kitsu_password', password)
            self.logged.emit()
            return True
        except Exception as exc:
            self._logged = False
            self.reset_user_info()
            return False

    def logout(self, *args, **kwargs):
        """
        Logout from tracker service
        :param args:
        :param kwargs:
        :return: bool
        """

        if not self.is_logged():
            LOGGER.warning('Impossible to logout from Kitsu because you are not currently logged')
            return False

        kitsulib.set_host(None)
        self._logged = False
        self.reset_user_info()

        remove_credentials = kwargs.get('remove_credentials', False)
        if remove_credentials:
            self._project.settings.set('kitsu_email', '')
            self._project.settings.set('kitsu_password', '')
            self._project.settings.set('kitsu_store_credentials', False)

        self._load_user_settings()

        self.unlogged.emit()

        return True

    def all_project_assets(self):
        """
        Return all the assets information of the assets of the current project
        :return: list
        """

        if not self.is_logged():
            LOGGER.warning('Impossible to retrieve assets because user is not logged into Kitsu!')
            return

        assets_path = artellapipe.AssetsMgr().get_assets_path()
        if not artellapipe.AssetsMgr().is_valid_assets_path():
            LOGGER.warning('Impossible to retrieve assets from invalid assets path: "{}"'.format(assets_path))
            return

        project_id = kitsu_lib.config.get('project_id', default=None)
        if not project_id:
            LOGGER.warning('Impossible to retrieve assets because does not defines a valid Kitsu ID')
            return

        kitsu_assets = kitsulib.all_assets_for_project(project_id=project_id)
        asset_types = self.update_entity_types_from_kitsu(force=False)
        # category_names = [asset_type.name for asset_type in asset_types]

        assets_data = list()
        for kitsu_asset in kitsu_assets:
            entity_type = self.get_entity_type_by_id(kitsu_asset.entity_type_id)
            if not entity_type:
                LOGGER.warning(
                    'Entity Type {} for Asset {} is not valid! Skipping ...'.format(entity_type, kitsu_asset.name))
                continue

            asset_id = kitsu_asset.id
            custom_id_attr = kitsu_lib.config.get('custom_id_attribute', default=None)
            if custom_id_attr:
                asset_metadata = kitsu_asset.data or dict()
                asset_id = asset_metadata.get(custom_id_attr, asset_id)

            assets_data.append(
                {
                    'asset': kitsu_asset,
                    'name': kitsu_asset.name,
                    'thumb': kitsu_asset.preview_file_id,
                    'category': entity_type.name,
                    'id': asset_id
                }
            )

        return assets_data

    def all_project_sequences(self):
        """
        Returns all the sequences of the current project
        :return:
        """

        if not self.is_logged():
            LOGGER.warning('Impossible to retrieve sequences because user is not logged into Kitsu!')
            return

        production_path = self._project.get_production_path()
        if not production_path or not os.path.isdir(production_path):
            LOGGER.warning(
                'Impossible to retrieve sequences from invalid production path: "{}"'.format(production_path))
            return

        project_id = kitsu_lib.config.get('project_id', default=None)
        if not project_id:
            LOGGER.warning('Impossible to retrieve assets because does not defines a valid Kitsu ID')
            return

        kitsu_sequences = kitsulib.get_all_sequences(project_id=project_id)

        sequences_data = list()
        for kitsu_sequence in kitsu_sequences:
            entity_type = self.get_entity_type_by_id(kitsu_sequence.entity_type_id)
            if not entity_type:
                LOGGER.warning(
                    'Entity Type {} for Sequence {} is not valid! Skipping ...'.format(
                        entity_type, kitsu_sequence.name))
                continue
            sequences_data.append(
                {
                    'sequence': kitsu_sequence,
                    'name': kitsu_sequence.name,
                    'thumb': kitsu_sequence.preview_file_id,
                    'category': entity_type.name,
                    'id': kitsu_sequence.id
                }
            )

        return sequences_data

    def all_project_shots(self):
        """
        Returns all the shots of the current project
        :return:
        """

        if not self.is_logged():
            LOGGER.warning('Impossible to retrieve sequences because user is not logged into Kitsu!')
            return

        production_path = self._project.get_production_path()
        if not production_path or not os.path.isdir(production_path):
            LOGGER.warning(
                'Impossible to retrieve sequences from invalid production path: "{}"'.format(production_path))
            return

        project_id = kitsu_lib.config.get('project_id', default=None)
        if not project_id:
            LOGGER.warning('Impossible to retrieve assets because does not defines a valid Kitsu ID')
            return

        kitsu_shots = kitsulib.get_all_shots(project_id=project_id)

        shots_data = list()
        for kitsu_shot in kitsu_shots:
            entity_type = self.get_entity_type_by_id(kitsu_shot.entity_type_id)
            if not entity_type:
                LOGGER.warning(
                    'Entity Type {} for Shot {} is not valid! Skipping ...'.format(entity_type, kitsu_shot.name))
                continue
            shots_data.append(
                {
                    'shot': kitsu_shot,
                    'name': kitsu_shot.name,
                    'thumb': kitsu_shot.preview_file_id,
                    'category': entity_type.name,
                    'id': kitsu_shot.id,
                    'sequence_name': kitsu_shot.parent_id
                }
            )

        return shots_data

    def download_preview_file_thumbnail(self, preview_id, file_path):
        """
        Downloads given preview file thumbnail and save it at given location
        :param preview_id:  str or dict, The preview file dict or ID.
        :param file_path: str, Location on hard drive where to save the file.
        """

        kitsulib.download_preview_file_thumbnail(preview_id=preview_id, file_path=file_path)

    def update_entity_types_from_kitsu(self, force=False):
        """
        Updates entity types from Kitsu project
        :param force: bool, Whether to return force the update if entity types are already retrieved
        :return: list(KitsuEntityType)
        """

        if not self.is_logged():
            return list()

        if self._entity_types and not force:
            return self._entity_types

        entity_types_list = kitsulib.get_project_entity_types()
        entity_types = [kitsuclasses.KitsuEntityType(entity_type) for entity_type in entity_types_list]
        self._entity_types = entity_types

        return self._entity_types

    def get_entity_type_by_id(self, entity_type_id, force_update=False):
        """
        Returns entity type name by the given project
        :param entity_type_id: str
        :param force_update: bool, Whether to force entity types sync if they are not already snced
        :return: str
        """

        if not self.is_logged():
            return list()

        if force_update or not self._entity_types:
            self.update_entity_types_from_kitsu(force=True)

        for entity_type in self._entity_types:
            if entity_type.id == entity_type_id:
                return entity_type

        return ''

    def _load_user_settings(self):
        """
        Internal function that tries to retrieve user data from project settings
        """

        if not self._project:
            return None

        self._email = self._project.settings.get(
            'kitsu_email') if self._project.settings.has_setting('kitsu_email') else None
        self._password = self._project.settings.get(
            'kitsu_password') if self._project.settings.has_setting('kitsu_password') else None
        self._store_credentials = self._project.settings.get(
            'kitsu_store_credentials') if self._project.settings.has_setting('kitsu_store_credentials') else False


artellapipe.register.register_class('Tracker', KitsuTrackingManager)
