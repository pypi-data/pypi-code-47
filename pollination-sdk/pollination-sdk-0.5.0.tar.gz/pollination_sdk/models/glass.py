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


class Glass(object):
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
        'r_transmittance': 'float',
        'g_transmittance': 'float',
        'b_transmittance': 'float',
        'refraction_index': 'float',
        'modifier': 'str'
    }

    attribute_map = {
        'type': 'type',
        'name': 'name',
        'r_transmittance': 'r_transmittance',
        'g_transmittance': 'g_transmittance',
        'b_transmittance': 'b_transmittance',
        'refraction_index': 'refraction_index',
        'modifier': 'modifier'
    }

    def __init__(self, type=None, name=None, r_transmittance=None, g_transmittance=None, b_transmittance=None, refraction_index=None, modifier='void', local_vars_configuration=None):  # noqa: E501
        """Glass - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._name = None
        self._r_transmittance = None
        self._g_transmittance = None
        self._b_transmittance = None
        self._refraction_index = None
        self._modifier = None
        self.discriminator = None

        self.type = type
        self.name = name
        self.r_transmittance = r_transmittance
        self.g_transmittance = g_transmittance
        self.b_transmittance = b_transmittance
        self.refraction_index = refraction_index
        if modifier is not None:
            self.modifier = modifier

    @property
    def type(self):
        """Gets the type of this Glass.  # noqa: E501


        :return: The type of this Glass.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Glass.


        :param type: The type of this Glass.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["Glass"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def name(self):
        """Gets the name of this Glass.  # noqa: E501


        :return: The name of this Glass.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Glass.


        :param name: The name of this Glass.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and not re.search(r'^[.A-Za-z0-9_-]*$', name)):  # noqa: E501
            raise ValueError(r"Invalid value for `name`, must be a follow pattern or equal to `/^[.A-Za-z0-9_-]*$/`")  # noqa: E501

        self._name = name

    @property
    def r_transmittance(self):
        """Gets the r_transmittance of this Glass.  # noqa: E501


        :return: The r_transmittance of this Glass.  # noqa: E501
        :rtype: float
        """
        return self._r_transmittance

    @r_transmittance.setter
    def r_transmittance(self, r_transmittance):
        """Sets the r_transmittance of this Glass.


        :param r_transmittance: The r_transmittance of this Glass.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and r_transmittance is None:  # noqa: E501
            raise ValueError("Invalid value for `r_transmittance`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                r_transmittance is not None and r_transmittance > 1.0):  # noqa: E501
            raise ValueError("Invalid value for `r_transmittance`, must be a value less than or equal to `1.0`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                r_transmittance is not None and r_transmittance < 0.0):  # noqa: E501
            raise ValueError("Invalid value for `r_transmittance`, must be a value greater than or equal to `0.0`")  # noqa: E501

        self._r_transmittance = r_transmittance

    @property
    def g_transmittance(self):
        """Gets the g_transmittance of this Glass.  # noqa: E501


        :return: The g_transmittance of this Glass.  # noqa: E501
        :rtype: float
        """
        return self._g_transmittance

    @g_transmittance.setter
    def g_transmittance(self, g_transmittance):
        """Sets the g_transmittance of this Glass.


        :param g_transmittance: The g_transmittance of this Glass.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and g_transmittance is None:  # noqa: E501
            raise ValueError("Invalid value for `g_transmittance`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                g_transmittance is not None and g_transmittance > 1.0):  # noqa: E501
            raise ValueError("Invalid value for `g_transmittance`, must be a value less than or equal to `1.0`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                g_transmittance is not None and g_transmittance < 0.0):  # noqa: E501
            raise ValueError("Invalid value for `g_transmittance`, must be a value greater than or equal to `0.0`")  # noqa: E501

        self._g_transmittance = g_transmittance

    @property
    def b_transmittance(self):
        """Gets the b_transmittance of this Glass.  # noqa: E501


        :return: The b_transmittance of this Glass.  # noqa: E501
        :rtype: float
        """
        return self._b_transmittance

    @b_transmittance.setter
    def b_transmittance(self, b_transmittance):
        """Sets the b_transmittance of this Glass.


        :param b_transmittance: The b_transmittance of this Glass.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and b_transmittance is None:  # noqa: E501
            raise ValueError("Invalid value for `b_transmittance`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                b_transmittance is not None and b_transmittance > 1.0):  # noqa: E501
            raise ValueError("Invalid value for `b_transmittance`, must be a value less than or equal to `1.0`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                b_transmittance is not None and b_transmittance < 0.0):  # noqa: E501
            raise ValueError("Invalid value for `b_transmittance`, must be a value greater than or equal to `0.0`")  # noqa: E501

        self._b_transmittance = b_transmittance

    @property
    def refraction_index(self):
        """Gets the refraction_index of this Glass.  # noqa: E501


        :return: The refraction_index of this Glass.  # noqa: E501
        :rtype: float
        """
        return self._refraction_index

    @refraction_index.setter
    def refraction_index(self, refraction_index):
        """Sets the refraction_index of this Glass.


        :param refraction_index: The refraction_index of this Glass.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and refraction_index is None:  # noqa: E501
            raise ValueError("Invalid value for `refraction_index`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                refraction_index is not None and refraction_index > 5.0):  # noqa: E501
            raise ValueError("Invalid value for `refraction_index`, must be a value less than or equal to `5.0`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                refraction_index is not None and refraction_index < 0.0):  # noqa: E501
            raise ValueError("Invalid value for `refraction_index`, must be a value greater than or equal to `0.0`")  # noqa: E501

        self._refraction_index = refraction_index

    @property
    def modifier(self):
        """Gets the modifier of this Glass.  # noqa: E501


        :return: The modifier of this Glass.  # noqa: E501
        :rtype: str
        """
        return self._modifier

    @modifier.setter
    def modifier(self, modifier):
        """Sets the modifier of this Glass.


        :param modifier: The modifier of this Glass.  # noqa: E501
        :type: str
        """

        self._modifier = modifier

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
        if not isinstance(other, Glass):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Glass):
            return True

        return self.to_dict() != other.to_dict()
