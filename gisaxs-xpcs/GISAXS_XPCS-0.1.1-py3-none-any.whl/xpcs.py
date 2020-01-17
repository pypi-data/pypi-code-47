#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import re
import logging
from typing import Tuple, Union, List
from pprint import pprint

import numpy as np
from scipy.ndimage import zoom
import h5py
from tqdm import tqdm

import matplotlib.pyplot as plt
import matplotlib.patches as patches

from gisaxs_xpcs.common_tools import get_zaptime_files
from gisaxs_xpcs.gisaxs_parameters import GisaxsParameters
from gisaxs_xpcs.extract_data import ExtractData

logger = logging.getLogger(__name__)


class XPCS(object):
    """
    Class contains the basic functionality to calculate
    two-time correlation functions for
    GISAXS images stored to .h5 file.
    """

    DEFAULT_H5_FILEPATH = '/media/vladimir/data/GISAXS_DATA/test_raw_data.h5'

    @staticmethod
    def _default_h5_path(folder_num: int):
        return '/'.join(['Raw data', 'zaptime_%s' % str(folder_num).zfill(2)])

    def __init__(self, folder_num: int = None,
                 cut_region: Tuple[float, float, float, float] = None,
                 gp: GisaxsParameters = None,
                 h5_filepath: str = None,
                 h5_path: str = None):
        """

        :param folder_num: number of the zaptime folder to analyse
        :param cut_region: tuple(x_min, x_max, y_min, y_max) in [deg]
        :param gp: gisaxs parameters object (necessary to extract angles)
        :param h5_filepath: path to the data source
        :param h5_path: path to zaptime folder in h5 file
        """
        if not folder_num and not h5_filepath:
            raise ValueError('Either folder_num or h5_filename should be provided')

        self.folder_num = folder_num
        self.size = len(get_zaptime_files(self.folder_num))
        self.index_x = self.index_y = None
        if not gp and folder_num:
            self.gp = GisaxsParameters.init_from_folder_number(folder_num)
        else:
            self.gp = gp or GisaxsParameters()
        self.cut_region = cut_region
        self.h5_filepath = h5_filepath or self.DEFAULT_H5_FILEPATH
        self.h5_path = h5_path or self._default_h5_path(self.folder_num)
        if not self.setup_h5():
            raise NotImplementedError('Reading from remote folder is not'
                                      ' implemented yet.')

        self.x_angles, self.y_angles = self.gp.get_angle_vectors(units='deg',
                                                                 flip=False)
        self.x, self.y = np.sort(self.x_angles), np.flip(np.sort(self.y_angles),
                                                         axis=0)

        if self.cut_region is not None:
            self.init_indexes()

    def set_region(self, cut_region: Tuple[float, float, float, float]):
        self.cut_region = cut_region
        self.init_indexes()

    def setup_h5(self) -> bool:
        """
        Checks .h5 file. If it exists and contains the provided path to the dataset,
        returns True, otherwise False.
        """
        if not os.path.isfile(self.h5_filepath):
            logger.error('File %s doesn\'t exist.' % self.h5_filepath)
            return False
        try:
            with h5py.File(self.h5_filepath, 'r') as f:
                if f.get(self.h5_path, None) is None:
                    logger.error('File does not contain path %s' % self.h5_path)
                    return False
                # data = f[self.h5_path][list(f[self.h5_path].keys())[0]][()]
                # print(data.shape)
        except Exception as err:
            logger.error(err)
            return False
        return True

    def init_indexes(self):
        self.index_x = np.min(np.where(self.y < self.cut_region[3])[0]), \
                       np.max(np.where(self.y > self.cut_region[2])[0])
        self.index_y = np.min(np.where(self.x > self.cut_region[0])[0]), \
                       np.max(np.where(self.x < self.cut_region[1])[0])
        logger.debug(f'self.index_x, self.index_y')

    def get_qt_array(self, mode='one-time'):
        if mode not in ['one-time', 'mean', 'std']:
            raise ValueError("Mode should be one of 'one-time', 'mean', 'std'.")
        if self.cut_region is None:
            raise ValueError('cut region is not defined')
        with h5py.File(self.h5_filepath, 'r') as f:
            digits_pattern = r'^([\s\d]+)$'
            dset_keys = [k for k in f[self.h5_path].keys() if re.search(digits_pattern, k)]
            dset_sorted_keys = sorted(dset_keys, key=lambda x: int(x))

            dset = f[self.h5_path][dset_sorted_keys[0]]
            intensity = dset[self.index_x[0]:self.index_x[1],
                        self.index_y[0]:self.index_y[1]]

            intensity_array = np.empty((self.size, intensity.shape[0] * intensity.shape[1]))
            t_array = np.empty(self.size)

            for dset_number, dset_name in enumerate(dset_sorted_keys):
                dataset = f[self.h5_path][dset_name]
                intensity = dataset[self.index_x[0]:self.index_x[1],
                            self.index_y[0]:self.index_y[1]]
                intensity = intensity.flatten()

                if mode == 'one-time':
                    intensity_array[dset_number] = intensity
                elif mode == 'mean':
                    intensity_array[dset_number, :] = intensity / intensity.mean()
                else:
                    intensity_array[dset_number, :] = intensity / intensity.std()

                t_array[dset_number] = dataset.attrs.get('time_of_frame', dset_number)
            return intensity_array, t_array

    def get_one_time_corr_function(self, mode='one-time'):
        if mode not in ['one-time', 'mean']:
            raise ValueError('Mode should be one of "one-time" and "mean".')
        intensity_array, t_array = self.get_qt_array(mode=mode)
        if mode == 'one-time':
            norm_constant = intensity_array.mean(axis=1).mean(axis=0) ** 2
        else:
            norm_constant = 1
        corr_matrix = intensity_array.dot(intensity_array.transpose()) / intensity_array.shape[1]
        corr_function = np.empty(intensity_array.shape[0])

        for t in range(corr_matrix.shape[0]):
            corr_function[t] = corr_matrix.diagonal(t).mean() / norm_constant
        return corr_function, t_array

    def get_two_time_corr_function(self, mode='std'):
        if mode not in ['mean', 'std']:
            raise ValueError("Mode should be one of 'mean', 'std'.")
        intensity_array, _ = self.get_qt_array(mode=mode)
        if mode == 'mean':
            res = intensity_array.dot(intensity_array.transpose()) / intensity_array.shape[1]
        else:
            res = intensity_array.dot(intensity_array.transpose()) / intensity_array.shape[1]
            i_mean = np.expand_dims(intensity_array.mean(axis=1), axis=1)
            # assert i_mean.shape == (intensity_array.shape[0], 1), 'Wrong i_mean shape: %s' % str(i_mean.shape)
            # m_res = i_mean.dot(i_mean.transpose())
            # assert m_res.shape == res.shape, 'Wrong m_res shape: %s' % str(m_res.shape)
            res -= i_mean.dot(i_mean.transpose())
        return res

    def get_intensity(self):
        intensity, t = self.get_qt_array('one-time')
        intensity = intensity.mean(axis=1)
        return intensity, t

    def plot_cut(self, filenum: int = 1):
        extract_data = ExtractData()
        extract_data.get_images(self.folder_num, filenum,
                                apply_log=True, plot=True, show=False, gp=self.gp)
        ax = plt.gca()
        cut = self.cut_region
        r = patches.Rectangle((cut[0], cut[2]), cut[1] - cut[0], cut[3] - cut[2],
                              fill=False, color='red')
        ax.add_patch(r)
        plt.show()


