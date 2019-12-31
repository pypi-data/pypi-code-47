#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="EmailDocument.py">
#    Copyright (c) 2018-2019 Aspose Pty Ltd. All rights reserved.
#  </copyright>
#  <summary>
#    Permission is hereby granted, free of charge, to any person obtaining a
#   copy  of this software and associated documentation files (the "Software"),
#   to deal  in the Software without restriction, including without limitation
#   the rights  to use, copy, modify, merge, publish, distribute, sublicense,
#   and/or sell  copies of the Software, and to permit persons to whom the
#   Software is  furnished to do so, subject to the following conditions:
#
#   The above copyright notice and this permission notice shall be included in
#   all  copies or substantial portions of the Software.
#
#   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#   IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#   FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#   AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#   LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#   FROM,  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#   DEALINGS IN THE SOFTWARE.
#  </summary>
#  ----------------------------------------------------------------------------

import pprint
import re
import six
from typing import List, Set, Dict, Tuple, Optional
from datetime import datetime

from AsposeEmailCloudSdk.models.email_properties import EmailProperties
from AsposeEmailCloudSdk.models.link import Link


class EmailDocument(object):
    """Represents Email document DTO.             
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'links': 'list[Link]',
        'document_properties': 'EmailProperties'
    }

    attribute_map = {
        'links': 'links',
        'document_properties': 'documentProperties'
    }

    def __init__(self, links: List[Link] = None, document_properties: EmailProperties = None):
        """EmailDocument - a model defined in Swagger"""

        self._links = None
        self._document_properties = None
        self.discriminator = None

        if links is not None:
            self.links = links
        if document_properties is not None:
            self.document_properties = document_properties

    @property
    def links(self) -> List[Link]:
        """Gets the links of this EmailDocument.

        Links that originate from this document.             

        :return: The links of this EmailDocument.
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links: List[Link]):
        """Sets the links of this EmailDocument.

        Links that originate from this document.             

        :param links: The links of this EmailDocument.
        :type: list[Link]
        """
        self._links = links

    @property
    def document_properties(self) -> EmailProperties:
        """Gets the document_properties of this EmailDocument.

        List of document properties.             

        :return: The document_properties of this EmailDocument.
        :rtype: EmailProperties
        """
        return self._document_properties

    @document_properties.setter
    def document_properties(self, document_properties: EmailProperties):
        """Sets the document_properties of this EmailDocument.

        List of document properties.             

        :param document_properties: The document_properties of this EmailDocument.
        :type: EmailProperties
        """
        if document_properties is None:
            raise ValueError("Invalid value for `document_properties`, must not be `None`")
        self._document_properties = document_properties

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if not isinstance(other, EmailDocument):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
