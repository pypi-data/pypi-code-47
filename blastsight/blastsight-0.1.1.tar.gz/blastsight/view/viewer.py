#!/usr/bin/env python

#  Copyright (c) 2019 Gabriel Sanhueza.
#
#  Distributed under the MIT License.
#  See LICENSE for more info.

import sys

from qtpy.QtCore import Qt
from qtpy.QtCore import QTimer
from qtpy.QtWidgets import QApplication

from .integrableviewer import IntegrableViewer


class Viewer(IntegrableViewer):
    def __init__(self):
        self.app = QApplication(sys.argv)
        super().__init__()
        self.setWindowTitle('BlastSight (Viewer)')

    def show(self, detached: bool = False, timer: int = 0, autofit: bool = True) -> None:
        # This will auto-fit to screen when used from a script,
        # as it's reasonable to expect the figure to be shown
        # immediately, even if it's far from [0.0, 0.0, 0.0].
        if autofit:
            self.fit_to_screen()

        super().show()

        if detached:
            # This allow us to detach the widget (convenient if running
            # the viewer in an interactive console).
            # WARNING: On PySide2, the viewer WILL freeze when the timer
            # runs out, but you can manually close it with `viewer.close()`.
            QTimer.singleShot(timer, self.app.quit)

        self.app.exec_()

    def take_screenshot(self, save_path=None, width=None, height=None) -> None:
        width = width or self.width()
        height = height or self.height()

        self.resize(width, height)
        super().take_screenshot(save_path)

    def dragEnterEvent(self, event, *args, **kwargs) -> None:
        super().dragEnterEvent(event, *args, **kwargs)

    def dropEvent(self, event, *args, **kwargs) -> None:
        super().dropEvent(event, *args, **kwargs)
        self.camera_at(self.last_id)

    def keyPressEvent(self, event) -> None:
        def rotate(angle_list: list) -> None:
            self.rotation_angle += angle_list
            self.update()

        def move(pos_list: list) -> None:
            self.camera_position += pos_list
            self.update()

        shortcut_commands_dict = {
            Qt.Key_1: self.plan_view,
            Qt.Key_2: self.north_view,
            Qt.Key_3: self.east_view,
            Qt.Key_4: self.perspective_projection,
            Qt.Key_5: self.orthographic_projection,
            Qt.Key_Space: self.fit_to_screen,
            Qt.Key_Delete: lambda: self.delete(self.last_id),
            Qt.Key_W: lambda: rotate([-10.0, 0.0, 0.0]),
            Qt.Key_S: lambda: rotate([10.0, 0.0, 0.0]),
            Qt.Key_A: lambda: rotate([0.0, -10.0, 0.0]),
            Qt.Key_D: lambda: rotate([0.0, 10.0, 0.0]),
            Qt.Key_Q: lambda: rotate([0.0, 0.0, 10.0]),
            Qt.Key_E: lambda: rotate([0.0, 0.0, -10.0]),
            Qt.Key_Left: lambda: move([1.0, 0.0, 0.0]),
            Qt.Key_Right: lambda: move([-1.0, 0.0, 0.0]),
            Qt.Key_Up: lambda: move([0.0, -1.0, 0.0]),
            Qt.Key_Down: lambda: move([0.0, 1.0, 0.0]),
            Qt.Key_PageDown: lambda: move([0.0, 0.0, -1.0]),
            Qt.Key_PageUp: lambda: move([0.0, 0.0, 1.0]),
        }

        # Execute command based on event.key()
        shortcut_commands_dict.get(event.key(), lambda: None)()
