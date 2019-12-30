# coding: utf-8

"""
    Red Rover API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Contact: contact@edustaff.org
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from redrover_api.configuration import Configuration


class AdministratorDto(object):
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
        'role': 'int',
        'is_super_user': 'bool',
        'access_control': 'AccessControlDto',
        'org_id': 'int',
        'row_version': 'int',
        'id': 'int',
        'external_id': 'str',
        'first_name': 'str',
        'middle_name': 'str',
        'last_name': 'str',
        'email': 'str',
        'date_of_birth': 'datetime',
        'address1': 'str',
        'address2': 'str',
        'city': 'str',
        'postal_code': 'str',
        'state_id': 'int',
        'country_id': 'int',
        'phone_number': 'str',
        'active': 'bool',
        'permission_set': 'LocatorInt32',
        'related_org_ids': 'list[int]',
        'invite_immediately': 'bool'
    }

    attribute_map = {
        'role': 'role',
        'is_super_user': 'isSuperUser',
        'access_control': 'accessControl',
        'org_id': 'orgId',
        'row_version': 'rowVersion',
        'id': 'id',
        'external_id': 'externalId',
        'first_name': 'firstName',
        'middle_name': 'middleName',
        'last_name': 'lastName',
        'email': 'email',
        'date_of_birth': 'dateOfBirth',
        'address1': 'address1',
        'address2': 'address2',
        'city': 'city',
        'postal_code': 'postalCode',
        'state_id': 'stateId',
        'country_id': 'countryId',
        'phone_number': 'phoneNumber',
        'active': 'active',
        'permission_set': 'permissionSet',
        'related_org_ids': 'relatedOrgIds',
        'invite_immediately': 'inviteImmediately'
    }

    def __init__(self, role=None, is_super_user=None, access_control=None, org_id=None, row_version=None, id=None, external_id=None, first_name=None, middle_name=None, last_name=None, email=None, date_of_birth=None, address1=None, address2=None, city=None, postal_code=None, state_id=None, country_id=None, phone_number=None, active=None, permission_set=None, related_org_ids=None, invite_immediately=None, local_vars_configuration=None):  # noqa: E501
        """AdministratorDto - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._role = None
        self._is_super_user = None
        self._access_control = None
        self._org_id = None
        self._row_version = None
        self._id = None
        self._external_id = None
        self._first_name = None
        self._middle_name = None
        self._last_name = None
        self._email = None
        self._date_of_birth = None
        self._address1 = None
        self._address2 = None
        self._city = None
        self._postal_code = None
        self._state_id = None
        self._country_id = None
        self._phone_number = None
        self._active = None
        self._permission_set = None
        self._related_org_ids = None
        self._invite_immediately = None
        self.discriminator = None

        if role is not None:
            self.role = role
        if is_super_user is not None:
            self.is_super_user = is_super_user
        if access_control is not None:
            self.access_control = access_control
        if org_id is not None:
            self.org_id = org_id
        if row_version is not None:
            self.row_version = row_version
        if id is not None:
            self.id = id
        if external_id is not None:
            self.external_id = external_id
        if first_name is not None:
            self.first_name = first_name
        if middle_name is not None:
            self.middle_name = middle_name
        if last_name is not None:
            self.last_name = last_name
        if email is not None:
            self.email = email
        if date_of_birth is not None:
            self.date_of_birth = date_of_birth
        if address1 is not None:
            self.address1 = address1
        if address2 is not None:
            self.address2 = address2
        if city is not None:
            self.city = city
        if postal_code is not None:
            self.postal_code = postal_code
        if state_id is not None:
            self.state_id = state_id
        if country_id is not None:
            self.country_id = country_id
        if phone_number is not None:
            self.phone_number = phone_number
        if active is not None:
            self.active = active
        if permission_set is not None:
            self.permission_set = permission_set
        if related_org_ids is not None:
            self.related_org_ids = related_org_ids
        if invite_immediately is not None:
            self.invite_immediately = invite_immediately

    @property
    def role(self):
        """Gets the role of this AdministratorDto.  # noqa: E501


        :return: The role of this AdministratorDto.  # noqa: E501
        :rtype: int
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this AdministratorDto.


        :param role: The role of this AdministratorDto.  # noqa: E501
        :type: int
        """
        allowed_values = [0, 1, 2, 3, 4, 5]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and role not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `role` ({0}), must be one of {1}"  # noqa: E501
                .format(role, allowed_values)
            )

        self._role = role

    @property
    def is_super_user(self):
        """Gets the is_super_user of this AdministratorDto.  # noqa: E501


        :return: The is_super_user of this AdministratorDto.  # noqa: E501
        :rtype: bool
        """
        return self._is_super_user

    @is_super_user.setter
    def is_super_user(self, is_super_user):
        """Sets the is_super_user of this AdministratorDto.


        :param is_super_user: The is_super_user of this AdministratorDto.  # noqa: E501
        :type: bool
        """

        self._is_super_user = is_super_user

    @property
    def access_control(self):
        """Gets the access_control of this AdministratorDto.  # noqa: E501


        :return: The access_control of this AdministratorDto.  # noqa: E501
        :rtype: AccessControlDto
        """
        return self._access_control

    @access_control.setter
    def access_control(self, access_control):
        """Sets the access_control of this AdministratorDto.


        :param access_control: The access_control of this AdministratorDto.  # noqa: E501
        :type: AccessControlDto
        """

        self._access_control = access_control

    @property
    def org_id(self):
        """Gets the org_id of this AdministratorDto.  # noqa: E501


        :return: The org_id of this AdministratorDto.  # noqa: E501
        :rtype: int
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this AdministratorDto.


        :param org_id: The org_id of this AdministratorDto.  # noqa: E501
        :type: int
        """

        self._org_id = org_id

    @property
    def row_version(self):
        """Gets the row_version of this AdministratorDto.  # noqa: E501


        :return: The row_version of this AdministratorDto.  # noqa: E501
        :rtype: int
        """
        return self._row_version

    @row_version.setter
    def row_version(self, row_version):
        """Sets the row_version of this AdministratorDto.


        :param row_version: The row_version of this AdministratorDto.  # noqa: E501
        :type: int
        """

        self._row_version = row_version

    @property
    def id(self):
        """Gets the id of this AdministratorDto.  # noqa: E501


        :return: The id of this AdministratorDto.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AdministratorDto.


        :param id: The id of this AdministratorDto.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def external_id(self):
        """Gets the external_id of this AdministratorDto.  # noqa: E501


        :return: The external_id of this AdministratorDto.  # noqa: E501
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this AdministratorDto.


        :param external_id: The external_id of this AdministratorDto.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                external_id is not None and len(external_id) > 40):
            raise ValueError("Invalid value for `external_id`, length must be less than or equal to `40`")  # noqa: E501

        self._external_id = external_id

    @property
    def first_name(self):
        """Gets the first_name of this AdministratorDto.  # noqa: E501


        :return: The first_name of this AdministratorDto.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this AdministratorDto.


        :param first_name: The first_name of this AdministratorDto.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                first_name is not None and len(first_name) > 40):
            raise ValueError("Invalid value for `first_name`, length must be less than or equal to `40`")  # noqa: E501

        self._first_name = first_name

    @property
    def middle_name(self):
        """Gets the middle_name of this AdministratorDto.  # noqa: E501


        :return: The middle_name of this AdministratorDto.  # noqa: E501
        :rtype: str
        """
        return self._middle_name

    @middle_name.setter
    def middle_name(self, middle_name):
        """Sets the middle_name of this AdministratorDto.


        :param middle_name: The middle_name of this AdministratorDto.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                middle_name is not None and len(middle_name) > 40):
            raise ValueError("Invalid value for `middle_name`, length must be less than or equal to `40`")  # noqa: E501

        self._middle_name = middle_name

    @property
    def last_name(self):
        """Gets the last_name of this AdministratorDto.  # noqa: E501


        :return: The last_name of this AdministratorDto.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this AdministratorDto.


        :param last_name: The last_name of this AdministratorDto.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                last_name is not None and len(last_name) > 40):
            raise ValueError("Invalid value for `last_name`, length must be less than or equal to `40`")  # noqa: E501

        self._last_name = last_name

    @property
    def email(self):
        """Gets the email of this AdministratorDto.  # noqa: E501


        :return: The email of this AdministratorDto.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this AdministratorDto.


        :param email: The email of this AdministratorDto.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                email is not None and len(email) > 100):
            raise ValueError("Invalid value for `email`, length must be less than or equal to `100`")  # noqa: E501

        self._email = email

    @property
    def date_of_birth(self):
        """Gets the date_of_birth of this AdministratorDto.  # noqa: E501


        :return: The date_of_birth of this AdministratorDto.  # noqa: E501
        :rtype: datetime
        """
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, date_of_birth):
        """Sets the date_of_birth of this AdministratorDto.


        :param date_of_birth: The date_of_birth of this AdministratorDto.  # noqa: E501
        :type: datetime
        """

        self._date_of_birth = date_of_birth

    @property
    def address1(self):
        """Gets the address1 of this AdministratorDto.  # noqa: E501


        :return: The address1 of this AdministratorDto.  # noqa: E501
        :rtype: str
        """
        return self._address1

    @address1.setter
    def address1(self, address1):
        """Sets the address1 of this AdministratorDto.


        :param address1: The address1 of this AdministratorDto.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                address1 is not None and len(address1) > 100):
            raise ValueError("Invalid value for `address1`, length must be less than or equal to `100`")  # noqa: E501

        self._address1 = address1

    @property
    def address2(self):
        """Gets the address2 of this AdministratorDto.  # noqa: E501


        :return: The address2 of this AdministratorDto.  # noqa: E501
        :rtype: str
        """
        return self._address2

    @address2.setter
    def address2(self, address2):
        """Sets the address2 of this AdministratorDto.


        :param address2: The address2 of this AdministratorDto.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                address2 is not None and len(address2) > 100):
            raise ValueError("Invalid value for `address2`, length must be less than or equal to `100`")  # noqa: E501

        self._address2 = address2

    @property
    def city(self):
        """Gets the city of this AdministratorDto.  # noqa: E501


        :return: The city of this AdministratorDto.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this AdministratorDto.


        :param city: The city of this AdministratorDto.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                city is not None and len(city) > 40):
            raise ValueError("Invalid value for `city`, length must be less than or equal to `40`")  # noqa: E501

        self._city = city

    @property
    def postal_code(self):
        """Gets the postal_code of this AdministratorDto.  # noqa: E501


        :return: The postal_code of this AdministratorDto.  # noqa: E501
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """Sets the postal_code of this AdministratorDto.


        :param postal_code: The postal_code of this AdministratorDto.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                postal_code is not None and len(postal_code) > 20):
            raise ValueError("Invalid value for `postal_code`, length must be less than or equal to `20`")  # noqa: E501

        self._postal_code = postal_code

    @property
    def state_id(self):
        """Gets the state_id of this AdministratorDto.  # noqa: E501


        :return: The state_id of this AdministratorDto.  # noqa: E501
        :rtype: int
        """
        return self._state_id

    @state_id.setter
    def state_id(self, state_id):
        """Sets the state_id of this AdministratorDto.


        :param state_id: The state_id of this AdministratorDto.  # noqa: E501
        :type: int
        """
        allowed_values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 101, 102, 103, 104, 105, 106, 107, 108, 109, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and state_id not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `state_id` ({0}), must be one of {1}"  # noqa: E501
                .format(state_id, allowed_values)
            )

        self._state_id = state_id

    @property
    def country_id(self):
        """Gets the country_id of this AdministratorDto.  # noqa: E501


        :return: The country_id of this AdministratorDto.  # noqa: E501
        :rtype: int
        """
        return self._country_id

    @country_id.setter
    def country_id(self, country_id):
        """Sets the country_id of this AdministratorDto.


        :param country_id: The country_id of this AdministratorDto.  # noqa: E501
        :type: int
        """
        allowed_values = [0, 1, 2]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and country_id not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `country_id` ({0}), must be one of {1}"  # noqa: E501
                .format(country_id, allowed_values)
            )

        self._country_id = country_id

    @property
    def phone_number(self):
        """Gets the phone_number of this AdministratorDto.  # noqa: E501


        :return: The phone_number of this AdministratorDto.  # noqa: E501
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """Sets the phone_number of this AdministratorDto.


        :param phone_number: The phone_number of this AdministratorDto.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                phone_number is not None and len(phone_number) > 20):
            raise ValueError("Invalid value for `phone_number`, length must be less than or equal to `20`")  # noqa: E501

        self._phone_number = phone_number

    @property
    def active(self):
        """Gets the active of this AdministratorDto.  # noqa: E501


        :return: The active of this AdministratorDto.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this AdministratorDto.


        :param active: The active of this AdministratorDto.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def permission_set(self):
        """Gets the permission_set of this AdministratorDto.  # noqa: E501


        :return: The permission_set of this AdministratorDto.  # noqa: E501
        :rtype: LocatorInt32
        """
        return self._permission_set

    @permission_set.setter
    def permission_set(self, permission_set):
        """Sets the permission_set of this AdministratorDto.


        :param permission_set: The permission_set of this AdministratorDto.  # noqa: E501
        :type: LocatorInt32
        """

        self._permission_set = permission_set

    @property
    def related_org_ids(self):
        """Gets the related_org_ids of this AdministratorDto.  # noqa: E501


        :return: The related_org_ids of this AdministratorDto.  # noqa: E501
        :rtype: list[int]
        """
        return self._related_org_ids

    @related_org_ids.setter
    def related_org_ids(self, related_org_ids):
        """Sets the related_org_ids of this AdministratorDto.


        :param related_org_ids: The related_org_ids of this AdministratorDto.  # noqa: E501
        :type: list[int]
        """

        self._related_org_ids = related_org_ids

    @property
    def invite_immediately(self):
        """Gets the invite_immediately of this AdministratorDto.  # noqa: E501


        :return: The invite_immediately of this AdministratorDto.  # noqa: E501
        :rtype: bool
        """
        return self._invite_immediately

    @invite_immediately.setter
    def invite_immediately(self, invite_immediately):
        """Sets the invite_immediately of this AdministratorDto.


        :param invite_immediately: The invite_immediately of this AdministratorDto.  # noqa: E501
        :type: bool
        """

        self._invite_immediately = invite_immediately

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
        if not isinstance(other, AdministratorDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AdministratorDto):
            return True

        return self.to_dict() != other.to_dict()
