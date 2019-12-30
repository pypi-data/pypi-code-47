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


class AttributionInfo(object):

    def __init__(self, service_provider=None, publisher=None, campaign=None):
        """
        AttributionInfo - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'service_provider': 'str',
            'publisher': 'str',
            'campaign': 'str'
        }

        self.attribute_map = {
            'service_provider': 'service_provider',
            'publisher': 'publisher',
            'campaign': 'campaign'
        }

        self._service_provider = service_provider
        self._publisher = publisher
        self._campaign = campaign

    @property
    def service_provider(self):
        """
        Gets the service_provider of this AttributionInfo.


        :return: The service_provider of this AttributionInfo.
        :rtype: str
        """
        return self._service_provider

    @service_provider.setter
    def service_provider(self, service_provider):
        """
        Sets the service_provider of this AttributionInfo.


        :param service_provider: The service_provider of this AttributionInfo.
        :type: str
        """

        self._service_provider = service_provider

    @property
    def publisher(self):
        """
        Gets the publisher of this AttributionInfo.


        :return: The publisher of this AttributionInfo.
        :rtype: str
        """
        return self._publisher

    @publisher.setter
    def publisher(self, publisher):
        """
        Sets the publisher of this AttributionInfo.


        :param publisher: The publisher of this AttributionInfo.
        :type: str
        """

        self._publisher = publisher

    @property
    def campaign(self):
        """
        Gets the campaign of this AttributionInfo.


        :return: The campaign of this AttributionInfo.
        :rtype: str
        """
        return self._campaign

    @campaign.setter
    def campaign(self, campaign):
        """
        Sets the campaign of this AttributionInfo.


        :param campaign: The campaign of this AttributionInfo.
        :type: str
        """

        self._campaign = campaign

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
