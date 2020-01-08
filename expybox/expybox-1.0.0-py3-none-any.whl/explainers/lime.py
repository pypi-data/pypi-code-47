from typing import Callable, List, Optional, Dict

from ipywidgets import GridspecLayout, BoundedIntText, BoundedFloatText, Dropdown, Checkbox, Text
from lime.lime_tabular import LimeTabularExplainer
from math import sqrt
import numpy as np
from ..utils.utils import UpdatingCombobox
from .explainer import Explainer


class Lime(Explainer):
    resources = {
        'Documentation (lime_tabular)': 'https://lime-ml.readthedocs.io/en/latest/lime.html#module-lime.lime_tabular',
        'LIME in IML book': 'https://christophm.github.io/interpretable-ml-book/lime.html',
        'LIME paper': 'https://arxiv.org/abs/1602.04938',
        'lime package on GitHub': 'https://github.com/marcotcr/lime',
        'Options for distance metric':
            'https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise_distances.html'
    }

    require_instance = True

    def __init__(self, train_data: np.array, predict_function: Callable, mode: str,
                 globals_options: dict.keys, feature_names: List[str],
                 categorical_names: Optional[Dict[int, str]] = None, class_names: Optional[List[str]] = None):
        self.X_train = train_data
        self.predict_function = predict_function
        self.mode = mode
        self.globals_options = globals_options
        self.categorical_names = categorical_names or {}
        self.class_names = class_names or []
        self.feature_names=feature_names

    def build_options(self):
        grid = GridspecLayout(4, 2)
        options_map = {}

        style = {'description_width': '60%', 'width': 'auto'}

        # num features
        num_features = BoundedIntText(
            value=10,
            min=0,
            max=999999,
            step=1,
            description='Number of features:',
            style=style,
            description_tooltip='Maximum number of features present in explanation'
        )
        options_map['num_features'] = num_features

        # num samples
        num_samples = BoundedIntText(
            value=5000,
            min=0,
            max=999999,
            step=1,
            description='Number of samples:',
            style=style,
            description_tooltip='Size of the neighborhood to learn the linear model'
        )
        options_map['num_samples'] = num_samples

        # kernel_width
        kernel_width = BoundedFloatText(
            value=0.75,
            min=0,
            max=999999,
            step=0.05,
            description='Kernel width:',
            style=style,
            description_tooltip='Kernel width for the exponential kernel. Actual value used will be '
                                'value * sqrt(num_of_cols_in_train_data)'
        )
        options_map['kernel_width'] = kernel_width

        # feature_selection
        feature_selection = Dropdown(
            description='Feature selection:',
            style=style,
            description_tooltip='Feature selection method\n'
                                ' - forward_selection: iteratively add features to the model, '
                                'costly when num_features is high\n'
                                ' - highest_weights: selects the features that have the highest'
                                'product of absolute weight * original data point when learning with all the features\n'
                                ' - lasso_path: chooses features based on the lasso regularization path\n'
                                ' - none: uses all features, ignores num_features\n'
                                ' - auto: uses forward_selection if num_features <= 6, and highest_weights otherwise'
                                ,
            options=['forward_selection', 'highest_weights', 'lasso_path', 'none', 'auto'],
            value='auto'
        )
        options_map['feature_selection'] = feature_selection

        # discretize_continuous
        discretize_continuous = Checkbox(
            description='Discretize continuous',
            # style=style,
            value=True,
            title='Whether to discretize all non-categorical features'  # This doesn't work...
                                                                        # I don't know how to get a tooltip to checkbox
        )
        options_map['discretize_continuous']= discretize_continuous

        # discretizer
        discretizer = Dropdown(
            description='Discretizer:',
            style=style,
            options=['quartile', 'decile'],  # not supporting entropy, because we don't have training labels :/
            value='quartile',
            description_tooltip='Which discretizer to use. Only matters if discretize continuous is True'
        )
        options_map['discretizer'] = discretizer

        # set up disabling of discretizer dropdown if discretize_continuous is not checked
        def disable_discretizer(change):
            discretizer.disabled = not change['new']
        discretize_continuous.observe(disable_discretizer, names=['value'])

        # distance_metric
        distance_metric = Text(
            description='Distance metric:',
            style=style,
            value='euclidean',
            description_tooltip='What distance metric to use (for weights). '
                                'Used as an "distance_metric" argument for sklearn.metrics.pairwise_distances'
        )
        options_map['distance_metric'] = distance_metric

        # model_regressor
        model_regressor = UpdatingCombobox(
            options_keys=self.globals_options,
            description='Variable with model regressor:',
            style=style,
            value='None',
            description_tooltip='sklearn regressor to use in explanation. Defaults to Ridge regression if None. '
                                'Must have model_regressor.coef_ and "sample_weight" as a parameter '
                                'to model_regressor.fit()\n\n'
                                '(specify the name of the variable with regressor that you have in the notebook)'
        )
        model_regressor.lookup_in_kernel = True
        options_map['model_regressor'] = model_regressor

        grid[0, 0] = num_features
        grid[0, 1] = num_samples
        grid[1, 0] = kernel_width
        grid[1, 1] = feature_selection
        grid[2, 0] = discretize_continuous
        grid[2, 1] = discretizer
        grid[3, 0] = distance_metric
        grid[3, 1] = model_regressor

        return options_map, grid

    def explain(self, options, instance=None):
        if instance is None:
            raise ValueError("Instance was not provided")
        explainer = LimeTabularExplainer(training_data=self.X_train,
                                         feature_names=self.feature_names,
                                         mode=self.mode,
                                         categorical_features=self.categorical_names.keys(),
                                         categorical_names=self.categorical_names,
                                         class_names=self.class_names,
                                         kernel_width=options['kernel_width'] * sqrt(self.X_train.shape[1]),
                                         feature_selection=options['feature_selection'],
                                         discretize_continuous=options['discretize_continuous'],
                                         discretizer=options['discretizer'])
        explanation = explainer.explain_instance(data_row=instance,
                                                 predict_fn=self.predict_function,
                                                 num_features=options['num_features'],
                                                 num_samples=options['num_samples'],
                                                 distance_metric=options['distance_metric'],
                                                 model_regressor=options['model_regressor'])
        explanation.show_in_notebook()