class CutList(list):
    """
    CutList is a list containing elements
    of type Tuple[x_min, x_max, y_min, y_max].
    x_min, x_max, y_min, y_max are values in degrees
    that define a window on a GISAXS image within which
    XPCS correlation functions will be calculated.

    Should be only initialized via classmethods and never from __init__().
    """

    __slots__ = ['parameters']

    @classmethod
    def get_cut_list(cls, init_window: Union[Tuple[float, float, float, float],
                                             Tuple[float, float]],
                     axis: int, step: float, number_of_cuts: int):
        self = cls()
        if axis not in (0, 1):
            raise ValueError('Axis value should be 0 (cuts along q parallel)'
                             ' or 1 (cuts along q z axis)')
        if len(init_window) == 2:
            init_window = (init_window[0], init_window[0] + step,
                           init_window[1], init_window[1] + step)
        if axis == 0:
            self.append([(init_window[0] + step * i,
                          init_window[1] + step * i,
                          init_window[2],
                          init_window[3]) for i in range(number_of_cuts)])
        else:
            self.append([(init_window[0],
                          init_window[1],
                          init_window[2] + step * i,
                          init_window[3] + step * i)
                         for i in range(number_of_cuts)])
        setattr(self, 'parameters', dict(init_window=init_window, step=step,
                                         axis=axis, number_of_cuts=number_of_cuts, mode='list'))
        return self

    @classmethod
    def get_cut_grid(cls, init_window: Union[Tuple[float, float, float, float],
                                             Tuple[float, float]],
                     xy_step: Tuple[float, float],
                     xy_size: Tuple[int, int]):
        if len(init_window) == 2:
            init_window = (init_window[0], init_window[0] + xy_step[0],
                           init_window[1], init_window[1] + xy_step[1])
        self = cls()
        for i in range(xy_size[0]):
            for j in range(xy_size[1]):
                self.append((init_window[0] + xy_step[0] * i,
                             init_window[1] + xy_step[0] * i,
                             init_window[2] + xy_step[1] * j,
                             init_window[3] + xy_step[1] * j))
        setattr(self, 'parameters', dict(init_window=init_window, xy_step=xy_step,
                                         xy_size=xy_size, mode='grid'))
        return self

    @classmethod
    def init_from_parameters_dict(cls, parameters: dict):
        try:
            mode = parameters.pop('mode')
            if mode == 'grid':
                return cls.get_cut_grid(**parameters)
            elif mode == 'list':
                return cls.get_cut_list(**parameters)
            else:
                raise ValueError('Mode should be "grid" or "list".')

        except TypeError as err:
            raise KeyError('Provided parameters dict does not contain'
                           ' necessary parameter. Error: %s ' % err)

    def get_ranges(self) -> dict:
        def func(i):
            return [x[i] for x in self]

        x_range = (min(func(0)), max(func(1)))
        y_range = (min(func(2)), max(func(3)))
        return dict(x_range=x_range, y_range=y_range)

    def __repr__(self):
        return f'<CutList>.\nParameters: {self.parameters}\n' \
            f'Values:{super(CutList, self).__repr__()}>'


