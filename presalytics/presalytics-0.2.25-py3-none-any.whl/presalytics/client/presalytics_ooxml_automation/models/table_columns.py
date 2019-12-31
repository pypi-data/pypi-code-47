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


class TableColumns(object):
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
        'index': 'int',
        'width': 'int',
        'table_id': 'str',
        'id': 'str'
    }

    attribute_map = {
        'index': 'index',
        'width': 'width',
        'table_id': 'tableId',
        'id': 'id'
    }

    def __init__(self, index=None, width=None, table_id=None, id=None, local_vars_configuration=None):  # noqa: E501
        """TableColumns - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._index = None
        self._width = None
        self._table_id = None
        self._id = None
        self.discriminator = None

        if index is not None:
            self.index = index
        if width is not None:
            self.width = width
        self.table_id = table_id
        if id is not None:
            self.id = id

    @property
    def index(self):
        """Gets the index of this TableColumns.  # noqa: E501


        :return: The index of this TableColumns.  # noqa: E501
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this TableColumns.


        :param index: The index of this TableColumns.  # noqa: E501
        :type: int
        """

        self._index = index

    @property
    def width(self):
        """Gets the width of this TableColumns.  # noqa: E501


        :return: The width of this TableColumns.  # noqa: E501
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this TableColumns.


        :param width: The width of this TableColumns.  # noqa: E501
        :type: int
        """

        self._width = width

    @property
    def table_id(self):
        """Gets the table_id of this TableColumns.  # noqa: E501


        :return: The table_id of this TableColumns.  # noqa: E501
        :rtype: str
        """
        return self._table_id

    @table_id.setter
    def table_id(self, table_id):
        """Sets the table_id of this TableColumns.


        :param table_id: The table_id of this TableColumns.  # noqa: E501
        :type: str
        """

        self._table_id = table_id

    @property
    def id(self):
        """Gets the id of this TableColumns.  # noqa: E501


        :return: The id of this TableColumns.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TableColumns.


        :param id: The id of this TableColumns.  # noqa: E501
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
        if not isinstance(other, TableColumns):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TableColumns):
            return True

        return self.to_dict() != other.to_dict()
