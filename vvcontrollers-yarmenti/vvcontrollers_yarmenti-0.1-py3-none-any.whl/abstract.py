import abc
from pubsub import Publisher


class AbstrController(Publisher, metaclass=abc.ABCMeta):
    def __init__(self, name):
        self.name = name

    def render(self):
        return [self._get_layout()]

    @property
    def triggerable_messages(self):
        return ["show_dialog", "hide_dialog"]

    def show_dialog(self, title, text):
        self.trigger("show_dialog", {"title": title, "content": text})

    def hide_dialog(self):
        self.trigger("hide_dialog")

    @abc.abstractmethod
    def _get_layout(self):
        pass
