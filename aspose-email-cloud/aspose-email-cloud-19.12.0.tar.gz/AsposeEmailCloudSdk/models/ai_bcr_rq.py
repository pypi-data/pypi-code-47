#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="AiBcrRq.py">
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

from AsposeEmailCloudSdk.models.ai_bcr_options import AiBcrOptions


class AiBcrRq(object):
    """Business card recognition request             
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'options': 'AiBcrOptions'
    }

    attribute_map = {
        'options': 'options'
    }

    discriminator_value_class_map = {
        'AiBcrParseStorageRq': 'AiBcrParseStorageRq',
        'AiBcrStorageImageRq': 'AiBcrStorageImageRq',
        'AiBcrBase64Rq': 'AiBcrBase64Rq'
    }

    def __init__(self, options: AiBcrOptions = None):
        """AiBcrRq - a model defined in Swagger"""

        self._options = None
        self.discriminator = 'Type'

        if options is not None:
            self.options = options

    @property
    def options(self) -> AiBcrOptions:
        """Gets the options of this AiBcrRq.

        Recognition options             

        :return: The options of this AiBcrRq.
        :rtype: AiBcrOptions
        """
        return self._options

    @options.setter
    def options(self, options: AiBcrOptions):
        """Sets the options of this AiBcrRq.

        Recognition options             

        :param options: The options of this AiBcrRq.
        :type: AiBcrOptions
        """
        self._options = options

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_value = data.get(self.discriminator)
        return self.discriminator_value_class_map.get(discriminator_value.lower()) if discriminator_value else None

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
        if not isinstance(other, AiBcrRq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
