from typing import List, Callable, Optional, Dict, Union, Tuple
import numpy as np
from IPython.core.display import display
from shap import kmeans, KernelExplainer, force_plot, initjs, decision_plot, summary_plot
from shap.common import DenseData
from ..utils.utils import UpdatingCombobox
from .explainer import Explainer
from ipywidgets import Dropdown, GridspecLayout, Checkbox, BoundedIntText, Combobox, Widget


class Shap(Explainer):
    resources = {
        'SHAP paper': 'https://arxiv.org/abs/1705.07874',
        'SHAP in IML book': 'https://christophm.github.io/interpretable-ml-book/shap.html',
        'Documentation of shap': 'https://shap.readthedocs.io/en/latest/#shap.KernelExplainer',
        'Implementation (currently documentation replacement) of <b>force</b> plot':
            'https://github.com/slundberg/shap/blob/master/shap/plots/force.py#L31',
        'Implementation (currently documentation replacement) of <b>decision</b> plot':
            'https://github.com/slundberg/shap/blob/master/shap/plots/decision.py#L216',
    }

    require_instance = True

    def __init__(self, train_data: np.array, predict_function: Callable, globals_options: dict.keys,
                 feature_names: List[str], is_classification: bool = True, class_names: Optional[List[str]] = None):
        self.X_train = train_data
        self.predict_function = predict_function
        self.globals_options = globals_options
        self.is_classification = is_classification
        self.class_names = class_names or []
        self.sampled_background = {}
        self.feature_names = feature_names

    def build_options(self):
        grid = GridspecLayout(4, 2)
        options_map = {}
        style = {'description_width': '60%'}

        # plot_type
        plot_type = Dropdown(
            description='Plot:',
            options=['force', 'decision', 'both'],
            description_tooltip='Which plot to draw, decision or force',
            style=style
        )
        options_map['plot_type'] = plot_type

        # background_data
        background_data = Dropdown(
            description='Background data:',
            options={'KMeans': 'kmeans', 'Custom variable': 'custom'},
            value='kmeans',
            description_tooltip='What background data will be used to sample from, when simulating "missing" feature\n'
                                ' - KMeans: use KMeans to sample from provided dataset\n'
                                ' - Custom variable: provide variable with instances to use',
            style=style
        )
        options_map['background_data'] = background_data

        # kmeans_count (only show when KMeans is chosen)
        kmeans_count = BoundedIntText(
            value=100,
            min=1,
            max=len(self.X_train),
            description='Count of KMeans centers:',
            description_tooltip='Number of means to use when creating background data',
            style=style
        )
        options_map['kmeans_count'] = kmeans_count

        # data (only show when Custom variable is chosen)
        data = UpdatingCombobox(
            options_keys=self.globals_options,
            description='Background data variable:',
            options=list(self.globals_options),
            description_tooltip='Variable with background data from which the "missing" features will be sampled',
            style=style
        )
        options_map['data'] = data

        # set up swap of options
        def swap_kmeans(change):
            if change['new'] == 'kmeans':
                data.lookup_in_kernel = False
                grid[1, 1] = kmeans_count
            else:
                data.lookup_in_kernel = True
                grid[1, 1] = data

        background_data.observe(swap_kmeans, names=['value'])

        # link
        link = Dropdown(
            description='Link:',
            options=['identity', 'logit'],
            value='identity',
            description_tooltip='A generalized linear model link to connect the feature importance values '
                                'to the model output.\n'
                                'Since the feature importance values, phi, sum up to the model output, '
                                'it often makes sense to connect them to the ouput with a link function '
                                'where link(outout) = sum(phi).\n '
                                'If the model output is a probability then the LogitLink link function makes '
                                'the feature importance values have log-odds units.',
            style=style
        )
        options_map['link'] = link

        # nsamples
        nsamples = BoundedIntText(
            min=1,
            max=999999,
            value=2048,
            disabled=True,
            description='Model sample size:',
            description_tooltip='Number of times to re-evaluate the model when explaining each prediction.\n'
                                'More samples lead to lower variance estimates of the SHAP values.\n'
                                'The "auto" setting uses nsamples = 2 * X.shape[1] + 2048.',
            style=style
        )
        options_map['nsamples'] = nsamples

        # auto_nsamples
        auto_nsamples = Checkbox(
            description='Auto choose model sample size',
            value=True,
            style={'description_width': 'auto'}
        )
        options_map['auto_nsamples'] = auto_nsamples

        def disable_nsamples(change):
            nsamples.disabled = change['new']

        auto_nsamples.observe(disable_nsamples, names=['value'])

        # l1_reg
        l1_reg = Combobox(
            description='L1 regularization:',
            options=['auto', 'aic', 'bic'],
            value='auto',
            description_tooltip='The l1 regularization to use for feature selection '
                                '(the estimation procedure is based on a debiased lasso).\n'
                                ' - The auto option currently uses "aic" when less that 20% '
                                'of the possible sample space is enumerated, otherwise it uses no regularization.\n'
                                ' - The "aic" and "bic" options use the AIC and BIC rules for regularization.\n'
                                ' - Integer selects a fix number of top features.\n'
                                ' - float directly sets the "alpha" parameter of the sklearn.linear_model.Lasso model '
                                'used for feature selection',
            style=style
        )
        options_map['l1_reg'] = l1_reg

        # class_to_explain (only if classification)
        if self.is_classification:
            class_to_explain = Dropdown(
                description='Class to plot:',
                options={val: e for e, val in enumerate(self.class_names)},
                description_tooltip='For classification select a class for which the prediction will be explained',
                style=style
            )
            options_map['class_to_explain'] = class_to_explain
            grid[3, 1] = class_to_explain

        grid[0, 0] = plot_type
        grid[1, 0] = background_data
        grid[1, 1] = kmeans_count
        grid[0, 1] = link
        grid[2, 0] = nsamples
        grid[2, 1] = auto_nsamples
        grid[3, 0] = l1_reg

        return options_map, grid

    def explain(self, options, instance=None):

        if instance is None:
            raise ValueError("Instance was not provided")

        initjs()
        instance = instance.to_numpy()
        data = self._kmeans(options['kmeans_count']) \
            if options['background_data'] == 'kmeans' else options['data']
        nsamples = 'auto' if options['auto_nsamples'] else options['nsamples']
        explainer = KernelExplainer(
            model=self.predict_function,
            data=data,
            link=options['link']
        )
        shap_values = explainer.shap_values(
            X=instance,
            nsamples=nsamples,
            l1_reg=options['l1_reg']
        )
        if self.is_classification:
            shap_values = shap_values[options['class_to_explain']]
            base_value = explainer.expected_value[[options['class_to_explain']]]
        else:
            base_value = explainer.expected_value

        if options['plot_type'] == 'force' or options['plot_type'] == 'both':
            display(force_plot(
                base_value=base_value,
                shap_values=shap_values,
                features=instance,
                feature_names=self.feature_names,
                show=True,
                link=options['link'])
            )

        if options['plot_type'] == 'decision' or options['plot_type'] == 'both':
            decision_plot(
                base_value=base_value,
                shap_values=shap_values,
                features=instance,
                feature_names=list(self.feature_names),
                show=True,
                color_bar=True,
                link=options['link']
            )

    def _kmeans(self, means: int) -> DenseData:
        """
        Wrapper to cache kmeans results for repeated runs
        :param means: amount of centers for kmeans
        :return: kmeaned background data for shap (either from cache or newly counted)
        """
        if means in self.sampled_background.keys():
            return self.sampled_background[means]
        self.sampled_background[means] = kmeans(self.X_train, means)
        return self.sampled_background[means]


