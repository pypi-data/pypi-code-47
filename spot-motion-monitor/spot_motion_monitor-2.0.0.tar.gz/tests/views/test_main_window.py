# This file is part of spot_motion_monitor.
#
# Developed for LSST System Integration, Test and Commissioning.
#
# See the LICENSE file at the top-level directory of this distribution
# for details of code ownership.
#
# Use of this source code is governed by a 3-clause BSD-style
# license that can be found in the LICENSE file.

import collections
import os

import numpy as np
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QAction, QMainWindow
import yaml

from spot_motion_monitor.camera import CameraStatus
from spot_motion_monitor.utils import CameraNotFound, FrameRejected, ONE_SECOND_IN_MILLISECONDS, YAML_INPUT
from spot_motion_monitor.views.main_window import SpotMotionMonitor

class TestMainWindow():

    # def setup_class(cls):
    #     cls.fastTimeout = 1250  # ms

    def write_config(self, filename):
        with open(filename, 'w') as ofile:
            yaml.dump(yaml.load(YAML_INPUT, yaml.Loader), ofile)

    def test_mainWindowExit(self, qtbot, mocker):
        mocker.patch('PyQt5.QtWidgets.QMainWindow.close')
        mw = SpotMotionMonitor()
        mw.show()
        qtbot.addWidget(mw)
        mw.actionExit.trigger()
        assert QMainWindow.close.call_count == 1

    def test_mainWindowAbout(self, qtbot, mocker):
        mocker.patch('spot_motion_monitor.views.main_window.SpotMotionMonitor.about')
        mw = SpotMotionMonitor()
        mw.show()
        qtbot.addWidget(mw)
        mw.actionAbout.trigger()
        assert SpotMotionMonitor.about.call_count == 1

    def test_setActionIcon(self, qtbot):
        mw = SpotMotionMonitor()
        qtbot.addWidget(mw)
        action = QAction()
        mw.setActionIcon(action, "test.png", True)
        assert action.icon() is not None
        assert action.isIconVisibleInMenu() is True

    def test_updateStatusBar(self, qtbot):
        mw = SpotMotionMonitor()
        mw.show()
        qtbot.addWidget(mw)
        message1 = "Hello World!"
        mw.cameraController.updater.displayStatus.emit(message1, ONE_SECOND_IN_MILLISECONDS)
        assert mw.statusbar.currentMessage() == message1
        message2 = "Have a nice evening!"
        mw.plotController.updater.displayStatus.emit(message2, ONE_SECOND_IN_MILLISECONDS)
        assert mw.statusbar.currentMessage() == message2
        message3 = "See you later!"
        mw.dataController.updater.displayStatus.emit(message3, ONE_SECOND_IN_MILLISECONDS)
        assert mw.statusbar.currentMessage() == message3

    def test_statusForFrameRejection(self, qtbot, mocker):
        mw = SpotMotionMonitor()
        mw.cameraController.setupCamera('GaussianCamera')
        qtbot.addWidget(mw)
        mockCamCont = mocker.patch('spot_motion_monitor.views.main_window.CameraController',
                                   spec=True)
        mocker.patch('spot_motion_monitor.camera.gaussian_camera.GaussianCamera.getFullFrame')
        mockCamCont.getFrame = mocker.MagicMock(return_value=np.ones((3, 5)))
        emessage = "Frame failed!"
        mw.cameraController.currentStatus = mocker.Mock(return_value=CameraStatus('Gaussian', 24, False,
                                                                                  (0, 0), True))
        mw.dataController.fullFrameModel.calculateCentroid = mocker.Mock(side_effect=FrameRejected(emessage))
        mw.plotController.passFrame = mocker.Mock(return_value=None)
        mw.acquireFrame()
        assert mw.statusbar.currentMessage() == emessage
        assert mw.plotController.passFrame.call_count == 1

    def test_updateBufferSize(self, qtbot):
        mw = SpotMotionMonitor()
        qtbot.addWidget(mw)
        truth_buffer_size = 2048
        mw.cameraController.updater.bufferSizeChanged.emit(truth_buffer_size)
        assert mw.dataController.getBufferSize() == truth_buffer_size

    def test_statusForCameraNotFound(self, qtbot, mocker):
        mw = SpotMotionMonitor()
        qtbot.addWidget(mw)
        emessage = "Camera Not Found!"
        mw.cameraController.camera.startup = mocker.Mock(side_effect=CameraNotFound(emessage))
        qtbot.mouseClick(mw.cameraControl.startStopButton, Qt.LeftButton)
        assert mw.statusbar.currentMessage() == emessage

    def test_cameraMenu(self, qtbot, mocker):
        mocker.patch('spot_motion_monitor.views.main_window.SpotMotionMonitor.handleCameraSelection')
        mw = SpotMotionMonitor()
        mw.show()
        qtbot.addWidget(mw)
        numCameras = len(mw.cameraController.getAvailableCameras())
        assert len(mw.menuCamera.actions()) == numCameras
        # Force camera setup
        mw.cameraController.setupCamera('GaussianCamera')
        assert mw.menuCamera.isEnabled() is True
        qtbot.mouseClick(mw.cameraControl.startStopButton, Qt.LeftButton)
        assert mw.menuCamera.isEnabled() is False

    def test_configurationMenu(self, qtbot):
        mw = SpotMotionMonitor()
        mw.show()
        qtbot.addWidget(mw)
        # Force camera setup
        mw.cameraController.setupCamera('GaussianCamera')
        assert mw.actionCameraConfig.isEnabled() is True
        assert mw.actionPlotsConfig.isEnabled() is True
        assert mw.actionDataConfig.isEnabled() is True
        assert mw.actionGeneralConfig.isEnabled() is True
        assert mw.actionCameraInfo.isEnabled() is False
        qtbot.mouseClick(mw.cameraControl.startStopButton, Qt.LeftButton)
        assert mw.actionCameraConfig.isEnabled() is False
        assert mw.actionPlotsConfig.isEnabled() is True
        assert mw.actionDataConfig.isEnabled() is True
        assert mw.actionGeneralConfig.isEnabled() is True
        assert mw.actionCameraInfo.isEnabled() is True

    def test_commandLineConfiguration(self, qtbot, mocker):
        mw = SpotMotionMonitor()
        mw.show()
        qtbot.addWidget(mw)
        # Force camera setup
        mw.cameraController.setupCamera('GaussianCamera')

        args = collections.namedtuple('args', ['profile', 'telemetry_dir', 'config_file', 'auto_run',
                                               'vimba_camera_index'])
        args.telemetry_dir = "/new/path/for/telemetry"
        args.auto_run = False
        filename = "test_new_config.yaml"
        args.config_file = filename
        self.write_config(filename)

        mw.handleConfig(args)
        assert mw.dataController.getDataConfiguration().fullTelemetrySavePath == args.telemetry_dir
        assert mw.dataController.bufferModel.bufferSize == 512

        os.remove(filename)

    def test_autoRun(self, qtbot, mocker):
        mw = SpotMotionMonitor()
        mw.show()
        qtbot.addWidget(mw)
        # Force camera setup
        mw.cameraController.setupCamera('GaussianCamera')
        mockCameraControllerAutoRun = mocker.patch.object(mw.cameraController, 'autoRun')

        args = collections.namedtuple('args', ['profile', 'telemetry_dir', 'config_file', 'auto_run',
                                               'vimba_camera_index'])
        args.telemetry_dir = None
        args.auto_run = True

        mw.handleConfig(args)
        mw.autoRunIfNecessary()
        assert mockCameraControllerAutoRun.call_count == 1

    def test_saveConfiguration(self, qtbot, mocker):
        mw = SpotMotionMonitor()
        mw.show()
        qtbot.addWidget(mw)
        # Force camera setup
        mw.cameraController.setupCamera('GaussianCamera')

        truthFile = "./configuration.yaml"

        mask = mw.getSaveConfigurationMask()
        assert mask == 0

        mw._saveFileDialog = mocker.Mock(return_value=truthFile)
        mw.saveConfiguration()
        assert os.path.exists(truthFile)
        os.remove(truthFile)

    def test_saveConfigurationMask(self, qtbot):
        mw = SpotMotionMonitor()
        mw.show()
        qtbot.addWidget(mw)
        # Force camera setup
        mw.cameraController.setupCamera('GaussianCamera')

        mask = mw.getSaveConfigurationMask()
        assert mask == 0
        mw.actionWritePlotConfig.setChecked(True)
        mask = mw.getSaveConfigurationMask()
        assert mask == 1
        mw.actionWriteEmptyConfig.setChecked(True)
        mask = mw.getSaveConfigurationMask()
        assert mask == 3
        mw.actionWritePlotConfig.setChecked(False)
        mask = mw.getSaveConfigurationMask()
        assert mask == 2

    def test_setConfiguration(self, qtbot, mocker):
        mw = SpotMotionMonitor()
        mw.show()
        qtbot.addWidget(mw)
        # Force camera setup
        mw.cameraController.setupCamera('GaussianCamera')

        filename = "test_config.yaml"
        self.write_config(filename)
        mw.setConfiguration(filename)

        assert mw.cameraController.doAutoRun is True
        assert mw.dataController.getGeneralConfiguration().configVersion == "1.5.2"
        assert mw.dataController.getDataConfiguration().buffer.bufferSize == 512

        os.remove(filename)

    # def test_openConfiguration(self, qtbot, mocker):
    #     mw = SpotMotionMonitor()
    #     mw.show()
    #     qtbot.addWidget(mw)
    #     # Force camera setup
    #     mw.cameraController.setupCamera('GaussianCamera')

    #     truthFile = "./configuration.yaml"
    #     mw._configOverrideWarning = mocker.Mock()
    #     mw._openFileDialog = mocker.Mock(return_value=truthFile)
    #     mwSetConfigurationMock = mocker.patch.object(mw, 'setConfiguration')

    #     mw.openConfiguration()
    #     assert mwSetConfigurationMock.call_count == 1

    # def test_acquire_frame(self, qtbot, mocker):
    #     mw = SpotMotionMonitor()
    #     qtbot.addWidget(mw)
    #     mocker.patch('spot_motion_monitor.views.main_window.SpotMotionMonitor.acquireFrame')
    #     signals = [mw.cameraController.cc_widget.acquireFramesState,
    #                mw.cameraController.frameTimer.timeout]
    #     with qtbot.waitSignals(signals):  # , timeout=self.fastTimeout):
    #         qtbot.mouseClick(mw.cameraControl.acquireFramesButton, Qt.LeftButton)
    #     assert mw.acquireFrame.call_count == 1
    #     qtbot.mouseClick(mw.cameraControl.acquireFramesButton, Qt.LeftButton)
