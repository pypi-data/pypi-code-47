# This file is part of spot_motion_monitor.
#
# Developed for LSST System Integration, Test and Commissioning.
#
# See the LICENSE file at the top-level directory of this distribution
# for details of code ownership.
#
# Use of this source code is governed by a 3-clause BSD-style
# license that can be found in the LICENSE file.

__all__ = ["CSS"]

"""The CSS definition for the application.
"""
CSS = """
        QGroupBox {
            border: 1px solid gray;
            border-radius: 3px;
            margin-top: 0.5em;
            font-size: 14px;
        }

        QGroupBox::title {
            subcontrol-origin: margin;
            subcontrol-position: top center; /* position at the top center */
            padding: 0 3px;
            background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                      stop: 0 #D0D0D0, stop: 1 #F0F0F0);
        }

        QLineEdit[readOnly="true"] {
            background: #f0f0f0;
        }
      """
