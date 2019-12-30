#############################################################################################
#                                                                                           #
# Author:   GeoPy Team                                                                      #
# Email:    geopy.info@gmail.com                                                            #
# Date:     November 2019                                                                   #
#                                                                                           #
#############################################################################################

# Create a GUI for canvas

from PyQt5 import QtCore, QtGui, QtWidgets
import os, sys
import numpy as np
import vispy.io as vispy_io
from vispy import scene
from vispy.color import Colormap
from functools import partial
#
sys.path.append(os.path.dirname(__file__)[:-4][:-4][:-13])
from cognitivegeo.src.basic.data import data as basic_data
from cognitivegeo.src.core.settings import settings as core_set
from cognitivegeo.src.seismic.analysis import analysis as seis_ays
from cognitivegeo.src.vis.colormap import colormap as vis_cmap
from cognitivegeo.src.gui.configseisvis import configseisvis as gui_configseisvis
from cognitivegeo.src.vis.messager import messager as vis_msg

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

class plotviscanvas(object):

    survinfo = {}
    seisdata = {}
    pointdata = {}
    settings = core_set.Settings
    #
    iconpath = os.path.dirname(__file__)
    dialog = None
    #
    canvas = None
    view = None
    canvasproperties = {}
    canvascomponents = {}
    seisvisconfig = {}


    def setupGUI(self, PlotVisCanvas):
        PlotVisCanvas.setObjectName("PlotVisCanvas")
        PlotVisCanvas.setFixedSize(1400, 960)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(os.path.join(self.iconpath, "icons/canvas.png")),
                       QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        PlotVisCanvas.setWindowIcon(icon)
        #
        # seismic
        self.lblseis = QtWidgets.QLabel(PlotVisCanvas)
        self.lblseis.setObjectName("lblseis")
        self.lblseis.setGeometry(QtCore.QRect(10, 10, 50, 30))
        # config seismic
        self.btnconfigseisvis = QtWidgets.QPushButton(PlotVisCanvas)
        self.btnconfigseisvis.setObjectName("btnconfigseisvis")
        self.btnconfigseisvis.setGeometry(QtCore.QRect(60, 10, 30, 30))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(os.path.join(self.iconpath, "icons/settings.png")),
                       QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        self.btnconfigseisvis.setIcon(icon)
        # seismic list
        self.cbblistseis = QtWidgets.QComboBox(PlotVisCanvas)
        self.cbblistseis.setObjectName("cbblistseis")
        self.cbblistseis.setGeometry(QtCore.QRect(10, 50, 240, 30))
        # add to canvas
        self.btnaddseis2canvas = QtWidgets.QPushButton(PlotVisCanvas)
        self.btnaddseis2canvas.setObjectName("btnaddseis2canvas")
        self.btnaddseis2canvas.setGeometry(QtCore.QRect(260, 50, 30, 30))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(os.path.join(self.iconpath, "icons/add.png")),
                       QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        self.btnaddseis2canvas.setIcon(icon)
        # seismic on canvas
        self.twgseisoncanvas = QtWidgets.QTableWidget(PlotVisCanvas)
        self.twgseisoncanvas.setObjectName("twgseisoncanvas")
        self.twgseisoncanvas.setGeometry(QtCore.QRect(10, 90, 280, 300))
        self.twgseisoncanvas.setColumnCount(5)
        self.twgseisoncanvas.setRowCount(0)
        self.twgseisoncanvas.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.twgseisoncanvas.horizontalHeader().hide()
        self.twgseisoncanvas.verticalHeader().hide()
        self.twgseisoncanvas.setColumnWidth(0, 18)
        self.twgseisoncanvas.setColumnWidth(1, 108)
        self.twgseisoncanvas.setColumnWidth(2, 60)
        self.twgseisoncanvas.setColumnWidth(3, 60)
        self.twgseisoncanvas.setColumnWidth(4, 30)
        #
        # main canvas
        self.wgtcanvas = QtWidgets.QWidget(PlotVisCanvas)
        self.wgtcanvas.setObjectName("wdtcanvas")
        self.wgtcanvas.setGeometry(QtCore.QRect(300, 50, 1050, 900))
        #
        # survey box
        self.btnsrvbox = QtWidgets.QPushButton(PlotVisCanvas)
        self.btnsrvbox.setObjectName("btnsrvbox")
        self.btnsrvbox.setGeometry(QtCore.QRect(1360, 50, 30, 30))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(os.path.join(self.iconpath, "icons/box.png")),
                       QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        self.btnsrvbox.setIcon(icon)
        #
        # xyz axis
        self.btnxyzaxis = QtWidgets.QPushButton(PlotVisCanvas)
        self.btnxyzaxis.setObjectName("btnxyzaxis")
        self.btnxyzaxis.setGeometry(QtCore.QRect(1360, 90, 30, 30))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(os.path.join(self.iconpath, "icons/xyz.png")),
                       QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        self.btnxyzaxis.setIcon(icon)
        #
        # snapshot
        self.btnsnapshot = QtWidgets.QPushButton(PlotVisCanvas)
        self.btnsnapshot.setObjectName("btnsnapshot")
        self.btnsnapshot.setGeometry(QtCore.QRect(1360, 130, 30, 30))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(os.path.join(self.iconpath, "icons/camera.png")),
                       QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        self.btnsnapshot.setIcon(icon)
        #
        # home
        self.btngohome = QtWidgets.QPushButton(PlotVisCanvas)
        self.btngohome.setObjectName("btngohome")
        self.btngohome.setGeometry(QtCore.QRect(300, 10, 30, 30))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(os.path.join(self.iconpath, "icons/home.png")),
                       QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        self.btngohome.setIcon(icon)
        #
        # view angle
        self.cbbviewfrom = QtWidgets.QComboBox(PlotVisCanvas)
        self.cbbviewfrom.setObjectName("cbbviewfrom")
        self.cbbviewfrom.setGeometry(QtCore.QRect(340, 10, 90, 30))
        #
        # z scale
        self.ldtzscale = QtWidgets.QLineEdit(PlotVisCanvas)
        self.ldtzscale.setObjectName("ldtzscale")
        self.ldtzscale.setGeometry(QtCore.QRect(440, 10, 60, 30))
        self.ldtzscale.setAlignment(QtCore.Qt.AlignCenter)
        #
        self.msgbox = QtWidgets.QMessageBox(PlotVisCanvas)
        self.msgbox.setObjectName("msgbox")
        _center_x = PlotVisCanvas.geometry().center().x()
        _center_y = PlotVisCanvas.geometry().center().y()
        self.msgbox.setGeometry(QtCore.QRect(_center_x - 150, _center_y - 50, 300, 100))
        #
        self.retranslateGUI(PlotVisCanvas)
        QtCore.QMetaObject.connectSlotsByName(PlotVisCanvas)


    def retranslateGUI(self, PlotVisCanvas):
        self.dialog = PlotVisCanvas
        #
        _translate = QtCore.QCoreApplication.translate
        PlotVisCanvas.setWindowTitle(_translate("PlotVisCanvas", "Canvas"))
        #
        # seismic
        self.lblseis.setText(_translate("PlotVisCanvas", "Seismic:"))
        # seismic configuration
        self.btnconfigseisvis.setText(_translate("PlotVisCanvas", ""))
        self.btnconfigseisvis.clicked.connect(self.clickBtnConfigSeisVis)
        # seismic list
        self.cbblistseis.addItems(list(self.seisdata.keys()))
        # add seismic to canvas
        self.btnaddseis2canvas.setText(_translate("PlotVisCanvas", ""))
        self.btnaddseis2canvas.setToolTip("Add to canvas")
        self.btnaddseis2canvas.clicked.connect(self.clickBtnAddSeis2Canvas)
        # seismic on canvas
        # self.twgseisoncanvas.currentCellChanged.connect(self.changeTwgSeisOnCanvas)
        #
        # main canvas
        self.canvas = scene.SceneCanvas(keys='interactive', title='Canvas', bgcolor=[0.5, 0.5, 0.5],
                                        size=(1080, 920), app='pyqt5', parent=self.wgtcanvas)
        self.view = self.canvas.central_widget.add_view()
        self.view.camera = scene.TurntableCamera(elevation=30, azimuth=135)
        #
        # survey box
        self.btnsrvbox.setText(_translate("PlotVisCanvas", ""))
        self.btnsrvbox.setToolTip("Survey box")
        self.btnsrvbox.setDefault(False)
        self.btnsrvbox.clicked.connect(self.clickBtnSrvBox)
        #
        # xyz axis
        self.btnxyzaxis.setText(_translate("PlotVisCanvas", ""))
        self.btnxyzaxis.setToolTip("XYZ axis")
        self.btnxyzaxis.setDefault(False)
        self.btnxyzaxis.clicked.connect(self.clickBtnXYZAxis)
        #
        # snapshot
        self.btnsnapshot.setText(_translate("PlotVisCanvas", ""))
        self.btnsnapshot.setToolTip("Snapshot")
        self.btnsnapshot.setDefault(False)
        self.btnsnapshot.clicked.connect(self.clickBtnSnapshot)
        #
        # home
        self.btngohome.setText(_translate("PlotVisCanvas", ""))
        self.btngohome.setDefault(True)
        self.btngohome.setToolTip("Home view")
        self.btngohome.clicked.connect(self.clickBtnGoHome)
        #
        # view angle
        self.cbbviewfrom.addItems(['Inline', 'Crossline', 'Top'])
        self.cbbviewfrom.setItemIcon(0, QtGui.QIcon(
                QtGui.QPixmap(os.path.join(self.iconpath, "icons/visinl.png")).scaled(30, 30)))
        self.cbbviewfrom.setItemIcon(1, QtGui.QIcon(
            QtGui.QPixmap(os.path.join(self.iconpath, "icons/visxl.png")).scaled(30, 30)))
        self.cbbviewfrom.setItemIcon(2, QtGui.QIcon(
            QtGui.QPixmap(os.path.join(self.iconpath, "icons/visz.png")).scaled(30, 30)))
        self.cbbviewfrom.setCurrentIndex(0)
        self.cbbviewfrom.currentIndexChanged.connect(self.changeCbbViewFrom)
        #
        # z scale
        self.ldtzscale.setText(_translate("PlotVisCanvas", "1.0"))
        self.ldtzscale.textChanged.connect(self.changeLdtZScale)
        #
        self.initSeisVis()
        self.initCanvas()


    def initSeisVis(self):
        self.seisvisconfig = {}
        if len(self.seisdata.keys()) > 0:
            for seis in self.seisdata.keys():
                if self.checkSeisData(seis):
                    self.seisvisconfig[seis] = {}
                    self.seisvisconfig[seis]['Colormap'] = self.settings['Visual']['Image']['Colormap']
                    self.seisvisconfig[seis]['Flip'] = False
                    self.seisvisconfig[seis]['Opacity'] = '100%'
                    self.seisvisconfig[seis]['Interpolation'] = self.settings['Visual']['Image']['Interpolation']
                    self.seisvisconfig[seis]['Maximum'] = np.max(self.seisdata[seis])
                    self.seisvisconfig[seis]['Minimum'] = np.min(self.seisdata[seis])


    def initCanvas(self):
        #
        # components and properties
        self.canvasproperties['Seismic'] = []
        self.canvascomponents['Seismic'] = []
        self.canvasproperties['Survey_Box'] = False
        self.canvascomponents['Survey_Box'] = []
        self.canvasproperties['XYZ_Axis'] = False
        self.canvascomponents['XYZ_Axis'] = None
        self.canvasproperties['Z_Scale'] = 1.0
        #
        # add survey box
        self.canvascomponents['Survey_Box'] = self.createSrvBox()
        if len(self.canvascomponents['Survey_Box']) == 12:
            for _i in self.canvascomponents['Survey_Box']:
                _i.parent = self.view.scene
            self.canvasproperties['Survey_Box'] = True
        #
        # add xyz axis
        self.canvascomponents['XYZ_Axis'] = self.createXYZAxis()
        if self.canvascomponents['XYZ_Axis'] is not None:
            self.canvascomponents['XYZ_Axis'].parent = self.view.scene
            self.canvasproperties['XYZ_Axis'] = True
        #
        # z scale
        _zscale = basic_data.str2float(self.ldtzscale.text())
        if _zscale is not False and _zscale > 0.0:
            self.canvasproperties['Z_Scale'] = _zscale
        #
        # set camara range
        self.setCameraRange()
        #
        self.canvas.show()


    def clickBtnConfigSeisVis(self):
        _config = QtWidgets.QDialog()
        _gui = gui_configseisvis()
        _gui.seisvisconfig = self.seisvisconfig
        _gui.setupGUI(_config)
        _config.exec()
        self.seisvisconfig = _gui.seisvisconfig
        _config.show()
        #
        # update seismic
        for _i in range(len(self.canvascomponents['Seismic'])):
            self.canvascomponents['Seismic'][_i].parent = None
            _vis = self.createVisualSeis(self.canvasproperties['Seismic'][_i]['Name'],
                                         self.canvasproperties['Seismic'][_i]['Orientation'],
                                         self.canvasproperties['Seismic'][_i]['Number'])
            if self.canvasproperties['Seismic'][_i]['Visible']:
                _vis.parent = self.view.scene
            self.canvascomponents['Seismic'][_i] = _vis


    def clickBtnAddSeis2Canvas(self):
        if len(self.seisdata.keys()) > 0 and \
                self.checkSeisData(list(self.seisdata.keys())[self.cbblistseis.currentIndex()]):
            ##### property
            _seis = {}
            _seis['Visible'] = False
            _seis['Name'] = list(self.seisdata.keys())[self.cbblistseis.currentIndex()]
            _seis['Orientation'] = 'Inline'
            _seis['Number'] = self.survinfo['ILStart']
            _seis['Remove'] = False
            #
            self.canvasproperties['Seismic'].append(_seis)
            #
            _nseis = len(self.canvasproperties['Seismic'])
            # add one more row
            self.twgseisoncanvas.setRowCount(_nseis)
            # visible
            _item = QtWidgets.QCheckBox()
            _item.setChecked(_seis['Visible'])
            _item.stateChanged.connect(partial(self.changeCbxVisSeisOnCanvas, idx=_nseis - 1))
            self.twgseisoncanvas.setCellWidget(_nseis - 1, 0, _item)
            # name
            _item = QtWidgets.QTableWidgetItem()
            _item.setText(_seis['Name'])
            _item.setTextAlignment(QtCore.Qt.AlignCenter)
            _item.setFlags(QtCore.Qt.ItemIsEditable)
            self.twgseisoncanvas.setItem(_nseis - 1, 1, _item)
            # orientation
            _item = QtWidgets.QComboBox()
            _item.addItems(['Inline', 'Xline', 'Z'])
            _item.setCurrentIndex(list.index(['Inline', 'Crossline', 'Z'], _seis['Orientation']))
            _item.currentIndexChanged.connect(partial(self.changeCbbOrtSeisOnCanvas, idx=_nseis - 1))
            self.twgseisoncanvas.setCellWidget(_nseis - 1, 2, _item)
            # number
            _item = QtWidgets.QComboBox()
            _slices = []
            if _seis['Orientation'] == 'Inline':
                _slices = [str(_no) for _no in self.survinfo['ILRange']]
            if _seis['Orientation'] == 'Crossline':
                _slices = [str(_no) for _no in self.survinfo['XLRange']]
            if _seis['Orientation'] == 'Z':
                _slices = [str(_no) for _no in self.survinfo['ZRange']]
            _item.addItems(_slices)
            _item.setCurrentIndex(list.index(_slices, str(_seis['Number'])))
            _item.currentIndexChanged.connect(partial(self.changeCbbNoSeisOnCanvas, idx=_nseis - 1))
            self.twgseisoncanvas.setCellWidget(_nseis - 1, 3, _item)
            # remove
            _item = QtWidgets.QPushButton()
            _icon = QtGui.QIcon()
            _icon.addPixmap(QtGui.QPixmap(os.path.join(self.iconpath, "icons/no.png")),
                            QtGui.QIcon.Normal,
                            QtGui.QIcon.Off)
            _item.setIcon(_icon)
            _item.clicked.connect(partial(self.clickBtnRmSeisOnCanvas, idx=_nseis - 1))
            self.twgseisoncanvas.setCellWidget(_nseis - 1, 4, _item)
            #
            ### component
            _vis = self.createVisualSeis(_seis['Name'], _seis['Orientation'], _seis['Number'])
            if _seis['Visible']:
                _vis.parent = self.view.scene
            self.canvascomponents['Seismic'].append(_vis)


    def changeCbxVisSeisOnCanvas(self, idx):
        if idx < len(self.canvasproperties['Seismic']):
           self.canvasproperties['Seismic'][idx]['Visible'] = self.twgseisoncanvas.cellWidget(idx, 0).isChecked()
           #
           if self.twgseisoncanvas.cellWidget(idx, 0).isChecked():
               self.canvascomponents['Seismic'][idx].parent = self.view.scene
           else:
               self.canvascomponents['Seismic'][idx].parent = None
           #
           # print(idx)
           # print(self.canvasproperties['Seismic'][idx])


    def changeCbbOrtSeisOnCanvas(self, idx):
        if idx < len(self.canvasproperties['Seismic']):
            self.twgseisoncanvas.cellWidget(idx, 3).clear()
            _ort = ""
            _no = 0
            if self.twgseisoncanvas.cellWidget(idx, 2).currentIndex() == 0:
                self.twgseisoncanvas.cellWidget(idx, 3).addItems([str(_no) for _no in self.survinfo['ILRange']])
                self.twgseisoncanvas.cellWidget(idx, 3).setCurrentIndex(0)
                _ort = 'Inline'
                _no = self.survinfo['ILRange'][0]
            if self.twgseisoncanvas.cellWidget(idx, 2).currentIndex() == 1:
                self.twgseisoncanvas.cellWidget(idx, 3).addItems([str(_no) for _no in self.survinfo['XLRange']])
                self.twgseisoncanvas.cellWidget(idx, 3).setCurrentIndex(0)
                _ort = 'Crossline'
                _no = self.survinfo['XLRange'][0]
            if self.twgseisoncanvas.cellWidget(idx, 2).currentIndex() == 2:
                self.twgseisoncanvas.cellWidget(idx, 3).addItems([str(_no) for _no in self.survinfo['ZRange']])
                self.twgseisoncanvas.cellWidget(idx, 3).setCurrentIndex(0)
                _ort = 'Z'
                _no = self.survinfo['ZRange'][0]
            #
            self.canvasproperties['Seismic'][idx]['Orientation'] = _ort
            self.canvasproperties['Seismic'][idx]['Number'] = _no
            #
            self.canvascomponents['Seismic'][idx].parent = None
            _vis = self.createVisualSeis(self.canvasproperties['Seismic'][idx]['Name'], _ort, _no)
            if self.canvasproperties['Seismic'][idx]['Visible']:
                _vis.parent = self.view.scene
            self.canvascomponents['Seismic'][idx] = _vis


    def changeCbbNoSeisOnCanvas(self, idx):
        if idx < len(self.canvasproperties['Seismic']):
            _no = 0
            _ort = ''
            if self.twgseisoncanvas.cellWidget(idx, 2).currentIndex() == 0:
                _ort = 'Inline'
                _no = self.survinfo['ILRange'][self.twgseisoncanvas.cellWidget(idx, 3).currentIndex()]
            if self.twgseisoncanvas.cellWidget(idx, 2).currentIndex() == 1:
                _ort = 'Crossline'
                _no = self.survinfo['XLRange'][self.twgseisoncanvas.cellWidget(idx, 3).currentIndex()]
            if self.twgseisoncanvas.cellWidget(idx, 2).currentIndex() == 2:
                _ort = 'Z'
                _no = self.survinfo['ZRange'][self.twgseisoncanvas.cellWidget(idx, 3).currentIndex()]
            #
            self.canvasproperties['Seismic'][idx]['Number'] = _no
            #
            self.canvascomponents['Seismic'][idx].parent = None
            _vis = self.createVisualSeis(self.canvasproperties['Seismic'][idx]['Name'], _ort, _no)
            if self.canvasproperties['Seismic'][idx]['Visible']:
                _vis.parent = self.view.scene
            self.canvascomponents['Seismic'][idx] = _vis


    def clickBtnRmSeisOnCanvas(self, idx):
        if idx < len(self.canvasproperties['Seismic']):
            self.twgseisoncanvas.clear()
            self.canvasproperties['Seismic'].pop(idx)
            self.canvascomponents['Seismic'][idx].parent = None
            self.canvascomponents['Seismic'].pop(idx)
            self.updateTwgSeisOnCanvas()


    def updateTwgSeisOnCanvas(self):
        self.twgseisoncanvas.clear()
        #
        _seis = self.canvasproperties['Seismic']
        #
        self.twgseisoncanvas.setRowCount(len(_seis))
        for _i in range(len(_seis)):
            # visible
            _item = QtWidgets.QCheckBox()
            _item.setChecked(_seis[_i]['Visible'])
            _item.stateChanged.connect(partial(self.changeCbxVisSeisOnCanvas, idx=_i))
            self.twgseisoncanvas.setCellWidget(_i, 0, _item)
            # name
            _item = QtWidgets.QTableWidgetItem()
            _item.setText(_seis[_i]['Name'])
            _item.setTextAlignment(QtCore.Qt.AlignCenter)
            _item.setFlags(QtCore.Qt.ItemIsEditable)
            self.twgseisoncanvas.setItem(_i, 1, _item)
            # orientation
            _item = QtWidgets.QComboBox()
            _item.addItems(['Inline', 'Xline', 'Z'])
            _item.setCurrentIndex(list.index(['Inline', 'Crossline', 'Z'], _seis[_i]['Orientation']))
            _item.currentIndexChanged.connect(partial(self.changeCbbOrtSeisOnCanvas, idx=_i))
            self.twgseisoncanvas.setCellWidget(_i, 2, _item)
            # number
            _item = QtWidgets.QComboBox()
            _slices = []
            if _seis[_i]['Orientation'] == 'Inline':
                _slices = [str(_no) for _no in self.survinfo['ILRange']]
            if _seis[_i]['Orientation'] == 'Crossline':
                _slices = [str(_no) for _no in self.survinfo['XLRange']]
            if _seis[_i]['Orientation'] == 'Z':
                _slices = [str(_no) for _no in self.survinfo['ZRange']]
            _item.addItems(_slices)
            _item.setCurrentIndex(list.index(_slices, str(_seis[_i]['Number'])))
            _item.currentIndexChanged.connect(partial(self.changeCbbNoSeisOnCanvas, idx=_i))
            self.twgseisoncanvas.setCellWidget(_i, 3, _item)
            # remove
            _item = QtWidgets.QPushButton()
            _icon = QtGui.QIcon()
            _icon.addPixmap(QtGui.QPixmap(os.path.join(self.iconpath, "icons/no.png")),
                            QtGui.QIcon.Normal,
                            QtGui.QIcon.Off)
            _item.setIcon(_icon)
            _item.clicked.connect(partial(self.clickBtnRmSeisOnCanvas, idx=_i))
            self.twgseisoncanvas.setCellWidget(_i, 4, _item)


    def clickBtnSrvBox(self):
        if len(self.canvascomponents['Survey_Box']) == 12:
            if self.canvasproperties['Survey_Box'] is True:
                for _i in self.canvascomponents['Survey_Box']:
                    _i.parent = None
                self.canvasproperties['Survey_Box'] = False
            else:
                for _i in self.canvascomponents['Survey_Box']:
                    _i.parent = self.view.scene
                self.canvasproperties['Survey_Box'] = True


    def clickBtnXYZAxis(self):
        if self.canvascomponents['XYZ_Axis'] is not None:
            if self.canvasproperties['XYZ_Axis'] is True:
                self.canvascomponents['XYZ_Axis'].parent = None
                self.canvasproperties['XYZ_Axis'] = False
            else:
                self.canvascomponents['XYZ_Axis'].parent = self.view.scene
                self.canvasproperties['XYZ_Axis'] = True


    def clickBtnSnapshot(self):
        res = self.canvas.render()[:, :, 0:3]
        #
        _dialog = QtWidgets.QFileDialog()
        _file = _dialog.getSaveFileName(None, 'Save canvas', self.settings['General']['RootPath'],
                                        filter="Portable Network Graphic file (PNG) (*.PNG);;All files (*.*)")
        if len(_file[0]) > 0:
            vispy_io.write_png(_file[0], res)


    def clickBtnGoHome(self):
        self.setCameraRange()
        self.view.camera.elevation = 30
        self.view.camera.azimuth = 135


    def changeCbbViewFrom(self):
        if self.cbbviewfrom.currentIndex() == 0:
            self.view.camera.elevation = 0
            self.view.camera.azimuth = 0
        if self.cbbviewfrom.currentIndex() == 1:
            self.view.camera.elevation = 0
            self.view.camera.azimuth = 90
        if self.cbbviewfrom.currentIndex() == 2:
            self.view.camera.elevation = 90
            self.view.camera.azimuth = 0


    def changeLdtZScale(self):
        #
        _zscale = basic_data.str2float(self.ldtzscale.text())
        if _zscale is not False and _zscale > 0.0:
            self.canvasproperties['Z_Scale'] = _zscale
        #
        # update seismic
        for _i in range(len(self.canvascomponents['Seismic'])):
            self.canvascomponents['Seismic'][_i].parent = None
            _vis = self.createVisualSeis(self.canvasproperties['Seismic'][_i]['Name'],
                                         self.canvasproperties['Seismic'][_i]['Orientation'],
                                         self.canvasproperties['Seismic'][_i]['Number'])
            if self.canvasproperties['Seismic'][_i]['Visible']:
                _vis.parent = self.view.scene
            self.canvascomponents['Seismic'][_i] = _vis
        #
        # update survey box
        _srvbox = self.createSrvBox()
        if len(_srvbox) == 12:
            # remove old one
            for _i in self.canvascomponents['Survey_Box']:
                _i.parent = None
            # plot new one
            self.canvascomponents['Survey_Box'] = _srvbox
            for _i in self.canvascomponents['Survey_Box']:
                _i.parent = self.view.scene
            self.canvasproperties['Survey_Box'] = True
        #
        # update xyz axis
        _xyzaxis = self.createXYZAxis()
        if _xyzaxis is not None:
            # remove old one
            self.canvascomponents['XYZ_Axis'].parent = None
            # plot new one
            self.canvascomponents['XYZ_Axis'] = _xyzaxis
            self.canvascomponents['XYZ_Axis'].parent = self.view.scene
            self.canvasproperties['XYZ_Axis'] = True
        #
        # set camara range
        self.setCameraRange()


    def refreshMsgBox(self):
        _center_x = self.dialog.geometry().center().x()
        _center_y = self.dialog.geometry().center().y()
        self.msgbox.setGeometry(QtCore.QRect(_center_x - 150, _center_y - 50, 300, 100))


    def createVisualSeis(self, seis, ort, no):
        if self.checkSurvInfo() is False:
            return None
        if seis not in self.seisdata.keys():
            return None
        if ort != 'Inline' and ort != 'Crossline' and ort != 'Z':
            return None
        #
        _xlstart = self.survinfo['XLStart']
        _xlend = self.survinfo['XLEnd']
        _zstart = self.survinfo['ZStart'] * self.canvasproperties['Z_Scale']
        _zend = self.survinfo['ZEnd'] * self.canvasproperties['Z_Scale']
        _inlstart = self.survinfo['ILStart']
        _inlend = self.survinfo['ILEnd']
        _inlstep = self.survinfo['ILStep']
        _inlnum = self.survinfo['ILNum']
        if _inlnum == 1:
            _inlstep = 1
        _xlstep = self.survinfo['XLStep']
        _xlnum = self.survinfo['XLNum']
        if _xlnum == 1:
            _xlstep = 1
        _zstep = self.survinfo['ZStep'] * self.canvasproperties['Z_Scale']
        _znum = self.survinfo['ZNum']
        if _znum == 1:
            _zstep = 1
        #
        if ort == 'Z':
            no = no * self.canvasproperties['Z_Scale']
        #
        if no < _inlstart and no > _inlend \
            and no < _xlstart and no > _xlend \
            and no > _zstart and no < _zend:
            return None
        #
        _data = np.zeros([2, 2])
        _cmp = vis_cmap.makeColorMap(cmapname=self.seisvisconfig[seis]['Colormap'],
                                     flip=self.seisvisconfig[seis]['Flip'],
                                     opacity=self.seisvisconfig[seis]['Opacity'])
        _cmp = Colormap(_cmp.colors)
        _interp = self.seisvisconfig[seis]['Interpolation'].lower()
        if _interp is None or _interp == 'None' or _interp == 'none':
            _interp = 'nearest'
        _vis = scene.visuals.Image(_data, parent=None, cmap=_cmp,
                                   clim=(self.seisvisconfig[seis]['Minimum'], self.seisvisconfig[seis]['Maximum']),
                                   interpolation=_interp)
        _tr = scene.transforms.MatrixTransform()
        if ort == 'Inline':
            _idx = np.round((no - _inlstart) / _inlstep).astype(np.int32)
            _data = self.seisdata[seis][:, :, _idx]
            _tr.scale((abs(_xlstep), abs(_zstep)))
            _tr.rotate(-90, (1, 0, 0))
            _tr.translate((_xlstart, no, _zstart))
            _tr.translate((-0.5 * _xlstep, 0, -0.5 * _zstep))
        if ort == 'Crossline':
            _idx = np.round((no - _xlstart) / _xlstep).astype(np.int32)
            _data = self.seisdata[seis][:, _idx, :]
            _tr.scale((abs(_inlstep), abs(_zstep)))
            _tr.rotate(-90, (1, 0, 0))
            _tr.rotate(90, (0, 0, 1))
            _tr.translate((no, _inlstart, _zstart))
            _tr.translate((0, -0.5*_inlstep, -0.5*_zstep))
        if ort == 'Z':
            _idx = np.round((no - _zstart) / _zstep).astype(np.int32)
            _data = self.seisdata[seis][_idx, :, :]
            _tr.scale((abs(_inlstep), abs(_xlstep)))
            _tr.rotate(90, (0, 0, 1))
            _tr.rotate(180, (0, 1, 0))
            _tr.translate((_xlstart, _inlstart, no))
            _tr.translate((-0.5*_xlstep, -0.5*_inlstep, 0))
        _vis.set_data(_data)
        _vis.transform = _tr
        #
        return _vis


    def createSrvBox(self):
        _srvlines = []
        if self.checkSurvInfo():
            _xlstart = self.survinfo['XLStart']
            _xlend = self.survinfo['XLEnd']
            _zstart = self.survinfo['ZStart'] * self.canvasproperties['Z_Scale']
            _zend = self.survinfo['ZEnd'] * self.canvasproperties['Z_Scale']
            _inlstart = self.survinfo['ILStart']
            _inlend = self.survinfo['ILEnd']
            _inlstep = self.survinfo['ILStep']
            _inlnum = self.survinfo['ILNum']
            if _inlnum == 1:
                _inlstep = 1
            _xlstep = self.survinfo['XLStep']
            _xlnum = self.survinfo['XLNum']
            if _xlnum == 1:
                _xlstep = 1
            _zstep = self.survinfo['ZStep'] * self.canvasproperties['Z_Scale']
            _znum = self.survinfo['ZNum']
            if _znum == 1:
                _zstep = 1
            #
            for p in ([_xlstart-0.5*_xlstep, _inlstart-0.5*_inlstep, _zend+0.5*_zstep, _xlend+0.5*_xlstep, _inlstart-0.5*_inlstep, _zend+0.5*_zstep],
                      [_xlstart-0.5*_xlstep, _inlstart-0.5*_inlstep, _zend+0.5*_zstep, _xlstart-0.5*_xlstep, _inlend+0.5*_inlstep, _zend+0.5*_zstep],
                      [_xlstart-0.5*_xlstep, _inlstart-0.5*_inlstep, _zend+0.5*_zstep, _xlstart-0.5*_xlstep, _inlstart-0.5*_inlstep, _zstart-0.5*_zstep],
                      [_xlstart-0.5*_xlstep, _inlend+0.5*_inlstep, _zstart-0.5*_zstep, _xlend+0.5*_xlstep, _inlend+0.5*_inlstep, _zstart-0.5*_zstep],
                      [_xlend+0.5*_xlstep, _inlstart-0.5*_inlstep, _zstart-0.5*_zstep, _xlend+0.5*_xlstep, _inlend+0.5*_inlstep, _zstart-0.5*_zstep],
                      [_xlend+0.5*_xlstep, _inlend+0.5*_inlstep, _zend+0.5*_zstep, _xlend+0.5*_xlstep, _inlend+0.5*_inlstep, _zstart-0.5*_zstep],
                      [_xlend+0.5*_xlstep, _inlstart-0.5*_inlstep, _zend+0.5*_zstep, _xlend+0.5*_xlstep, _inlend+0.5*_inlstep, _zend+0.5*_zstep],
                      [_xlstart-0.5*_xlstep, _inlend+0.5*_inlstep, _zend+0.5*_zstep, _xlend+0.5*_xlstep, _inlend+0.5*_inlstep, _zend+0.5*_zstep],
                      [_xlstart-0.5*_xlstep, _inlend+0.5*_inlstep, _zend+0.5*_zstep, _xlstart-0.5*_xlstep, _inlend+0.5*_inlstep, _zstart-0.5*_zstep],
                      [_xlstart-0.5*_xlstep, _inlstart-0.5*_inlstep, _zstart-0.5*_zstep, _xlstart-0.5*_xlstep, _inlend+0.5*_inlstep, _zstart-0.5*_zstep],
                      [_xlend+0.5*_xlstep, _inlstart-0.5*_inlstep, _zend+0.5*_zstep, _xlend+0.5*_xlstep, _inlstart-0.5*_inlstep, _zstart-0.5*_zstep],
                      [_xlstart-0.5*_xlstep, _inlstart-0.5*_inlstep, _zstart-0.5*_zstep, _xlend+0.5*_xlstep, _inlstart-0.5*_inlstep, _zstart-0.5*_zstep]):
                _line = scene.visuals.Line(pos=np.array([[p[0], p[1], p[2]], [p[3], p[4], p[5]]]),
                                           color='black', parent=None)
                _srvlines.append(_line)
        #
        return _srvlines


    def createXYZAxis(self):
        _xyz = None
        if self.checkSurvInfo():
            _xlstart = self.survinfo['XLStart']
            _xlend = self.survinfo['XLEnd']
            _zstart = self.survinfo['ZStart'] * self.canvasproperties['Z_Scale']
            _zend = self.survinfo['ZEnd'] * self.canvasproperties['Z_Scale']
            _inlstart = self.survinfo['ILStart']
            _inlend = self.survinfo['ILEnd']
            _inlstep = self.survinfo['ILStep']
            _inlnum = self.survinfo['ILNum']
            if _inlnum == 1:
                _inlstep = 1
            _xlstep = self.survinfo['XLStep']
            _xlnum = self.survinfo['XLNum']
            if _xlnum == 1:
                _xlstep = 1
            _zstep = self.survinfo['ZStep'] * self.canvasproperties['Z_Scale']
            _znum = self.survinfo['ZNum']
            if _znum == 1:
                _zstep = 1
            _x0 = 0.5 * (_xlstart + _xlend)  # _xlstart
            _y0 = 0.5 * (_inlstart + _inlend)  # _inlend + _inlend - _inlstart
            _z0 = 0.5 * (_zstart + _zend)  # _zend + _zend - _zstart
            _len = np.max(np.abs(np.array([_xlstep, _inlstep, _zstep])))
            _xyz = scene.visuals.XYZAxis(parent=None,
                                         pos=np.array([[_x0, _y0, _z0], [_x0 + _len, _y0, _z0],
                                                       [_x0, _y0, _z0], [_x0, _y0 + _len, _z0],
                                                       [_x0, _y0, _z0], [_x0, _y0, _z0 - _len]]))
        #
        return _xyz


    def setCameraRange(self):
        if self.checkSurvInfo():
            _xlstart = self.survinfo['XLStart']
            _xlend = self.survinfo['XLEnd']
            _zstart = self.survinfo['ZStart'] * self.canvasproperties['Z_Scale']
            _zend = self.survinfo['ZEnd'] * self.canvasproperties['Z_Scale']
            _inlstart = self.survinfo['ILStart']
            _inlend = self.survinfo['ILEnd']
            #
            self.view.camera.set_range((_xlstart, _xlend), (_inlstart, _inlend), (_zend, _zstart))


    def checkSurvInfo(self):
        self.refreshMsgBox()
        #
        if seis_ays.checkSeisInfo(self.survinfo) is False:
            return False
        return True


    def checkSeisData(self, f):
        self.refreshMsgBox()
        #
        return seis_ays.isSeis3DMatConsistentWithSeisInfo(self.seisdata[f], self.survinfo)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PlotVisCanvas = QtWidgets.QWidget()
    gui = plotviscanvas()
    gui.setupGUI(PlotVisCanvas)
    PlotVisCanvas.show()
    sys.exit(app.exec_())