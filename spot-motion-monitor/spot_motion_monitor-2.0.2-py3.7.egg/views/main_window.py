# This file is part of spot_motion_monitor.
#
# Developed for LSST System Integration, Test and Commissioning.
#
# See the LICENSE file at the top-level directory of this distribution
# for details of code ownership.
#
# Use of this source code is governed by a 3-clause BSD-style
# license that can be found in the LICENSE file.

import cProfile
from datetime import datetime
import os
import sys

from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets

from spot_motion_monitor.controller.camera_controller import CameraController
from spot_motion_monitor.controller.data_controller import DataController
from spot_motion_monitor.controller.plot_ccd_controller import PlotCcdController
from spot_motion_monitor.controller.plot_centroid_controller import PlotCentroidController
from spot_motion_monitor.controller.plot_psd_controller import PlotPsdController
from spot_motion_monitor.utils import create_parser, CSS, DEFAULT_PSD_ARRAY_SIZE, readYamlFile, writeYamlFile
import spot_motion_monitor.utils.constants as consts
from spot_motion_monitor.views import CameraConfigurationDialog
from spot_motion_monitor.views import DataConfigurationDialog
from . import CameraInformationDialog
from . import GeneralConfigurationDialog
from spot_motion_monitor.views import PlotConfigurationDialog
from spot_motion_monitor.views.forms import Ui_MainWindow
from spot_motion_monitor import __version__, APP_COPYRIGHT

__all__ = ['main']

