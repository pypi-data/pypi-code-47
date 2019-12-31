'''
CheckBox
========

.. versionadded:: 1.4.0

.. image:: images/checkbox.png
    :align: right

:class:`CheckBox` is a specific two-state button that can be either checked or
unchecked. If the CheckBox is in a Group, it becomes a Radio button.
As with the :class:`~kivy.uix.togglebutton.ToggleButton`, only one Radio button
at a time can be selected when the :attr:`CheckBox.group` is set.

An example usage::

    from kivy.uix.checkbox import CheckBox

    # ...

    def on_checkbox_active(checkbox, value):
        if value:
            print('The checkbox', checkbox, 'is active')
        else:
            print('The checkbox', checkbox, 'is inactive')

    checkbox = CheckBox()
    checkbox.bind(active=on_checkbox_active)
'''

__all__ = ('CheckBox', )

from kivy.properties import AliasProperty, StringProperty, ListProperty
from kivy.uix.behaviors import ToggleButtonBehavior
from kivy.uix.widget import Widget


class CheckBox(ToggleButtonBehavior, Widget):
    '''CheckBox class, see module documentation for more information.
    '''

    def _get_active(self):
        return self.state == 'down'

    def _set_active(self, value):
        self.state = 'down' if value else 'normal'

    active = AliasProperty(
        _get_active, _set_active, bind=('state', ), cache=True)
    '''Indicates if the switch is active or inactive.

    :attr:`active` is a boolean and reflects and sets whether the underlying
    :attr:`~kivy.uix.button.Button.state` is 'down' (True) or 'normal' (False).
    It is a :class:`~kivy.properties.AliasProperty`, which accepts boolean
    values and defaults to False.

    .. versionchanged:: 1.11.0

        It changed from a BooleanProperty to a AliasProperty.
    '''

    background_checkbox_normal = StringProperty(
        'atlas://data/images/defaulttheme/checkbox_off')
    '''Background image of the checkbox used for the default graphical
    representation when the checkbox is not active.

    .. versionadded:: 1.9.0

    :attr:`background_checkbox_normal` is a
    :class:`~kivy.properties.StringProperty` and defaults to
    'atlas://data/images/defaulttheme/checkbox_off'.
    '''

    background_checkbox_down = StringProperty(
        'atlas://data/images/defaulttheme/checkbox_on')
    '''Background image of the checkbox used for the default graphical
    representation when the checkbox is active.

    .. versionadded:: 1.9.0

    :attr:`background_checkbox_down` is a
    :class:`~kivy.properties.StringProperty` and defaults to
    'atlas://data/images/defaulttheme/checkbox_on'.
    '''

    background_checkbox_disabled_normal = StringProperty(
        'atlas://data/images/defaulttheme/checkbox_disabled_off')
    '''Background image of the checkbox used for the default graphical
    representation when the checkbox is disabled and not active.

    .. versionadded:: 1.9.0

    :attr:`background_checkbox_disabled_normal` is a
    :class:`~kivy.properties.StringProperty` and defaults to
    'atlas://data/images/defaulttheme/checkbox_disabled_off'.
    '''

    background_checkbox_disabled_down = StringProperty(
        'atlas://data/images/defaulttheme/checkbox_disabled_on')
    '''Background image of the checkbox used for the default graphical
    representation when the checkbox is disabled and active.

    .. versionadded:: 1.9.0

    :attr:`background_checkbox_disabled_down` is a
    :class:`~kivy.properties.StringProperty` and defaults to
    'atlas://data/images/defaulttheme/checkbox_disabled_on'.
    '''

    background_radio_normal = StringProperty(
        'atlas://data/images/defaulttheme/checkbox_radio_off')
    '''Background image of the radio button used for the default graphical
    representation when the radio button is not active.

    .. versionadded:: 1.9.0

    :attr:`background_radio_normal` is a
    :class:`~kivy.properties.StringProperty` and defaults to
    'atlas://data/images/defaulttheme/checkbox_radio_off'.
    '''

    background_radio_down = StringProperty(
        'atlas://data/images/defaulttheme/checkbox_radio_on')
    '''Background image of the radio button used for the default graphical
    representation when the radio button is active.

    .. versionadded:: 1.9.0

    :attr:`background_radio_down` is a
    :class:`~kivy.properties.StringProperty` and defaults to
    'atlas://data/images/defaulttheme/checkbox_radio_on'.
    '''

    background_radio_disabled_normal = StringProperty(
        'atlas://data/images/defaulttheme/checkbox_radio_disabled_off')
    '''Background image of the radio button used for the default graphical
    representation when the radio button is disabled and not active.

    .. versionadded:: 1.9.0

    :attr:`background_radio_disabled_normal` is a
    :class:`~kivy.properties.StringProperty` and defaults to
    'atlas://data/images/defaulttheme/checkbox_radio_disabled_off'.
    '''

    background_radio_disabled_down = StringProperty(
        'atlas://data/images/defaulttheme/checkbox_radio_disabled_on')
    '''Background image of the radio button used for the default graphical
    representation when the radio button is disabled and active.

    .. versionadded:: 1.9.0

    :attr:`background_radio_disabled_down` is a
    :class:`~kivy.properties.StringProperty` and defaults to
    'atlas://data/images/defaulttheme/checkbox_radio_disabled_on'.
    '''

    color = ListProperty([1, 1, 1, 1])
    '''Color is used for tinting the default graphical representation
    of checkbox and radio button (images).

    Color is in the format (r, g, b, a).

    .. versionadded:: 1.10.0

    :attr:`color` is a
    :class:`~kivy.properties.ListProperty` and defaults to
    '[1, 1, 1, 1]'.
    '''

    def __init__(self, **kwargs):
        self.fbind('state', self._on_state)
        super(CheckBox, self).__init__(**kwargs)

    def _on_state(self, instance, value):
        if self.group and self.state == 'down':
            self._release_group(self)

    def on_group(self, *largs):
        super(CheckBox, self).on_group(*largs)
        if self.active:
            self._release_group(self)


if __name__ == '__main__':
    from random import uniform
    from kivy.base import runTouchApp
    from kivy.uix.gridlayout import GridLayout
    x = GridLayout(cols=4)
    for i in range(36):
        r, g, b = [uniform(0.2, 1.0) for j in range(3)]
        x.add_widget(CheckBox(group='1' if i % 2 else '', color=[r, g, b, 2]))
    runTouchApp(x)
