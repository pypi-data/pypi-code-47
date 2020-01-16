# This file is part of spot_motion_monitor.
#
# Developed for LSST System Integration, Test and Commissioning.
#
# See the LICENSE file at the top-level directory of this distribution
# for details of code ownership.
#
# Use of this source code is governed by a 3-clause BSD-style
# license that can be found in the LICENSE file.

import argparse

__all__ = ['create_parser']

def create_parser():
    """Create the argument parser for the main application.

    Returns
    -------
    argparse.ArgumentParser
        The application command-line parser.
    """
    description = ['This is the UI for running the Dome Seeing Monitor.']

    parser = argparse.ArgumentParser(description=' '.join(description),
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('--profile', dest='profile', action='store_true',
                        help='Supply a filename to trigger profiling the code.')
    parser.add_argument('-t', '--telemetry_dir', dest='telemetry_dir',
                        help='Provide an alternate full path for telemetry saving.')
    parser.add_argument('-c', '--config', dest='config_file',
                        help='Supply a YAML configuration file.')
    parser.add_argument('-a', '--auto-run', dest='auto_run', action='store_true',
                        help='Startup and run the UI in ROI mode.')

    vimba_camera_group_descr = ['This group controls features of Vimba class cameras.']
    vimba_camera_group = parser.add_argument_group('vimba', ' '.join(vimba_camera_group_descr))
    vimba_camera_group.add_argument('-i', '--camera-index', dest='vimba_camera_index', type=int,
                                    help='Supply a different index for the Vimba camera if more '
                                         'than one is present.')

    return parser
