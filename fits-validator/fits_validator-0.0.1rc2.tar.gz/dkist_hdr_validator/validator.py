"""
The main module for the spec 122 validator
"""


from typing import Union
import os
import glob
from pathlib import Path

from astropy.io import fits
from astropy.io.fits.hdu.hdulist import HDUList
from voluptuous import Schema, MultipleInvalid, Required, All, Any, ALLOW_EXTRA
import yaml

from dkist_hdr_validator.exceptions import Spec122ValidationException, YamlSchemaException


class FitsValidator:
    """
    Construct a Spec0122 schema for use in validating multiple formats of spec122 data
    """

    type_map = {"int": int, "float": float, "str": str, "bool": bool}

    @property
    def yml_schema(self):
        """
        Make a voluptuous schema to validate Spec122 yaml files
        """
        ymlvalschema = {
            "required": Any(True, False),
            "type": Any("int", "float", "str", "bool"),
        }
        specschema = Schema(ymlvalschema, extra=ALLOW_EXTRA)
        return specschema

    def __init__(self):
        # make a list of yml files to be used
        self.yml_files = []
        path = Path("/Users/alysaderks/repos/dkist_hdr_validator/dkist_hdr_validator/spec122")
        for file in path.rglob("*.yml"):
            self.yml_files.append(file)

        # send to open .yml files and validate
        self._validate_spec122_definition_files()
        # send to create voluptuous schema to be used with file validation
        self._create_vol_schema()

    def _generate_voluptuous_schema_for_required_key(self, key_schema: dict) -> Union[type, object]:
        """
        Create a dictionary from spec122 required keys

        :param key_schema:
        :return:
        """
        if key_schema.get("values"):
            keyschema = All(self.type_map[key_schema.get("type")], Any(*key_schema.get("values")))
        else:
            keyschema = All(self.type_map[key_schema.get("type")])
        return keyschema

    def _generate_voluptuous_schema_for_key(self, key_schema: dict) -> Union[type, object]:
        """
        Create a dictionary from spec122 non-required keys

        :param key_schema:
        :return:
        """
        if key_schema.get("values"):
            keyschema = All(self.type_map[key_schema.get("type")], Any(*key_schema.get("values")))
        else:
            keyschema = All(self.type_map[key_schema.get("type")])
        return keyschema

    def _validate_spec122_definition(self, stream):
        """
        Spec122 keyword validation
        """
        for key, key_schemaa in self.stream.items():
            schemaerrors = {}
            try:
                self.yml_schema(key_schemaa)
            except MultipleInvalid as e:
                for error in e.errors:
                    message = error.msg
                    keyword = error.path[0]
                    schemaerrors.update(((keyword, message),))
            if schemaerrors:
                raise YamlSchemaException(key=key, errors=schemaerrors)

    def _validate_spec122_definition_files(self) -> None:
        """
        Open Spec122 files and validate them using the Spec122 vol schema

        :return: None
        :raises: YamlValidationException
        """
        # open .yml file
        self.dictlist = []
        for file_name in self.yml_files:
            with open(file_name) as ymlstring:
                stream = yaml.load(ymlstring, Loader=yaml.FullLoader)
                self.stream = stream
                self.dictlist.append(stream)
                self._validate_spec122_definition(self.stream)

    def _create_vol_schema(self):
        """
        A voluptuous.schema object to validate headers against. 
        Constructed from Spec0122 keywords. 
        """

        ymlschema = {}
        # populate dictionary to go into schema
        for specdict in self.dictlist:
            for key, key_schema in specdict.items():
                if key_schema["required"] is True:
                    ymlschema[Required(key)] = self._generate_voluptuous_schema_for_required_key(
                        key_schema
                    )
                else:
                    ymlschema[key] = self._generate_voluptuous_schema_for_key(key_schema)
        schema = Schema(ymlschema, extra=ALLOW_EXTRA)
        self.schema = schema

    def _headers_to_dict(self, headers):
        """
        Extract headers and make sure they are dictionaries.
        """

        # if headers are already a dictionary, good.
        if isinstance(headers, dict):
            return headers
        # if headers are HDUList, read them into a ditionary.
        if isinstance(headers, HDUList):
            return dict(headers[0].header)
        # If headers are of any other type, see if it is a file and try to open that
        # or else raise an error.
        try:
            with fits.open(headers) as hdus:
                headers = dict(hdus[0].header)
                return headers
        except ValueError as exc:
            raise Exception(f"Cannot open file: detail = {exc}")

    def validate(self, headers: Union[HDUList, dict, str]):
        """
        Validate the header against the schema.


        Usage:
        ------
        > from validator import FitsValidator
        > val = FitsValidator()
        > val.validate(input)


        :param headers: The headers to validate in the following formats:
            string file path
            HDUList object
            Dictionary of header keys and values
        :return: None

        :raises: Spec122ValidationException
        ______
        all_errors: dict
            dictionary of keywords and their corresponding errors
        """

        self.headers = self._headers_to_dict(headers)

        all_errors = {}

        try:
            self.schema(self.headers)
        except MultipleInvalid as e:
            for error in e.errors:
                message = error.msg
                keyword = error.path[0]
                message = (
                    message
                    + f". Actual value: {self.headers.get(keyword, 'Required keyword not present')}"
                )
                all_errors.update(((keyword, message),))

        # Raise exception if we have errors
        if all_errors:
            raise Spec122ValidationException(errors=all_errors)
        print("No errors during validation!")
