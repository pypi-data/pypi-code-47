
from pubsub import Subscriber

from abstract import AbstrController
from dialog import DialogController
import ipyvuetify as v


class CoreController(AbstrController, Subscriber):
    __layout = v.Container(
        _metadata={"mount_id": "content-main"},
        class_="my-4 mx-5", fluid=True,
        children=[]
    )

    def __init__(self, dialog_ctrlr=None):
        super().__init__("core")
        self.__init_dialog(dialog_ctrlr)
        self.__init_event_reactions()

    def __init_dialog(self, dialog_ctrlr):
        if dialog_ctrlr is None:
            dialog_ctrlr = DialogController()

        self.__dialog = dialog_ctrlr

    def __init_event_reactions(self):
        self.__on_message = {
            "change_view": self.__on_change_view,
            "show_dialog": self.__on_show_dialog,
            "hide_dialog": self.__on_hide_dialog
        }

    def __on_change_view(self, arg):
        children = self.__dialog.render() + arg.render()
        self.__layout.children = children

    def __on_show_dialog(self, arg):
        self.__dialog.show(arg["title"], arg["content"])

    def __on_hide_dialog(self, arg):
        self.__dialog.hide()

    def _get_layout(self):
        return self.__layout

    def on_message(self, message, arg):
        self.__on_message[message](arg)
