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


class SensorGridOut(object):
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
        'id': 'str',
        'name': 'str',
        'sensor_count': 'int',
        'created_at': 'str',
        'url': 'str',
        'sensors_url': 'str'
    }

    attribute_map = {
        'type': 'type',
        'id': 'id',
        'name': 'name',
        'sensor_count': 'sensor_count',
        'created_at': 'created_at',
        'url': 'url',
        'sensors_url': 'sensors_url'
    }

    def __init__(self, type='SensorGrid', id=None, name=None, sensor_count=None, created_at=None, url=None, sensors_url=None, local_vars_configuration=None):  # noqa: E501
        """SensorGridOut - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._id = None
        self._name = None
        self._sensor_count = None
        self._created_at = None
        self._url = None
        self._sensors_url = None
        self.discriminator = None

        if type is not None:
            self.type = type
        self.id = id
        self.name = name
        self.sensor_count = sensor_count
        if created_at is not None:
            self.created_at = created_at
        self.url = url
        self.sensors_url = sensors_url

    @property
    def type(self):
        """Gets the type of this SensorGridOut.  # noqa: E501


        :return: The type of this SensorGridOut.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SensorGridOut.


        :param type: The type of this SensorGridOut.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                type is not None and not re.search(r'SensorGrid', type)):  # noqa: E501
            raise ValueError(r"Invalid value for `type`, must be a follow pattern or equal to `/SensorGrid/`")  # noqa: E501

        self._type = type

    @property
    def id(self):
        """Gets the id of this SensorGridOut.  # noqa: E501

        Unique UUID value.  # noqa: E501

        :return: The id of this SensorGridOut.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SensorGridOut.

        Unique UUID value.  # noqa: E501

        :param id: The id of this SensorGridOut.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this SensorGridOut.  # noqa: E501


        :return: The name of this SensorGridOut.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SensorGridOut.


        :param name: The name of this SensorGridOut.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and not re.search(r'^[.A-Za-z0-9_-]*$', name)):  # noqa: E501
            raise ValueError(r"Invalid value for `name`, must be a follow pattern or equal to `/^[.A-Za-z0-9_-]*$/`")  # noqa: E501

        self._name = name

    @property
    def sensor_count(self):
        """Gets the sensor_count of this SensorGridOut.  # noqa: E501

        Total number of sensors.  # noqa: E501

        :return: The sensor_count of this SensorGridOut.  # noqa: E501
        :rtype: int
        """
        return self._sensor_count

    @sensor_count.setter
    def sensor_count(self, sensor_count):
        """Sets the sensor_count of this SensorGridOut.

        Total number of sensors.  # noqa: E501

        :param sensor_count: The sensor_count of this SensorGridOut.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and sensor_count is None:  # noqa: E501
            raise ValueError("Invalid value for `sensor_count`, must not be `None`")  # noqa: E501

        self._sensor_count = sensor_count

    @property
    def created_at(self):
        """Gets the created_at of this SensorGridOut.  # noqa: E501

        Sensor grid creation time.  # noqa: E501

        :return: The created_at of this SensorGridOut.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this SensorGridOut.

        Sensor grid creation time.  # noqa: E501

        :param created_at: The created_at of this SensorGridOut.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def url(self):
        """Gets the url of this SensorGridOut.  # noqa: E501

        URL to get sensors for this grid.  # noqa: E501

        :return: The url of this SensorGridOut.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this SensorGridOut.

        URL to get sensors for this grid.  # noqa: E501

        :param url: The url of this SensorGridOut.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and url is None:  # noqa: E501
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                url is not None and len(url) > 65536):
            raise ValueError("Invalid value for `url`, length must be less than or equal to `65536`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                url is not None and len(url) < 1):
            raise ValueError("Invalid value for `url`, length must be greater than or equal to `1`")  # noqa: E501

        self._url = url

    @property
    def sensors_url(self):
        """Gets the sensors_url of this SensorGridOut.  # noqa: E501

        URL to the sensor grid.  # noqa: E501

        :return: The sensors_url of this SensorGridOut.  # noqa: E501
        :rtype: str
        """
        return self._sensors_url

    @sensors_url.setter
    def sensors_url(self, sensors_url):
        """Sets the sensors_url of this SensorGridOut.

        URL to the sensor grid.  # noqa: E501

        :param sensors_url: The sensors_url of this SensorGridOut.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and sensors_url is None:  # noqa: E501
            raise ValueError("Invalid value for `sensors_url`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                sensors_url is not None and len(sensors_url) > 65536):
            raise ValueError("Invalid value for `sensors_url`, length must be less than or equal to `65536`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                sensors_url is not None and len(sensors_url) < 1):
            raise ValueError("Invalid value for `sensors_url`, length must be greater than or equal to `1`")  # noqa: E501

        self._sensors_url = sensors_url

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
        if not isinstance(other, SensorGridOut):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SensorGridOut):
            return True

        return self.to_dict() != other.to_dict()
