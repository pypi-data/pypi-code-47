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


class SlideShapesDetails(object):
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
        'height': 'int',
        'width': 'int',
        'x_offset': 'int',
        'y_offset': 'int',
        'text_container': 'object',
        'group_elements_id': 'str',
        'group_element': 'object',
        'ooxml_id': 'int',
        'svg_blob_url': 'str',
        'preset_type_id': 'str',
        'free_form_path_xml': 'str',
        'fill_map': 'object',
        'is_theme_fill': 'bool',
        'effect': 'object',
        'is_theme_effect': 'bool',
        'line': 'object',
        'is_theme_line': 'bool',
        'flip_horizontal': 'bool',
        'flip_vertical': 'bool',
        'rotation': 'int',
        'hidden': 'bool',
        'base_element_blob_url': 'str',
        'changed_base_element_blob_url': 'str',
        'package_uri': 'str',
        'name': 'str',
        'id': 'str',
        'date_created': 'datetime',
        'user_created': 'str',
        'date_modified': 'datetime',
        'user_modified': 'str'
    }

    attribute_map = {
        'height': 'height',
        'width': 'width',
        'x_offset': 'xOffset',
        'y_offset': 'yOffset',
        'text_container': 'textContainer',
        'group_elements_id': 'groupElementsId',
        'group_element': 'groupElement',
        'ooxml_id': 'ooxmlId',
        'svg_blob_url': 'svgBlobUrl',
        'preset_type_id': 'presetTypeId',
        'free_form_path_xml': 'freeFormPathXml',
        'fill_map': 'fillMap',
        'is_theme_fill': 'isThemeFill',
        'effect': 'effect',
        'is_theme_effect': 'isThemeEffect',
        'line': 'line',
        'is_theme_line': 'isThemeLine',
        'flip_horizontal': 'flipHorizontal',
        'flip_vertical': 'flipVertical',
        'rotation': 'rotation',
        'hidden': 'hidden',
        'base_element_blob_url': 'baseElementBlobUrl',
        'changed_base_element_blob_url': 'changedBaseElementBlobUrl',
        'package_uri': 'packageUri',
        'name': 'name',
        'id': 'id',
        'date_created': 'dateCreated',
        'user_created': 'userCreated',
        'date_modified': 'dateModified',
        'user_modified': 'userModified'
    }

    def __init__(self, height=None, width=None, x_offset=None, y_offset=None, text_container=None, group_elements_id=None, group_element=None, ooxml_id=None, svg_blob_url=None, preset_type_id=None, free_form_path_xml=None, fill_map=None, is_theme_fill=None, effect=None, is_theme_effect=None, line=None, is_theme_line=None, flip_horizontal=None, flip_vertical=None, rotation=None, hidden=None, base_element_blob_url=None, changed_base_element_blob_url=None, package_uri=None, name=None, id=None, date_created=None, user_created=None, date_modified=None, user_modified=None, local_vars_configuration=None):  # noqa: E501
        """SlideShapesDetails - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._height = None
        self._width = None
        self._x_offset = None
        self._y_offset = None
        self._text_container = None
        self._group_elements_id = None
        self._group_element = None
        self._ooxml_id = None
        self._svg_blob_url = None
        self._preset_type_id = None
        self._free_form_path_xml = None
        self._fill_map = None
        self._is_theme_fill = None
        self._effect = None
        self._is_theme_effect = None
        self._line = None
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
        self._date_created = None
        self._user_created = None
        self._date_modified = None
        self._user_modified = None
        self.discriminator = None

        if height is not None:
            self.height = height
        if width is not None:
            self.width = width
        if x_offset is not None:
            self.x_offset = x_offset
        if y_offset is not None:
            self.y_offset = y_offset
        if text_container is not None:
            self.text_container = text_container
        self.group_elements_id = group_elements_id
        if group_element is not None:
            self.group_element = group_element
        if ooxml_id is not None:
            self.ooxml_id = ooxml_id
        self.svg_blob_url = svg_blob_url
        self.preset_type_id = preset_type_id
        self.free_form_path_xml = free_form_path_xml
        if fill_map is not None:
            self.fill_map = fill_map
        if is_theme_fill is not None:
            self.is_theme_fill = is_theme_fill
        if effect is not None:
            self.effect = effect
        if is_theme_effect is not None:
            self.is_theme_effect = is_theme_effect
        if line is not None:
            self.line = line
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
        if date_created is not None:
            self.date_created = date_created
        if user_created is not None:
            self.user_created = user_created
        if date_modified is not None:
            self.date_modified = date_modified
        if user_modified is not None:
            self.user_modified = user_modified

    @property
    def height(self):
        """Gets the height of this SlideShapesDetails.  # noqa: E501


        :return: The height of this SlideShapesDetails.  # noqa: E501
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this SlideShapesDetails.


        :param height: The height of this SlideShapesDetails.  # noqa: E501
        :type: int
        """

        self._height = height

    @property
    def width(self):
        """Gets the width of this SlideShapesDetails.  # noqa: E501


        :return: The width of this SlideShapesDetails.  # noqa: E501
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this SlideShapesDetails.


        :param width: The width of this SlideShapesDetails.  # noqa: E501
        :type: int
        """

        self._width = width

    @property
    def x_offset(self):
        """Gets the x_offset of this SlideShapesDetails.  # noqa: E501


        :return: The x_offset of this SlideShapesDetails.  # noqa: E501
        :rtype: int
        """
        return self._x_offset

    @x_offset.setter
    def x_offset(self, x_offset):
        """Sets the x_offset of this SlideShapesDetails.


        :param x_offset: The x_offset of this SlideShapesDetails.  # noqa: E501
        :type: int
        """

        self._x_offset = x_offset

    @property
    def y_offset(self):
        """Gets the y_offset of this SlideShapesDetails.  # noqa: E501


        :return: The y_offset of this SlideShapesDetails.  # noqa: E501
        :rtype: int
        """
        return self._y_offset

    @y_offset.setter
    def y_offset(self, y_offset):
        """Sets the y_offset of this SlideShapesDetails.


        :param y_offset: The y_offset of this SlideShapesDetails.  # noqa: E501
        :type: int
        """

        self._y_offset = y_offset

    @property
    def text_container(self):
        """Gets the text_container of this SlideShapesDetails.  # noqa: E501


        :return: The text_container of this SlideShapesDetails.  # noqa: E501
        :rtype: object
        """
        return self._text_container

    @text_container.setter
    def text_container(self, text_container):
        """Sets the text_container of this SlideShapesDetails.


        :param text_container: The text_container of this SlideShapesDetails.  # noqa: E501
        :type: object
        """

        self._text_container = text_container

    @property
    def group_elements_id(self):
        """Gets the group_elements_id of this SlideShapesDetails.  # noqa: E501


        :return: The group_elements_id of this SlideShapesDetails.  # noqa: E501
        :rtype: str
        """
        return self._group_elements_id

    @group_elements_id.setter
    def group_elements_id(self, group_elements_id):
        """Sets the group_elements_id of this SlideShapesDetails.


        :param group_elements_id: The group_elements_id of this SlideShapesDetails.  # noqa: E501
        :type: str
        """

        self._group_elements_id = group_elements_id

    @property
    def group_element(self):
        """Gets the group_element of this SlideShapesDetails.  # noqa: E501


        :return: The group_element of this SlideShapesDetails.  # noqa: E501
        :rtype: object
        """
        return self._group_element

    @group_element.setter
    def group_element(self, group_element):
        """Sets the group_element of this SlideShapesDetails.


        :param group_element: The group_element of this SlideShapesDetails.  # noqa: E501
        :type: object
        """

        self._group_element = group_element

    @property
    def ooxml_id(self):
        """Gets the ooxml_id of this SlideShapesDetails.  # noqa: E501


        :return: The ooxml_id of this SlideShapesDetails.  # noqa: E501
        :rtype: int
        """
        return self._ooxml_id

    @ooxml_id.setter
    def ooxml_id(self, ooxml_id):
        """Sets the ooxml_id of this SlideShapesDetails.


        :param ooxml_id: The ooxml_id of this SlideShapesDetails.  # noqa: E501
        :type: int
        """

        self._ooxml_id = ooxml_id

    @property
    def svg_blob_url(self):
        """Gets the svg_blob_url of this SlideShapesDetails.  # noqa: E501


        :return: The svg_blob_url of this SlideShapesDetails.  # noqa: E501
        :rtype: str
        """
        return self._svg_blob_url

    @svg_blob_url.setter
    def svg_blob_url(self, svg_blob_url):
        """Sets the svg_blob_url of this SlideShapesDetails.


        :param svg_blob_url: The svg_blob_url of this SlideShapesDetails.  # noqa: E501
        :type: str
        """

        self._svg_blob_url = svg_blob_url

    @property
    def preset_type_id(self):
        """Gets the preset_type_id of this SlideShapesDetails.  # noqa: E501


        :return: The preset_type_id of this SlideShapesDetails.  # noqa: E501
        :rtype: str
        """
        return self._preset_type_id

    @preset_type_id.setter
    def preset_type_id(self, preset_type_id):
        """Sets the preset_type_id of this SlideShapesDetails.


        :param preset_type_id: The preset_type_id of this SlideShapesDetails.  # noqa: E501
        :type: str
        """

        self._preset_type_id = preset_type_id

    @property
    def free_form_path_xml(self):
        """Gets the free_form_path_xml of this SlideShapesDetails.  # noqa: E501


        :return: The free_form_path_xml of this SlideShapesDetails.  # noqa: E501
        :rtype: str
        """
        return self._free_form_path_xml

    @free_form_path_xml.setter
    def free_form_path_xml(self, free_form_path_xml):
        """Sets the free_form_path_xml of this SlideShapesDetails.


        :param free_form_path_xml: The free_form_path_xml of this SlideShapesDetails.  # noqa: E501
        :type: str
        """

        self._free_form_path_xml = free_form_path_xml

    @property
    def fill_map(self):
        """Gets the fill_map of this SlideShapesDetails.  # noqa: E501


        :return: The fill_map of this SlideShapesDetails.  # noqa: E501
        :rtype: object
        """
        return self._fill_map

    @fill_map.setter
    def fill_map(self, fill_map):
        """Sets the fill_map of this SlideShapesDetails.


        :param fill_map: The fill_map of this SlideShapesDetails.  # noqa: E501
        :type: object
        """

        self._fill_map = fill_map

    @property
    def is_theme_fill(self):
        """Gets the is_theme_fill of this SlideShapesDetails.  # noqa: E501


        :return: The is_theme_fill of this SlideShapesDetails.  # noqa: E501
        :rtype: bool
        """
        return self._is_theme_fill

    @is_theme_fill.setter
    def is_theme_fill(self, is_theme_fill):
        """Sets the is_theme_fill of this SlideShapesDetails.


        :param is_theme_fill: The is_theme_fill of this SlideShapesDetails.  # noqa: E501
        :type: bool
        """

        self._is_theme_fill = is_theme_fill

    @property
    def effect(self):
        """Gets the effect of this SlideShapesDetails.  # noqa: E501


        :return: The effect of this SlideShapesDetails.  # noqa: E501
        :rtype: object
        """
        return self._effect

    @effect.setter
    def effect(self, effect):
        """Sets the effect of this SlideShapesDetails.


        :param effect: The effect of this SlideShapesDetails.  # noqa: E501
        :type: object
        """

        self._effect = effect

    @property
    def is_theme_effect(self):
        """Gets the is_theme_effect of this SlideShapesDetails.  # noqa: E501


        :return: The is_theme_effect of this SlideShapesDetails.  # noqa: E501
        :rtype: bool
        """
        return self._is_theme_effect

    @is_theme_effect.setter
    def is_theme_effect(self, is_theme_effect):
        """Sets the is_theme_effect of this SlideShapesDetails.


        :param is_theme_effect: The is_theme_effect of this SlideShapesDetails.  # noqa: E501
        :type: bool
        """

        self._is_theme_effect = is_theme_effect

    @property
    def line(self):
        """Gets the line of this SlideShapesDetails.  # noqa: E501


        :return: The line of this SlideShapesDetails.  # noqa: E501
        :rtype: object
        """
        return self._line

    @line.setter
    def line(self, line):
        """Sets the line of this SlideShapesDetails.


        :param line: The line of this SlideShapesDetails.  # noqa: E501
        :type: object
        """

        self._line = line

    @property
    def is_theme_line(self):
        """Gets the is_theme_line of this SlideShapesDetails.  # noqa: E501


        :return: The is_theme_line of this SlideShapesDetails.  # noqa: E501
        :rtype: bool
        """
        return self._is_theme_line

    @is_theme_line.setter
    def is_theme_line(self, is_theme_line):
        """Sets the is_theme_line of this SlideShapesDetails.


        :param is_theme_line: The is_theme_line of this SlideShapesDetails.  # noqa: E501
        :type: bool
        """

        self._is_theme_line = is_theme_line

    @property
    def flip_horizontal(self):
        """Gets the flip_horizontal of this SlideShapesDetails.  # noqa: E501


        :return: The flip_horizontal of this SlideShapesDetails.  # noqa: E501
        :rtype: bool
        """
        return self._flip_horizontal

    @flip_horizontal.setter
    def flip_horizontal(self, flip_horizontal):
        """Sets the flip_horizontal of this SlideShapesDetails.


        :param flip_horizontal: The flip_horizontal of this SlideShapesDetails.  # noqa: E501
        :type: bool
        """

        self._flip_horizontal = flip_horizontal

    @property
    def flip_vertical(self):
        """Gets the flip_vertical of this SlideShapesDetails.  # noqa: E501


        :return: The flip_vertical of this SlideShapesDetails.  # noqa: E501
        :rtype: bool
        """
        return self._flip_vertical

    @flip_vertical.setter
    def flip_vertical(self, flip_vertical):
        """Sets the flip_vertical of this SlideShapesDetails.


        :param flip_vertical: The flip_vertical of this SlideShapesDetails.  # noqa: E501
        :type: bool
        """

        self._flip_vertical = flip_vertical

    @property
    def rotation(self):
        """Gets the rotation of this SlideShapesDetails.  # noqa: E501


        :return: The rotation of this SlideShapesDetails.  # noqa: E501
        :rtype: int
        """
        return self._rotation

    @rotation.setter
    def rotation(self, rotation):
        """Sets the rotation of this SlideShapesDetails.


        :param rotation: The rotation of this SlideShapesDetails.  # noqa: E501
        :type: int
        """

        self._rotation = rotation

    @property
    def hidden(self):
        """Gets the hidden of this SlideShapesDetails.  # noqa: E501


        :return: The hidden of this SlideShapesDetails.  # noqa: E501
        :rtype: bool
        """
        return self._hidden

    @hidden.setter
    def hidden(self, hidden):
        """Sets the hidden of this SlideShapesDetails.


        :param hidden: The hidden of this SlideShapesDetails.  # noqa: E501
        :type: bool
        """

        self._hidden = hidden

    @property
    def base_element_blob_url(self):
        """Gets the base_element_blob_url of this SlideShapesDetails.  # noqa: E501


        :return: The base_element_blob_url of this SlideShapesDetails.  # noqa: E501
        :rtype: str
        """
        return self._base_element_blob_url

    @base_element_blob_url.setter
    def base_element_blob_url(self, base_element_blob_url):
        """Sets the base_element_blob_url of this SlideShapesDetails.


        :param base_element_blob_url: The base_element_blob_url of this SlideShapesDetails.  # noqa: E501
        :type: str
        """

        self._base_element_blob_url = base_element_blob_url

    @property
    def changed_base_element_blob_url(self):
        """Gets the changed_base_element_blob_url of this SlideShapesDetails.  # noqa: E501


        :return: The changed_base_element_blob_url of this SlideShapesDetails.  # noqa: E501
        :rtype: str
        """
        return self._changed_base_element_blob_url

    @changed_base_element_blob_url.setter
    def changed_base_element_blob_url(self, changed_base_element_blob_url):
        """Sets the changed_base_element_blob_url of this SlideShapesDetails.


        :param changed_base_element_blob_url: The changed_base_element_blob_url of this SlideShapesDetails.  # noqa: E501
        :type: str
        """

        self._changed_base_element_blob_url = changed_base_element_blob_url

    @property
    def package_uri(self):
        """Gets the package_uri of this SlideShapesDetails.  # noqa: E501


        :return: The package_uri of this SlideShapesDetails.  # noqa: E501
        :rtype: str
        """
        return self._package_uri

    @package_uri.setter
    def package_uri(self, package_uri):
        """Sets the package_uri of this SlideShapesDetails.


        :param package_uri: The package_uri of this SlideShapesDetails.  # noqa: E501
        :type: str
        """

        self._package_uri = package_uri

    @property
    def name(self):
        """Gets the name of this SlideShapesDetails.  # noqa: E501


        :return: The name of this SlideShapesDetails.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SlideShapesDetails.


        :param name: The name of this SlideShapesDetails.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def id(self):
        """Gets the id of this SlideShapesDetails.  # noqa: E501


        :return: The id of this SlideShapesDetails.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SlideShapesDetails.


        :param id: The id of this SlideShapesDetails.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def date_created(self):
        """Gets the date_created of this SlideShapesDetails.  # noqa: E501


        :return: The date_created of this SlideShapesDetails.  # noqa: E501
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this SlideShapesDetails.


        :param date_created: The date_created of this SlideShapesDetails.  # noqa: E501
        :type: datetime
        """

        self._date_created = date_created

    @property
    def user_created(self):
        """Gets the user_created of this SlideShapesDetails.  # noqa: E501


        :return: The user_created of this SlideShapesDetails.  # noqa: E501
        :rtype: str
        """
        return self._user_created

    @user_created.setter
    def user_created(self, user_created):
        """Sets the user_created of this SlideShapesDetails.


        :param user_created: The user_created of this SlideShapesDetails.  # noqa: E501
        :type: str
        """

        self._user_created = user_created

    @property
    def date_modified(self):
        """Gets the date_modified of this SlideShapesDetails.  # noqa: E501


        :return: The date_modified of this SlideShapesDetails.  # noqa: E501
        :rtype: datetime
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this SlideShapesDetails.


        :param date_modified: The date_modified of this SlideShapesDetails.  # noqa: E501
        :type: datetime
        """

        self._date_modified = date_modified

    @property
    def user_modified(self):
        """Gets the user_modified of this SlideShapesDetails.  # noqa: E501


        :return: The user_modified of this SlideShapesDetails.  # noqa: E501
        :rtype: str
        """
        return self._user_modified

    @user_modified.setter
    def user_modified(self, user_modified):
        """Sets the user_modified of this SlideShapesDetails.


        :param user_modified: The user_modified of this SlideShapesDetails.  # noqa: E501
        :type: str
        """

        self._user_modified = user_modified

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
        if not isinstance(other, SlideShapesDetails):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SlideShapesDetails):
            return True

        return self.to_dict() != other.to_dict()
