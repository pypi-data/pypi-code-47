# coding: utf-8

"""
    OOXML Automation

    This API helps users convert Excel and Powerpoint documents into rich, live dashboards and stories.  # noqa: E501

    The version of the OpenAPI document: 0.1.0-no-tags
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from presalytics.client.presalytics_ooxml_automation.configuration import Configuration


class SlideConnector(object):
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
        'start_connection_shape_id': 'str',
        'start_connection_idx': 'int',
        'end_connection_shape_id': 'str',
        'end_connection_idx': 'int',
        'group_elements_id': 'str',
        'ooxml_id': 'int',
        'svg_blob_url': 'str',
        'preset_type_id': 'str',
        'free_form_path_xml': 'str',
        'is_theme_fill': 'bool',
        'is_theme_effect': 'bool',
        'is_theme_line': 'bool',
        'flip_horizontal': 'bool',
        'flip_vertical': 'bool',
        'rotation': 'int',
        'hidden': 'bool',
        'base_element_blob_url': 'str',
        'changed_base_element_blob_url': 'str',
        'package_uri': 'str',
        'name': 'str',
        'id': 'str'
    }

    attribute_map = {
        'start_connection_shape_id': 'startConnectionShapeId',
        'start_connection_idx': 'startConnectionIdx',
        'end_connection_shape_id': 'endConnectionShapeId',
        'end_connection_idx': 'endConnectionIdx',
        'group_elements_id': 'groupElementsId',
        'ooxml_id': 'ooxmlId',
        'svg_blob_url': 'svgBlobUrl',
        'preset_type_id': 'presetTypeId',
        'free_form_path_xml': 'freeFormPathXml',
        'is_theme_fill': 'isThemeFill',
        'is_theme_effect': 'isThemeEffect',
        'is_theme_line': 'isThemeLine',
        'flip_horizontal': 'flipHorizontal',
        'flip_vertical': 'flipVertical',
        'rotation': 'rotation',
        'hidden': 'hidden',
        'base_element_blob_url': 'baseElementBlobUrl',
        'changed_base_element_blob_url': 'changedBaseElementBlobUrl',
        'package_uri': 'packageUri',
        'name': 'name',
        'id': 'id'
    }

    def __init__(self, start_connection_shape_id=None, start_connection_idx=None, end_connection_shape_id=None, end_connection_idx=None, group_elements_id=None, ooxml_id=None, svg_blob_url=None, preset_type_id=None, free_form_path_xml=None, is_theme_fill=None, is_theme_effect=None, is_theme_line=None, flip_horizontal=None, flip_vertical=None, rotation=None, hidden=None, base_element_blob_url=None, changed_base_element_blob_url=None, package_uri=None, name=None, id=None, local_vars_configuration=None):  # noqa: E501
        """SlideConnector - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._start_connection_shape_id = None
        self._start_connection_idx = None
        self._end_connection_shape_id = None
        self._end_connection_idx = None
        self._group_elements_id = None
        self._ooxml_id = None
        self._svg_blob_url = None
        self._preset_type_id = None
        self._free_form_path_xml = None
        self._is_theme_fill = None
        self._is_theme_effect = None
        self._is_theme_line = None
        self._flip_horizontal = None
        self._flip_vertical = None
        self._rotation = None
        self._hidden = None
        self._base_element_blob_url = None
        self._changed_base_element_blob_url = None
        self._package_uri = None
        self._name = None
        self._id = None
        self.discriminator = None

        self.start_connection_shape_id = start_connection_shape_id
        if start_connection_idx is not None:
            self.start_connection_idx = start_connection_idx
        self.end_connection_shape_id = end_connection_shape_id
        if end_connection_idx is not None:
            self.end_connection_idx = end_connection_idx
        self.group_elements_id = group_elements_id
        if ooxml_id is not None:
            self.ooxml_id = ooxml_id
        self.svg_blob_url = svg_blob_url
        self.preset_type_id = preset_type_id
        self.free_form_path_xml = free_form_path_xml
        if is_theme_fill is not None:
            self.is_theme_fill = is_theme_fill
        if is_theme_effect is not None:
            self.is_theme_effect = is_theme_effect
        if is_theme_line is not None:
            self.is_theme_line = is_theme_line
        if flip_horizontal is not None:
            self.flip_horizontal = flip_horizontal
        if flip_vertical is not None:
            self.flip_vertical = flip_vertical
        if rotation is not None:
            self.rotation = rotation
        if hidden is not None:
            self.hidden = hidden
        self.base_element_blob_url = base_element_blob_url
        self.changed_base_element_blob_url = changed_base_element_blob_url
        self.package_uri = package_uri
        self.name = name
        if id is not None:
            self.id = id

    @property
    def start_connection_shape_id(self):
        """Gets the start_connection_shape_id of this SlideConnector.  # noqa: E501


        :return: The start_connection_shape_id of this SlideConnector.  # noqa: E501
        :rtype: str
        """
        return self._start_connection_shape_id

    @start_connection_shape_id.setter
    def start_connection_shape_id(self, start_connection_shape_id):
        """Sets the start_connection_shape_id of this SlideConnector.


        :param start_connection_shape_id: The start_connection_shape_id of this SlideConnector.  # noqa: E501
        :type: str
        """

        self._start_connection_shape_id = start_connection_shape_id

    @property
    def start_connection_idx(self):
        """Gets the start_connection_idx of this SlideConnector.  # noqa: E501


        :return: The start_connection_idx of this SlideConnector.  # noqa: E501
        :rtype: int
        """
        return self._start_connection_idx

    @start_connection_idx.setter
    def start_connection_idx(self, start_connection_idx):
        """Sets the start_connection_idx of this SlideConnector.


        :param start_connection_idx: The start_connection_idx of this SlideConnector.  # noqa: E501
        :type: int
        """

        self._start_connection_idx = start_connection_idx

    @property
    def end_connection_shape_id(self):
        """Gets the end_connection_shape_id of this SlideConnector.  # noqa: E501


        :return: The end_connection_shape_id of this SlideConnector.  # noqa: E501
        :rtype: str
        """
        return self._end_connection_shape_id

    @end_connection_shape_id.setter
    def end_connection_shape_id(self, end_connection_shape_id):
        """Sets the end_connection_shape_id of this SlideConnector.


        :param end_connection_shape_id: The end_connection_shape_id of this SlideConnector.  # noqa: E501
        :type: str
        """

        self._end_connection_shape_id = end_connection_shape_id

    @property
    def end_connection_idx(self):
        """Gets the end_connection_idx of this SlideConnector.  # noqa: E501


        :return: The end_connection_idx of this SlideConnector.  # noqa: E501
        :rtype: int
        """
        return self._end_connection_idx

    @end_connection_idx.setter
    def end_connection_idx(self, end_connection_idx):
        """Sets the end_connection_idx of this SlideConnector.


        :param end_connection_idx: The end_connection_idx of this SlideConnector.  # noqa: E501
        :type: int
        """

        self._end_connection_idx = end_connection_idx

    @property
    def group_elements_id(self):
        """Gets the group_elements_id of this SlideConnector.  # noqa: E501


        :return: The group_elements_id of this SlideConnector.  # noqa: E501
        :rtype: str
        """
        return self._group_elements_id

    @group_elements_id.setter
    def group_elements_id(self, group_elements_id):
        """Sets the group_elements_id of this SlideConnector.


        :param group_elements_id: The group_elements_id of this SlideConnector.  # noqa: E501
        :type: str
        """

        self._group_elements_id = group_elements_id

    @property
    def ooxml_id(self):
        """Gets the ooxml_id of this SlideConnector.  # noqa: E501


        :return: The ooxml_id of this SlideConnector.  # noqa: E501
        :rtype: int
        """
        return self._ooxml_id

    @ooxml_id.setter
    def ooxml_id(self, ooxml_id):
        """Sets the ooxml_id of this SlideConnector.


        :param ooxml_id: The ooxml_id of this SlideConnector.  # noqa: E501
        :type: int
        """

        self._ooxml_id = ooxml_id

    @property
    def svg_blob_url(self):
        """Gets the svg_blob_url of this SlideConnector.  # noqa: E501


        :return: The svg_blob_url of this SlideConnector.  # noqa: E501
        :rtype: str
        """
        return self._svg_blob_url

    @svg_blob_url.setter
    def svg_blob_url(self, svg_blob_url):
        """Sets the svg_blob_url of this SlideConnector.


        :param svg_blob_url: The svg_blob_url of this SlideConnector.  # noqa: E501
        :type: str
        """

        self._svg_blob_url = svg_blob_url

    @property
    def preset_type_id(self):
        """Gets the preset_type_id of this SlideConnector.  # noqa: E501


        :return: The preset_type_id of this SlideConnector.  # noqa: E501
        :rtype: str
        """
        return self._preset_type_id

    @preset_type_id.setter
    def preset_type_id(self, preset_type_id):
        """Sets the preset_type_id of this SlideConnector.


        :param preset_type_id: The preset_type_id of this SlideConnector.  # noqa: E501
        :type: str
        """

        self._preset_type_id = preset_type_id

    @property
    def free_form_path_xml(self):
        """Gets the free_form_path_xml of this SlideConnector.  # noqa: E501


        :return: The free_form_path_xml of this SlideConnector.  # noqa: E501
        :rtype: str
        """
        return self._free_form_path_xml

    @free_form_path_xml.setter
    def free_form_path_xml(self, free_form_path_xml):
        """Sets the free_form_path_xml of this SlideConnector.


        :param free_form_path_xml: The free_form_path_xml of this SlideConnector.  # noqa: E501
        :type: str
        """

        self._free_form_path_xml = free_form_path_xml

    @property
    def is_theme_fill(self):
        """Gets the is_theme_fill of this SlideConnector.  # noqa: E501


        :return: The is_theme_fill of this SlideConnector.  # noqa: E501
        :rtype: bool
        """
        return self._is_theme_fill

    @is_theme_fill.setter
    def is_theme_fill(self, is_theme_fill):
        """Sets the is_theme_fill of this SlideConnector.


        :param is_theme_fill: The is_theme_fill of this SlideConnector.  # noqa: E501
        :type: bool
        """

        self._is_theme_fill = is_theme_fill

    @property
    def is_theme_effect(self):
        """Gets the is_theme_effect of this SlideConnector.  # noqa: E501


        :return: The is_theme_effect of this SlideConnector.  # noqa: E501
        :rtype: bool
        """
        return self._is_theme_effect

    @is_theme_effect.setter
    def is_theme_effect(self, is_theme_effect):
        """Sets the is_theme_effect of this SlideConnector.


        :param is_theme_effect: The is_theme_effect of this SlideConnector.  # noqa: E501
        :type: bool
        """

        self._is_theme_effect = is_theme_effect

    @property
    def is_theme_line(self):
        """Gets the is_theme_line of this SlideConnector.  # noqa: E501


        :return: The is_theme_line of this SlideConnector.  # noqa: E501
        :rtype: bool
        """
        return self._is_theme_line

    @is_theme_line.setter
    def is_theme_line(self, is_theme_line):
        """Sets the is_theme_line of this SlideConnector.


        :param is_theme_line: The is_theme_line of this SlideConnector.  # noqa: E501
        :type: bool
        """

        self._is_theme_line = is_theme_line

    @property
    def flip_horizontal(self):
        """Gets the flip_horizontal of this SlideConnector.  # noqa: E501


        :return: The flip_horizontal of this SlideConnector.  # noqa: E501
        :rtype: bool
        """
        return self._flip_horizontal

    @flip_horizontal.setter
    def flip_horizontal(self, flip_horizontal):
        """Sets the flip_horizontal of this SlideConnector.


        :param flip_horizontal: The flip_horizontal of this SlideConnector.  # noqa: E501
        :type: bool
        """

        self._flip_horizontal = flip_horizontal

    @property
    def flip_vertical(self):
        """Gets the flip_vertical of this SlideConnector.  # noqa: E501


        :return: The flip_vertical of this SlideConnector.  # noqa: E501
        :rtype: bool
        """
        return self._flip_vertical

    @flip_vertical.setter
    def flip_vertical(self, flip_vertical):
        """Sets the flip_vertical of this SlideConnector.


        :param flip_vertical: The flip_vertical of this SlideConnector.  # noqa: E501
        :type: bool
        """

        self._flip_vertical = flip_vertical

    @property
    def rotation(self):
        """Gets the rotation of this SlideConnector.  # noqa: E501


        :return: The rotation of this SlideConnector.  # noqa: E501
        :rtype: int
        """
        return self._rotation

    @rotation.setter
    def rotation(self, rotation):
        """Sets the rotation of this SlideConnector.


        :param rotation: The rotation of this SlideConnector.  # noqa: E501
        :type: int
        """

        self._rotation = rotation

    @property
    def hidden(self):
        """Gets the hidden of this SlideConnector.  # noqa: E501


        :return: The hidden of this SlideConnector.  # noqa: E501
        :rtype: bool
        """
        return self._hidden

    @hidden.setter
    def hidden(self, hidden):
        """Sets the hidden of this SlideConnector.


        :param hidden: The hidden of this SlideConnector.  # noqa: E501
        :type: bool
        """

        self._hidden = hidden

    @property
    def base_element_blob_url(self):
        """Gets the base_element_blob_url of this SlideConnector.  # noqa: E501


        :return: The base_element_blob_url of this SlideConnector.  # noqa: E501
        :rtype: str
        """
        return self._base_element_blob_url

    @base_element_blob_url.setter
    def base_element_blob_url(self, base_element_blob_url):
        """Sets the base_element_blob_url of this SlideConnector.


        :param base_element_blob_url: The base_element_blob_url of this SlideConnector.  # noqa: E501
        :type: str
        """

        self._base_element_blob_url = base_element_blob_url

    @property
    def changed_base_element_blob_url(self):
        """Gets the changed_base_element_blob_url of this SlideConnector.  # noqa: E501


        :return: The changed_base_element_blob_url of this SlideConnector.  # noqa: E501
        :rtype: str
        """
        return self._changed_base_element_blob_url

    @changed_base_element_blob_url.setter
    def changed_base_element_blob_url(self, changed_base_element_blob_url):
        """Sets the changed_base_element_blob_url of this SlideConnector.


        :param changed_base_element_blob_url: The changed_base_element_blob_url of this SlideConnector.  # noqa: E501
        :type: str
        """

        self._changed_base_element_blob_url = changed_base_element_blob_url

    @property
    def package_uri(self):
        """Gets the package_uri of this SlideConnector.  # noqa: E501


        :return: The package_uri of this SlideConnector.  # noqa: E501
        :rtype: str
        """
        return self._package_uri

    @package_uri.setter
    def package_uri(self, package_uri):
        """Sets the package_uri of this SlideConnector.


        :param package_uri: The package_uri of this SlideConnector.  # noqa: E501
        :type: str
        """

        self._package_uri = package_uri

    @property
    def name(self):
        """Gets the name of this SlideConnector.  # noqa: E501


        :return: The name of this SlideConnector.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SlideConnector.


        :param name: The name of this SlideConnector.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def id(self):
        """Gets the id of this SlideConnector.  # noqa: E501


        :return: The id of this SlideConnector.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SlideConnector.


        :param id: The id of this SlideConnector.  # noqa: E501
        :type: str
        """

        self._id = id

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
        if not isinstance(other, SlideConnector):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SlideConnector):
            return True

        return self.to_dict() != other.to_dict()
