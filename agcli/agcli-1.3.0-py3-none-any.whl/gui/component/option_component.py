import wx
from wx import CheckBox, Panel, ComboBox
from wx.lib.scrolledpanel import ScrolledPanel
from ..component.base_component import BaseComponent
from ..component import custom_widget
from .. import command_notebook
from ..component.option_name import OptionName, OptionArgumentName
from ...interface.interface_generator import types


class SimpleOptionComponent(BaseComponent):

    def __init__(self, parent, template_option, interface_option):
        super().__init__(parent, template_option, interface_option)
        self.frame = parent
        self.interface_option = interface_option
        self.help = interface_option['help']
        self.SetToolTip(self.help)
        self.options = []

        self._create_options(template_option, interface_option)
        self.refresh_collapse()
        self.GetParent().Layout()

    def _create_options(self, template_option, interface_option):
        """
        Create the different option name for one type of options
        """
        for index, option_name in enumerate(interface_option['names']):
            option = self._get_option_constructor()(self.GetPane(), option_name,
             template_option['names'][index], self.OnCheckBox)
            self.component_sizer.Add(option, 1, wx.ALL, 5)
            self.options.append(option)

    def _get_option_constructor(self):
        """
        Return the constructor to use to build an option name
        """
        return OptionName

    def OnCheckBox(self, event):
        """
        This function is called when the checkbox of an option name is checked.
        It ensures that at most one option name is checked.
        """
        for option in self.options:
            if not option.checkbox.GetId() == event.GetId():
                option.check(False)

    def to_template(self):
        template = super().to_template()
        names = []
        for option in self.options:
            names.append(option.to_template())
        template['names'] = names
        return template

    def get_command(self):
        for option in self.options:
            if option.is_checked():
                return option.as_command()
        return ''

class ArgumentOptionComponent(SimpleOptionComponent):

    def __init__(self, parent, template, interface_option):
        super().__init__(parent, template, interface_option)
        value_dict = self._get_default_value_dict(interface_option, template)
        self.widget = custom_widget.create_widget(template['argument_type'],
         self.GetPane(), **value_dict)
        self.component_sizer.Insert(0, self.widget, proportion=1, flag=wx.ALL|wx.EXPAND)
        self.component_sizer.Layout()

        self.change_type_button = ComboBox(self.GetPane(), choices=types,
            value=template['argument_type'], style=wx.CB_READONLY)
        self.Bind(wx.EVT_COMBOBOX, self.OnChangeType, self.change_type_button)
        self.management_sizer.Add(self.change_type_button, flag=wx.ALL, border=2)

        self.pane_sizer.Layout()
        self.refresh_collapse()
        self.GetParent().Layout()

    def OnChangeType(self, event):
        """
        Is called when the user change the type of the argument widget. It changes
        the old widget by a new one with the appropriate type.
        """
        new_type = self.change_type_button.GetValue()
        self.component_sizer.Remove(0)
        self.widget.Destroy()
        self.widget = custom_widget.create_widget(new_type, self.GetPane())
        self.component_sizer.Insert(0, self.widget, proportion=1, flag=wx.ALL|wx.EXPAND)
        self.GetParent().Layout()

    def _get_option_constructor(self):
        return OptionArgumentName

    def _get_default_value_dict(self, interface_option, template_option):
        """
        Check if an option has a value specified in its template.
        The value found is returned in a dictionnary of this form: {'value': value}
        where 'value' is the value mentioned above. If no value is found, an empty
        dictionnary is returned.
        """
        value = template_option.get('value', None)
        if value is None:
            return {}
        else:
            return {'value': value}

    def to_template(self):
        template = super().to_template()
        if template is not None:
            template['value'] = self.widget.get_value()
            template['argument_type'] = self.change_type_button.GetValue()
            return template

    def get_command(self):
        command = super().get_command()
        if command == '':
            return ''
        elif command.startswith('--') and not self.widget.get_value()=='':
            #Add value to a long option
            command += "={}".format(self.widget.get_value())
        elif not self.widget.get_value()=='':
            #Add value to a short or BSD option
            command += " {}".format(self.widget.get_value())
        return command
