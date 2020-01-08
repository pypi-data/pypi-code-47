from typing import List, Callable
import numpy as np
import pandas as pd
from ipywidgets import GridspecLayout, Dropdown, Checkbox, BoundedIntText, FloatText, Text, BoundedFloatText, Combobox
from ..utils.utils import UpdatingCombobox
from pdpbox import pdp
from .explainer import Explainer


class PDP(Explainer):
    resources = {
        'Documentation (pdp_isolate)': 'https://pdpbox.readthedocs.io/en/latest/pdp_isolate.html',
        'Documentation (pdp_plot)': 'https://pdpbox.readthedocs.io/en/latest/pdp_plot.html',
        'Partial Dependence plot': 'https://christophm.github.io/interpretable-ml-book/pdp.html',
        'Individual Conditional Expectation': 'https://christophm.github.io/interpretable-ml-book/ice.html',
        'PDPbox on GitHub': 'https://github.com/SauceCat/PDPbox'
    }

    require_instance = False

    def __init__(self, train_data: np.array, predict_function: Callable, globals_options: dict.keys,
                 feature_names: List[str], is_classification: bool = True):
        self.X_train = train_data
        self.predict_function = predict_function
        self.globals_options = globals_options
        self.feature_names = feature_names
        self.is_classification = is_classification

    def build_options(self):
        grid = GridspecLayout(10, 2)
        options_map = {}
        style = {'description_width': '60%', 'width': 'auto'}

        # feature
        feature = Combobox(
            description='Feature to plot:',
            style=style,
            options=list(self.feature_names),
            ensure_option=True,
            value=self.feature_names[0]
        )
        options_map['feature'] = feature

        # num_grid_points
        num_grid_points = BoundedIntText(
            value=10,
            min=1,
            max=999999,
            step=1,
            description='Number of grid points:',
            style=style,
            description_tooltip='Number of grid points for numeric feature'
        )
        options_map['num_grid_points'] = num_grid_points

        # grid_type
        grid_type = Dropdown(
            description='Grid type:',
            options=['percentile', 'equal'],
            style=style,
            description_tooltip='Type of grid points for numeric feature'
        )
        options_map['grid_type'] = grid_type

        # cust_range
        cust_range = Checkbox(
            description='Custom grid range',
            value=False
        )
        options_map['cust_range'] = cust_range

        # range_min
        range_min = FloatText(
            description='Custom range minimum:',
            style=style,
            description_tooltip='Percentile (when grid_type="percentile") or value (when grid_type="equal") '
                                'lower bound of range to investigate (for numeric feature)\n'
                                ' - Enabled only when custom grid range is True and variable with grid points is None',
            disabled=True
        )
        options_map['range_min'] = range_min

        # range_max
        range_max = FloatText(
            description='Custom range maximum:',
            style=style,
            description_tooltip='Percentile (when grid_type="percentile") or value (when grid_type="equal") '
                                'upper bound of range to investigate (for numeric feature)\n'
                                ' - Enabled only when custom grid range is True and variable with grid points is None',
            disabled=True
        )
        options_map['range_max'] = range_max

        # cust_grid_points
        cust_grid_points = UpdatingCombobox(
            options_keys=self.globals_options,
            description='Variable with grid points:',
            style=style,
            description_tooltip='Name of variable (or None) with customized list of grid points for numeric feature',
            value='None',
            disabled=True
        )
        cust_grid_points.lookup_in_kernel = True
        options_map['cust_grid_points'] = cust_grid_points

        # set up disabling of range inputs, when user doesn't want custom range
        def disable_ranges(change):
            range_min.disabled = not change['new']
            range_max.disabled = not change['new']
            cust_grid_points.disabled = not change['new']
            # but if the cust_grid_points has a value filled in keep range_max and range_min disabled
            if cust_grid_points.value != 'None':
                range_max.disabled = True
                range_min.disabled = True
        cust_range.observe(disable_ranges, names=['value'])

        # set up disabling of range_max and range_min if user specifies custom grid points
        def disable_max_min(change):
            if change['new'] == 'None':
                range_max.disabled = False
                range_min.disabled = False
            else:
                range_max.disabled = True
                range_min.disabled = True
        cust_grid_points.observe(disable_max_min, names=['value'])

        # set up links between upper and lower ranges
        def set_ranges(change):
            if grid_type.value == 'percentile':
                if change['owner'] == range_min or change['owner'] == num_grid_points:
                    range_max.value = max(range_max.value, range_min.value + num_grid_points.value)
                if change['owner'] == range_max:
                    range_min.value = min(range_min.value, range_max.value - num_grid_points.value)
            else:
                if change['owner'] == range_min:
                    range_max.value = max(range_max.value, range_min.value)
                if change['owner'] == range_max:
                    range_min.value = min(range_min.value, range_max.value)
        range_min.observe(set_ranges, names=['value'])
        range_max.observe(set_ranges, names=['value'])
        num_grid_points.observe(set_ranges, names=['value'])

        # center
        center = Checkbox(
            description='Center the plot',
            value=True
        )
        options_map['center'] = center

        # plot_pts_dist
        plot_pts_dist = Checkbox(
            description='Plot data points distribution',
            value=True
        )
        options_map['plot_pts_dist'] = plot_pts_dist

        # x_quantile
        x_quantile = Checkbox(
            description='X-axis as quantiles',
            value=False
        )
        options_map['x_quantile'] = x_quantile

        # show_percentile
        show_percentile = Checkbox(
            description='Show precentile buckets',
            value=False
        )
        options_map['show_percentile'] = show_percentile

        # lines
        lines = Checkbox(
            description='Plot lines - ICE plot',
            value=False
        )
        options_map['lines'] = lines

        # frac_to_plot
        frac_to_plot = BoundedFloatText(
            description='Lines to plot:',
            value=1,
            description_tooltip='How many lines to plot, can be a integer or a float.\n'
                                ' - integer values higher than 1 are interpreted as absolute amount\n'
                                ' - floats are interpreted as fraction (e.g. 0.5 means half of all possible lines)',
            style=style,
            disabled=True
        )
        options_map['frac_to_plot'] = frac_to_plot

        # cluster
        cluster = Checkbox(
            description='Cluster lines',
            value=False,
            disabled=True
        )
        options_map['cluster'] = cluster

        # n_cluster_centers
        n_cluster_centers = BoundedIntText(
            value=10,
            min=1,
            max=999999,
            step=1,
            description='Number of cluster centers:',
            style=style,
            description_tooltip='Number of cluster centers for lines',
            disabled=True
        )
        options_map['n_cluster_centers'] = n_cluster_centers

        # cluster method
        cluster_method = Dropdown(
            description='Cluster method',
            style=style,
            options={'KMeans': 'accurate', 'MiniBatchKMeans': 'approx'},
            description_tooltip='Method to use for clustering of lines',
            disabled=True
        )
        options_map['cluster_method'] = cluster_method

        # set up disabling of lines related options
        def disable_lines(change):
            frac_to_plot.disabled = not change['new']
            cluster.disabled = not change['new']
            n_cluster_centers.disabled = not (change['new'] and cluster.value)
            cluster_method.disabled = not (change['new'] and cluster.value)
        lines.observe(disable_lines, names=['value'])

        # set up disabling of clustering options
        def disable_clustering(change):
            n_cluster_centers.disabled = not (cluster.value and change['new'])
            cluster_method.disabled = not (cluster.value and change['new'])
        cluster.observe(disable_clustering, names=['value'])

        grid[0, :] = feature
        grid[1, 0] = num_grid_points
        grid[1, 1] = grid_type
        grid[2, 0] = cust_range
        grid[2, 1] = cust_grid_points
        grid[3, 0] = range_min
        grid[3, 1] = range_max
        grid[4, 0] = center
        grid[4, 1] = plot_pts_dist
        grid[5, 0] = x_quantile
        grid[5, 1] = show_percentile
        grid[6, :] = lines
        grid[7, :] = frac_to_plot
        grid[8, :] = cluster
        grid[9, 0] = n_cluster_centers
        grid[9, 1] = cluster_method

        return options_map, grid

    def explain(self, options, instance=None):
        # create dummy object with predict function to pose as a model
        class ModelRegression:
            def __init__(self, predict_function: Callable):
                self.predict_function = predict_function

            # we require predict_function to be able to deal with numpy array, but pdpbox sends in pandas dataframe
            # so we create a wrapper that transforms the df to numpy array
            def predict(self, instances):
                return self.predict_function(instances.to_numpy())

        class ModelClassification:
            def __init__(self, predict_function: Callable):
                self.predict_function = predict_function

            # we require predict_function to be able to deal with numpy array, but pdpbox sends in pandas dataframe
            # so we create a wrapper that transforms the df to numpy array
            # in this case the predict function is predict_proba
            def predict_proba(self, instances):
                return self.predict_function(instances.to_numpy())

            # pdpbox requires model to also have predict function, so we have to create that as well
            def predict(self, instances):
                predictions = self.predict_function(instances.to_numpy())
                res = []
                for prediction in predictions:
                    res.append(list(prediction).index(max(prediction)))
                return np.array(res)

        if self.is_classification:
            model = ModelClassification(self.predict_function)
        else:
            model = ModelRegression(self.predict_function)

        # pdpbox only accepts pandas dataframe
        dataset = pd.DataFrame(self.X_train, columns=self.feature_names)

        percentile_range = None
        grid_range = None
        grid_points = None
        if options['cust_range'] is True:
            grid_points = options['cust_grid_points']
            if grid_points is None:
                if options['range_min'] >= options['range_max']:
                    raise ValueError("Custom range minimum is >= custom range maximum")

                if options['grid_type'] == 'percentile':
                    percentile_range = (options['range_min'], options['range_max'])
                else:
                    grid_range = (options['range_min'], options['range_max'])

        if options['lines'] is False:
            options['cluster'] = False

        isolated = pdp.pdp_isolate(
            model=model,
            dataset=dataset,
            model_features=self.feature_names,
            feature=options['feature'],
            num_grid_points=options['num_grid_points'],
            grid_type=options['grid_type'],
            percentile_range=percentile_range,
            grid_range=grid_range,
            cust_grid_points=grid_points
        )

        pdp.pdp_plot(
            pdp_isolate_out=isolated,
            feature_name=options['feature'],
            center=options['center'],
            plot_pts_dist=options['plot_pts_dist'],
            plot_lines=options['lines'],
            cluster=options['cluster'],
            n_cluster_centers=options['n_cluster_centers'],
            cluster_method=options['cluster_method'],
            x_quantile=options['x_quantile'],
            show_percentile=options['show_percentile']
        )
