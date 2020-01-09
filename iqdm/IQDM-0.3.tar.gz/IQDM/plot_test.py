#!/usr/bin/env python
# -*- coding: utf-8 -*-

# figure.py
"""
Class to generate a single view of Carepaths by physician(s) or SBRT
"""
# Copyright (c) 2019
# Dan Cutright, PhD
# Medical Physicist
# University of Chicago Medical Center
# This file is part of treatment planning Whiteboard for Aria

from bokeh.io import curdoc
from bokeh.plotting import figure
from bokeh.models import HoverTool, ColumnDataSource, Select, Div, TextInput, Legend
from bokeh.layouts import column, row
from bokeh.models.widgets import DatePicker, CheckboxButtonGroup
from datetime import datetime
import numpy as np
import codecs

FILE_PATH = 'delta4_results_2019-12-16 09-06-03-921586.csv'


def import_csv(file_path):
    with codecs.open(file_path, 'r', encoding='utf-8', errors='ignore') as doc:
        raw_data = []
        for line in doc:
            raw_data.append(line.split(','))

    keys = raw_data.pop(0)
    keys = [key.strip() for key in keys] + ['file_name']
    data = {key: [] for key in keys}
    for row in raw_data:
        if float(row[keys.index('Daily Corr')]) < 1.06:
            for col, key in enumerate(keys):
                data[key].append(row[col])

    sorted_data = {key: [] for key in keys}
    for i in get_sorted_indices(data['Plan Date']):
        for key in keys:
            sorted_data[key].append(data[key][i])

    return sorted_data


def collapse_into_single_dates(x, y):
    """
    Function used for a time plot to convert multiple values into one value, while retaining enough information
    to perform a moving average over time
    :param x: a list of dates in ascending order
    :param y: a list of values and can use the '+' operator as a function of date
    :return: a unique list of dates, sum of y for that date, and number of original points for that date
    :rtype: dict
    """

    # average daily data and keep track of points per day
    x_collapsed = [x[0]]
    y_collapsed = [y[0]]
    w_collapsed = [1]
    for n in range(1, len(x)):
        if x[n] == x_collapsed[-1]:
            y_collapsed[-1] = (y_collapsed[-1] + y[n])
            w_collapsed[-1] += 1
        else:
            x_collapsed.append(x[n])
            y_collapsed.append(y[n])
            w_collapsed.append(1)

    return {'x': x_collapsed, 'y': y_collapsed, 'w': w_collapsed}


def moving_avg(xyw, avg_len):
    """
    Calculate a moving average for a given averaging length
    :param xyw: output from collapse_into_single_dates
    :type xyw: dict
    :param avg_len: average of these number of points, i.e., look-back window
    :type avg_len: int
    :return: list of x values, list of y values
    :rtype: tuple
    """
    cumsum, moving_aves, x_final = [0], [], []

    for i, y in enumerate(xyw['y'], 1):
        cumsum.append(cumsum[i - 1] + y / xyw['w'][i - 1])
        if i >= avg_len:
            moving_ave = (cumsum[i] - cumsum[i - avg_len]) / avg_len
            moving_aves.append(moving_ave)
    x_final = [xyw['x'][i] for i in range(avg_len - 1, len(xyw['x']))]

    return x_final, moving_aves


def get_sorted_indices(some_list):
    try:
        return [i[0] for i in sorted(enumerate(some_list), key=lambda x: x[1])]
    except TypeError:  # can't sort if a mix of str and float
        try:
            temp_data = [[value, -float('inf')][value == 'None'] for value in some_list]
            return [i[0] for i in sorted(enumerate(temp_data), key=lambda x: x[1])]
        except TypeError:
            temp_data = [str(value) for value in some_list]
            return [i[0] for i in sorted(enumerate(temp_data), key=lambda x: x[1])]


def string_to_date_time(date_string):
    return datetime(int(date_string.split('-')[0]), int(date_string.split('-')[1]), int(date_string.split('-')[2])).date()