class ShapFI(Shap):
    resources = {
        'SHAP paper': 'https://arxiv.org/abs/1705.07874',
        'SHAP in IML book': 'https://christophm.github.io/interpretable-ml-book/shap.html',
        'Documentation of shap': 'https://shap.readthedocs.io/en/latest/#shap.KernelExplainer',
        'Implementation (currently documentation replacement) of <b>summary</b> plot':
            'https://github.com/slundberg/shap/blob/master/shap/plots/summary.py#L18'
    }

    require_instance = False

    def build_options(self):
        options_map, options_grid = super().build_options()
        # remove unnecessary dropdown with plot selection
        options_map['plot_type'].layout.visibility = 'hidden'
        del options_map['plot_type']

        # and with class_to_explain (if it exists)
        if self.is_classification:
            # only the assignment triggers actual change of the widget (and only if it's not the original dict)
            options = options_map['class_to_explain'].options.copy()
            options['All'] = -1
            options_map['class_to_explain'].options = options
            options_map['class_to_explain'].value = -1

        # sample_size
        sample_size = BoundedIntText(
            min=1,
            max=self.X_train.shape[0],
            step=1,
            value=min(self.X_train.shape[0], 1000),
            description='Sample size:',
            description_tooltip='Number of instances from train data to use for calculating mean shap value.',
            style={'description_width': '60%'}
        )
        options_map['sample_size'] = sample_size
        options_grid[0, 0] = sample_size

        return options_map, options_grid

    def explain(self, options, instance=None):
        initjs()
        background_data = self._kmeans(options['kmeans_count']) \
            if options['background_data'] == 'kmeans' else options['data']
        nsamples = 'auto' if options['auto_nsamples'] else options['nsamples']
        explainer = KernelExplainer(
            model=self.predict_function,
            data=background_data,
            link=options['link']
        )
        # create sample from train data
        data = self.X_train[np.random.choice(self.X_train.shape[0], size=options['sample_size'], replace=False), :]

        shap_values = explainer.shap_values(
            X=data,
            nsamples=nsamples,
            l1_reg=options['l1_reg']
        )

        # limit to only selected class (if any was selected)
        if 'class_to_explain' in options and options['class_to_explain'] != -1:
            shap_values = shap_values[options['class_to_explain']]

        summary_plot(
            shap_values=shap_values,
            features=data,
            feature_names=self.feature_names,
            plot_type='bar',
            class_names=self.class_names
        )
