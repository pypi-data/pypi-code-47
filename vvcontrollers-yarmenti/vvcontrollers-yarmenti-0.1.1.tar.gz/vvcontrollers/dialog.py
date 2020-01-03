
from .abstract import AbstrController
import ipyvuetify as v


class DialogController(AbstrController):
    __layout = v.Dialog(
        width="unset",
        v_model=False,
        children=[
            v.Card(children=[
                v.CardTitle(class_='headline gray lighten-2',
                            primary_title=True,
                            children=[]),
                v.CardText(children=[])
            ])
        ]
    )

    def __init__(self):
        super().__init__("dialog")

    def _get_layout(self):
        return self.__layout

    def show(self, card_title, card_text):
        card = self.__layout.children[0]
        card.children[0].children = [card_title]
        card.children[1].children = [card_text]

        self.__layout.v_model = True

    def hide(self):
        self.__layout.v_model = False
