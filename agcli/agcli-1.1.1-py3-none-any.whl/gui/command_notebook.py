from ..utils import yaml
from .component import option_component, subcommand_component, argument_component, base_component, custom_notebook
from .component.parameter_component import ParametersComponent
from wx import Panel, TextCtrl, StaticText, Button
from wx.lib.dialogs import ScrolledMessageDialog
from ..event import event_handler
from ..template.template_generator import DefaultGenerator
import wx
import shlex, subprocess


instance = None

class CommandNoteBook(Panel):

    def __init__(self, parent, cmd, template_file, interface_file):
        super(Panel, self).__init__(parent)
        global instance
        instance = self
        self.command = cmd
        self.other_tab = None
        self.notebook = custom_notebook.CustomNotebook(self)
        self.Bind(event_handler.EVT_VALUE_CHANGED, self.OnRefresh, id=wx.ID_ANY)
        self.Bind(event_handler.EVT_ADD_TAB, self.OnAddTab, self.notebook)

        sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(sizer)

        template = yaml.open_yaml(template_file)
        self.interface = yaml.open_yaml(interface_file)
        self._create_tabs(template)

        label = StaticText(self, label='Command:')
        self.command_field = TextCtrl(self, value=self.as_command(), style=wx.TE_READONLY)
        command_panel = self._create_command_panel()


        sizer.Add(self.notebook, 10 , wx.EXPAND)
        sizer.Add(label)
        sizer.Add(self.command_field, 1, wx.EXPAND)
        sizer.Add(command_panel, 1, wx.EXPAND )

        sizer.Layout()

    def fill_template(self, complete_template):
        """
        Fill the template with the informations gathered by the "complete" option
        of the program.
        """
        for page in range(self.notebook.GetPageCount()):
            component = self.notebook.GetPage(page)
            for parameter in complete_template['Complete']:
                index = component.get_parameter_index(parameter['ID'])
                if not index is None:
                    component.delete_parameter(index)
        self._create_template_tabs(complete_template, select=True)
        event_handler.trigger_value_changed_event(self)

    def _create_tabs(self, template):
        """
        Create all the tabs according to the 'template' argument and create another
        tab caintaining all paramaters that doesn't appears in 'template'.
        """
        self._create_template_tabs(template)
        self._create_other_tab(template)

    def _create_template_tabs(self, template, renamable=True, select=False):
        """
        Create the tabs according to the template argument.
        """
        for i, tab_name in enumerate(template):
            component = ParametersComponent(self.notebook, template[tab_name], self.interface)
            self.notebook.AddPage(component, tab_name, select=select)
            self.notebook.SetRenamable(i, renamable)

    def _create_other_tab(self, template):
        """
        Create an "Others" tab that contains all the paramaters that are not listed
        in other tabs. If 'template' lists all parameters, this function does nothing.
        """
        other_param = self._get_unused_parameters(template)
        other_template = DefaultGenerator().generate_other_template(other_param)
        self._create_template_tabs(other_template, False)
        self.other_tab = self.notebook.GetPage(self.notebook.GetPageCount()-1)
        if len(other_param) < 1:
            self.notebook.HidePage(self.notebook.GetPageCount()-1, hidden=True)
            self.notebook.SetCloseButton(self.notebook.GetPageCount()-1, False)

    def delete_tab(self, tab_index):
        """
        Move the parameters of the "tab_index" tab to the "Others" tab. This
        funtion is meant to be called before deleting the "tab_index" tab.
        """
        deleted_tab = self.notebook.GetPage(tab_index)
        for parameter in deleted_tab.parameters:
            parameter.Collapse()
        self.other_tab.add_parameters(deleted_tab.parameters)
        self.notebook.HidePage(self.notebook.GetPageIndex(self.other_tab), hidden=False)

    def _get_unused_parameters(self, template):
        """
        Return all the parameters that doesn't appears in 'template'.
        """
        other_param = []
        for interface_paramater in self.interface:
            is_found = False
            for tab_name in template:
                for template_parameter in template[tab_name]:
                    if interface_paramater["ID"] == template_parameter["ID"]:
                        is_found = True
                        break
            if not is_found:
                other_param.append(interface_paramater)
        return other_param

    def _create_management_panel(self):
        """
        Create the panel containing the "add tabs" button.
        """
        panel = Panel(self)
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        panel.SetSizer(sizer)

        add_button = Button(self, label="Add a tab")
        self.Bind(wx.EVT_BUTTON, self.OnAddTab, add_button)

        sizer.Add(add_button, wx.ALIGN_LEFT)
        sizer.Layout()
        return panel

    def OnAddTab(self, event):
        """
        Display the form that allows the user the name of the new tab. It creates
        an empty tab if the user press the "OK" button.
        """
        dlg = wx.TextEntryDialog(self, "Choose the name of the new tab")
        if dlg.ShowModal() == wx.ID_OK:
            tab_name = dlg.GetValue()
            component = ParametersComponent(self.notebook, [], self.interface)
            self.notebook.AddPage(component, tab_name, select=True)
            self.OnRefresh(None)
        dlg.Destroy()

    def _create_command_panel(self):
        """
        Create the panel that handles the display of the build command and the
         buttons that allows the user to refresh, copy or execute this command.
        """
        panel = Panel(self)
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        panel.SetSizer(sizer)

        exec_button = Button(panel, label="Exec")
        terminal_button = Button(panel, label="Exec in Terminal")
        copy_button = Button(panel, label="Copy")

        self.Bind(wx.EVT_BUTTON, self.OnTerminal, terminal_button)
        self.Bind(wx.EVT_BUTTON, self.OnCopy, copy_button)
        self.Bind(wx.EVT_BUTTON, self.OnExec, exec_button)

        sizer.Add(exec_button, 1, wx.EXPAND)
        sizer.Add(terminal_button, 1, wx.EXPAND)
        sizer.Add(copy_button, 1, wx.EXPAND)
        sizer.Layout()

        return panel

    def OnRefresh(self, event):
        """
        Refresh the display of the build command.
        """
        self.command_field.ChangeValue(self.as_command())

    def OnTerminal(self, event):
        """
        Execute the build command and display the result in a popup window.
        """
        instruction = shlex.split(self.as_command())
        proc = subprocess.run(instruction, universal_newlines=True)

    def OnExec(self, event):
        """
        Execute the build command and display the result in a popup window.
        """
        output = self._exec_command(self.as_command())
        dlg = ScrolledMessageDialog(self, output,
         "Output of the command:", size=(600, 300))
        dlg.ShowModal() # Shows it
        dlg.Destroy() # finally destroy it when finished.

    def _exec_command(self, command):
        """
        Execute a command and return its result.
        """
        instruction = shlex.split(command)
        proc = subprocess.run(instruction, stdout=subprocess.PIPE,
         stderr=subprocess.PIPE, universal_newlines=True)

        if proc.returncode == 0:
            return proc.stdout
        else:
            return proc.stderr

    def OnCopy(self, event):
        """
        Copy the build command into the clipboard.
        """
        clipdata = wx.TextDataObject()
        clipdata.SetText(self.as_command())
        wx.TheClipboard.Open()
        wx.TheClipboard.SetData(clipdata)
        wx.TheClipboard.Close()

    def to_template(self):
        """
        This function translate the object into a template dict in order to ease
        the writing of yaml template
        """
        template = {}
        for page in range(self.notebook.GetPageCount()):
            component = self.notebook.GetPage(page)
            tab_name = self.notebook.GetPageText(page)
            template.update({tab_name:component.to_template()})
        return template

    def as_command(self):
        """
        This function return the part of the instruction it represents as a string
        """
        command = []
        for page in range(self.notebook.GetPageCount()):
            component = self.notebook.GetPage(page)
            command_part = component.as_command()
            if not command_part == '':
                command.append(command_part)
        return "{} {}".format(self.command, " ".join(command))
