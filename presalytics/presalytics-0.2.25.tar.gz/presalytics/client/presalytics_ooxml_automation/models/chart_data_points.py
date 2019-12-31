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


class ChartDataPoints(object):
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
        'value': 'float',
        'column_id': 'str',
        'row_id': 'str',
        'chart_data_id': 'str',
        'id': 'str'
    }

    attribute_map = {
        'value': 'value',
        'column_id': 'columnId',
        'row_id': 'rowId',
        'chart_data_id': 'chartDataId',
        'id': 'id'
    }

    def __init__(self, value=None, column_id=None, row_id=None, chart_data_id=None, id=None, local_vars_configuration=None):  # noqa: E501
        """ChartDataPoints - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._value = None
        self._column_id = None
        self._row_id = None
        self._chart_data_id = None
        self._id = None
        self.discriminator = None

        if value is not None:
            self.value = value
        self.column_id = column_id
        self.row_id = row_id
        self.chart_data_id = chart_data_id
        if id is not None:
            self.id = id

    @property
    def value(self):
        """Gets the value of this ChartDataPoints.  # noqa: E501


        :return: The value of this ChartDataPoints.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ChartDataPoints.


        :param value: The value of this ChartDataPoints.  # noqa: E501
        :type: float
        """

        self._value = value

    @property
    def column_id(self):
        """Gets the column_id of this ChartDataPoints.  # noqa: E501


        :return: The column_id of this ChartDataPoints.  # noqa: E501
        :rtype: str
        """
        return self._column_id

    @column_id.setter
    def column_id(self, column_id):
        """Sets the column_id of this ChartDataPoints.


        :param column_id: The column_id of this ChartDataPoints.  # noqa: E501
        :type: str
        """

        self._column_id = column_id

    @property
    def row_id(self):
        """Gets the row_id of this ChartDataPoints.  # noqa: E501


        :return: The row_id of this ChartDataPoints.  # noqa: E501
        :rtype: str
        """
        return self._row_id

    @row_id.setter
    def row_id(self, row_id):
        """Sets the row_id of this ChartDataPoints.


        :param row_id: The row_id of this ChartDataPoints.  # noqa: E501
        :type: str
        """

        self._row_id = row_id

    @property
    def chart_data_id(self):
        """Gets the chart_data_id of this ChartDataPoints.  # noqa: E501


        :return: The chart_data_id of this ChartDataPoints.  # noqa: E501
        :rtype: str
        """
        return self._chart_data_id

    @chart_data_id.setter
    def chart_data_id(self, chart_data_id):
        """Sets the chart_data_id of this ChartDataPoints.


        :param chart_data_id: The chart_data_id of this ChartDataPoints.  # noqa: E501
        :type: str
        """

        self._chart_data_id = chart_data_id

    @property
    def id(self):
        """Gets the id of this ChartDataPoints.  # noqa: E501


        :return: The id of this ChartDataPoints.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ChartDataPoints.


        :param id: The id of this ChartDataPoints.  # noqa: E501
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
        if not isinstance(other, ChartDataPoints):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ChartDataPoints):
            return True

        return self.to_dict() != other.to_dict()
