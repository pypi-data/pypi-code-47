# coding: utf-8

"""
    OOXML Automation

    This API helps users convert Excel and Powerpoint documents into rich, live dashboards and stories.  # noqa: E501

    The version of the OpenAPI document: 0.1.0-no-tags
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from presalytics.client.presalytics_ooxml_automation.configuration import Configuration


class SharedEffectAttributes(object):
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
        'effect_type_id': 'int',
        'attributes_json': 'str',
        'effect_id': 'str',
        'id': 'str'
    }

    attribute_map = {
        'effect_type_id': 'effectTypeId',
        'attributes_json': 'attributesJson',
        'effect_id': 'effectId',
        'id': 'id'
    }

    def __init__(self, effect_type_id=None, attributes_json=None, effect_id=None, id=None, local_vars_configuration=None):  # noqa: E501
        """SharedEffectAttributes - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._effect_type_id = None
        self._attributes_json = None
        self._effect_id = None
        self._id = None
        self.discriminator = None

        if effect_type_id is not None:
            self.effect_type_id = effect_type_id
        self.attributes_json = attributes_json
        self.effect_id = effect_id
        if id is not None:
            self.id = id

    @property
    def effect_type_id(self):
        """Gets the effect_type_id of this SharedEffectAttributes.  # noqa: E501


        :return: The effect_type_id of this SharedEffectAttributes.  # noqa: E501
        :rtype: int
        """
        return self._effect_type_id

    @effect_type_id.setter
    def effect_type_id(self, effect_type_id):
        """Sets the effect_type_id of this SharedEffectAttributes.


        :param effect_type_id: The effect_type_id of this SharedEffectAttributes.  # noqa: E501
        :type: int
        """

        self._effect_type_id = effect_type_id

    @property
    def attributes_json(self):
        """Gets the attributes_json of this SharedEffectAttributes.  # noqa: E501


        :return: The attributes_json of this SharedEffectAttributes.  # noqa: E501
        :rtype: str
        """
        return self._attributes_json

    @attributes_json.setter
    def attributes_json(self, attributes_json):
        """Sets the attributes_json of this SharedEffectAttributes.


        :param attributes_json: The attributes_json of this SharedEffectAttributes.  # noqa: E501
        :type: str
        """

        self._attributes_json = attributes_json

    @property
    def effect_id(self):
        """Gets the effect_id of this SharedEffectAttributes.  # noqa: E501


        :return: The effect_id of this SharedEffectAttributes.  # noqa: E501
        :rtype: str
        """
        return self._effect_id

    @effect_id.setter
    def effect_id(self, effect_id):
        """Sets the effect_id of this SharedEffectAttributes.


        :param effect_id: The effect_id of this SharedEffectAttributes.  # noqa: E501
        :type: str
        """

        self._effect_id = effect_id

    @property
    def id(self):
        """Gets the id of this SharedEffectAttributes.  # noqa: E501


        :return: The id of this SharedEffectAttributes.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SharedEffectAttributes.


        :param id: The id of this SharedEffectAttributes.  # noqa: E501
        :type: str
        """

        self._id = id

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
        if not isinstance(other, SharedEffectAttributes):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SharedEffectAttributes):
            return True

        return self.to_dict() != other.to_dict()
