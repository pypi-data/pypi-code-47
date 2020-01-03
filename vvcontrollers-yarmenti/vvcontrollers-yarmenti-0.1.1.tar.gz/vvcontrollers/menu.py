
from pubsub import Publisher
from .abstract import AbstrController
import ipyvuetify as v


class MenuController(AbstrController, Publisher):
    __elements = []
    __controllers = []

    def __init__(self):
        super().__init__("menu")

    @property
    def triggerable_messages(self):
        return ["change_view"]

    @property
    def controllers(self):
        return self.__controllers

    def add_element(self, icon, controller):
        link = v.ListItem(href="#", children=[
            v.ListItemAction(
                children=[v.Icon(children=[icon])]
            ),
            v.ListItemContent(
                children=[v.ListItemTitle(children=[controller.name])]
            )
        ])

        def on_click(*change):
            self.trigger("change_view", controller)

        link.on_event("click", on_click)

        self.__elements.append(link)
        self.__controllers.append(controller)

    def _get_layout(self):
        return v.Container(
            pa_4=True, _metadata={"mount_id": "content-nav"},
            column=True, children=[
                v.List(dense=True, children=self.__elements)
            ]
        )
