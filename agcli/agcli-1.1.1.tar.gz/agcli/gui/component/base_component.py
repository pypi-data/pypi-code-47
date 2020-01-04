import wx
from ...event import event_handler
from wx import Panel
import wx
from wx.lib.agw.pycollapsiblepane import PyCollapsiblePane


class Serializable():

    def to_template(self):
        """
        This function translate the object into a template dict in order to ease
        the writing of yaml template. Return nothing if no template should be written.
        """
        raise NotImplementedError

    def as_command(self):
        """
        This function return the part of the instruction it represents as a string.
        Return the empty string if no command should be build.
        """
        raise NotImplementedError

    def _trigger_change_event(self, event):
        """
        Trigger an event to notify that the command has to be refreshed
        """
        event_handler.trigger_value_changed_event(self)

class BaseComponent(wx.CollapsiblePane, Serializable):

    def __init__(self, parent, template, interface):
        super().__init__(parent, label=interface['ID'], style=wx.TAB_TRAVERSAL)
        self.id = interface['ID']
        self.component_sizer = wx.BoxSizer(wx.VERTICAL)
        self.management_sizer = wx.BoxSizer(wx.VERTICAL)
        self.pane_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.GetPane().SetSizer(self.pane_sizer)
        #self.GetPane().SetBackgroundColour("RED")
        self.pane_sizer.Add(self.component_sizer,flag=wx.ALL|wx.EXPAND, border=5, proportion=1)
        self.pane_sizer.Add(self.management_sizer, flag=wx.ALIGN_RIGHT|wx.ALL, border=5)

        self.Bind(wx.EVT_COLLAPSIBLEPANE_CHANGED, self.OnStateChange)
        self.Bind(wx.EVT_MOUSE_EVENTS, self.OnBeginDrag)
        self.Collapse(template['is_collapsed'])

        self.GetParent().Layout()
        self.GetParent().PostSizeEvent()

    def OnStateChange(self, sz):
        """
        This function is called when the collapsible pane is collapsed/uncollapse
        and is use to refresh the parent window.
        """
        self._trigger_change_event(None)
        self.GetParent().PostSizeEvent()
        self.GetParent().Layout()

    def OnBeginDrag(self, event):
        """
        It is called when the user begin a drag and drop action (left button
        mouse is kept down). It computes the data that will be send by the drag
        and drop.
        """
        if event.ButtonDown(wx.MOUSE_BTN_LEFT):
            # Create a Text Data Object, which holds the index of the parameter
            # that is to be dragged
            parameter_index = self.GetParent().get_parameter_index(self.id)
            parameter_path = self.GetParent().get_parameter_path(parameter_index)
            tdo = wx.TextDataObject(parameter_path)
            tds = wx.DropSource(self)
            tds.SetData(tdo)
            # Initiate the Drag Operation
            tds.DoDragDrop(True)

    def refresh_collapse(self):
        """
        Force the widget to compute the size of an expanded panel because the
        size of the panel is not good if it is expanded before other widgets are
        added.
        """
        self.Collapse(not self.IsCollapsed())
        self.Collapse(not self.IsCollapsed())

    def get_command(self):
        """
        This function return the commands the component must returned if the panel
        is not collapsed
        """
        raise NotImplementedError

    def as_command(self):
        if self.IsCollapsed():
            return ''
        else:
            return self.get_command()

    def to_template(self):
        return {"ID": self.id, 'is_collapsed':self.IsCollapsed()}
