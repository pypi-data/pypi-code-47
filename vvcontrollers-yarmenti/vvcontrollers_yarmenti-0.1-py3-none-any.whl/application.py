
import ipyvuetify as v


class ApplicationVoilaVuetify():
    def __init__(self, core_view, menu_view):
        self.__res = core_view
        self.__menu = menu_view

        # Attaching events
        self.__menu.attach(self.__res, "change_view")
        _ = [controller.attach(self.__res, "show_dialog")
             for controller in self.__menu.controllers]
        _ = [controller.attach(self.__res, "hide_dialog")
             for controller in self.__menu.controllers]

    def render(self):
        children = self.__menu.render() + self.__res.render()
        return v.Container(children=children)
