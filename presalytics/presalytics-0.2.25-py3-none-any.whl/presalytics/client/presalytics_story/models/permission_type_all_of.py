# coding: utf-8

"""
    Story

    This API is the main entry point for creating, editing and publishing analytics throught the Presalytics API  # noqa: E501

    The version of the OpenAPI document: 0.3.1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from presalytics.client.presalytics_story.configuration import Configuration


class PermissionTypeAllOf(object):
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
        'name': 'str',
        'can_edit': 'bool',
        'can_view': 'bool',
        'can_add_collaborators': 'bool',
        'can_delete': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'can_edit': 'can_edit',
        'can_view': 'can_view',
        'can_add_collaborators': 'can_add_collaborators',
        'can_delete': 'can_delete'
    }

    def __init__(self, name=None, can_edit=None, can_view=None, can_add_collaborators=None, can_delete=None, local_vars_configuration=None):  # noqa: E501
        """PermissionTypeAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._can_edit = None
        self._can_view = None
        self._can_add_collaborators = None
        self._can_delete = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if can_edit is not None:
            self.can_edit = can_edit
        if can_view is not None:
            self.can_view = can_view
        if can_add_collaborators is not None:
            self.can_add_collaborators = can_add_collaborators
        if can_delete is not None:
            self.can_delete = can_delete

    @property
    def name(self):
        """Gets the name of this PermissionTypeAllOf.  # noqa: E501


        :return: The name of this PermissionTypeAllOf.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PermissionTypeAllOf.


        :param name: The name of this PermissionTypeAllOf.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def can_edit(self):
        """Gets the can_edit of this PermissionTypeAllOf.  # noqa: E501


        :return: The can_edit of this PermissionTypeAllOf.  # noqa: E501
        :rtype: bool
        """
        return self._can_edit

    @can_edit.setter
    def can_edit(self, can_edit):
        """Sets the can_edit of this PermissionTypeAllOf.


        :param can_edit: The can_edit of this PermissionTypeAllOf.  # noqa: E501
        :type: bool
        """

        self._can_edit = can_edit

    @property
    def can_view(self):
        """Gets the can_view of this PermissionTypeAllOf.  # noqa: E501


        :return: The can_view of this PermissionTypeAllOf.  # noqa: E501
        :rtype: bool
        """
        return self._can_view

    @can_view.setter
    def can_view(self, can_view):
        """Sets the can_view of this PermissionTypeAllOf.


        :param can_view: The can_view of this PermissionTypeAllOf.  # noqa: E501
        :type: bool
        """

        self._can_view = can_view

    @property
    def can_add_collaborators(self):
        """Gets the can_add_collaborators of this PermissionTypeAllOf.  # noqa: E501


        :return: The can_add_collaborators of this PermissionTypeAllOf.  # noqa: E501
        :rtype: bool
        """
        return self._can_add_collaborators

    @can_add_collaborators.setter
    def can_add_collaborators(self, can_add_collaborators):
        """Sets the can_add_collaborators of this PermissionTypeAllOf.


        :param can_add_collaborators: The can_add_collaborators of this PermissionTypeAllOf.  # noqa: E501
        :type: bool
        """

        self._can_add_collaborators = can_add_collaborators

    @property
    def can_delete(self):
        """Gets the can_delete of this PermissionTypeAllOf.  # noqa: E501


        :return: The can_delete of this PermissionTypeAllOf.  # noqa: E501
        :rtype: bool
        """
        return self._can_delete

    @can_delete.setter
    def can_delete(self, can_delete):
        """Sets the can_delete of this PermissionTypeAllOf.


        :param can_delete: The can_delete of this PermissionTypeAllOf.  # noqa: E501
        :type: bool
        """

        self._can_delete = can_delete

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
        if not isinstance(other, PermissionTypeAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PermissionTypeAllOf):
            return True

        return self.to_dict() != other.to_dict()