class Plot:
    def __init__(self, data):

        self.data = data
        self.source = {key: {'plot': ColumnDataSource(data=dict(x=[], y=[])),
                             'trend': ColumnDataSource(data=dict(x=[], y=[])),
                             'bound': ColumnDataSource(data=dict(x=[], y=[])),
                             'patch': ColumnDataSource(data=dict(x=[], y=[])),
                             'hist': ColumnDataSource(data=dict(x=[], y=[]))} for key in [1, 2]}

        self.__set_x()
        self.__create_figure()
        self.__add_plot_data()
        self.__add_histogram_data()
        self.__add_hover()
        self.__add_legend()
        self.__set_plot_attr()

    def __create_figure(self):

        self.fig = figure(plot_width=1000, plot_height=500, x_axis_type='datetime')

    def __add_hover(self):
        self.fig.add_tools(HoverTool(tooltips=[("Plan Date", "@x{%F}"),
                                               ("Patient", "@id"),
                                               ('Gamma Crit', "@gamma_crit"),
                                               ("y", "@y"),
                                               ('file', '@file_name')],
                                     formatters={'x': 'datetime'},
                                     renderers=[self.plot_data_1, self.plot_data_2]))

    def __set_plot_attr(self):
        self.fig.title.align = 'center'

    def __set_x(self):
        self.x = [string_to_date_time(d) for d in self.data['Plan Date']]

    def __add_plot_data(self):
        self.plot_data_1 = self.fig.circle('x', 'y', source=self.source[1]['plot'], color='blue', size=4, alpha=0.4)
        self.plot_trend_1 = self.fig.line('x', 'y', source=self.source[1]['trend'], line_color='black', line_width=4)
        self.plot_avg_1 = self.fig.line('x', 'avg', source=self.source[1]['bound'], line_color='black')
        self.plot_patch_1 = self.fig.patch('x', 'y', source=self.source[1]['patch'], color='blue', alpha=0.2)

        self.plot_data_2 = self.fig.circle('x', 'y', source=self.source[2]['plot'], color='red', size=4, alpha=0.4)
        self.plot_trend_2 = self.fig.line('x', 'y', source=self.source[2]['trend'], line_color='black', line_width=4)
        self.plot_avg_2 = self.fig.line('x', 'avg', source=self.source[2]['bound'], line_color='black')
        self.plot_patch_2 = self.fig.patch('x', 'y', source=self.source[2]['patch'], color='red', alpha=0.2)

    def __add_legend(self):
        # Set the legend
        legend_plot = Legend(items=[("Data 1 ", [self.plot_data_1]),
                                    ("Series Average 1 ", [self.plot_avg_1]),
                                    ("Rolling Average 1 ", [self.plot_trend_1]),
                                    ("Percentile Region 1 ", [self.plot_patch_1]),
                                    ("Data 2 ", [self.plot_data_2]),
                                    ("Series Average 2 ", [self.plot_avg_2]),
                                    ("Rolling Average 2 ", [self.plot_trend_2]),
                                    ("Percentile Region 2 ", [self.plot_patch_2])
                                    ],
                             orientation='horizontal')

        # Add the layout outside the plot, clicking legend item hides the line
        self.fig.add_layout(legend_plot, 'above')
        self.fig.legend.click_policy = "hide"

    def __add_histogram_data(self):
        self.histogram = figure(tools="", plot_width=1000, plot_height=400)
        # self.histogram.xaxis.axis_label_text_font_size = self.options.PLOT_AXIS_LABEL_FONT_SIZE
        # self.histogram.yaxis.axis_label_text_font_size = self.options.PLOT_AXIS_LABEL_FONT_SIZE
        # self.histogram.xaxis.major_label_text_font_size = self.options.PLOT_AXIS_MAJOR_LABEL_FONT_SIZE
        # self.histogram.yaxis.major_label_text_font_size = self.options.PLOT_AXIS_MAJOR_LABEL_FONT_SIZE
        # self.histogram.min_border_left = self.options.MIN_BORDER
        # self.histogram.min_border_bottom = self.options.MIN_BORDER
        self.vbar_1 = self.histogram.vbar(x='x', width='width', bottom=0, top='top', source=self.source[1]['hist'], alpha=0.5, color='blue')
        self.vbar_2 = self.histogram.vbar(x='x', width='width', bottom=0, top='top', source=self.source[2]['hist'], alpha=0.5, color='red')

        self.histogram.xaxis.axis_label = ""
        self.histogram.yaxis.axis_label = "Frequency"

    def update_source(self, attr, old, new):
        for source_key in [1, 2]:
            new_data = {key: [] for key in ['x', 'y', 'id', 'gamma_crit', 'file_name']}
            active_gamma = [gamma_options[a] for a in checkbox_button_group.active]
            if select_linac[source_key] != 'None':
                for i in range(len(self.x)):
                    if select_linac[source_key].value == 'All' or \
                            self.data['Radiation Dev'][i] == select_linac[source_key].value:
                        if end_date_picker.value > self.x[i] > start_date_picker.value:
                            gamma_crit = "%s%%/%smm" % (self.data['Gamma Dose Criteria'][i], self.data['Gamma Dist Criteria'][i])
                            if 'Any' in active_gamma or gamma_crit in active_gamma:
                                new_data['x'].append(self.x[i])
                                new_data['y'].append(float(self.data[select_y.value][i]))
                                new_data['id'].append(self.data['Patient ID'][i])
                                new_data['gamma_crit'].append(gamma_crit)
                                new_data['file_name'].append(self.data['file_name'][i])

            try:
                y = new_data['y']
                text[source_key].text = "<b>Linac %s</b>: <b>Min</b>: %0.3f | <b>Low</b>: %0.3f | <b>Mean</b>: %0.3f | <b>Median</b>: %0.3f | <b>Upper</b>: %0.3f | <b>Max</b>: %0.3f" % \
                             (source_key, np.min(y), np.percentile(y, 25), np.sum(y)/len(y), np.percentile(y, 50), np.percentile(y, 75), np.max(y))
            except:
                text[source_key].text = "<b>Linac %s</b>" % source_key

            self.source[source_key]['plot'].data = new_data

            self.fig.yaxis.axis_label = select_y.value
            self.fig.xaxis.axis_label = 'Plan Date'

            self.update_histogram(source_key, bin_size=20)
            self.update_trend(source_key, int(float(avg_len_input.value)), float(percentile_input.value))

    def update_histogram(self, source_key, bin_size=10):
        width_fraction = 0.9
        hist, bins = np.histogram(self.source[source_key]['plot'].data['y'], bins=bin_size)
        width = [width_fraction * (bins[1] - bins[0])] * bin_size
        center = (bins[:-1] + bins[1:]) / 2.
        self.source[source_key]['hist'].data = {'x': center, 'top': hist, 'width': width}

        self.histogram.xaxis.axis_label = select_y.value

    def update_trend(self, source_key, avg_len, percentile):
        x = self.source[source_key]['plot'].data['x']
        y = self.source[source_key]['plot'].data['y']
        if x and y:
            x_len = len(x)

            data_collapsed = collapse_into_single_dates(x, y)
            x_trend, y_trend = moving_avg(data_collapsed, avg_len)

            y_np = np.array(self.source[source_key]['plot'].data['y'])
            upper_bound = float(np.percentile(y_np, 50. + percentile / 2.))
            average = float(np.percentile(y_np, 50))
            lower_bound = float(np.percentile(y_np, 50. - percentile / 2.))

            self.source[source_key]['trend'].data = {'x': x_trend,
                                                     'y': y_trend,
                                                     'mrn': ['Avg'] * len(x_trend)}
            self.source[source_key]['bound'].data = {'x': [x[0], x[-1]],
                                                     'mrn': ['Series Avg'] * 2,
                                                     'upper': [upper_bound] * 2,
                                                     'avg': [average] * 2,
                                                     'lower': [lower_bound] * 2,
                                                     'y': [average] * 2}
            self.source[source_key]['patch'].data = {'x': [x[0], x[-1], x[-1], x[0]],
                                                     'y': [upper_bound, upper_bound, lower_bound, lower_bound]}
        else:
            self.source[source_key]['trend'].data = {'x': [],
                                                     'y': [],
                                                     'mrn': []}
            self.source[source_key]['bound'].data = {'x': [],
                                                     'mrn': [],
                                                     'upper': [],
                                                     'avg': [],
                                                     'lower': [],
                                                     'y': []}
            self.source[source_key]['patch'].data = {'x': [],
                                                     'y': []}