class XPCSMap(XPCS):
    DEFAULT_XPCS_MAP_H5_FILEPATH = '/media/vladimir/data/GISAXS_DATA/xpcs2d.h5'

    @staticmethod
    def _default_xpcs_map_h5_group_name(folder_num: int):
        return 'zaptime_%d' % folder_num

    def __init__(self, folder_num: int = None,
                 cut_list: CutList = None,
                 gp: GisaxsParameters = None,
                 h5_filepath: str = None,
                 h5_path: str = None,
                 xpcs_map_h5_filepath: str = None,
                 h5_group_name: str = None):
        super(XPCSMap, self).__init__(folder_num, None,
                                      gp, h5_filepath, h5_path)
        self.cut_list = cut_list
        self.xpcs_map_h5_filepath = xpcs_map_h5_filepath or self.DEFAULT_XPCS_MAP_H5_FILEPATH
        self.group_name = h5_group_name or self._default_xpcs_map_h5_group_name(folder_num)
        self.map_is_saved = False

    def set_cut_grid(self):
        raise NotImplementedError()

    def set_cut_list(self):
        raise NotImplementedError()

    def plot_grid(self):
        raise NotImplementedError()

    def save_map(self, cut_list: CutList = None):
        if cut_list is not None:
            self.cut_list = cut_list
        if self.cut_list is None:
            raise ValueError('cut_list should be provided.')

        def save_dset_to_h5(dset, dset_name, cut):
            with h5py.File(self.xpcs_map_h5_filepath, 'a') as f:
                folder = f[self.group_name]
                dset = folder.create_dataset(dset_name, data=dset)
                dset.attrs['cut'] = cut
                logger.debug(f'XPCS saved to {"/".join([self.xpcs_map_h5_filepath, self.group_name, dset_name])}')

        with h5py.File(self.xpcs_map_h5_filepath, 'a') as f:
            if self.group_name in f.keys():
                del f[self.group_name]
            folder = f.create_group(self.group_name)
            folder.attrs.update(self.cut_list.parameters)

        for i, cut in enumerate(tqdm(self.cut_list)):
            self.set_region(cut)
            res = self.get_two_time_corr_function(mode='std')
            save_dset_to_h5(res, str(i), cut)
            del res

        self.map_is_saved = True

    def plot_grid_on_fly(self, cut_list: CutList = None, figsize: Tuple[int, int] = None,
                         reduce_factor: float = None,
                         reduce_mode: str = 'nearest',
                         save_path: str = None):
        if cut_list is not None:
            self.cut_list = cut_list
        if self.cut_list is None:
            raise ValueError('cut_list should be provided.')

        parameters = self.cut_list.parameters

        if parameters['mode'] != 'grid':
            raise ValueError('Method is allowed only for a grid mode.')

        nx, ny = parameters['xy_size']

        figsize = figsize or (nx, ny)
        fig, axs = plt.subplots(nrows=ny, ncols=nx, sharex=True, figsize=figsize)
        axs = np.flip(axs.transpose(), axis=1).flatten()

        for i, (ax, cut) in enumerate(tqdm(zip(axs, self.cut_list))):
            self.set_region(cut)
            res = self.get_two_time_corr_function(mode='std')
            if reduce_factor:
                res = zoom(res, reduce_factor, mode=reduce_mode)
            ax.imshow(res, cmap='jet')
            ax.set_xticks([], [])
            ax.set_yticks([], [])
            if i < ny:
                ax.set_ylabel(str((cut[2] + cut[3]) / 2)[:5])
            if i % ny == 0:
                ax.set_xlabel(str((cut[0] + cut[1]) / 2)[:5])

        plt.subplots_adjust(wspace=0, hspace=0)
        if not save_path:
            plt.show()
        else:
            plt.savefig(save_path)

    def plot_map(self, figsize: Tuple[int, int] = None,
                 reduce_factor: float = None,
                 reduce_mode: str = 'nearest',
                 save_path: str = None):
        if not self.map_is_saved:
            raise ValueError('Map is not saved. '
                             'Use plot_saved_map method to plot previously saved maps.')
        try:
            mode = self.cut_list.parameters['mode']
        except (KeyError, AttributeError) as err:
            raise ValueError('cut_list attribute is wrong. Error: %s' % err)

        if mode == 'grid':
            self._plot_grid_map(figsize, reduce_factor, reduce_mode)
        elif mode == 'list':
            self._plot_list_map(figsize, reduce_factor, reduce_mode)
        else:
            raise ValueError(f"cut_list.parameters['mode'] should be 'list' or 'grid'. "
                             f"Found {mode} instead.")
        if not save_path:
            plt.show()
        else:
            plt.savefig(save_path)

    def _plot_grid_map(self, figsize: Tuple[int, int] = None,
                       reduce_factor: float = None,
                       reduce_mode: str = 'nearest'):

        with h5py.File(self.xpcs_map_h5_filepath, 'r') as f:
            parameters = dict(f[self.group_name].attrs)

        nx, ny = parameters['xy_size']

        def get_dset(name):
            with h5py.File(self.xpcs_map_h5_filepath, 'r') as f:
                dset = f[self.group_name][name]
                cut = dset.attrs['cut']
                res = dset[()]
                return res, cut

        figsize = figsize or (nx, ny)
        fig, axs = plt.subplots(nrows=ny, ncols=nx, sharex=True, figsize=figsize)
        axs = np.flip(axs.transpose(), axis=1).flatten()

        for i, ax in enumerate(tqdm(axs)):
            res, cut = get_dset(str(i))
            if reduce_factor:
                res = zoom(res, reduce_factor, mode=reduce_mode)
            ax.imshow(res, cmap='jet')
            ax.set_xticks([], [])
            ax.set_yticks([], [])
            if i < ny:
                ax.set_ylabel(str((cut[2] + cut[3]) / 2)[:5])
            if i % ny == 0:
                ax.set_xlabel(str((cut[0] + cut[1]) / 2)[:5])

        plt.subplots_adjust(wspace=0, hspace=0)

    def plot_grid_part(self, xy_size: Tuple[int, int, int, int],
                       figsize: Tuple[int, int] = None,
                       save_path: str = None, reduce_factor: float = None,
                       reduce_mode: str = 'nearest', parameters: dict = None):
        parameters = parameters or self.cut_list.parameters
        nx, ny = parameters['xy_size']

        def get_dset(name):
            with h5py.File(self.xpcs_map_h5_filepath, 'r') as f:
                dset = f[self.group_name][name]
                cut = dset.attrs['cut']
                res = dset[()]
                return res, cut

        figsize = figsize or (nx, ny)
        fig, axs = plt.subplots(nrows=ny, ncols=nx, sharex=True, figsize=figsize)
        axs = np.flip(axs.transpose(), axis=1).flatten()

        for i, ax in enumerate(tqdm(axs)):
            res, cut = get_dset(str(i))
            if reduce_factor:
                res = zoom(res, reduce_factor, mode=reduce_mode)
            ax.imshow(res, cmap='jet')
            ax.set_xticks([], [])
            ax.set_yticks([], [])
            if i < ny:
                ax.set_ylabel(str((cut[2] + cut[3]) / 2)[:5])
            if i % ny == 0:
                ax.set_xlabel(str((cut[0] + cut[1]) / 2)[:5])

        plt.subplots_adjust(wspace=0, hspace=0)

    def _plot_list_map(self, figsize: Tuple[int, int] = None,
                       reduce_factor: float = None,
                       reduce_mode: str = 'nearest', parameters: dict = None):
        # parameters = parameters or cut_list.parameters
        raise NotImplementedError

    def plot_saved_map(self, folder_num: int = None, group_name: str = None,
                       h5_file_path: str = None,
                       save_path: str = None, **kwargs):
        raise NotImplementedError('Need to fix bugs first.')

        if group_name:
            pass
        elif folder_num:
            group_name = self._default_xpcs_map_h5_group_name(folder_num)
        else:
            group_name = self.group_name
        h5_file_path = h5_file_path or self.xpcs_map_h5_filepath

        with h5py.File(h5_file_path, 'r') as f:
            try:
                group = f[group_name]
            except KeyError:
                raise KeyError('Group %s is not in the file %s' % (group_name, h5_file_path))
            parameters = dict(group.attrs)

        mode = parameters.pop('mode')

        if mode == 'grid':
            self._plot_grid_map(parameters=parameters, **kwargs)
        elif mode == 'list':
            self._plot_list_map(parameters=parameters, **kwargs)

        if not save_path:
            plt.show()
        else:
            plt.savefig(save_path)

    def plot_cut(self, filenum: int = 0, **kwargs):
        extract_data = ExtractData()
        extract_data.get_images(self.folder_num, filenum,
                                apply_log=True, plot=True, show=False,
                                gp=self.gp,
                                **self.cut_list.get_ranges())
        ax = plt.gca()
        for cut in self.cut_list:
            r = patches.Rectangle((cut[0], cut[2]), cut[1] - cut[0],
                                  cut[3] - cut[2],
                                  fill=False, color='red', **kwargs)
            ax.add_patch(r)
        plt.show()


