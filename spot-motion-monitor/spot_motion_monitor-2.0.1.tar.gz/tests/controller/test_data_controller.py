# This file is part of spot_motion_monitor.
#
# Developed for LSST System Integration, Test and Commissioning.
#
# See the LICENSE file at the top-level directory of this distribution
# for details of code ownership.
#
# Use of this source code is governed by a 3-clause BSD-style
# license that can be found in the LICENSE file.

from datetime import timedelta
import os

from freezegun import freeze_time
import numpy as np
from PyQt5.QtCore import Qt

from spot_motion_monitor.camera import CameraStatus
from spot_motion_monitor.config import DataConfig, GeneralConfig
from spot_motion_monitor.controller import DataController
from spot_motion_monitor.utils import FrameRejected, GenericFrameInformation, RoiFrameInformation
from spot_motion_monitor.utils import getTimestamp, passFrame
from spot_motion_monitor.views import CameraDataWidget

class TestDataController():

    def setup_class(cls):
        cls.frame = np.ones((3, 5))
        cls.fullFrameStatus = CameraStatus('Gaussian', 24, False, (0, 0), True)
        cls.roiFrameStatus = CameraStatus('Gaussian', 40, True, (264, 200), True)
        cls.timestamp = getTimestamp()
        cls.deltaTime = timedelta(seconds=1)

    def test_parametersAfterConstruction(self, qtbot):
        cdw = CameraDataWidget()
        qtbot.addWidget(cdw)
        dc = DataController(cdw)
        assert dc.cameraDataWidget is not None
        assert dc.updater is not None
        assert dc.fullFrameModel is not None
        assert dc.roiFrameModel is not None
        assert dc.bufferModel is not None
        assert dc.roiResetDone is False
        assert dc.filesCreated is False
        assert dc.centroidFilename is None
        assert dc.psdFilename is None
        assert dc.telemetrySavePath is None
        assert dc.telemetrySetup is False
        assert dc.fullTelemetrySavePath is None
        assert dc.configVersion is None
        assert dc.configFile is None
        assert dc.dataConfig is not None
        assert dc.generalConfig is not None
        assert dc.timeHandler is not None
        assert dc.cameraModelName is None
        assert dc.roiFrameModel.timeHandler is not None
        assert dc.fullFrameModel.timeHandler is not None

    def test_updateFullFrameData(self, qtbot, mocker):
        cdw = CameraDataWidget()
        qtbot.addWidget(cdw)
        dc = DataController(cdw)
        mockCameraDataWidgetReset = mocker.patch.object(cdw, 'reset')
        mocker.patch('spot_motion_monitor.views.camera_data_widget.CameraDataWidget.updateFullFrameData')
        dc.fullFrameModel.calculateCentroid = mocker.Mock(return_value=GenericFrameInformation(self.timestamp,
                                                                                               300.3,
                                                                                               400.2,
                                                                                               32042.42,
                                                                                               145.422,
                                                                                               17.525,
                                                                                               70,
                                                                                               None))
        dc.passFrame(self.frame, self.fullFrameStatus)
        assert dc.cameraDataWidget.updateFullFrameData.call_count == 1
        assert mockCameraDataWidgetReset.call_count == 0
        assert dc.roiResetDone is False
        dc.roiResetDone = True
        dc.passFrame(self.frame, self.fullFrameStatus)
        assert mockCameraDataWidgetReset.call_count == 1
        assert dc.roiResetDone is False

    def test_failedFrame(self, qtbot, mocker):
        cdw = CameraDataWidget()
        qtbot.addWidget(cdw)
        dc = DataController(cdw)
        mocker.patch('spot_motion_monitor.views.camera_data_widget.CameraDataWidget.updateFullFrameData')
        dc.fullFrameModel.calculateCentroid = mocker.Mock(side_effect=FrameRejected)
        dc.passFrame(self.frame, self.fullFrameStatus)
        assert dc.cameraDataWidget.updateFullFrameData.call_count == 0

    def test_updateRoiFrameData(self, qtbot, mocker):
        cdw = CameraDataWidget()
        qtbot.addWidget(cdw)
        dc = DataController(cdw)
        mockCameraDataWidgetReset = mocker.patch.object(cdw, 'reset')
        mockBufferModelUpdateInfo = mocker.patch.object(dc.bufferModel, 'updateInformation')
        dc.roiFrameModel.calculateCentroid = mocker.Mock(return_value=GenericFrameInformation(self.timestamp,
                                                                                              242.3,
                                                                                              286.2,
                                                                                              2519.534,
                                                                                              104.343,
                                                                                              11.963,
                                                                                              50,
                                                                                              1.532))

        dc.passFrame(self.frame, self.roiFrameStatus)
        assert mockCameraDataWidgetReset.call_count == 1
        assert mockBufferModelUpdateInfo.call_count == 1
        dc.passFrame(self.frame, self.roiFrameStatus)
        assert mockCameraDataWidgetReset.call_count == 1
        assert mockBufferModelUpdateInfo.call_count == 2

    def test_getBufferSize(self, qtbot):
        cdw = CameraDataWidget()
        qtbot.addWidget(cdw)
        dc = DataController(cdw)
        bufferSize = dc.getBufferSize()
        assert bufferSize == 1024

    def test_getCentroids(self, qtbot, mocker):
        cdw = CameraDataWidget()
        qtbot.addWidget(cdw)
        dc = DataController(cdw)
        truth_centroids = (241.542, 346.931)
        centroids = dc.getCentroids(False)
        assert centroids == (None, None)
        dc.bufferModel.getCentroids = mocker.Mock(return_value=truth_centroids)
        centroids = dc.getCentroids(True)
        assert centroids == truth_centroids

    def test_getPsd(self, qtbot, mocker):
        cdw = CameraDataWidget()
        qtbot.addWidget(cdw)
        dc = DataController(cdw)
        currentFps = 40
        psd = dc.getPsd(False, currentFps)
        assert psd == (None, None, None)
        dc.bufferModel.rollBuffer = True
        truth_psd = (np.random.random(3), np.random.random(3), np.random.random(3))
        dc.bufferModel.getPsd = mocker.Mock(return_value=truth_psd)
        psd = dc.getPsd(True, currentFps)
        dc.bufferModel.getPsd.assert_called_with(currentFps)
        assert psd == truth_psd

    def test_setBufferSize(self, qtbot):
        cdw = CameraDataWidget()
        qtbot.addWidget(cdw)
        dc = DataController(cdw)
        truthBufferSize = 256
        dc.setBufferSize(truthBufferSize)
        assert dc.getBufferSize() == truthBufferSize

    def test_setFrameChecks(self, qtbot):
        cdw = CameraDataWidget()
        qtbot.addWidget(cdw)
        dc = DataController(cdw)
        dc.setFrameChecks(passFrame, passFrame)
        assert dc.fullFrameModel.frameCheck is not None
        assert dc.roiFrameModel.frameCheck is not None

    def test_noneFrame(self, qtbot, mocker):
        cdw = CameraDataWidget()
        qtbot.addWidget(cdw)
        dc = DataController(cdw)
        ffModel = mocker.patch.object(dc.fullFrameModel, "calculateCentroid")
        dc.passFrame(None, self.fullFrameStatus)
        assert ffModel.call_count == 0

    def test_getCentroidForUpdate(self, qtbot, mocker):
        cdw = CameraDataWidget()
        qtbot.addWidget(cdw)
        dc = DataController(cdw)
        truthInfo = GenericFrameInformation(self.timestamp, 300.3, 400.2, 32042.42, 145.422, 15.532, 70, None)
        dc.fullFrameModel.calculateCentroid = mocker.Mock(return_value=truthInfo)
        info = dc.getCentroidForUpdate(self.frame)
        assert info.centerX == truthInfo.centerX
        assert info.centerY == truthInfo.centerY

    def test_showRoiInformation(self, qtbot, mocker):
        cdw = CameraDataWidget()
        qtbot.addWidget(cdw)
        dc = DataController(cdw)
        mockCameraDataWidgetUpdateRoiInfo = mocker.patch.object(cdw, 'updateRoiFrameData')
        mockWriteTelemetryFile = mocker.patch.object(dc, 'writeTelemetryFile')
        roiInfo = RoiFrameInformation(242.5,
                                      286.3,
                                      2501.42,
                                      104.753,
                                      13.672,
                                      2.5432,
                                      2.2353,
                                      (1000, 25))
        dc.bufferModel.getInformation = mocker.Mock(return_value=roiInfo)

        dc.showRoiInformation(True, self.roiFrameStatus)
        assert mockCameraDataWidgetUpdateRoiInfo.call_count == 1
        mockCameraDataWidgetUpdateRoiInfo.assert_called_with(roiInfo)
        assert mockWriteTelemetryFile.call_count == 1
        mockWriteTelemetryFile.assert_called_with(roiInfo, self.roiFrameStatus)
        dc.showRoiInformation(False, self.roiFrameStatus)
        assert mockCameraDataWidgetUpdateRoiInfo.call_count == 1
        assert mockWriteTelemetryFile.call_count == 1
        mockWriteTelemetryFile.assert_called_once_with(roiInfo, self.roiFrameStatus)

    def test_getDataConfiguration(self, qtbot):
        cdw = CameraDataWidget()
        qtbot.addWidget(cdw)
        dc = DataController(cdw)
        currentConfig = dc.getDataConfiguration()
        truthConfig = DataConfig()
        assert currentConfig == truthConfig

    def test_setDataConfiguration(self, qtbot):
        cdw = CameraDataWidget()
        qtbot.addWidget(cdw)
        dc = DataController(cdw)

        truthConfig = DataConfig()
        truthConfig.buffer.pixelScale = 0.5
        truthConfig.fullFrame.sigmaScale = 1.753
        truthConfig.fullFrame.minimumNumPixels = 15
        truthConfig.roiFrame.thresholdFactor = 0.99
        dc.setDataConfiguration(truthConfig)
        assert dc.bufferModel.pixelScale == truthConfig.buffer.pixelScale
        assert dc.fullFrameModel.sigmaScale == truthConfig.fullFrame.sigmaScale
        assert dc.fullFrameModel.minimumNumPixels == truthConfig.fullFrame.minimumNumPixels
        assert dc.roiFrameModel.thresholdFactor == truthConfig.roiFrame.thresholdFactor

    @freeze_time('2018-10-30 22:30:15')
    def test_writingData(self, qtbot):
        cdw = CameraDataWidget()
        qtbot.addWidget(cdw)
        currentFps = 40
        dc = DataController(cdw)
        assert dc.cameraDataWidget.saveDataCheckBox.isChecked() is False
        assert dc.generalConfig.saveBufferData is False
        assert dc.filesCreated is False

        nonePsd = (None, None, None)

        dc.writeDataToFile(nonePsd, currentFps)
        assert dc.filesCreated is False

        qtbot.mouseClick(cdw.saveDataCheckBox, Qt.LeftButton)
        assert dc.generalConfig.saveBufferData is True

        dc.writeDataToFile(nonePsd, currentFps)
        assert dc.filesCreated is False

        # Setup buffer model
        dc.setBufferSize(4)
        dc.bufferModel.updateInformation(GenericFrameInformation(self.timestamp,
                                                                 300.3, 400.2,
                                                                 32042.42, 145.422, 14.836,
                                                                 70, None), (0, 0))
        dc.bufferModel.updateInformation(GenericFrameInformation(self.timestamp + self.deltaTime,
                                                                 300.4, 400.4,
                                                                 32045.42, 146.422, 15.836,
                                                                 70, None), (0, 0))
        dc.bufferModel.updateInformation(GenericFrameInformation(self.timestamp + self.deltaTime * 2,
                                                                 300.2, 400.5,
                                                                 32040.42, 142.422, 12.836,
                                                                 70, None), (0, 0))
        dc.bufferModel.updateInformation(GenericFrameInformation(self.timestamp + self.deltaTime * 3,
                                                                 300.1, 400.3,
                                                                 32043.42, 143.422, 13.836,
                                                                 70, None), (0, 0))
        assert dc.bufferModel.rollBuffer is True
        centroidOutputFile = 'smm_centroid_20181030_223015.h5'
        psdOutputFile = 'smm_psd_20181030_223015.h5'
        psdInfo = dc.bufferModel.getPsd(currentFps)
        dc.writeDataToFile(psdInfo, currentFps)
        assert dc.filesCreated is True
        assert dc.centroidFilename == centroidOutputFile
        assert dc.psdFilename == psdOutputFile
        assert os.path.exists(centroidOutputFile)
        assert os.path.exists(psdOutputFile)
        os.remove(centroidOutputFile)
        os.remove(psdOutputFile)

    @freeze_time('2018-10-30 22:30:15')
    def test_writeTelemetryFile(self, qtbot):
        cdw = CameraDataWidget()
        qtbot.addWidget(cdw)
        saveTelemetryDir = os.path.join(os.path.abspath(os.path.curdir), 'temp')
        telemetryOutputDir = 'dsm_telemetry'
        fullSaveDir = os.path.join(saveTelemetryDir, telemetryOutputDir)
        dc = DataController(cdw)
        dc.telemetrySavePath = saveTelemetryDir

        # Setup buffer model
        dc.setBufferSize(4)
        dc.bufferModel.updateInformation(GenericFrameInformation(self.timestamp,
                                                                 300.3, 400.2,
                                                                 32042.42, 145.422, 14.836,
                                                                 70, None), (0, 0))
        dc.bufferModel.updateInformation(GenericFrameInformation(self.timestamp + self.deltaTime,
                                                                 300.4, 400.4,
                                                                 32045.42, 146.422, 15.836,
                                                                 70, None), (0, 0))
        dc.bufferModel.updateInformation(GenericFrameInformation(self.timestamp + self.deltaTime * 2,
                                                                 300.2, 400.5,
                                                                 32040.42, 142.422, 12.836,
                                                                 70, None), (0, 0))
        dc.bufferModel.updateInformation(GenericFrameInformation(self.timestamp + self.deltaTime * 3,
                                                                 300.1, 400.3,
                                                                 32043.42, 143.422, 13.836,
                                                                 70, None), (0, 0))
        telemetryFile = 'dsm_20181030_223015.dat'
        configFile = 'dsm_ui_config.yaml'
        roiInfo = dc.bufferModel.getInformation(self.roiFrameStatus.currentFps)
        dc.writeTelemetryFile(roiInfo, self.roiFrameStatus)
        assert os.path.exists(fullSaveDir) is True
        assert os.path.exists(os.path.join(fullSaveDir, telemetryFile)) is True
        assert os.path.exists(os.path.join(fullSaveDir, configFile)) is True
        dc.cleanTelemetry()
        assert os.path.exists(os.path.join(fullSaveDir, telemetryFile)) is False
        assert os.path.exists(os.path.join(fullSaveDir, configFile)) is False
        assert os.path.exists(fullSaveDir) is False
        assert dc.telemetrySetup is False

    @freeze_time('2018-10-30 22:30:15')
    def test_noTelemetryDirCleanup(self, qtbot):
        cdw = CameraDataWidget()
        qtbot.addWidget(cdw)
        saveTelemetryDir = os.path.join(os.path.abspath(os.path.curdir), 'temp2')
        telemetryOutputDir = 'dsm_telemetry'
        fullSaveDir = os.path.join(saveTelemetryDir, telemetryOutputDir)
        dc = DataController(cdw)
        dc.telemetrySavePath = saveTelemetryDir
        dc.removeTelemetryDir = False

        # Setup buffer model
        dc.setBufferSize(4)
        dc.bufferModel.updateInformation(GenericFrameInformation(self.timestamp,
                                                                 300.3, 400.2,
                                                                 32042.42, 145.422, 14.836,
                                                                 70, None), (0, 0))
        dc.bufferModel.updateInformation(GenericFrameInformation(self.timestamp + self.deltaTime,
                                                                 300.4, 400.4,
                                                                 32045.42, 146.422, 15.836,
                                                                 70, None), (0, 0))
        dc.bufferModel.updateInformation(GenericFrameInformation(self.timestamp + self.deltaTime * 2,
                                                                 300.2, 400.5,
                                                                 32040.42, 142.422, 12.836,
                                                                 70, None), (0, 0))
        dc.bufferModel.updateInformation(GenericFrameInformation(self.timestamp + self.deltaTime * 3,
                                                                 300.1, 400.3,
                                                                 32043.42, 143.422, 13.836,
                                                                 70, None), (0, 0))

        telemetryFile = 'dsm_20181030_223015.dat'
        configFile = 'dsm_ui_config.yaml'
        roiInfo = dc.bufferModel.getInformation(self.roiFrameStatus.currentFps)
        dc.writeTelemetryFile(roiInfo, self.roiFrameStatus)
        assert os.path.exists(fullSaveDir) is True
        assert os.path.exists(os.path.join(fullSaveDir, telemetryFile)) is True
        assert os.path.exists(os.path.join(fullSaveDir, configFile)) is True
        dc.cleanTelemetry()
        assert os.path.exists(os.path.join(fullSaveDir, telemetryFile)) is False
        assert os.path.exists(os.path.join(fullSaveDir, configFile)) is False
        assert os.path.exists(fullSaveDir) is True
        assert dc.telemetrySetup is False
        os.removedirs(fullSaveDir)

    def test_handleAcquireRoiStateChange(self, qtbot, mocker):
        cdw = CameraDataWidget()
        qtbot.addWidget(cdw)
        dc = DataController(cdw)
        mockCleanTelemetry = mocker.patch.object(dc, 'cleanTelemetry')
        mockBufferModelReset = mocker.patch.object(dc.bufferModel, 'reset')
        dc.handleAcquireRoiStateChange(Qt.Unchecked)
        assert mockCleanTelemetry.call_count == 1
        assert mockBufferModelReset.call_count == 1

    def test_getGeneralConfiguration(self, qtbot):
        cdw = CameraDataWidget()
        qtbot.addWidget(cdw)
        dc = DataController(cdw)
        currentConfig = dc.getGeneralConfiguration()
        truthConfig = GeneralConfig()
        assert currentConfig == truthConfig

    def test_setGeneralConfiguration(self, qtbot):
        cdw = CameraDataWidget()
        qtbot.addWidget(cdw)
        dc = DataController(cdw)

        truthConfig = GeneralConfig()
        truthConfig.site = "Cerro Pachon"
        truthConfig.configVersion = "0.1.10"
        truthConfig.timezone = "TAI"
        dc.setGeneralConfiguration(truthConfig)
        assert dc.generalConfig == truthConfig
        assert dc.fullTelemetrySavePath == truthConfig.fullTelemetrySavePath
        assert dc.removeTelemetryDir == truthConfig.removeTelemetryDir
        assert dc.configVersion == truthConfig.configVersion
        assert dc.timeHandler.timezone == truthConfig.timezone
        assert dc.fullFrameModel.timeHandler.timezone == truthConfig.timezone
        assert dc.roiFrameModel.timeHandler.timezone == truthConfig.timezone

    def test_setCameraModelName(self, qtbot):
        cdw = CameraDataWidget()
        qtbot.addWidget(cdw)
        dc = DataController(cdw)

        modelName = "ProSilice GT-650"
        dc.setCameraModelName(modelName)
        assert dc.cameraModelName == modelName
