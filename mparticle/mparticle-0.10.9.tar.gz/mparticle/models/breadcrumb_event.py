# coding: utf-8

"""
    mParticle

    mParticle Event API

    OpenAPI spec version: 1.0.1
    Contact: support@mparticle.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class BreadcrumbEvent(object):

    def __init__(self, timestamp_unixtime_ms=None, event_id=None, source_message_id=None, session_id=None, session_uuid=None, custom_attributes=None, location=None, device_current_state=None, session_number=None, label=None):
        """
        BreadcrumbEvent - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'timestamp_unixtime_ms': 'int',
            'event_id': 'int',
            'source_message_id': 'str',
            'session_id': 'int',
            'session_uuid': 'str',
            'custom_attributes': 'dict(str, str)',
            'location': 'GeoLocation',
            'device_current_state': 'DeviceCurrentState',
            'session_number': 'int',
            'label': 'str'
        }

        self.attribute_map = {
            'timestamp_unixtime_ms': 'timestamp_unixtime_ms',
            'event_id': 'event_id',
            'source_message_id': 'source_message_id',
            'session_id': 'session_id',
            'session_uuid': 'session_uuid',
            'custom_attributes': 'custom_attributes',
            'location': 'location',
            'device_current_state': 'device_current_state',
            'session_number': 'session_number',
            'label': 'label'
        }

        self._timestamp_unixtime_ms = timestamp_unixtime_ms
        self._event_id = event_id
        self._source_message_id = source_message_id
        self._session_id = session_id
        self._session_uuid = session_uuid
        self._custom_attributes = custom_attributes
        self._location = location
        self._device_current_state = device_current_state
        self._session_number = session_number
        self._label = label

    @property
    def timestamp_unixtime_ms(self):
        """
        Gets the timestamp_unixtime_ms of this BreadcrumbEvent.


        :return: The timestamp_unixtime_ms of this BreadcrumbEvent.
        :rtype: int
        """
        return self._timestamp_unixtime_ms

    @timestamp_unixtime_ms.setter
    def timestamp_unixtime_ms(self, timestamp_unixtime_ms):
        """
        Sets the timestamp_unixtime_ms of this BreadcrumbEvent.


        :param timestamp_unixtime_ms: The timestamp_unixtime_ms of this BreadcrumbEvent.
        :type: int
        """

        self._timestamp_unixtime_ms = timestamp_unixtime_ms

    @property
    def event_id(self):
        """
        Gets the event_id of this BreadcrumbEvent.


        :return: The event_id of this BreadcrumbEvent.
        :rtype: int
        """
        return self._event_id

    @event_id.setter
    def event_id(self, event_id):
        """
        Sets the event_id of this BreadcrumbEvent.


        :param event_id: The event_id of this BreadcrumbEvent.
        :type: int
        """

        self._event_id = event_id

    @property
    def source_message_id(self):
        """
        Gets the source_message_id of this BreadcrumbEvent.


        :return: The source_message_id of this BreadcrumbEvent.
        :rtype: str
        """
        return self._source_message_id

    @source_message_id.setter
    def source_message_id(self, source_message_id):
        """
        Sets the source_message_id of this BreadcrumbEvent.


        :param source_message_id: The source_message_id of this BreadcrumbEvent.
        :type: str
        """

        self._source_message_id = source_message_id

    @property
    def session_id(self):
        """
        Gets the session_id of this BreadcrumbEvent.


        :return: The session_id of this BreadcrumbEvent.
        :rtype: int
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        """
        Sets the session_id of this BreadcrumbEvent.


        :param session_id: The session_id of this BreadcrumbEvent.
        :type: int
        """

        self._session_id = session_id

    @property
    def session_uuid(self):
        """
        Gets the session_uuid of this BreadcrumbEvent.


        :return: The session_uuid of this BreadcrumbEvent.
        :rtype: str
        """
        return self._session_uuid

    @session_uuid.setter
    def session_uuid(self, session_uuid):
        """
        Sets the session_uuid of this BreadcrumbEvent.


        :param session_uuid: The session_uuid of this BreadcrumbEvent.
        :type: str
        """

        self._session_uuid = session_uuid

    @property
    def custom_attributes(self):
        """
        Gets the custom_attributes of this BreadcrumbEvent.


        :return: The custom_attributes of this BreadcrumbEvent.
        :rtype: dict(str, str)
        """
        return self._custom_attributes

    @custom_attributes.setter
    def custom_attributes(self, custom_attributes):
        """
        Sets the custom_attributes of this BreadcrumbEvent.


        :param custom_attributes: The custom_attributes of this BreadcrumbEvent.
        :type: dict(str, str)
        """

        self._custom_attributes = custom_attributes

    @property
    def location(self):
        """
        Gets the location of this BreadcrumbEvent.


        :return: The location of this BreadcrumbEvent.
        :rtype: GeoLocation
        """
        return self._location

    @location.setter
    def location(self, location):
        """
        Sets the location of this BreadcrumbEvent.


        :param location: The location of this BreadcrumbEvent.
        :type: GeoLocation
        """

        self._location = location

    @property
    def device_current_state(self):
        """
        Gets the device_current_state of this BreadcrumbEvent.


        :return: The device_current_state of this BreadcrumbEvent.
        :rtype: DeviceCurrentState
        """
        return self._device_current_state

    @device_current_state.setter
    def device_current_state(self, device_current_state):
        """
        Sets the device_current_state of this BreadcrumbEvent.


        :param device_current_state: The device_current_state of this BreadcrumbEvent.
        :type: DeviceCurrentState
        """

        self._device_current_state = device_current_state

    @property
    def session_number(self):
        """
        Gets the session_number of this BreadcrumbEvent.


        :return: The session_number of this BreadcrumbEvent.
        :rtype: int
        """
        return self._session_number

    @session_number.setter
    def session_number(self, session_number):
        """
        Sets the session_number of this BreadcrumbEvent.


        :param session_number: The session_number of this BreadcrumbEvent.
        :type: int
        """

        self._session_number = session_number

    @property
    def label(self):
        """
        Gets the label of this BreadcrumbEvent.


        :return: The label of this BreadcrumbEvent.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """
        Sets the label of this BreadcrumbEvent.


        :param label: The label of this BreadcrumbEvent.
        :type: str
        """

        self._label = label

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