def plot_one_time_g(folder_num: int, x_range_cut: Tuple[float, float],
                    delta_x: float, y_position: Tuple[float, float],
                    x_range: Tuple[float, float] = (0, 0.3),
                    y_range: Tuple[float, float] = (0, 0.4)):
    extract_data = ExtractData()
    extract_data.get_images(folder_num, 1, x_range=x_range, y_range=y_range,
                            apply_log=True, plot=True, show=False)
    ax = plt.gca()
    xpcs = XPCS(folder_num)
    f_list = list()
    x_cuts = np.linspace(x_range_cut[0], x_range_cut[1],
                         int((x_range_cut[1] - x_range_cut[0]) / delta_x + 1))
    for i in tqdm(x_cuts):
        cut = (i, i + delta_x, y_position[0], y_position[1])
        r = patches.Rectangle((cut[0], cut[2]), cut[1] - cut[0], cut[3] - cut[2],
                              fill=False, color='red')
        ax.add_patch(r)
        xpcs.set_region(cut)
        f, t = xpcs.get_one_time_corr_function()
        f_list.append(f)

    plt.show()
    plt.figure()
    for i, f in enumerate(f_list):
        plt.plot(t, f, label=str(x_cuts[i])[:4])
    plt.legend()
    plt.show()
    return f_list, t


