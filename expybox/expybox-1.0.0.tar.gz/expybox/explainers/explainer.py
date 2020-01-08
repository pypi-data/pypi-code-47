from typing import Dict, Any, Tuple, Optional
from ipywidgets import Widget, Box
from numpy import array


class Explainer:
    """
    This is base class for all explainers. It just specifies what methods should they implement
    """
    resources = {}
    """
    Each explainer should provide its dict of resources {Description (str): link (str)}
    These will be shown in the 'Resources' tab.
    """
    require_instance = False
    """
    This parameter tells the ExpyBox if the method requires an instance for explanation.
    If True, the explain method will be called with valid instance (i.e. not None) and user will be offered a form to
    build such instance.
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

    def explain(self, options: Dict[str, Any], instance: Optional[array] = None) -> None:
        """
        Run the explanataion and show result in notebook. If self.require_instance is True instance to explain will be
        passed otherwise None is passed
        :param options: dictionary of options {str: Any} with values based on what build_options method returned as
        the first value in returned tuple (see documentation of build_options).
        :param instance: numpy array with shape (1, #features) representing the single instance to explain
        :return: None
        """
        pass
