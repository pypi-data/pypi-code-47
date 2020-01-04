from typing import Iterable
from ipywidgets import Combobox


class UpdatingCombobox(Combobox):
    """
    Custom Combobox that updates its options from provided options_keys
    Unfortunately I didn't come up with a better way of detecting when to update the options
    (I can't make an observer, because I can't force Jupyter kernel to update globals() through my class)
    """
    def __init__(self, options_keys: Iterable, *args, **kwargs):
        """
        The same init as for ipywidgets.Combobox, but with additional argument options_keys
        :param options_keys: Keys object of a dictionary (or anything else that can be made into a list :))
        :param args:
        :param kwargs:
        """
        super().__init__(*args, **kwargs)
        self.options_keys = options_keys
        self.observe(self.update_options)

    def update_options(self, change) -> None:
        """
        Updates the options
        :param change: ignored, but required by ipywidgets api
        :return: None
        """
        options = list(self.options_keys)
        options.append('None')
        self.options = options
