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


class SharedSolidFills(object):
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
        'hex_value': 'str',
        'is_user_color': 'bool',
        'color_type_id': 'int',
        'fill_map_id': 'str',
        'parent_line_id': 'str',
        'parent_text_id': 'str',
        'parent_gradient_stop_id': 'str',
        'id': 'str'
    }

    attribute_map = {
        'hex_value': 'hexValue',
        'is_user_color': 'isUserColor',
        'color_type_id': 'colorTypeId',
        'fill_map_id': 'fillMapId',
        'parent_line_id': 'parentLineId',
        'parent_text_id': 'parentTextId',
        'parent_gradient_stop_id': 'parentGradientStopId',
        'id': 'id'
    }

    def __init__(self, hex_value=None, is_user_color=None, color_type_id=None, fill_map_id=None, parent_line_id=None, parent_text_id=None, parent_gradient_stop_id=None, id=None, local_vars_configuration=None):  # noqa: E501
        """SharedSolidFills - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._hex_value = None
        self._is_user_color = None
        self._color_type_id = None
        self._fill_map_id = None
        self._parent_line_id = None
        self._parent_text_id = None
        self._parent_gradient_stop_id = None
        self._id = None
        self.discriminator = None

        self.hex_value = hex_value
        if is_user_color is not None:
            self.is_user_color = is_user_color
        self.color_type_id = color_type_id
        self.fill_map_id = fill_map_id
        self.parent_line_id = parent_line_id
        self.parent_text_id = parent_text_id
        self.parent_gradient_stop_id = parent_gradient_stop_id
        if id is not None:
            self.id = id

    @property
    def hex_value(self):
        """Gets the hex_value of this SharedSolidFills.  # noqa: E501


        :return: The hex_value of this SharedSolidFills.  # noqa: E501
        :rtype: str
        """
        return self._hex_value

    @hex_value.setter
    def hex_value(self, hex_value):
        """Sets the hex_value of this SharedSolidFills.


        :param hex_value: The hex_value of this SharedSolidFills.  # noqa: E501
        :type: str
        """

        self._hex_value = hex_value

    @property
    def is_user_color(self):
        """Gets the is_user_color of this SharedSolidFills.  # noqa: E501


        :return: The is_user_color of this SharedSolidFills.  # noqa: E501
        :rtype: bool
        """
        return self._is_user_color

    @is_user_color.setter
    def is_user_color(self, is_user_color):
        """Sets the is_user_color of this SharedSolidFills.


        :param is_user_color: The is_user_color of this SharedSolidFills.  # noqa: E501
        :type: bool
        """

        self._is_user_color = is_user_color

    @property
    def color_type_id(self):
        """Gets the color_type_id of this SharedSolidFills.  # noqa: E501


        :return: The color_type_id of this SharedSolidFills.  # noqa: E501
        :rtype: int
        """
        return self._color_type_id

    @color_type_id.setter
    def color_type_id(self, color_type_id):
        """Sets the color_type_id of this SharedSolidFills.


        :param color_type_id: The color_type_id of this SharedSolidFills.  # noqa: E501
        :type: int
        """

        self._color_type_id = color_type_id

    @property
    def fill_map_id(self):
        """Gets the fill_map_id of this SharedSolidFills.  # noqa: E501


        :return: The fill_map_id of this SharedSolidFills.  # noqa: E501
        :rtype: str
        """
        return self._fill_map_id

    @fill_map_id.setter
    def fill_map_id(self, fill_map_id):
        """Sets the fill_map_id of this SharedSolidFills.


        :param fill_map_id: The fill_map_id of this SharedSolidFills.  # noqa: E501
        :type: str
        """

        self._fill_map_id = fill_map_id

    @property
    def parent_line_id(self):
        """Gets the parent_line_id of this SharedSolidFills.  # noqa: E501


        :return: The parent_line_id of this SharedSolidFills.  # noqa: E501
        :rtype: str
        """
        return self._parent_line_id

    @parent_line_id.setter
    def parent_line_id(self, parent_line_id):
        """Sets the parent_line_id of this SharedSolidFills.


        :param parent_line_id: The parent_line_id of this SharedSolidFills.  # noqa: E501
        :type: str
        """

        self._parent_line_id = parent_line_id

    @property
    def parent_text_id(self):
        """Gets the parent_text_id of this SharedSolidFills.  # noqa: E501


        :return: The parent_text_id of this SharedSolidFills.  # noqa: E501
        :rtype: str
        """
        return self._parent_text_id

    @parent_text_id.setter
    def parent_text_id(self, parent_text_id):
        """Sets the parent_text_id of this SharedSolidFills.


        :param parent_text_id: The parent_text_id of this SharedSolidFills.  # noqa: E501
        :type: str
        """

        self._parent_text_id = parent_text_id

    @property
    def parent_gradient_stop_id(self):
        """Gets the parent_gradient_stop_id of this SharedSolidFills.  # noqa: E501


        :return: The parent_gradient_stop_id of this SharedSolidFills.  # noqa: E501
        :rtype: str
        """
        return self._parent_gradient_stop_id

    @parent_gradient_stop_id.setter
    def parent_gradient_stop_id(self, parent_gradient_stop_id):
        """Sets the parent_gradient_stop_id of this SharedSolidFills.


        :param parent_gradient_stop_id: The parent_gradient_stop_id of this SharedSolidFills.  # noqa: E501
        :type: str
        """

        self._parent_gradient_stop_id = parent_gradient_stop_id

    @property
    def id(self):
        """Gets the id of this SharedSolidFills.  # noqa: E501


        :return: The id of this SharedSolidFills.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SharedSolidFills.


        :param id: The id of this SharedSolidFills.  # noqa: E501
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
        if not isinstance(other, SharedSolidFills):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SharedSolidFills):
            return True

        return self.to_dict() != other.to_dict()
