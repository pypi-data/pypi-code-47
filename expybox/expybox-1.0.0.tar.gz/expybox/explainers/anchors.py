import warnings
from typing import Callable, Dict, List, Optional
from ipywidgets import GridspecLayout, BoundedFloatText, FloatSlider, BoundedIntText, Combobox
from ..utils.utils import UpdatingCombobox
from .explainer import Explainer
from alibi.explainers.anchor_tabular import AnchorTabular
import numpy as np


class Anchors(Explainer):
    resources = {
        'Anchors paper': 'https://homes.cs.washington.edu/~marcotcr/aaai18.pdf',
        'Anchors (alibi) documentation': 'https://docs.seldon.io/projects/alibi/en/stable/methods/Anchors.html',
        'Alibi API reference':
            'https://docs.seldon.io/projects/alibi/en/stable/api/alibi.explainers.anchor_tabular.html',
        'compute_beta in alibi (how B parameter for beam search is calculated from delta)':
            'https://github.com/SeldonIO/alibi/blob/master/alibi/explainers/anchor_base.py#L116',
    }

    require_instance = True

    def __init__(self, train_data: np.array, predict_function: Callable, globals_options: dict.keys,
                 feature_names: List[str], categorical_names: Dict[int, str], is_classification: bool = True,
                 class_names: Optional[List[str]] = None):
        self.predict_function = predict_function
        self.globals_options = globals_options
        self.X_train = train_data
        self.feature_names = feature_names
        self.categorical_names = categorical_names
        self.is_classification = is_classification
        self.class_names = class_names

    def build_options(self):
        grid = GridspecLayout(3, 2)
        options_map = {}
        style = {'description_width': '60%'}

        # threshold
        threshold = FloatSlider(
            description='Precision threshold',
            value=0.95,
            min=0.,
            max=1.,
            step=0.01,
            disabled=False,
            continuous_update=False,
            orientation='horizontal',
            readout=True,
            readout_format='.2f',
            style={'description_width': 'auto'},
            description_tooltip='Minimum precision threshold for anchor rules',
            layout={'width': 'initial', 'margin': '0 15% 0 15%'}
        )
        options_map['threshold'] = threshold

        # delta
        delta = BoundedFloatText(
            description='Delta:',
            value=0.1,
            min=0.,
            max=999999,
            step=0.01,
            description_tooltip='Used to compute beta.\n '
                                'The lower the value, the higher the beta parameter for beam search (wider beam)\n'
                                'You can see how exactly beta is computed by following a link in resources',
            style=style
        )
        options_map['delta'] = delta

        # tau
        tau = BoundedFloatText(
            description='Tau:',
            value=0.15,
            min=0.,
            max=1.,
            step=0.01,
            disabled=False,
            continuous_update=False,
            orientation='horizontal',
            readout=True,
            readout_format='.2f',
            style=style,
            description_tooltip='Margin between lower confidence bound and minimum precision or upper bound.\n'
                                'Here tau is used in place of delta from IML book',  # I'm not 100% sure about this
        )
        options_map['tau'] = tau

        # batch_size
        batch_size = BoundedIntText(
            description='Batch size:',
            value=100,
            step=1,
            min=1,
            description_tooltip='Batch size used for sampling',
            style=style
        )
        options_map['batch_size'] = batch_size

        # disc_perc
        disc_perc = UpdatingCombobox(
            options_keys=self.globals_options,
            description='Discretizer percentiles:',
            style=style,
            value='None',
            description_tooltip='Iterable with percentiles (int) used for discretization of ordinal features\n'
                                'If None, [25, 50, 75] will be used\n\n'
                                '(specify the name of the variable with list of percentiles that you have '
                                'in the notebook kernel)'
        )
        disc_perc.lookup_in_kernel = True
        options_map['disc_perc'] = disc_perc

        if not self.is_classification:
            warnings.warn('Anchors for regression are tricky, consider discretizing the model output.')

        grid[0, :] = threshold
        grid[1, 0] = delta
        grid[1, 1] = tau
        grid[2, 0] = batch_size
        grid[2, 1] = disc_perc

        return options_map, grid

    def explain(self, options, instance=None):
        if instance is None:
            raise ValueError("Instance was not provided")
        explainer = AnchorTabular(predict_fn=self.predict_function, feature_names=self.feature_names,
                                  categorical_names=self.categorical_names)
        if options['disc_perc'] is None:
            options['disc_perc'] = [25, 50, 75]
        explainer.fit(train_data=self.X_train, disc_perc=options['disc_perc'])

        explanation = explainer.explain(
            X=instance.to_numpy(),
            threshold=options['threshold'],
            delta=options['delta'],
            tau=options['tau'],
            batch_size=options['batch_size']
        )

        prediction = round(explanation['raw']['prediction'], 4)
        if self.is_classification:
            prediction = int(prediction)
            if self.class_names is not None:
                prediction = self.class_names[prediction]

        explanation_clauses = ' AND '.join(explanation['names'])
        print(f"IF {explanation_clauses}\n"
              f" THEN Prediction = {prediction}\n"  # todo: for classification show names if possible!
              f" WITH Precision: {explanation['precision']:.2f}\n"
              f"  AND Coverage: {explanation['coverage']:.2f}")