def show_copied_folders():
    xpcs = XPCS(96)
    print(xpcs.DEFAULT_H5_FILEPATH)
    with h5py.File(xpcs.DEFAULT_H5_FILEPATH, 'r') as f:
        pprint(list(f['Raw data'].keys()))


def save_xpcs_maps(folder_list: List[int], cut_list: CutList = None, *,
                   reduce_factor: float = 0.2):
    cut_list = cut_list or CutList.get_cut_grid((-0.1, 0),
                                                xy_size=(10, 15),
                                                xy_step=(0.02, 0.02))
    for folder_number in tqdm(folder_list):
        xpcs_map = XPCSMap(folder_number, cut_list=cut_list)
        xpcs_map.save_map()
        xpcs_map.plot_map(reduce_factor=reduce_factor,
                          save_path=f'xpcs_map_{folder_number}.png')


def xpcs_2d_profiler():
    import cProfile
    cProfile.run('XPCS(20, (0.03, 0.04, 0.09, 0.1)).get_two_time_corr_function()')


if __name__ == '__main__':
    logging.basicConfig(level=logging.ERROR)
    # show_copied_folders()
    folder_number = 38
    cut_list = CutList.get_cut_grid((-0.1, 0),
                                    xy_size=(10, 15),
                                    xy_step=(0.02, 0.02))
    xpcs_map = XPCSMap(folder_number, cut_list=cut_list)
    xpcs_map.plot_saved_map(folder_number, reduce_factor=0.4,
                            save_path=f'xpcs_map_{folder_number}.png')
    #
    # for folder in [69, 76, 85, 99]:
    #     try:
    #         xpcs_map = XPCSMap(folder_number, cut_list=cut_list)
    #         # xpcs_map.save_map()
    #         xpcs_map.plot_saved_map(folder_number, reduce_factor=0.2)
    #     except Exception as err:
    #         logger.error(err)
    # xpcs_map.plot_saved_map(folder_number, reduce_factor=0.05)

    # xpcs = XPCS(96, (0.03, 0.04, 0.09, 0.1))
    # xpcs_2d_profiler(xpcs)
    # [20, 38, 69, 76, 85, 90, 99]