class SpotMotionMonitor(QtWidgets.QMainWindow, Ui_MainWindow):

    """This is the main application class.

    Attributes
    ----------
    cameraActionGroup : QtWidgets.QActionGroup
        Allows the camera menu entries to be exclusive.
    cameraController : .CameraController
        An instance of the camera controller.
    dataController : .DataController
        An instance of the data controller.
    plotCentroidController : .PlotCentroidController
        An instance of the centroid (scatter and histograms) plot controller.
    plotController : .PlotCcdController
        An instance of the plot controller.
    plotPsdController : .PlotPsdController
        An instance of the Power Spectrum Distribution plot controller.
    """

    def __init__(self, parent=None):
        """Initialize the class.

        Parameters
        ----------
        parent : None, optional
            Top-level widget.
        """
        super().__init__(parent)
        self.cameraSwitched = False
        self.setupUi(self)
        self.setWindowTitle("Spot Motion Monitor")
        self.getProgramSettings()

        self.plotController = PlotCcdController(self.cameraPlot)
        self.cameraController = CameraController(self.cameraControl)
        self.dataController = DataController(self.cameraData)
        self.plotCentroidController = PlotCentroidController(self.centroidXPlot,
                                                             self.centroidYPlot,
                                                             self.scatterPlot)
        self.plotPsdController = PlotPsdController(self.psdWaterfallXPlot,
                                                   self.psdWaterfallYPlot,
                                                   self.psd1dXPlot,
                                                   self.psd1dYPlot)

        self.setupCameraMenu()

        self.setActionIcon(self.actionExit, "exit.svg", True)
        self.setActionIcon(self.actionSaveConfiguration, "filesave.svg", True)
        self.setActionIcon(self.actionOpenConfiguration, "folder_open.svg", True)
        self.actionOpenConfiguration.setShortcut(QtGui.QKeySequence.Open)
        self.actionSaveConfiguration.setShortcut(QtGui.QKeySequence.Save)
        self.actionExit.setShortcut(QtGui.QKeySequence.Quit)

        self.cameraController.frameTimer.timeout.connect(self.acquireFrame)
        self.cameraController.offsetTimer.timeout.connect(self.updateOffset)
        self.cameraController.updater.displayStatus.connect(self.updateStatusBar)
        self.cameraController.updater.bufferSizeChanged.connect(self.handleBufferSizeChanged)
        self.cameraController.updater.roiFpsChanged.connect(self.handleRoiFpsChanged)
        self.cameraController.updater.cameraState.connect(self.updateApplicationForCameraState)
        self.cameraController.updater.acquireRoiState.connect(self.dataController.handleAcquireRoiStateChange)
        ccUpdArs = self.cameraController.updater.acquireRoiState.connect
        ccUpdArs(self.plotCentroidController.handleAcquireRoiStateChange)
        ccUpdArs(self.plotPsdController.handleAcquireRoiStateChange)
        self.plotController.updater.displayStatus.connect(self.updateStatusBar)
        self.dataController.updater.displayStatus.connect(self.updateStatusBar)
        self.actionExit.triggered.connect(self.close)
        self.actionAbout.triggered.connect(self.about)
        self.actionPlotsConfig.triggered.connect(self.updatePlotConfiguration)
        self.actionCameraConfig.triggered.connect(self.updateCameraConfiguration)
        self.actionDataConfig.triggered.connect(self.updateDataConfiguration)
        self.actionGeneralConfig.triggered.connect(self.updateGeneralConfiguration)
        self.actionSaveConfiguration.triggered.connect(self.saveConfiguration)
        self.actionOpenConfiguration.triggered.connect(self.openConfiguration)
        self.actionCameraInfo.triggered.connect(self.showCameraInformation)

    def _configOverrideWarning(self):
        """Show a configuration override warning message.
        """
        settings = QtCore.QSettings()
        value = settings.value("suppressOverrideWarning")
        if value is None:
            suppressOverrideWarning = False
        else:
            suppressOverrideWarning = value
        if not suppressOverrideWarning:
            buttons = QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No
            message = ["Opening a configuration file will override any "
                       "parameters brought in from the command line ",
                       "at program launch if those parameters are ",
                       "in the configuration file.",
                       "",
                       "To suppress this warning for future openings, "
                       "click \"Yes\". Clicking \"No\" will mean this ",
                       "message will be shown again when opening a ",
                       "configuration file."]

            answer = QtWidgets.QMessageBox.warning(self,
                                                   "Configuration Parameter Override Warning",
                                                   os.linesep.join(message),
                                                   buttons)
            if answer == QtWidgets.QMessageBox.Yes:
                saveSuppressWarning = True
            else:
                saveSuppressWarning = False
            settings.setValue("suppressOverrideWarning", saveSuppressWarning)

    def _openFileDialog(self):
        """Open the file opening dialog.

        Returns
        -------
        str
            The selected file, empty string if nothing selected.
        """
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(caption="Open Configuration File",
                                                            directory=os.path.expanduser("~/"),
                                                            filter="Config Files (*.yaml *.yml)",
                                                            options=QtWidgets.QFileDialog.DontUseNativeDialog)
        return fileName

    def _saveFileDialog(self):
        """Open the save file dialog.

        Returns
        -------
        str
            The selected file, empty string if nothing selected.
        """
        fileName, _ = QtWidgets.QFileDialog.getSaveFileName(caption="Save Configuration File",
                                                            directory=os.path.join(os.path.expanduser("~/"),
                                                                                   "configuration.yaml"),
                                                            filter="Config Files (*.yaml *.yml)",
                                                            options=QtWidgets.QFileDialog.DontUseNativeDialog)
        return fileName

    def about(self):
        """This function presents the about dialog box.
        """
        about = QtWidgets.QMessageBox()
        about.setIconPixmap(QtGui.QPixmap(":smm_logo_sm.png"))
        about.setWindowTitle("About the Spot Motion Monitor")
        about.setStandardButtons(QtWidgets.QMessageBox.Ok)
        about.setInformativeText('''
                                 <b>Spot Motion Monitor</b> v{}
                                 <p>
                                 This application is the front-end for a system that
                                 monitors seeing within a telescope dome.
                                 </p>
                                 <br><br>
                                 {}
                                 '''.format(__version__, APP_COPYRIGHT))
        about.exec_()

    def acquireFrame(self):
        """Handle a camera CCD frame.
        """
        frame = self.cameraController.getFrame()
        cameraStatus = self.cameraController.currentStatus()
        self.dataController.passFrame(frame, cameraStatus)
        self.plotController.passFrame(frame, cameraStatus.showFrames)
        centroids = self.dataController.getCentroids(cameraStatus.isRoiMode)
        self.plotCentroidController.update(centroids[0], centroids[1])
        psdData = self.dataController.getPsd(cameraStatus.isRoiMode, cameraStatus.currentFps)
        bufferReady = psdData[0] is not None
        self.plotCentroidController.showScatterPlots(bufferReady)
        self.cameraController.showFrameStatus(bufferReady)
        self.dataController.showRoiInformation(bufferReady, cameraStatus)
        self.plotPsdController.update(psdData[0], psdData[1], psdData[2])
        self.dataController.writeDataToFile(psdData, cameraStatus.currentFps)

    def autoRunIfNecessary(self):
        """Start the program in ROI mode if requested.
        """
        self.cameraController.autoRun()

    def closeEvent(self, event):
        """Handle saving settings on shutdown.

        Parameters
        ----------
        event : QtCore.QEvent
            The close event instance.
        """
        settings = QtCore.QSettings()
        currentCamera = self.cameraActionGroup.checkedAction()
        if currentCamera is not None:
            cameraName = currentCamera.objectName()
            cameraValue = QtCore.QVariant(cameraName)
        else:
            cameraValue = QtCore.QVariant()
        settings.setValue('LastCamera', cameraValue)

        self.cameraController.shutdownCamera()

    def getProgramSettings(self):
        """Retrieve program settings.
        """
        settings = QtCore.QSettings()
        self.lastCamera = str(settings.value('LastCamera'))

    def getSaveConfigurationMask(self):
        """Create mask for saving configuration information.

        Returns
        -------
        int
            The mask for saving configuration.
        """
        write_plot = int(self.actionWritePlotConfig.isChecked()) * consts.SaveConfigMask.PLOT
        write_empty = int(self.actionWriteEmptyConfig.isChecked()) * consts.SaveConfigMask.EMPTY
        return write_plot | write_empty

    def handleBufferSizeChanged(self, newBufferSize):
        """Update the necessary controllers when the buffer size changes.

        Parameters
        ----------
        newBufferSize : int
            The new buffer size.
        """
        self.dataController.setBufferSize(newBufferSize)
        self.plotCentroidController.updateBufferSize(newBufferSize)

    def handleCameraSelection(self, checked):
        """Respond to a choice from the camera menu.

        Parameters
        ----------
        checked : bool
            If the current camera is selected.
        """
        name = self.sender().objectName()
        self.cameraController.setupCamera(name)
        self.dataController.setFrameChecks(*self.cameraController.getFrameChecks())
        bufferSize = self.dataController.getBufferSize()
        roiFps = self.cameraController.currentRoiFps()
        if self.cameraSwitched:
            self.plotCentroidController.updateBufferSize(bufferSize)
            self.plotCentroidController.updateRoiFps(roiFps)
        else:
            self.plotCentroidController.setup(bufferSize, roiFps)
            self.cameraSwitched = True
        self.plotPsdController.setup(DEFAULT_PSD_ARRAY_SIZE, bufferSize / roiFps)

    def handleConfig(self, options):
        """Call controller configuration functions.

        Parameters
        ----------
        options : Namespace
            The options from command-line arguments.
        """
        self.setConfiguration(options.config_file, options)

    def handleRoiFpsChanged(self, newRoiFps):
        """Update the necessary controllers when the ROI FPS changes.

        Parameters
        ----------
        newRoiFps : int
            The new ROI FPS.
        """
        self.plotCentroidController.updateRoiFps(newRoiFps)
        bufferSize = self.dataController.getBufferSize()
        self.plotPsdController.updateTimeScale(bufferSize / newRoiFps)

    def openConfiguration(self):
        """Open a configuration file and apply it.
        """
        self._configOverrideWarning()
        openFile = self._openFileDialog()
        if openFile == '':
            return
        self.setConfiguration(openFile)

    def saveConfiguration(self):
        """Save the configuration from the program.
        """
        saveFile = self._saveFileDialog()
        if saveFile == '':
            return
        saveMask = self.getSaveConfigurationMask()
        writeEmpty = saveMask & consts.SaveConfigMask.EMPTY
        generalConf = self.dataController.getGeneralConfiguration()
        generalConf.autorun = self.cameraController.doAutoRun
        cameraConf = {"camera": self.cameraController.getCameraConfiguration().toDict(writeEmpty)}
        dataConf = {"data": self.dataController.getDataConfiguration().toDict()}
        if (saveMask & consts.SaveConfigMask.PLOT):
            plotConfig = {"plot":
                          {"centroid": self.plotCentroidController.getPlotConfiguration().toDict(writeEmpty),
                           "psd": self.plotPsdController.getPlotConfiguration().toDict(writeEmpty)}}
        else:
            plotConfig = {}
        config = {**generalConf.toDict(writeEmpty), **cameraConf, **dataConf, **plotConfig}
        writeYamlFile(saveFile, config)

    def setActionIcon(self, action, iconName, iconInMenu=False):
        """Setup the icon for the given action.

        Parameters
        ----------
        action : QAction
          A specific program action.
        iconName : str
          Name of the icon in the QRC file.
        iconInMenu : bool, optional
          Make the icon visible in the program menu.
        """
        action.setIcon(QtGui.QIcon(QtGui.QPixmap(':{}'.format(iconName))))
        action.setIconVisibleInMenu(iconInMenu)

    def setConfiguration(self, inputFile, options=None):
        """Get the configuration from file and optionally CLI.

        Parameters
        ----------
        inputFile : str
            Configuration YAML file.
        options : Namespace, optional
            Command line options.
        """
        config = readYamlFile(inputFile)

        generalConf = self.dataController.getGeneralConfiguration()
        dataConf = self.dataController.getDataConfiguration()
        cameraConf = self.cameraController.getCameraConfiguration()
        centroidPlotConf = self.plotCentroidController.getPlotConfiguration()
        psdPlotConf = self.plotPsdController.getPlotConfiguration()

        if config is not None:
            generalConf.fromDict(config)
            dataConf.fromDict(config["data"])
            try:
                cameraConf.fromDict(config["camera"])
            except KeyError:
                pass
            try:
                centroidPlotConf.fromDict(config["plot"]["centroid"])
                psdPlotConf.fromDict(config["plot"]["psd"])
                plotConfPresent = True
            except KeyError:
                plotConfPresent = False
        else:
            plotConfPresent = False

        self.cameraController.doAutoRun = generalConf.autorun
        if inputFile is not None:
            generalConf.configFile = inputFile

        if options is not None:
            generalConf.autorun = generalConf.autorun | options.auto_run
            self.cameraController.doAutoRun = generalConf.autorun
            if options.telemetry_dir is not None:
                dataConf.fullTelemetrySavePath = os.path.expanduser(options.telemetry_dir)
            if options.vimba_camera_index is not None:
                cameraConf.cameraIndex = options.vimba_camera_index

        self.dataController.setGeneralConfiguration(generalConf)
        self.dataController.setDataConfiguration(dataConf)
        self.cameraController.bufferSize(dataConf.buffer.bufferSize, updateWidget=True)

        self.cameraController.setCameraConfiguration(cameraConf)
        self.cameraController.updateRoiFps(cameraConf.fpsRoiFrame)

        if plotConfPresent:
            self.plotCentroidController.setPlotConfiguration(centroidPlotConf)
            self.plotPsdController.setPlotConfiguration(psdPlotConf)

    def setupCameraMenu(self):
        """Add the available cameras to the menu.
        """
        cameraList = self.cameraController.getAvailableCameras()
        self.cameraActionGroup = QtWidgets.QActionGroup(self)
        index = 0
        for i, cameraName in enumerate(cameraList):
            if cameraName == 'Gaussian':
                index = i
            cameraAction = QtWidgets.QAction(cameraName, self)
            self.cameraActionGroup.addAction(cameraAction)
            cameraAction.setObjectName('{}Camera'.format(cameraName))
            cameraAction.triggered.connect(self.handleCameraSelection)
            cameraAction.setCheckable(True)
            self.menuCamera.addAction(cameraAction)
        action = None
        if self.lastCamera != 'None':
            for menuAction in self.menuCamera.actions():
                if menuAction.objectName() == self.lastCamera:
                    action = menuAction
                    break
        else:
            # Setup the Gaussian camera.
            action = self.menuCamera.actions()[index]
        action.setChecked(True)
        action.trigger()

    def showCameraInformation(self):
        """Show the current camera information.
        """
        dialog = CameraInformationDialog()
        cameraInfo = self.cameraController.getCameraInformation()
        dialog.setCameraInformation(cameraInfo)
        dialog.exec_()

    def updateApplicationForCameraState(self, state):
        """Update any application UI elements based on camera state.

        Parameters
        ----------
        state : bool
            True is camera is started, False is stopped.
        """
        self.menuCamera.setEnabled(not state)
        self.actionCameraConfig.setEnabled(not state)
        self.actionCameraInfo.setEnabled(state)
        if state:
            self.dataController.setCameraModelName(self.cameraController.getCameraModelName())

    def updateCameraConfiguration(self):
        """This function handles camera configuration.

        The camera configuration dialog is shown when the menu action is
        triggered. If dialog is accepted (OK button pressed), then the
        configuration is read from the tab and applied to the current via the
        camera controller.
        """
        currentCamera = self.cameraActionGroup.checkedAction()
        if currentCamera is None:
            return
        cameraName = currentCamera.objectName()
        cameraConfigDialog = CameraConfigurationDialog(cameraName)
        currentConfig = self.cameraController.getCameraConfiguration()
        cameraConfigDialog.setCameraConfiguration(currentConfig)
        if cameraConfigDialog.exec_():
            config = cameraConfigDialog.getCameraConfiguration()
            self.cameraController.setCameraConfiguration(config)
            self.dataController.setCameraModelName(config.modelName)

    def updateDataConfiguration(self):
        """This function handles data configuration.

        The configuration is centered on the data structures used for the
        calculations.
        """
        dataConfigDialog = DataConfigurationDialog()
        currentDataConfig = self.dataController.getDataConfiguration()
        dataConfigDialog.setConfiguration(currentDataConfig)
        if dataConfigDialog.exec_():
            newDataConfig = dataConfigDialog.getConfiguration()
            self.dataController.setDataConfiguration(newDataConfig)

    def updateGeneralConfiguration(self):
        """This function handle general configuration.
        """
        generalConfigDialog = GeneralConfigurationDialog(self)
        currentGeneralConfig = self.dataController.getGeneralConfiguration()
        currentGeneralConfig.autorun = self.cameraController.doAutoRun
        generalConfigDialog.setConfiguration(currentGeneralConfig)
        if generalConfigDialog.exec_():
            newGeneralConfig = generalConfigDialog.getConfiguration()
            self.dataController.setGeneralConfiguration(newGeneralConfig)
            self.cameraController.doAutoRun = newGeneralConfig.autorun

    def updateOffset(self):
        """This function updates the camera offsets.
        """
        frame = self.cameraController.getUpdateFrame()
        info = self.dataController.getCentroidForUpdate(frame)
        self.cameraController.updateCameraOffset(info.centerX, info.centerY)

    def updatePlotConfiguration(self):
        """This function handles plot configuration.

        The plot configuration dialog is shown when the menu action is
        triggered. If dialog is accepted (OK button pressed), then the
        configuration is read from the tabs and applied to the plots via the
        respective controllers.
        """
        plotConfigDialog = PlotConfigurationDialog()
        plotConfigDialog.setMinimumSize(300, 500)
        currentCentroidConfig = self.plotCentroidController.getPlotConfiguration()
        currentPsdConfig = self.plotPsdController.getPlotConfiguration()
        plotConfigDialog.setPlotConfiguration(currentCentroidConfig, currentPsdConfig)
        if plotConfigDialog.exec_():
            newCentroidConfig, newPsdConfig = plotConfigDialog.getPlotConfiguration()
            self.plotCentroidController.setPlotConfiguration(newCentroidConfig)
            self.plotPsdController.setPlotConfiguration(newPsdConfig)

    def updateStatusBar(self, message, timeout):
        """This function updates the application status bar.

        Parameters
        ----------
        message : str
            The text to display in the status bar.
        timeout : int
            The time (in milliseconds) for the text to remain visible.
        """
        self.statusbar.showMessage(message, timeout)


def launch(opts):
    """This creates the application and launches the program.

    Parameters
    ----------
    opts : Namespace
        The parsed command-line options.
    """
    app = QtWidgets.QApplication(sys.argv)
    app.setOrganizationName("LSST-Systems-Engineering")
    app.setOrganizationDomain("lsst.org")
    app.setApplicationName("Spot Motion Monitor")
    app.setStyleSheet(CSS)
    form = SpotMotionMonitor()
    form.handleConfig(opts)
    form.show()
    form.autoRunIfNecessary()
    app.exec_()


def main():
    """This is the entrance point of the program.
    """
    parser = create_parser()
    args = parser.parse_args()
    if args.profile:
        profileFile = 'smm_prof_{}.dat'.format(datetime.now().strftime('%Y%m%d_%H%M%S'))
        cProfile.runctx('launch(args)', {'launch': launch, 'args': args}, {}, filename=profileFile)
    else:
        launch(args)
