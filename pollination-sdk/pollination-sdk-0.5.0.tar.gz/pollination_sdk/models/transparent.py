# coding: utf-8

"""
    pollination.cloud

    Pollination Cloud API  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pollination_sdk.configuration import Configuration


class Transparent(object):
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
        'type': 'str',
        'name': 'str',
        'transmittance': 'float'
    }

    attribute_map = {
        'type': 'type',
        'name': 'name',
        'transmittance': 'transmittance'
    }

    def __init__(self, type=None, name=None, transmittance=None, local_vars_configuration=None):  # noqa: E501
        """Transparent - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._name = None
        self._transmittance = None
        self.discriminator = None

        self.type = type
        self.name = name
        self.transmittance = transmittance

    @property
    def type(self):
        """Gets the type of this Transparent.  # noqa: E501


        :return: The type of this Transparent.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Transparent.


        :param type: The type of this Transparent.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["Transparent"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def name(self):
        """Gets the name of this Transparent.  # noqa: E501


        :return: The name of this Transparent.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Transparent.


        :param name: The name of this Transparent.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and not re.search(r'^[.A-Za-z0-9_-]*$', name)):  # noqa: E501
            raise ValueError(r"Invalid value for `name`, must be a follow pattern or equal to `/^[.A-Za-z0-9_-]*$/`")  # noqa: E501

        self._name = name

    @property
    def transmittance(self):
        """Gets the transmittance of this Transparent.  # noqa: E501


        :return: The transmittance of this Transparent.  # noqa: E501
        :rtype: float
        """
        return self._transmittance

    @transmittance.setter
    def transmittance(self, transmittance):
        """Sets the transmittance of this Transparent.


        :param transmittance: The transmittance of this Transparent.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and transmittance is None:  # noqa: E501
            raise ValueError("Invalid value for `transmittance`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                transmittance is not None and transmittance > 1.0):  # noqa: E501
            raise ValueError("Invalid value for `transmittance`, must be a value less than or equal to `1.0`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                transmittance is not None and transmittance < 0.0):  # noqa: E501
            raise ValueError("Invalid value for `transmittance`, must be a value greater than or equal to `0.0`")  # noqa: E501

        self._transmittance = transmittance

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
        if not isinstance(other, Transparent):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Transparent):
            return True

        return self.to_dict() != other.to_dict()
