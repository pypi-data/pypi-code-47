from typing import Dict, Any, Tuple
from ipywidgets import Widget, Box
from numpy import array


class Explainer:
    """
    This is base class for all explainers. It just specifies what methods should they implement
    """
    resources = {}
    """
    Each explainer should provide its dict of resources {Description (str): link (str)}
    These will be shown in the 'Resources' tab
    """

    def build_options(self) -> Tuple[Dict[str, Widget], Box]:
        """
        Builds tab that will be displayed as 'Method parameters' tab
        :return: - dictionary of options {str: widget} - the explain_model and explain_instance methods will get a dict
        with the same keys passed, but with values being the value property of the widgets.
        If the widget has .lookup_in_kernel attribute set to True, the value will be looked up in globals that were
        provided by the user when instantiating ExpyBox class.
                - Box of widgets to display on the 'Method parameters' tab.
        """
        pass

    def explain_model(self, options: Dict[str, Any]) -> None:
        """
        Explain the whole model, if the method supports it. This method is called if we don't provide an instance to be
        explained.
        If the method the subclass is implementing doesn't support such explanation of model, it can either fail
        (raise an Exception) or just not implement it, i.e. just pass.
        :param options: dictionary of options {str: Any} with values based on what build_options method returned as
        the first value in returned tuple (see documentation of build_options).
        :return: None
        """
        pass

    def explain_instance(self, options: Dict[str, Any], instance: array) -> None:
        """
        Explain the given instance, if the method supports it. This method is called when we provide an instance to be
        explained.
        If the method the subclass is implementing doesn't support such explanation of model, it can either fail
        (raise an Exception) or just not implement it, i.e. just pass.
        :param options: dictionary of options {str: Any} with values based on what build_options method returned as
        the first value in returned tuple (see documentation of build_options).
        :param instance: numpy array with shape (1, #features) representing the single instance to explain
        :return: None
        """
        pass
