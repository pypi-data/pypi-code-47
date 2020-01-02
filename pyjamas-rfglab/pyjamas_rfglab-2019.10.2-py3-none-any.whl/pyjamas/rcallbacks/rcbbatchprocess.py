"""
    PyJAMAS is Just A More Awesome Siesta
    Copyright (C) 2018  Rodrigo Fernandez-Gonzalez (rodrigo.fernandez.gonzalez@utoronto.ca)

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

from enum import IntEnum
import os
from typing import List, Tuple
import warnings

import matplotlib.pyplot as plt
import numpy
import pandas as pd
# import pylustrator
from PyQt5 import QtWidgets
import seaborn as sns
from scipy.optimize import curve_fit

from pyjamas.dialogs.batchanalysis import BatchMeasureDialog
from pyjamas.dialogs.batchprojectconcat import BatchProjectConcatenateDialog
from pyjamas.pjscore import PyJAMAS
from pyjamas.pjsthreads import ThreadSignals
from pyjamas.rcallbacks.rcallback import RCallback
from pyjamas.rimage.rimutils import rimutils as rimutils
from pyjamas.rutils import RUtils


class normalization_modes(IntEnum):
    """
      # 0 is raw intensities; 1 normalizes for photobleaching; 2 subtracts background -image mode-, normalizes for photobleaching, and then divides each sample by its mean value over time to remove effects due to differences in expression levels.
    """
    RAW_INTENSITIES: int = 0
    PHOTOBLEACHING: int = 1
    BACKGROUND_PHOTOBLEACHING_MEAN: int = 2


class RCBBatchProcess(RCallback):
    DEFAULT_FILE_NAME: str = 'projected'
    VALID_EXTENSIONS: Tuple[str] = ('.tif', '.tiff')
    OUTPUT_EXTENSION: str = '.tif'

    BATCH_MEASURE_SCRIPT: str = "from pyjamas.pjscore import PyJAMAS\na = PyJAMAS()\na.batch.cbMeasureBatch(parameters)"

    DIRS1_BM: str = '.'
    DIRS2_BM: str = ''
    ANALYZE_FLAG_BM: bool = True
    ANALYSIS_FILENAME_APPENDIX_BM: str = '_analysis'
    ANALYSIS_EXTENSION_BM: str = '.csv'
    SAVE_SCRIPT_BM: bool = True  # Save the analysis script in each folder in which an analysis flag is saved.
    SCRIPT_FILENAME_APPENDIX_BM: str = '_analysis_script'
    SCRIPT_EXTENSION_BM = '.py'
    INTENSITY_FLAG_BM: bool = True  # Run intensity section of the analysis/plots?
    IMAGE_EXTENSION_BM: str = '.tif'
    NORMALIZE_INTENSITY_FLAG_BM: int = normalization_modes.BACKGROUND_PHOTOBLEACHING_MEAN
    T_RES_BM: float = 30  # Time resolution in seconds.
    XY_RES_BM: float = 16 / (60 * 1.5)  # Spatial resolution in microns.
    # INDEX_TIME_ZERO_BM: Number of time points before treatment (e.g. number of images before wounding) if time zero is the time AFTER TREATMENT.
    # INDEX_TIME_ZERO_BM: Number of time points before treatment - 1 if time zero is the time BEFORE applying the treatment.
    INDEX_TIME_ZERO_BM: int = 4
    PLOT_FLAG_BM: bool = True  # Generate and display plots.
    GROUP_LABELS_BM: List[str] = ['group 1', 'group 2']
    ERR_STYLE_VALUE_BM: str = 'band'
    PLOT_STYLE_VALUE_BM: str = 'box'
    BRUSH_SZ_BM: int = 3

    COMPILE_DATA_FLAG_BM: bool = True  # Read all data and compile into DataFrames.
    NTP_BM: int = 308
    TIME_SHIFTS_BM = numpy.arange(-16, 17)
    MEASUREMENT_LIST_BM = ['area', 'area_pctg', 'perimeter', 'perimeter_pctg', 'circularity', 'circularity_pctg',
                           'pix_vals_interior', 'pix_vals_interior_pctg', 'pix_vals_perimeter',
                           'pix_vals_perimeter_pctg',
                           'image_mean', 'image_mode', 'norm_pix_vals_interior', 'norm_pix_vals_perimeter', ]
    BOX_PLOT_MEASUREMENTS_BM = ['area_exp_rate_constant']
    COLUMN_LIST_BM: List[str] = ['exp_group', 'exp_idx', 'time'] + MEASUREMENT_LIST_BM + BOX_PLOT_MEASUREMENTS_BM
    CI_VALUE_BM: str = 'sd'
    LINE_WIDTH_BM: int = 3

    def cbBatchProjectConcat(self, input_folder_name: str = None, slice_str: str = None, output_file_name: str = None,
                             wait_for_thread: bool = False) -> bool:
        # If not enough parameters, open dialog.
        if input_folder_name == '' or input_folder_name is False or not os.path.exists(
                input_folder_name):  # When the menu option is clicked on, for some reason that I do not understand, the function is called with filename = False, which causes a bunch of problems.
            dialog = QtWidgets.QDialog()
            ui = BatchProjectConcatenateDialog()
            ui.setupUi(dialog)
            dialog.exec_()
            dialog.show()
            # If the dialog was closed by pressing OK, then run the measurements.
            continue_flag = dialog.result() == QtWidgets.QDialog.Accepted
            theparameters = ui.parameters()

            dialog.close()

        # Otherwise, continue with supplied parameters
        else:
            theparameters = {'input_folder': input_folder_name,
                             'slice_list': slice_str,
                             'file_name': output_file_name}
            continue_flag = True

        if continue_flag:
            return_value = self.launch_thread(self.batch_project_concatenate,
                                              {'parameters': theparameters, 'progress': True, 'stop': True},
                                              finished_fn=self.finished_fn, stop_fn=self.stop_fn,
                                              progress_fn=self.progress_fn,
                                              wait_for_thread=wait_for_thread)

            if return_value:
                self.pjs.cwd = os.path.abspath(theparameters['input_folder'])

            return return_value
        else:
            return False

    def cbMeasureBatch(self, parameters: dict = None) -> bool:  # Handle IO errors.
        continue_flag = True

        if parameters is None or parameters is False:
            dialog = QtWidgets.QDialog()
            ui = BatchMeasureDialog()  # Replace with ui = dialogs.batchmeasure.BatchMeasureDialog()
            ui.setupUi(dialog)

            dialog.exec_()
            dialog.show()

            continue_flag = dialog.result() == QtWidgets.QDialog.Accepted

            if continue_flag:
                parameters = ui.parameters()

            dialog.close()

        if continue_flag:
            return self.batch_measure(parameters)

        else:
            return False

    def batch_project_concatenate(self, parameters: dict, progress_signal: ThreadSignals,
                                  stop_signal: ThreadSignals) -> bool:
        folder_name: str = parameters.get('input_folder', None)
        slices: str = parameters.get('slice_list', None)
        file_name: str = parameters.get('file_name', None)
        if file_name[-4:] != RCBBatchProcess.OUTPUT_EXTENSION:
            file_name = file_name + RCBBatchProcess.OUTPUT_EXTENSION

        if not os.path.exists(folder_name):
            if stop_signal is not None:
                stop_signal.emit('Output folder does not exist!')
            return False

        file_list: List[str] = os.listdir(folder_name)
        file_list.sort(key=RUtils.natural_sort)

        n_files: int = len(file_list)

        projected_image: numpy.ndarray = None
        projected_array: numpy.ndarray = None

        for ind, thefile in enumerate(file_list):
            _, extension = os.path.splitext(thefile)

            if extension.lower() in RCBBatchProcess.VALID_EXTENSIONS:
                theimage: numpy.ndarray = rimutils.read_stack(os.path.join(folder_name, thefile))

                if slices == '' or not slices:
                    projected_image = numpy.expand_dims(rimutils.mip(theimage), axis=0)
                else:
                    slice_list: List[int] = RUtils.parse_range_list(slices)
                    projected_image = numpy.expand_dims(rimutils.mip(theimage[slice_list]), axis=0)

                if projected_array is not None:
                    projected_array = numpy.concatenate((projected_array, projected_image), axis=0)

                else:
                    projected_array = projected_image.copy()

            if progress_signal is not None:
                progress_signal.emit(int((100 * (ind + 1)) / n_files))

        # Now write the file.
        rimutils.write_stack(os.path.join(folder_name, file_name), projected_array)

        return True

    def batch_measure(self, parameters: dict) -> bool:
        self._read_parameters(parameters)

        if self.analyze_flag:
            self._measure_data(parameters)

        if self.compile_data_flag:
            all_data = self._combine_measured_data()

            if self.plot_flag:
                self._plot_data(all_data)

        return True

    @classmethod
    def _default_batchmeasure_parameters(cls) -> dict:
        theparameters = {'folder1': RCBBatchProcess.DIRS1_BM,
                         'folder2': RCBBatchProcess.DIRS2_BM,
                         'analyze_flag': RCBBatchProcess.ANALYZE_FLAG_BM,
                         'analysis_filename_appendix': RCBBatchProcess.ANALYSIS_FILENAME_APPENDIX_BM,
                         'analysis_extension': RCBBatchProcess.ANALYSIS_EXTENSION_BM,
                         'save_script': RCBBatchProcess.SAVE_SCRIPT_BM,
                         'script_filename_appendix': RCBBatchProcess.SCRIPT_FILENAME_APPENDIX_BM,
                         'script_extension': RCBBatchProcess.SCRIPT_EXTENSION_BM,
                         'intensity_flag': RCBBatchProcess.INTENSITY_FLAG_BM,
                         'image_extension': RCBBatchProcess.IMAGE_EXTENSION_BM,
                         'normalize_intensity_flag': RCBBatchProcess.NORMALIZE_INTENSITY_FLAG_BM,
                         't_res': RCBBatchProcess.T_RES_BM,
                         'xy_res': RCBBatchProcess.XY_RES_BM,
                         'index_time_zero': RCBBatchProcess.INDEX_TIME_ZERO_BM,
                         'plot_flag': RCBBatchProcess.PLOT_FLAG_BM,
                         'name1': RCBBatchProcess.GROUP_LABELS_BM[0],
                         'name2': RCBBatchProcess.GROUP_LABELS_BM[1],
                         'err_style_value': RCBBatchProcess.ERR_STYLE_VALUE_BM,
                         'plot_style_value': RCBBatchProcess.PLOT_STYLE_VALUE_BM,
                         'brush_sz': RCBBatchProcess.BRUSH_SZ_BM
                         }

        return theparameters

    def _read_parameters(self, parameters: dict) -> bool:
        self.folder1: str = parameters.get('folder1', RCBBatchProcess.DIRS1_BM)
        self.folder2: str = parameters.get('folder2', RCBBatchProcess.DIRS2_BM)

        if self.folder1 == '' or not os.path.isdir(self.folder1):
            return False

        self.dirs1: List[str] = RUtils.extract_file_paths(self.folder1, [PyJAMAS.data_extension, PyJAMAS.matlab_extension])
        self.dirs2: List[str] = []

        # This enables analysis of a single set of folders.
        if self.folder2 != '' and os.path.isdir(self.folder2):
            dirs2 = RUtils.extract_file_paths(self.folder2, [PyJAMAS.data_extension, PyJAMAS.matlab_extension])

        self.analyze_flag: bool = parameters.get('analyze_flag', RCBBatchProcess.ANALYZE_FLAG_BM)
        self.analysis_filename_appendix: str = parameters.get('analysis_filename_appendix',
                                                         RCBBatchProcess.ANALYSIS_FILENAME_APPENDIX_BM)
        self.analysis_extension: str = parameters.get('analysis_extension', RCBBatchProcess.ANALYSIS_EXTENSION_BM)
        self.save_script: bool = parameters.get('save_script',
                                           RCBBatchProcess.SAVE_SCRIPT_BM)  # Save the analysis script in each folder in which an analysis flag is saved.
        self.script_filename_appendix: str = parameters.get('script_filename_appendix',
                                                       RCBBatchProcess.SCRIPT_FILENAME_APPENDIX_BM)
        self.script_extension = parameters.get('script_extension', RCBBatchProcess.SCRIPT_EXTENSION_BM)
        self.intensity_flag: bool = parameters.get('intensity_flag',
                                              RCBBatchProcess.INTENSITY_FLAG_BM)  # Run intensity section of the analysis/plots?
        self.image_extension: str = parameters.get('image_extension', RCBBatchProcess.IMAGE_EXTENSION_BM)
        self.normalize_intensity_flag: int = parameters.get('normalize_intensity_flag',
                                                                                       RCBBatchProcess.NORMALIZE_INTENSITY_FLAG_BM)
        self.t_res: float = parameters.get('t_res', RCBBatchProcess.T_RES_BM)  # Time resolution in seconds.
        self.xy_res: float = parameters.get('xy_res', RCBBatchProcess.XY_RES_BM)  # Spatial resolution in microns.
        self.index_time_zero: int = parameters.get('index_time_zero',
                                              RCBBatchProcess.INDEX_TIME_ZERO_BM)  # Number of time points before treatment (e.g. number of images before wounding).
        if self.index_time_zero == 0:
            RCBBatchProcess.MEASUREMENT_LIST_BM = ['area', 'perimeter', 'circularity','pix_vals_interior',
                                                   'pix_vals_perimeter', 'image_mean', 'image_mode',
                                                   'norm_pix_vals_interior', 'norm_pix_vals_perimeter']

        self.plot_flag: bool = parameters.get('plot_flag', RCBBatchProcess.PLOT_FLAG_BM)  # Generate and display plots.
        self.group_labels: List[str] = [parameters.get('name1', None), parameters.get('name2', None)]
        self.err_style_value: str = parameters.get('err_style_value', RCBBatchProcess.ERR_STYLE_VALUE_BM)
        self.plot_style_value: str = parameters.get('plot_style_value', RCBBatchProcess.PLOT_STYLE_VALUE_BM)
        self. brush_sz: int = parameters.get('brush_sz', RCBBatchProcess.BRUSH_SZ_BM)

        self.compile_data_flag: bool = RCBBatchProcess.COMPILE_DATA_FLAG_BM  # Read all data and compile into DataFrames.
        self.ntp: int = RCBBatchProcess.NTP_BM
        self.t = (numpy.arange(0, self.ntp) - self.index_time_zero) * self.t_res / 60.  # Time in minutes.
        self.time_shifts = RCBBatchProcess.TIME_SHIFTS_BM
        self.measurement_list = RCBBatchProcess.MEASUREMENT_LIST_BM
        self.box_plot_measurements = RCBBatchProcess.BOX_PLOT_MEASUREMENTS_BM
        self.column_list: List[str] = RCBBatchProcess.COLUMN_LIST_BM
        self.ci_value: str = parameters.get('ci_value', RCBBatchProcess.CI_VALUE_BM)
        self.line_width: int = RCBBatchProcess.LINE_WIDTH_BM

        return True

    def _measure_data(self, parameters: dict) -> bool:
        prev_image: numpy.ndarray = self.pjs.slices.copy()
        prev_brush_sz: int = self.pjs.brush_size
        prev_wd: str = os.getcwd()

        self.pjs.options.cbSetBrushSize(self.brush_sz)

        if self.intensity_flag:
            measurement_flags = None
            image_file_path = None
        else:
            measurement_flags = {'area': True, 'perimeter': True, 'pixels': False, 'image': False}
            image_file_path = ''

        for folder_list in [self.dirs1, self.dirs2]:
            for ii, annotations_file in enumerate(folder_list):
                print(f"Analyzing movie {ii + 1}/{len(folder_list)} ... ", end="")

                file_path, full_file_name = os.path.split(annotations_file)
                file_name, ext = os.path.splitext(full_file_name)

                # Create analysis file path.
                full_analysis_file_name = os.path.join(file_path,
                                                       file_name + self.analysis_filename_appendix + self.analysis_extension)
                full_script_file_name = os.path.join(file_path,
                                                     file_name + self.script_filename_appendix + self.script_extension)

                # Figure out image file name.
                if self.intensity_flag:
                    _, folder_name = os.path.split(file_path)
                    image_file_path = os.path.join(file_path, folder_name + self.image_extension)
                    if not os.path.exists(image_file_path):
                        image_file_path = os.path.join(file_path, folder_name + '_488' + self.image_extension)
                        if not os.path.exists(image_file_path):
                            image_file_path = os.path.join(file_path, folder_name + '_' + self.image_extension)
                            if not os.path.exists(image_file_path):
                                thefiles = [f for f in os.listdir(file_path) if f.endswith(self.image_extension)]
                                if len(thefiles) > 0:
                                    image_file_path = os.path.join(file_path, thefiles[0])
                                else:
                                    image_file_path = ''

                # Load annotation file (and image if intensity measurements are happening).
                if os.path.isfile(annotations_file) and ext == PyJAMAS.data_extension:
                    self.pjs.io.cbLoadAnnotations(annotations_file, image_file=image_file_path)
                elif os.path.isfile(annotations_file) and ext == PyJAMAS.matlab_extension:
                    self.pjs.io.cbImportSIESTAAnnotations(annotations_file, image_file=image_file_path)
                else:
                    continue

                # Find indexes of first and last slice with polylines.
                first: int = 0

                for slice in self.pjs.polylines:
                    if slice == []:
                        first += 1
                    else:
                        break

                last: int = len(self.pjs.polylines) - 1

                for slice in self.pjs.polylines[-1::-1]:
                    if slice == []:
                        last -= 1
                    else:
                        break

                # Index of last time point before treatment.
                # cut_t: int = index_time_zero - first - 1
                # if cut_t < 0:
                #    cut_t = 0

                self.pjs.measurements.cbMeasurePoly(first + 1, last + 1, measurement_flags, full_analysis_file_name)

                if self.save_script:
                    with open(full_script_file_name, "w") as f:
                        print(f"parameters = {str(parameters)}\n{RCBBatchProcess.BATCH_MEASURE_SCRIPT}", file=f)

                print("done!")

        # Restore GUI to its state before beginning batch analysis.
        self.pjs.io.cbLoadArray(prev_image)
        self.pjs.options.cbSetCWD(prev_wd)
        self.pjs.options.cbSetBrushSize(prev_brush_sz)

        return True

    def _combine_measured_data(self) -> pd.DataFrame:
        n_files_to_analyze = len(self.dirs1) + len(self.dirs2)

        # all_data is the DataFrame in which all the data will be compiled.
        # It contains one row per folder (i.e. annotation file) and time point.
        # Each row contains multiple columns with the values for different metrics in different folders and time points.
        all_data: pd.DataFrame = pd.DataFrame(numpy.nan * numpy.zeros((n_files_to_analyze * self.ntp, len(self.column_list))),
                                              columns=self.column_list)

        min_ind: int = 0
        max_ind: int = 0

        for ii, annotations_file in enumerate(self.dirs1 + self.dirs2):
            file_path, full_file_name = os.path.split(annotations_file)
            file_name, ext = os.path.splitext(full_file_name)

            # Create analysis file path.
            full_analysis_file_name = os.path.join(file_path,
                                                   file_name + self.analysis_filename_appendix + self.analysis_extension)

            msr_df = pd.read_csv(full_analysis_file_name, index_col=0)

            # Obtain the array of time points with measurements available.
            # The -1 here converts from slice numbers (starting at 1), into indeces (starting at zero).
            index_list = numpy.asarray(msr_df.values[0]-1, dtype=int)

            # min_ind and max_ind delimit the rows in all_data that correspond to the time points for the current folder.
            min_ind = max_ind
            max_ind = min_ind + self.ntp

            # Determine both the experimental group and the experiment index within that group.
            if annotations_file in self.dirs1:
                all_data['exp_group'].iloc[min_ind:max_ind] = self.group_labels[0]
                all_data['exp_idx'].iloc[min_ind:max_ind] = self.dirs1.index(annotations_file)
            else:
                all_data['exp_group'].iloc[min_ind:max_ind] = self.group_labels[1]
                all_data['exp_idx'].iloc[min_ind:max_ind] = self.dirs2.index(annotations_file)

            all_data['time'].values[min_ind+index_list] = self.t[0:index_list.size]

            # REMEMBER: index_list is an ndarray with the relative indeces to use.
            all_data['area'].values[min_ind + index_list] = numpy.asarray(msr_df.loc['area_1'])

            areas = all_data['area'].values[min_ind + index_list]
            times = all_data['time'].values[min_ind + index_list]
            max_area_ind = numpy.argmax(areas)

            with warnings.catch_warnings():
                warnings.filterwarnings('error')

                try:
                    popt, pcov = curve_fit(RUtils.func_exp, times[max_area_ind:], areas[max_area_ind:],
                                           p0=(areas[0], 1.0, areas[-1]))
                # If there is a Warning, spit out an error message.
                except Warning as w:
                    print(
                        f'WARNING!! Curve fitting error calculating rate of wound closure for {annotations_file}: {w}')
                else:
                    all_data['area_exp_rate_constant'].values[min_ind + index_list] = popt[1]

            all_data['area_pctg'].values[min_ind + index_list] = 100. * numpy.asarray(
                msr_df.loc['area_1']) / numpy.mean(numpy.asarray(msr_df.loc['area_1'])[0:self.index_time_zero])

            all_data['perimeter'].values[min_ind + index_list] = numpy.asarray(msr_df.loc['perimeter_1'])
            all_data['perimeter_pctg'].values[min_ind + index_list] = 100. * numpy.asarray(
                msr_df.loc['perimeter_1']) / numpy.mean(numpy.asarray(msr_df.loc['perimeter_1'])[0:self.index_time_zero])

            all_data['circularity_pctg'].values[min_ind + index_list] = 100. * (
                    all_data['area'].values[
                        min_ind + index_list] /
                    all_data['perimeter'].values[
                        min_ind + index_list]) / numpy.mean(
                numpy.asarray(msr_df.loc['area_1'])[0:self.index_time_zero] / numpy.asarray(msr_df.loc['perimeter_1'])[
                                                                         0:self.index_time_zero])

            all_data['pix_vals_interior'].values[min_ind + index_list] = numpy.asarray(
                msr_df.loc['pixel_values_interior_1'])
            all_data['pix_vals_interior_pctg'].values[min_ind + index_list] = 100. * numpy.asarray(
                msr_df.loc['pixel_values_interior_1']) / numpy.mean(
                numpy.asarray(msr_df.loc['pixel_values_interior_1'])[0:self.index_time_zero])

            all_data['pix_vals_perimeter'].values[min_ind + index_list] = numpy.asarray(
                msr_df.loc['pixel_values_perimeter_1'])
            all_data['pix_vals_perimeter_pctg'].values[min_ind + index_list] = 100. * numpy.asarray(
                msr_df.loc['pixel_values_perimeter_1']) / numpy.mean(
                numpy.asarray(msr_df.loc['pixel_values_perimeter_1'])[0:self.index_time_zero])

            all_data['image_mean'].values[min_ind + index_list] = numpy.asarray(msr_df.loc['image_mean'])
            all_data['image_mode'].values[min_ind + index_list] = numpy.asarray(msr_df.loc['image_mode'])

        all_data['circularity'] = 4 * numpy.pi * all_data['area'].values / numpy.square(
            all_data['perimeter'].values)

        if self.normalize_intensity_flag == normalization_modes.RAW_INTENSITIES:
            all_data['norm_pix_vals_interior'] = all_data['pix_vals_interior'].values
            all_data['norm_pix_vals_perimeter'] = all_data['pix_vals_perimeter'].values

        elif self.normalize_intensity_flag == normalization_modes.PHOTOBLEACHING:
            all_data['norm_pix_vals_interior'] = all_data['pix_vals_interior'].values / all_data[
                'image_mean'].values
            all_data['norm_pix_vals_perimeter'] = all_data['pix_vals_perimeter'] / all_data['image_mean'].values

        elif self.normalize_intensity_flag == normalization_modes.BACKGROUND_PHOTOBLEACHING_MEAN:
            all_data['norm_pix_vals_interior'] = (all_data['pix_vals_interior'].values - all_data[
                'image_mode'].values) / all_data['image_mean'].values
            all_data['norm_pix_vals_perimeter'] = (all_data['pix_vals_perimeter'] - all_data['image_mode'].values) / \
                                                  all_data['image_mean'].values

        return all_data

    def _plot_data(self, all_data: pd.DataFrame) -> bool:
        # We are going to plot A LOT. So we silence the warning that too many plots were opened.
        warnings.filterwarnings("ignore", message="More than 20 figures have been opened.")

        sns.set()
        sns.set_style("white")

        # Mean plots comparing two groups.
        # todo: outward pointing ticks, axes units.
        for a_measurement in self.measurement_list:
            plt.figure()
            ax = sns.lineplot(x='time', y=a_measurement, hue='exp_group', data=all_data, ci=self.ci_value,
                              err_style=self.err_style_value, lw=self.line_width, legend=None)
            ax.set_ylim(
                [min(ax.dataLim.ymin - .05 * ax.dataLim.ymin, 0), ax.dataLim.ymax + .05 * ax.dataLim.ymax])

            sns.despine()
            plt.show()

        # Plot individual curves for each of the folders.
        # All in the same plot.
        for a_measurement in self.measurement_list:
            plt.figure()
            ax = sns.lineplot(x='time', y=a_measurement, hue='exp_group', data=all_data, estimator=None,
                              units='exp_idx', lw=self.line_width, legend=None)
            ax.set_ylim([min(ax.dataLim.ymin - .05 * ax.dataLim.ymin, 0),
                         ax.dataLim.ymax + .05 * ax.dataLim.ymax])

            sns.despine()
            plt.show()

            # Each group independently, color-coding based on experiment index.
            for a_group in self.group_labels:
                thedata = all_data.query("exp_group==@a_group")

                if numpy.array(thedata).size == 0:
                    continue

                plt.figure()
                ax = sns.lineplot(x='time', y=a_measurement, hue='exp_idx', data=thedata,
                                  estimator=None, units='exp_idx', lw=self.line_width)
                ax.set_ylim([min(ax.dataLim.ymin - .05 * ax.dataLim.ymin, 0),
                             ax.dataLim.ymax + .05 * ax.dataLim.ymax])

                sns.despine()
                plt.show()

        # Box plots for metrics that summarize experiments with a number each (eg. area rate constant).
        for a_measurement in self.box_plot_measurements:
            plt.figure()

            if self.plot_style_value == 'box':
                sns.boxplot(x='exp_group', y=a_measurement, data=all_data, hue='exp_group')
            elif self.plot_style_value == 'violin':
                sns.violinplot(x='exp_group', y=a_measurement, data=all_data, hue='exp_group')

            ax = sns.swarmplot(x='exp_group', y=a_measurement, data=all_data, color='.5', size=6)

            ax.set_ylim([min(ax.dataLim.ymin - .05 * ax.dataLim.ymin, 0),
                         ax.dataLim.ymax + .05 * ax.dataLim.ymax])

            sns.despine()
            plt.show()

        return True
