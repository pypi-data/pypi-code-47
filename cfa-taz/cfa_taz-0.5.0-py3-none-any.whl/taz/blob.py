#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Taz library: blobs operations
"""


from azure.storage.common.cloudstorageaccount import CloudStorageAccount
import urllib
from azure.storage.blob import BlobPermissions
from datetime import datetime, timedelta
import pandas as pd
import gzip


class StorageAccount:
    def __init__(
        self,
        name,
        storage_key=None,
    ):
        """ Storage account object

        Args:
            name (TYPE): Description
            storage_key (None, optional): Description
        """
        self.storage_client = CloudStorageAccount(
            name,
            storage_key)

        self.name = name
        self.blob_service = self.storage_client.create_block_blob_service()
        self.page_blob_service = self.storage_client.create_page_blob_service()

    def list_containers(self):
        """ list storage account containers

        Returns:
            - azure.storage.blob.models.Container List: list of container, Container class attributes:
                - name
                - metadata
                - properties
        """
        return self.blob_service.list_containers()

    def list_blobs(self, container, prefix=None):
        """ list blobs in specified container

        Args:
            - container (string): container
            - prefix (string, optional): prefix of blobs to select

        Returns:
            - azure.storage.blob.models.Blob: Blob class attributes
                - name: blob name
                - snapshot
                - content
                - properties (BlobProperties)
                - deleted
        """
        return self.blob_service.list_blobs(container, prefix=prefix)

    def copy_blob(self, container, blob, file):
        """copy blob content to local file

        Args:
            container (string): container name
            blob (string): blob name
            file (string): local file name

        Returns:
            azure.storage.blob.models.Blob: blob copied
        """
        return self.page_blob_service.get_blob_to_path(
            container,
            blob,
            file,
        )


class Container:
    def __init__(
        self,
        storage_account,
        name
    ):
        """ define Container object 

        Args:
            storage_account (TYPE): Description
            name (TYPE): Description
        """
        self.storage_account = storage_account
        self.name = name

    def create(self):
        return self.storage_account.blob_service.create_container(self.name)

    def delete(self):
        return self.storage_account.blob_service.delete_container(self.name)


class Blob:
    def __init__(
        self,
        storage_account,
        container,
        name,
        sas_key=None,
    ):
        self.storage_account = storage_account
        self.container = container
        self.name = name
        self.sas_key = sas_key

    def get_sas_token(self):
        permission = BlobPermissions(_str="racwd")
        self.sas_token = self.storage_account.blob_service.generate_blob_shared_access_signature(
            self.container,
            self.name,
            permission,
            datetime.utcnow() + timedelta(hours=1))
        return self.sas_token

    def get_url(self):
        return self.storage_account.blob_service.make_blob_url(
            self.container,
            self.name,
            protocol='https',
            sas_token=self.get_sas_token())

    def read(self):
        with urllib.request.urlopen(self.get_url()) as response:
            return response.read()

    def read_csv(self, **kargs):
        """read CSV file from Blob

        Args:
            - path (string): remote csv file path to read
            - **kargs: arguments array passed to pandas.read_csv

        Returns:
            - pandas.DataFrame: DataFrame filled with read datas
        """

        return pd.read_csv(self.get_url(), **kargs)

    def gzip_write(self, name, data):
        return self.write(self.name, gzip.compress(data, compresslevel=9))

    def write(self, name, data):
        return self.storage_account.blob_service.create_blob_from_bytes(self.container, self.name, data)

    def delete(self):
        return self.storage_account.blob_service.delete_blob(self.container, self.name)
