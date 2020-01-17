# coding: utf-8
"""
Module for uploading locally stored IFS files into CDF
"""
import pandas as pd
import mimetypes
import os
import logging
import datetime
import re

from cognite.client import CogniteClient
from cognite.client.data_classes import Asset
from cognite.client.exceptions import CogniteAPIError

from .monitoring import Monitor


class FileUploader:
    def __init__(self, monitor: Monitor, client: CogniteClient, path: str, mapping_file: str):
        """
        Initialize class.
        """
        self.client = client
        self.monitor = monitor
        self.path = path
        self.mapping_file = mapping_file

        try:
            self.mapping = pd.read_csv(os.path.join(self.path, self.mapping_file), sep=";")
        except UnicodeDecodeError:
            self.mapping = pd.read_csv(os.path.join(self.path, self.mapping_file), sep=";", encoding="ISO-8859-1")
        self.list_of_files = os.listdir(self.path)
        self.unmatched_files = []
        self.unmatched_assets = []
        self.unknown_assets_df = pd.DataFrame()
        self.unknown_files = []
        self.duplicate_files = []

    @staticmethod
    def get_metadata(mapping: pd.DataFrame):
        """
        Create metadata dictionary from mapping dataframe
        """
        return {
            "DOC_NO": mapping["Doc No"],
            "DOC_REV": mapping["Doc rev"],
            "DOC_SHEET": mapping["Doc Sheet"],
            "DOC_CLASS": mapping["Doc Class"],
            "DOC_CLASS_NAME": mapping["Doc Class Name"],
            "DOC_FORMAT": mapping["Doc Format"],
            "DOC_FORMAT_NAME": mapping["Doc Format Name"],
            "DOC_RESP_SIGN": mapping["Doc Resp Sign"],
            "LETTER_DATE": mapping["Letter Date"],
            "DATE_CREATED": mapping["Dt Cre"],
            "DOC_REFERENCE": mapping["Doc Reference"]
        }

    def upload_file(self, file_name, int_ids, index, overwrite):
        """
        Uploads file according to the objects parameters
        """
        logging.info(int_ids)
        res = self.client.files.upload(
            path=os.path.join(self.path, file_name),
            external_id=file_name,
            name=self.mapping.loc[index, "Doc Title"].replace("/", "_"),
            source="IFS",
            mime_type=mimetypes.MimeTypes().guess_type(file_name)[0],
            metadata=self.get_metadata(self.mapping.loc[index, :]),
            asset_ids=int_ids,
            overwrite=overwrite
        )
        logging.info(res)

    def process_csv(self):
        """
        Upload files to the corresponding assets using the mapping file
        """
        for i in range(len(self.mapping)):

            logging.info(i)

            # Check if file exists in directory
            file_name = self.mapping.loc[i, "File Name"]
            if file_name not in self.list_of_files:
                print(f"Couldn't find file {file_name}")
                self.unknown_files.append(file_name)
                continue

            # Fetch external and internal asset ids from mapping
            asset_ext_ids = (
                self.mapping.loc[i, "Doc Reference"]
                    .replace("*", "_")
                    .replace("/", "_")
                    .replace("+", "_")
                    .replace(",", "_")
                    .replace(" ", "_")
                    .replace(" ", "_")
                    .replace("Æ", "_")
                    .replace("Ø", "_")
                    .replace("Å", "_")
                    .replace(".", "_")
            )
            logging.info(asset_ext_ids)
            asset_ext_ids = asset_ext_ids.split("|")
            if type(asset_ext_ids) != list:
                asset_ext_ids = [asset_ext_ids]
            ids_not_found = []
            asset_int_ids = []
            for ext_id in asset_ext_ids:
                asset = self.client.assets.retrieve(external_id=ext_id)
                if asset:
                    asset_int_ids.append(asset.id)
                else:
                    ids_not_found.append(ext_id)
                    logging.info(f"Couldn't upload file {file_name} to asset: {ext_id}. ExternalId not found!")
            if ids_not_found:
                self.unmatched_files.append(file_name)
                self.unmatched_assets.append(ids_not_found)

            # Process line by line depending on the desired operation
            if self.mapping.loc[i, "Change Type"] == "N":
                try:
                    self.upload_file(file_name=file_name, int_ids=asset_int_ids, index=i, overwrite=False)
                except CogniteAPIError:
                    self.duplicate_files.append(file_name)

            else:
                asset_int_ids_old = set(self.client.files.retrieve(external_id=file_name).asset_ids)
                asset_int_ids = set(asset_int_ids)

                if self.mapping.loc[i, "Change Type"] == "C":
                    # To not accidentally deleted the file from assets when changing another field, make sure that for
                    # the change option no asset_ids get deleted from the field
                    asset_int_ids_new = asset_int_ids_old.union(asset_int_ids)
                    self.upload_file(file_name=file_name, int_ids=list(asset_int_ids_new), index=i, overwrite=True)

                elif self.mapping.loc[i, "Change Type"] == "D":
                    if asset_int_ids == asset_int_ids_old:
                        # Delete the file from CDF and the local directory
                        self.client.files.delete(external_id=file_name)
                        os.remove(os.path.join(self.path, file_name))
                    else:
                        # Overwrite existing file without asset_int_ids
                        asset_int_ids_new = asset_int_ids_old - asset_int_ids
                        self.upload_file(file_name=file_name, int_ids=list(asset_int_ids_new), index=i, overwrite=True)

                else:
                    print(f"Non valid operation in row {i}")

        # Move mapping file to Archive folder
        print(f"old path: {os.path.join(self.path, self.mapping_file)}")
        print(f"new path: {os.path.join(self.path, 'Archive', self.mapping_file)}")
        os.rename(rf'{os.path.join(self.path, self.mapping_file)}',
                  rf'{os.path.join(self.path, "Archive", self.mapping_file)}')

        # Create new unknown_assets.csv, unknown_files.csv and duplicates.csv including the mapping_file date
        # information
        date_info = self.mapping_file.replace("METADATA_", "").replace(".csv", "")
        self.unknown_assets_df = pd.DataFrame(
            list(zip(self.unmatched_files, self.unmatched_assets)), columns=["File", "Assets"])
        if not self.unknown_assets_df.empty:
            self.unknown_assets_df.to_csv(
                os.path.join(self.path, "Archive", f"unknown_assets_{date_info}.csv"), index=None)
        if self.unknown_files:
            pd.DataFrame(self.unknown_files, columns=['Files']).to_csv(
                os.path.join(self.path, "Archive", f"unknown_files_{date_info}.csv"), index=None)
        if self.duplicate_files:
            pd.DataFrame(self.duplicate_files, columns=['Files']).to_csv(
                os.path.join(self.path, "Archive", f"duplicate_files_{date_info}.csv"), index=None)
