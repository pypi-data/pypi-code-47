# -*- coding: utf-8 -*-

from collections import defaultdict
from typing import Tuple, List
import os
from pprint import pprint
import logging

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib as mpl
from matplotlib import cm
from matplotlib import rc
from matplotlib.colors import LogNorm

import numpy as np
from scipy.ndimage.filters import gaussian_filter1d
from scipy.optimize import curve_fit
from scipy.fftpack import fft

import h5py
from tqdm import tqdm

from .extract_data import ExtractData, get_time_axis, get_temp_axis
from .common_tools import save_create, get_zaptime_files, get_pen_folder_number
from .gisaxs_parameters import GisaxsParameters
from .xpcs import XPCS, plot_one_time_g

logging.basicConfig(level=logging.ERROR,
                    format='%(asctime)s %(levelname)s:%(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')

ed0 = ed1 = ExtractData()

labels_size = 20
mpl.rcParams['text.latex.preamble'] = [r'\boldmath']
rc('text', usetex=True)
rc('xtick', labelsize=labels_size)
rc('ytick', labelsize=labels_size)
rc('axes', labelsize=labels_size)
rc('axes', titlesize=labels_size)
rc('axes', titlesize=labels_size)
rc('legend', fontsize=labels_size)
