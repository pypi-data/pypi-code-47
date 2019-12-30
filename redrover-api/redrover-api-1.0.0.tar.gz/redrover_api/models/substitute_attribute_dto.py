# coding: utf-8

"""
    Red Rover API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Contact: contact@edustaff.org
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from redrover_api.configuration import Configuration


class SubstituteAttributeDto(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'attribute': 'LocatorInt32',
        'expires': 'datetime',
        'has_changes': 'bool',
        'ignore_warnings': 'bool',
        'provided_property_names': 'str'
    }

    attribute_map = {
        'attribute': 'attribute',
        'expires': 'expires',
        'has_changes': 'hasChanges',
        'ignore_warnings': 'ignoreWarnings',
        'provided_property_names': 'providedPropertyNames'
    }

    def __init__(self, attribute=None, expires=None, has_changes=None, ignore_warnings=None, provided_property_names=None, local_vars_configuration=None):  # noqa: E501
        """SubstituteAttributeDto - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._attribute = None
        self._expires = None
        self._has_changes = None
        self._ignore_warnings = None
        self._provided_property_names = None
        self.discriminator = None

        if attribute is not None:
            self.attribute = attribute
        if expires is not None:
            self.expires = expires
        if has_changes is not None:
            self.has_changes = has_changes
        if ignore_warnings is not None:
            self.ignore_warnings = ignore_warnings
        if provided_property_names is not None:
            self.provided_property_names = provided_property_names

    @property
    def attribute(self):
        """Gets the attribute of this SubstituteAttributeDto.  # noqa: E501


        :return: The attribute of this SubstituteAttributeDto.  # noqa: E501
        :rtype: LocatorInt32
        """
        return self._attribute

    @attribute.setter
    def attribute(self, attribute):
        """Sets the attribute of this SubstituteAttributeDto.


        :param attribute: The attribute of this SubstituteAttributeDto.  # noqa: E501
        :type: LocatorInt32
        """

        self._attribute = attribute

    @property
    def expires(self):
        """Gets the expires of this SubstituteAttributeDto.  # noqa: E501


        :return: The expires of this SubstituteAttributeDto.  # noqa: E501
        :rtype: datetime
        """
        return self._expires

    @expires.setter
    def expires(self, expires):
        """Sets the expires of this SubstituteAttributeDto.


        :param expires: The expires of this SubstituteAttributeDto.  # noqa: E501
        :type: datetime
        """

        self._expires = expires

    @property
    def has_changes(self):
        """Gets the has_changes of this SubstituteAttributeDto.  # noqa: E501


        :return: The has_changes of this SubstituteAttributeDto.  # noqa: E501
        :rtype: bool
        """
        return self._has_changes

    @has_changes.setter
    def has_changes(self, has_changes):
        """Sets the has_changes of this SubstituteAttributeDto.


        :param has_changes: The has_changes of this SubstituteAttributeDto.  # noqa: E501
        :type: bool
        """

        self._has_changes = has_changes

    @property
    def ignore_warnings(self):
        """Gets the ignore_warnings of this SubstituteAttributeDto.  # noqa: E501


        :return: The ignore_warnings of this SubstituteAttributeDto.  # noqa: E501
        :rtype: bool
        """
        return self._ignore_warnings

    @ignore_warnings.setter
    def ignore_warnings(self, ignore_warnings):
        """Sets the ignore_warnings of this SubstituteAttributeDto.


        :param ignore_warnings: The ignore_warnings of this SubstituteAttributeDto.  # noqa: E501
        :type: bool
        """

        self._ignore_warnings = ignore_warnings

    @property
    def provided_property_names(self):
        """Gets the provided_property_names of this SubstituteAttributeDto.  # noqa: E501


        :return: The provided_property_names of this SubstituteAttributeDto.  # noqa: E501
        :rtype: str
        """
        return self._provided_property_names

    @provided_property_names.setter
    def provided_property_names(self, provided_property_names):
        """Sets the provided_property_names of this SubstituteAttributeDto.


        :param provided_property_names: The provided_property_names of this SubstituteAttributeDto.  # noqa: E501
        :type: str
        """

        self._provided_property_names = provided_property_names

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SubstituteAttributeDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SubstituteAttributeDto):
            return True

        return self.to_dict() != other.to_dict()
