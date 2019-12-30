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


class EmployeeResponse(object):
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
        'id': 'int',
        'org_id': 'int',
        'created_utc': 'datetime',
        'changed_utc': 'datetime',
        'external_id': 'str',
        'first_name': 'str',
        'middle_name': 'str',
        'last_name': 'str',
        'email': 'str',
        'date_of_birth': 'datetime',
        'address1': 'str',
        'address2': 'str',
        'city': 'str',
        'state_id': 'int',
        'state': 'str',
        'postal_code': 'str',
        'country_id': 'int',
        'country': 'str',
        'phone_number': 'str',
        'active': 'bool',
        'permission_set_id': 'int'
    }

    attribute_map = {
        'id': 'id',
        'org_id': 'orgId',
        'created_utc': 'createdUtc',
        'changed_utc': 'changedUtc',
        'external_id': 'externalId',
        'first_name': 'firstName',
        'middle_name': 'middleName',
        'last_name': 'lastName',
        'email': 'email',
        'date_of_birth': 'dateOfBirth',
        'address1': 'address1',
        'address2': 'address2',
        'city': 'city',
        'state_id': 'stateId',
        'state': 'state',
        'postal_code': 'postalCode',
        'country_id': 'countryId',
        'country': 'country',
        'phone_number': 'phoneNumber',
        'active': 'active',
        'permission_set_id': 'permissionSetId'
    }

    def __init__(self, id=None, org_id=None, created_utc=None, changed_utc=None, external_id=None, first_name=None, middle_name=None, last_name=None, email=None, date_of_birth=None, address1=None, address2=None, city=None, state_id=None, state=None, postal_code=None, country_id=None, country=None, phone_number=None, active=None, permission_set_id=None, local_vars_configuration=None):  # noqa: E501
        """EmployeeResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._org_id = None
        self._created_utc = None
        self._changed_utc = None
        self._external_id = None
        self._first_name = None
        self._middle_name = None
        self._last_name = None
        self._email = None
        self._date_of_birth = None
        self._address1 = None
        self._address2 = None
        self._city = None
        self._state_id = None
        self._state = None
        self._postal_code = None
        self._country_id = None
        self._country = None
        self._phone_number = None
        self._active = None
        self._permission_set_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if org_id is not None:
            self.org_id = org_id
        if created_utc is not None:
            self.created_utc = created_utc
        if changed_utc is not None:
            self.changed_utc = changed_utc
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
        if state_id is not None:
            self.state_id = state_id
        if state is not None:
            self.state = state
        if postal_code is not None:
            self.postal_code = postal_code
        if country_id is not None:
            self.country_id = country_id
        if country is not None:
            self.country = country
        if phone_number is not None:
            self.phone_number = phone_number
        if active is not None:
            self.active = active
        if permission_set_id is not None:
            self.permission_set_id = permission_set_id

    @property
    def id(self):
        """Gets the id of this EmployeeResponse.  # noqa: E501


        :return: The id of this EmployeeResponse.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EmployeeResponse.


        :param id: The id of this EmployeeResponse.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def org_id(self):
        """Gets the org_id of this EmployeeResponse.  # noqa: E501


        :return: The org_id of this EmployeeResponse.  # noqa: E501
        :rtype: int
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this EmployeeResponse.


        :param org_id: The org_id of this EmployeeResponse.  # noqa: E501
        :type: int
        """

        self._org_id = org_id

    @property
    def created_utc(self):
        """Gets the created_utc of this EmployeeResponse.  # noqa: E501


        :return: The created_utc of this EmployeeResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._created_utc

    @created_utc.setter
    def created_utc(self, created_utc):
        """Sets the created_utc of this EmployeeResponse.


        :param created_utc: The created_utc of this EmployeeResponse.  # noqa: E501
        :type: datetime
        """

        self._created_utc = created_utc

    @property
    def changed_utc(self):
        """Gets the changed_utc of this EmployeeResponse.  # noqa: E501


        :return: The changed_utc of this EmployeeResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._changed_utc

    @changed_utc.setter
    def changed_utc(self, changed_utc):
        """Sets the changed_utc of this EmployeeResponse.


        :param changed_utc: The changed_utc of this EmployeeResponse.  # noqa: E501
        :type: datetime
        """

        self._changed_utc = changed_utc

    @property
    def external_id(self):
        """Gets the external_id of this EmployeeResponse.  # noqa: E501


        :return: The external_id of this EmployeeResponse.  # noqa: E501
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this EmployeeResponse.


        :param external_id: The external_id of this EmployeeResponse.  # noqa: E501
        :type: str
        """

        self._external_id = external_id

    @property
    def first_name(self):
        """Gets the first_name of this EmployeeResponse.  # noqa: E501


        :return: The first_name of this EmployeeResponse.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this EmployeeResponse.


        :param first_name: The first_name of this EmployeeResponse.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def middle_name(self):
        """Gets the middle_name of this EmployeeResponse.  # noqa: E501


        :return: The middle_name of this EmployeeResponse.  # noqa: E501
        :rtype: str
        """
        return self._middle_name

    @middle_name.setter
    def middle_name(self, middle_name):
        """Sets the middle_name of this EmployeeResponse.


        :param middle_name: The middle_name of this EmployeeResponse.  # noqa: E501
        :type: str
        """

        self._middle_name = middle_name

    @property
    def last_name(self):
        """Gets the last_name of this EmployeeResponse.  # noqa: E501


        :return: The last_name of this EmployeeResponse.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this EmployeeResponse.


        :param last_name: The last_name of this EmployeeResponse.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def email(self):
        """Gets the email of this EmployeeResponse.  # noqa: E501


        :return: The email of this EmployeeResponse.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this EmployeeResponse.


        :param email: The email of this EmployeeResponse.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def date_of_birth(self):
        """Gets the date_of_birth of this EmployeeResponse.  # noqa: E501


        :return: The date_of_birth of this EmployeeResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, date_of_birth):
        """Sets the date_of_birth of this EmployeeResponse.


        :param date_of_birth: The date_of_birth of this EmployeeResponse.  # noqa: E501
        :type: datetime
        """

        self._date_of_birth = date_of_birth

    @property
    def address1(self):
        """Gets the address1 of this EmployeeResponse.  # noqa: E501


        :return: The address1 of this EmployeeResponse.  # noqa: E501
        :rtype: str
        """
        return self._address1

    @address1.setter
    def address1(self, address1):
        """Sets the address1 of this EmployeeResponse.


        :param address1: The address1 of this EmployeeResponse.  # noqa: E501
        :type: str
        """

        self._address1 = address1

    @property
    def address2(self):
        """Gets the address2 of this EmployeeResponse.  # noqa: E501


        :return: The address2 of this EmployeeResponse.  # noqa: E501
        :rtype: str
        """
        return self._address2

    @address2.setter
    def address2(self, address2):
        """Sets the address2 of this EmployeeResponse.


        :param address2: The address2 of this EmployeeResponse.  # noqa: E501
        :type: str
        """

        self._address2 = address2

    @property
    def city(self):
        """Gets the city of this EmployeeResponse.  # noqa: E501


        :return: The city of this EmployeeResponse.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this EmployeeResponse.


        :param city: The city of this EmployeeResponse.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def state_id(self):
        """Gets the state_id of this EmployeeResponse.  # noqa: E501


        :return: The state_id of this EmployeeResponse.  # noqa: E501
        :rtype: int
        """
        return self._state_id

    @state_id.setter
    def state_id(self, state_id):
        """Sets the state_id of this EmployeeResponse.


        :param state_id: The state_id of this EmployeeResponse.  # noqa: E501
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
    def state(self):
        """Gets the state of this EmployeeResponse.  # noqa: E501


        :return: The state of this EmployeeResponse.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this EmployeeResponse.


        :param state: The state of this EmployeeResponse.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def postal_code(self):
        """Gets the postal_code of this EmployeeResponse.  # noqa: E501


        :return: The postal_code of this EmployeeResponse.  # noqa: E501
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """Sets the postal_code of this EmployeeResponse.


        :param postal_code: The postal_code of this EmployeeResponse.  # noqa: E501
        :type: str
        """

        self._postal_code = postal_code

    @property
    def country_id(self):
        """Gets the country_id of this EmployeeResponse.  # noqa: E501


        :return: The country_id of this EmployeeResponse.  # noqa: E501
        :rtype: int
        """
        return self._country_id

    @country_id.setter
    def country_id(self, country_id):
        """Sets the country_id of this EmployeeResponse.


        :param country_id: The country_id of this EmployeeResponse.  # noqa: E501
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
    def country(self):
        """Gets the country of this EmployeeResponse.  # noqa: E501


        :return: The country of this EmployeeResponse.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this EmployeeResponse.


        :param country: The country of this EmployeeResponse.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def phone_number(self):
        """Gets the phone_number of this EmployeeResponse.  # noqa: E501


        :return: The phone_number of this EmployeeResponse.  # noqa: E501
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """Sets the phone_number of this EmployeeResponse.


        :param phone_number: The phone_number of this EmployeeResponse.  # noqa: E501
        :type: str
        """

        self._phone_number = phone_number

    @property
    def active(self):
        """Gets the active of this EmployeeResponse.  # noqa: E501


        :return: The active of this EmployeeResponse.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this EmployeeResponse.


        :param active: The active of this EmployeeResponse.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def permission_set_id(self):
        """Gets the permission_set_id of this EmployeeResponse.  # noqa: E501


        :return: The permission_set_id of this EmployeeResponse.  # noqa: E501
        :rtype: int
        """
        return self._permission_set_id

    @permission_set_id.setter
    def permission_set_id(self, permission_set_id):
        """Sets the permission_set_id of this EmployeeResponse.


        :param permission_set_id: The permission_set_id of this EmployeeResponse.  # noqa: E501
        :type: int
        """

        self._permission_set_id = permission_set_id

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
        if not isinstance(other, EmployeeResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EmployeeResponse):
            return True

        return self.to_dict() != other.to_dict()
