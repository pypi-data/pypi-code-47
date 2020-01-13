from math import ceil
from typing import Union, Callable, Optional, Tuple, List, Dict, Any
import numpy as np
import pandas as pd
from IPython.display import display
from ipywidgets import Dropdown, GridspecLayout, FloatText, widgets, Accordion, Tab, \
    interact_manual, fixed, VBox, Layout, HTML, Box, Widget, Button, ValueWidget
from .utils.utils import UpdatingCombobox
from .explainers.anchors import Anchors
from .explainers.explainer import Explainer
from .explainers.lime import Lime
from .explainers.pdp import PDP
from .explainers.shap import Shap, ShapFI
import warnings


class ExpyBox:
    """
    Main class to instantiate and hold global data like predict_function, train_data and so on.

    :param train_data: ``numpy array or pandas dataframe of shape (#instances, #features)``
        Data used to explain models (for methods that require data)
        and to offer instances from (when building instance).
        Categorical features need to be label_encoded into integers starting from 0.
        One-hot encoding is not currently supported.
    :param predict_function: ``Callable``
        Predict function of a model.
        In case of classification it should return probabilities of classes for each class.
        **Needs** to be able to deal with numpy array with shape (#instances, #features). If that's not the case for
        your model, I recommend writing a wrapper function and pass that one.
    :param kernel_globals: ``dict``
        A dictionary with name_of_variable: variable (NOT its value!) from your kernel.
        Used to enable passing variable declared in your Jupyter notebook as a value to certain fields.
        You can either create this dictionary yourself (if you know what you're doing)
        or just use globals() (this is the recommended usage as it updates when you declare new variable
        and you don't need to care about it - i.e. just do ... kernel_globals=globals(), ...)
    :param categorical_names: ``dict``
        A dictionary with index_of_feature: list of the names for categorical features.
        For example if n-th feature of train_data (train_data[:, n]) is categorical the dict entry should look like
        this: {n: [name_if_0, name_if_1, name_if_2, ... ]}
        Used for better readability and determining which features are categorical, which improves some methods.
    :param mode: `'classification' or 'regression'`
    :param class_names: ``list``
        Names for output classes in order in which the predict_function returns
        probabilities for them. Used just to make input and output more human-friendly
    :param feature_names: ``list``
        Names for features in order of appearing in train_data. If not filled and train_data is
        an instance of pandas.DataFrame, train_data.columns is used.
        Used to make input and output more human-friendly
    """

    def __init__(self,
                 train_data: Union[pd.DataFrame, np.array],
                 predict_function: Callable,
                 kernel_globals: Optional[dict] = None,
                 categorical_names: Optional[dict] = None,
                 mode: Optional[str] = 'classification',
                 class_names: Optional[list] = None,
                 feature_names: Optional[list] = None):
        if len(train_data.shape) == 1:
            raise ValueError(f"Expected 2D array, got 1D array instead:{train_data}.\n"
                             f"Reshape your data either using array.reshape(-1, 1) if your data has a single feature "
                             f"or array.reshape(1, -1) if it contains a single sample.")
        # transform to numpy
        if isinstance(train_data, pd.DataFrame):
            self.X_train = train_data.to_numpy()
        else:
            self.X_train = train_data

        self.categorical_names = categorical_names or {}
        self.predict_function = predict_function
        self.mode = mode
        self.kernel_globals = kernel_globals or {}
        # find out how many classes are there if this is classification
        self.class_count = 1
        if self.mode == 'classification':
            self.class_count = self.predict_function(self.X_train[0, :].reshape(1, -1)).shape[0]

        self.class_names = class_names or [i for i in range(self.class_count)]

        # feature names handling
        if not feature_names:
            if isinstance(train_data, pd.DataFrame):
                self.feature_names = list(train_data.columns)
            else:
                self.feature_names = [i for i in range(train_data.shape[1])]
        else:
            if len(feature_names) != self.X_train.shape[1]:
                raise ValueError('Len of feature_names != train_data.shape[1]. '
                                 'Please provide feature_names argument of correct length')
            self.feature_names = feature_names

    def _build_instance_creation_widgets(self) -> Tuple[list, VBox]:
        """
        Build widgets for creating instance and put them into their respective accordions
        :return: list of instance creation widgets (for easier manipulation and getting values from them),
                 VBox (layout) to be displayed in a tab
        """
        instance_widgets = []
        style = {'description_width': '60%', 'width': 'auto'}

        # create widget for each variable
        for e, column in enumerate(self.feature_names):
            if e in self.categorical_names:
                # for categoricals make dropdown with name, but value as a number (from 0)
                options = {key: val for val, key in enumerate(self.categorical_names[e])}
                instance_widgets.append(Dropdown(description=f"{column}:",
                                                 options=options,
                                                 style=style)
                                        )
            else:
                instance_widgets.append(FloatText(description=f"{column}: ", style=style))

        # fill grid with widgets
        widgets_grid = GridspecLayout(ceil(self.X_train.shape[1] / 2), 2,
                                      layout=Layout(overflow='scroll', max_height='25em'))

        for e, item in enumerate(instance_widgets):
            widgets_grid[e // 2, e % 2] = item

        # add the selection of instance in train data
        fill_from_df = widgets.BoundedIntText(
            value=0,
            min=0,
            max=len(self.X_train) - 1,
            step=1,
            description='Instance id:',
            style=style,
            description_tooltip='When changed all values in "Build your own instance" will be set accordingly'
        )

        # connect instance selection to builder widgets
        def on_value_change(change):
            instance = self.X_train[change['new']]
            for e, val in enumerate(instance):
                instance_widgets[e].value = val

        fill_from_df.observe(on_value_change, names='value')

        # importing instance from variable
        instance_variable = UpdatingCombobox(
            options_keys=self.kernel_globals.keys(),
            value='',
            description='Variable with instance:',
            description_tooltip='Variable with your instance as numpy array, pandas dataframe or series.\n'
                                'After clicking on "import instance", the values in "Build your own instance"'
                                ' will be set accordingly.',
            style=style
        )

        def fill_from_variable(orig_btn):
            # param ignored
            instance = self._get_variable_from_kernel(instance_variable.value)
            try:
                for e, val in enumerate(instance):
                    instance_widgets[e].value = val
                # reset to without error
                import_box.children = [instance_variable, import_btn]
            except:
                # add error to box
                import_box.children = [instance_variable, import_btn, import_error]

        import_error = HTML("Import from variable failed\n")
        import_btn = Button(
            description='Import'
        )
        import_btn.on_click(fill_from_variable)

        import_box = VBox(children=(instance_variable, import_btn))

        # put both into separate accordions to allow both opened at the same time
        accordion1 = Accordion(children=[fill_from_df, import_box])
        accordion1.set_title(0, 'Select instance from dataset')
        accordion1.set_title(1, 'Import instance from variable')
        accordion2 = Accordion(children=[widgets_grid])
        accordion2.set_title(0, 'Build your own instance')
        accordions = VBox([accordion1, accordion2])

        # set everything to first instance
        on_value_change({'new': 0})

        return instance_widgets, accordions

    @staticmethod
    def _build_resources_widgets(resources: Dict[str, str]) -> VBox:
        """
        Build tab with resources (description: html links) to be displayed under 'Resources' tab
        :param resources: Dictionary description: html link from which the values are put into HTML and presented as
        description and link
        :return: VBox with resources to display
        """
        widget_list = []
        for key, val in resources.items():
            widget_list.append(
                HTML(
                    value=f"{key}: <a href='{val}' target='_blank'>{val}</a>",
                )
            )
        return VBox(widget_list)

    def _build_instance_and_call(self, options: Dict[str, ValueWidget],
                                 call: Callable,
                                 instance_widgets: Optional[List[ValueWidget]] = None) -> None:
        """
        Build instance from instance_widgets values, transform options from widgets to their values (including lookup
        from Jupyter kernel) and then call provided callable
        :param options: Dictionary str: widget. Will be transformed to not contain widgets but actual values and passed
        to the callable specified in call.
        :param call: Callable to call after instance is built and options transformed. Will pass (options, instance).
        :param instance_widgets: List of widgets used for instance creation (should be of len(#features))
            if none, instance passed to call will be None
        :return: None
        """
        if instance_widgets is None:
            inst = None
        else:
            inst = pd.Series([x.value for x in instance_widgets], index=self.feature_names)
        options = options.copy()
        for key, val in options.items():
            if hasattr(val, 'lookup_in_kernel') and val.lookup_in_kernel:
                options[key] = self._get_variable_from_kernel(val.value)
            else:
                options[key] = val.value
        call(options, inst)

    def _get_variable_from_kernel(self, variable_name: str) -> Any:
        """
        Lookup variable in kernel_global, if it's not 'None' indicating that the lookup should not be done.
        :param variable_name:
        :return: Variable from Jupyter kernel or None if not found or str == 'None'
        """
        if variable_name == 'None':
            return None
        elif variable_name in self.kernel_globals:
            return self.kernel_globals[variable_name]
        else:
            warnings.warn(f"Variable {variable_name} was not found in provided kernel_globals, reverting to None")
            return None

    def _build_tabs(self, resources: dict, options_box: Box, instance_creation: Optional[Box] = None) -> Tab:
        """
        Build tabs of widgets to display in Jupyter notebook
        :param resources: Dictionary description: html link from which the values are put into HTML and presented as
        description and link
        :param options_box: Box with method parameters/options (displayed under 'Method parameters' tab)
        :param instance_creation: Box with instance creation widget (displayed under 'Explained instance' tab)
        if provided. If None, no 'Explained instance' tab will be created.
        :return: Tabs to be displayed
        """
        tabs = Tab()
        if instance_creation is not None:
            tabs.children = [instance_creation, options_box, self._build_resources_widgets(resources)]
            tabs.set_title(0, 'Explained instance')
            tabs.set_title(1, 'Method parameters')
            tabs.set_title(2, 'Resources')
        else:
            tabs.children = [options_box, self._build_resources_widgets(resources)]
            tabs.set_title(0, 'Method parameters')
            tabs.set_title(1, 'Resources')
        return tabs

    def _display_interact(self, explainer: Explainer, explain_instance: Optional[bool] = False) -> None:
        """
        Set up and display interact dialog with given explainer
        :param explainer: Explainer instance that will be used
        :param explain_instance: if true Explainer.explain_instance will be called and the dialog will be created with
        'Explained instance' tab, otherwise Explainer.explain_model will be called and no 'Explained instance' tab will
        be created
        :return: None
        """
        options_map, options_grid = explainer.build_options()
        if explain_instance:
            instance_widget_list, instance_creation_grid = self._build_instance_creation_widgets()
            display(self._build_tabs(resources=explainer.resources, options_box=options_grid,
                                     instance_creation=instance_creation_grid))
            interact_manual(self._build_instance_and_call, options=fixed(options_map),
                            call=fixed(explainer.explain), instance_widgets=fixed(instance_widget_list))
        else:
            display(self._build_tabs(resources=explainer.resources, options_box=options_grid))
            interact_manual(self._build_instance_and_call, options=fixed(options_map),
                            call=fixed(explainer.explain), instance_widgets=fixed(None))

    def pdplot(self) -> None:
        """
        Create dialog for partial dependence plot

        :return: None
        """
        pdp = PDP(train_data=self.X_train,
                  predict_function=self.predict_function,
                  feature_names=self.feature_names,
                  globals_options=self.kernel_globals.keys(),
                  is_classification=True if self.mode == 'classification' else False)
        self._display_interact(explainer=pdp, explain_instance=pdp.require_instance)

    def lime(self) -> None:
        """
        Create dialog for lime

        :return: None
        """
        lime = Lime(train_data=self.X_train,
                    predict_function=self.predict_function,
                    mode=self.mode,
                    globals_options=self.kernel_globals.keys(),
                    feature_names=self.feature_names,
                    categorical_names=self.categorical_names,
                    class_names=self.class_names)
        self._display_interact(explainer=lime, explain_instance=lime.require_instance)

    def anchors(self) -> None:
        """
        Create dialog for Anchors

        :return: None
        """
        anchors = Anchors(predict_function=self.predict_function,
                          globals_options=self.kernel_globals.keys(),
                          train_data=self.X_train,
                          feature_names=self.feature_names,
                          categorical_names=self.categorical_names,
                          is_classification=True if self.mode == 'classification' else False,
                          class_names=self.class_names
                          )
        self._display_interact(explainer=anchors, explain_instance=anchors.require_instance)

    def shap(self) -> None:
        """
        Create dialog for shap, providing force and decision plots

        :return: None
        """
        shap = Shap(train_data=self.X_train,
                    predict_function=self.predict_function,
                    globals_options=self.kernel_globals.keys(),
                    feature_names=self.feature_names,
                    is_classification=True if self.mode == 'classification' else False,
                    class_names=self.class_names
                    )
        self._display_interact(explainer=shap, explain_instance=shap.require_instance)

    def shap_feature_importance(self) -> None:
        """
        Create dialog for shap summary plot, i.e. feature importance based on Shapley values

        :return: None
        """
        shap = ShapFI(train_data=self.X_train,
                      predict_function=self.predict_function,
                      globals_options=self.kernel_globals.keys(),
                      feature_names=self.feature_names,
                      is_classification=True if self.mode == 'classification' else False,
                      class_names=self.class_names
                      )
        self._display_interact(explainer=shap, explain_instance=shap.require_instance)