data = import_csv(FILE_PATH)
plot = Plot(data)
select_y = Select(title='Y-variable:', value='Dose Dev', options=list(data))
select_y.on_change('value', plot.update_source)

linacs = list(set(data['Radiation Dev']))
linacs.sort()
linacs.insert(0, 'All')
linacs.extend(['Eclipse', 'Pinnacle'])
linacs.append('None')
select_linac = {key: Select(title='Linac/TPS %s:' % key, value='All', options=linacs, width=250) for key in [1, 2]}
select_linac[2].value = 'None'
select_linac[1].on_change('value', plot.update_source)
select_linac[2].on_change('value', plot.update_source)

avg_len_input = TextInput(title='Avg. Len', value='10', width=100)
avg_len_input.on_change('value', plot.update_source)

percentile_input = TextInput(title='Percentile', value='90', width=100)
percentile_input.on_change('value', plot.update_source)


start_date_picker = DatePicker(title='Start Date', value=plot.x[0])
end_date_picker = DatePicker(title='End Date', value=plot.x[-1])
start_date_picker.on_change('value', plot.update_source)
end_date_picker.on_change('value', plot.update_source)

gamma_options = ['5.0%/3.0mm', '3.0%/3.0mm', 'Any']
checkbox_button_group = CheckboxButtonGroup(labels=gamma_options, active=[2])
checkbox_button_group.on_change('active', plot.update_source)

text = {key: Div() for key in [1, 2]}

plot.update_source(None, None, None)

layout = column(row(select_y, select_linac[1], select_linac[2], avg_len_input, percentile_input),
                row(start_date_picker, end_date_picker, checkbox_button_group),
                text[1],
                text[2],
                plot.fig,
                plot.histogram)


curdoc().add_root(layout)
curdoc().title = "Test"
