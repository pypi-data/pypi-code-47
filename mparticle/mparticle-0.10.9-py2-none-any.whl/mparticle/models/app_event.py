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
import mparticle


class AppEvent(object):

    def __init__(self, event_name=None, custom_event_type='other',
                 timestamp_unixtime_ms=None, event_id=None,
                 source_message_id=None, session_id=None,
                 session_uuid=None, custom_attributes=None,
                 location=None, device_current_state=None,
                 media_info=None, custom_flags=None):
        """
        AppEvent - a model defined in Swagger

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
            'custom_event_type': 'str',
            'event_name': 'str',
            'media_info': 'MediaInfo',
            'custom_flags': 'dict(str, str)'
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
            'custom_event_type': 'custom_event_type',
            'event_name': 'event_name',
            'media_info': 'media_info',
            'custom_flags': 'custom_flags',
        }

        self._timestamp_unixtime_ms = timestamp_unixtime_ms
        self._event_id = event_id
        self._source_message_id = source_message_id
        self._session_id = session_id
        self._session_uuid = session_uuid
        self.custom_attributes = custom_attributes
        self._location = location
        self._device_current_state = device_current_state
        self._custom_event_type = custom_event_type
        if event_name is None:
            raise ValueError(
                "Event Name is required."
            )
        self._event_name = event_name
        self._media_info = media_info
        self._custom_flags = custom_flags

    @classmethod
    def create_attribution_event(cls, publisher=None, campaign=None):
        return cls(
            event_name='attribution',
            custom_event_type='attribution',
            custom_attributes={'campaign': campaign, 'publisher': publisher}
        )

    @classmethod
    def create_attribution_delete_event(cls):
        return cls(
            event_name='attribution',
            custom_event_type='attribution',
            custom_attributes={'action': 'delete'}
        )

    @property
    def timestamp_unixtime_ms(self):
        """
        Gets the timestamp_unixtime_ms of this AppEvent.


        :return: The timestamp_unixtime_ms of this AppEvent.
        :rtype: int
        """
        return self._timestamp_unixtime_ms

    @timestamp_unixtime_ms.setter
    def timestamp_unixtime_ms(self, timestamp_unixtime_ms):
        """
        Sets the timestamp_unixtime_ms of this AppEvent.


        :param timestamp_unixtime_ms: The timestamp_unixtime_ms of this AppEvent.
        :type: int
        """

        self._timestamp_unixtime_ms = timestamp_unixtime_ms

    @property
    def event_id(self):
        """
        Gets the event_id of this AppEvent.


        :return: The event_id of this AppEvent.
        :rtype: int
        """
        return self._event_id

    @event_id.setter
    def event_id(self, event_id):
        """
        Sets the event_id of this AppEvent.


        :param event_id: The event_id of this AppEvent.
        :type: int
        """

        self._event_id = event_id

    @property
    def source_message_id(self):
        """
        Gets the source_message_id of this AppEvent.


        :return: The source_message_id of this AppEvent.
        :rtype: str
        """
        return self._source_message_id

    @source_message_id.setter
    def source_message_id(self, source_message_id):
        """
        Sets the source_message_id of this AppEvent.


        :param source_message_id: The source_message_id of this AppEvent.
        :type: str
        """

        self._source_message_id = source_message_id

    @property
    def session_id(self):
        """
        Gets the session_id of this AppEvent.


        :return: The session_id of this AppEvent.
        :rtype: int
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        """
        Sets the session_id of this AppEvent.


        :param session_id: The session_id of this AppEvent.
        :type: int
        """

        self._session_id = session_id

    @property
    def session_uuid(self):
        """
        Gets the session_uuid of this AppEvent.


        :return: The session_uuid of this AppEvent.
        :rtype: str
        """
        return self._session_uuid

    @session_uuid.setter
    def session_uuid(self, session_uuid):
        """
        Sets the session_uuid of this AppEvent.


        :param session_uuid: The session_uuid of this AppEvent.
        :type: str
        """

        self._session_uuid = session_uuid

    @property
    def custom_attributes(self):
        """
        Gets the custom_attributes of this AppEvent.


        :return: The custom_attributes of this AppEvent.
        :rtype: dict(str, str)
        """
        return self._custom_attributes

    @custom_attributes.setter
    def custom_attributes(self, custom_attributes):
        """
        Sets the custom_attributes of this AppEvent.


        :param custom_attributes: The custom_attributes of this AppEvent.
        :type: dict(str, str)
        """

        if not mparticle.ApiClient.validate_attribute_bag_values(custom_attributes):
            raise ValueError(
                "Invalid custom_attributes passed to AppEvent: " + str(custom_attributes))

        self._custom_attributes = custom_attributes

    @property
    def location(self):
        """
        Gets the location of this AppEvent.


        :return: The location of this AppEvent.
        :rtype: GeoLocation
        """
        return self._location

    @location.setter
    def location(self, location):
        """
        Sets the location of this AppEvent.


        :param location: The location of this AppEvent.
        :type: GeoLocation
        """

        self._location = location

    @property
    def device_current_state(self):
        """
        Gets the device_current_state of this AppEvent.


        :return: The device_current_state of this AppEvent.
        :rtype: DeviceCurrentState
        """
        return self._device_current_state

    @device_current_state.setter
    def device_current_state(self, device_current_state):
        """
        Sets the device_current_state of this AppEvent.


        :param device_current_state: The device_current_state of this AppEvent.
        :type: DeviceCurrentState
        """

        self._device_current_state = device_current_state

    @property
    def custom_event_type(self):
        """
        Gets the custom_event_type of this AppEvent.


        :return: The custom_event_type of this AppEvent.
        :rtype: str
        """
        return self._custom_event_type

    @custom_event_type.setter
    def custom_event_type(self, custom_event_type):
        """
        Sets the custom_event_type of this AppEvent.


        :param custom_event_type: The custom_event_type of this AppEvent.
        :type: str
        """
        allowed_values = ["unknown", "navigation", "location", "search", "transaction",
                          "user_content", "user_preference", "social", "other", "attribution"]
        if custom_event_type not in allowed_values:
            raise ValueError(
                "Invalid value for `custom_event_type` ({0}), must be one of {1}"
                .format(custom_event_type, allowed_values)
            )

        self._custom_event_type = custom_event_type

    @property
    def event_name(self):
        """
        Gets the event_name of this AppEvent.


        :return: The event_name of this AppEvent.
        :rtype: str
        """
        return self._event_name

    @event_name.setter
    def event_name(self, event_name):
        """
        Sets the event_name of this AppEvent.


        :param event_name: The event_name of this AppEvent.
        :type: str
        """

        self._event_name = event_name

    @property
    def media_info(self):
        """
        Gets the media_info of this AppEvent.


        :return: The media_info of this AppEvent.
        :rtype: MediaInfo
        """
        return self._media_info

    @media_info.setter
    def media_info(self, media_info):
        """
        Sets the media_info of this AppEvent.


        :param media_info: The media_info of this AppEvent.
        :type: MediaInfo
        """

        self._media_info = media_info

    @property
    def ltv_amount(self):
        """
        Gets the ltv_amount of this AppEvent.


        :return: The ltv_amount of this AppEvent.
        :rtype: int
        """
        return self._ltv_amount

    @ltv_amount.setter
    def ltv_amount(self, ltv_amount):
        """
        Sets the ltv_amount of this AppEvent.


        :param ltv_amount: The ltv_amount of this AppEvent.
        :type: int
        """
        self._ltv_amount = ltv_amount

        if self.ltv_amount is not None:
            if self._custom_attributes is None:
                self._custom_attributes = {}
            self._custom_attributes["$Amount"] = self.ltv_amount
            self._custom_attributes["MethodName"] = "LogLTVIncrease"
        elif self.custom_attributes is not None:
            self._custom_attributes.pop("$Amount", None)
            self._custom_attributes.pop("MethodName", None)

    @property
    def custom_flags(self):
        """
        Gets the custom_flags of this AppEvent.


        :return: The custom_flags of this AppEvent.
        :rtype: dict(str, str)
        """
        return self._custom_flags

    @custom_flags.setter
    def custom_flags(self, custom_flags):
        """
        Sets the custom_flags of this AppEvent.


        :param custom_flags: The custom_flags of this AppEvent.
        :type: dict(str, str)
        """

        self._custom_flags = custom_flags

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
