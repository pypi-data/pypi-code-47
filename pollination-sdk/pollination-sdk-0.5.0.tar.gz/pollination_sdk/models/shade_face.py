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


class ShadeFace(object):
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
        'id': 'str',
        'name': 'str',
        'vertices': 'list[Vertex]',
        'face_type': 'str',
        'rad_modifier': 'object',
        'rad_modifier_dir': 'object',
        'type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'vertices': 'vertices',
        'face_type': 'face_type',
        'rad_modifier': 'rad_modifier',
        'rad_modifier_dir': 'rad_modifier_dir',
        'type': 'type'
    }

    def __init__(self, id=None, name=None, vertices=None, face_type=None, rad_modifier=None, rad_modifier_dir=None, type=None, local_vars_configuration=None):  # noqa: E501
        """ShadeFace - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._vertices = None
        self._face_type = None
        self._rad_modifier = None
        self._rad_modifier_dir = None
        self._type = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name = name
        self.vertices = vertices
        self.face_type = face_type
        if rad_modifier is not None:
            self.rad_modifier = rad_modifier
        if rad_modifier_dir is not None:
            self.rad_modifier_dir = rad_modifier_dir
        self.type = type

    @property
    def id(self):
        """Gets the id of this ShadeFace.  # noqa: E501

        Unique UUID value.  # noqa: E501

        :return: The id of this ShadeFace.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShadeFace.

        Unique UUID value.  # noqa: E501

        :param id: The id of this ShadeFace.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ShadeFace.  # noqa: E501


        :return: The name of this ShadeFace.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShadeFace.


        :param name: The name of this ShadeFace.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and not re.search(r'^[.A-Za-z0-9_-]*$', name)):  # noqa: E501
            raise ValueError(r"Invalid value for `name`, must be a follow pattern or equal to `/^[.A-Za-z0-9_-]*$/`")  # noqa: E501

        self._name = name

    @property
    def vertices(self):
        """Gets the vertices of this ShadeFace.  # noqa: E501


        :return: The vertices of this ShadeFace.  # noqa: E501
        :rtype: list[Vertex]
        """
        return self._vertices

    @vertices.setter
    def vertices(self, vertices):
        """Sets the vertices of this ShadeFace.


        :param vertices: The vertices of this ShadeFace.  # noqa: E501
        :type: list[Vertex]
        """
        if self.local_vars_configuration.client_side_validation and vertices is None:  # noqa: E501
            raise ValueError("Invalid value for `vertices`, must not be `None`")  # noqa: E501

        self._vertices = vertices

    @property
    def face_type(self):
        """Gets the face_type of this ShadeFace.  # noqa: E501


        :return: The face_type of this ShadeFace.  # noqa: E501
        :rtype: str
        """
        return self._face_type

    @face_type.setter
    def face_type(self, face_type):
        """Sets the face_type of this ShadeFace.


        :param face_type: The face_type of this ShadeFace.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and face_type is None:  # noqa: E501
            raise ValueError("Invalid value for `face_type`, must not be `None`")  # noqa: E501
        allowed_values = ["Shading"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and face_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `face_type` ({0}), must be one of {1}"  # noqa: E501
                .format(face_type, allowed_values)
            )

        self._face_type = face_type

    @property
    def rad_modifier(self):
        """Gets the rad_modifier of this ShadeFace.  # noqa: E501


        :return: The rad_modifier of this ShadeFace.  # noqa: E501
        :rtype: object
        """
        return self._rad_modifier

    @rad_modifier.setter
    def rad_modifier(self, rad_modifier):
        """Sets the rad_modifier of this ShadeFace.


        :param rad_modifier: The rad_modifier of this ShadeFace.  # noqa: E501
        :type: object
        """

        self._rad_modifier = rad_modifier

    @property
    def rad_modifier_dir(self):
        """Gets the rad_modifier_dir of this ShadeFace.  # noqa: E501


        :return: The rad_modifier_dir of this ShadeFace.  # noqa: E501
        :rtype: object
        """
        return self._rad_modifier_dir

    @rad_modifier_dir.setter
    def rad_modifier_dir(self, rad_modifier_dir):
        """Sets the rad_modifier_dir of this ShadeFace.


        :param rad_modifier_dir: The rad_modifier_dir of this ShadeFace.  # noqa: E501
        :type: object
        """

        self._rad_modifier_dir = rad_modifier_dir

    @property
    def type(self):
        """Gets the type of this ShadeFace.  # noqa: E501


        :return: The type of this ShadeFace.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ShadeFace.


        :param type: The type of this ShadeFace.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["ShadeFace"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

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
        if not isinstance(other, ShadeFace):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ShadeFace):
            return True

        return self.to_dict() != other.to_dict()
