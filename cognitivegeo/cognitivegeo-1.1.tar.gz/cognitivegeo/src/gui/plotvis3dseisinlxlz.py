#############################################################################################
#                                                                                           #
# Author:   GeoPy Team                                                                      #
# Email:    geopy.info@gmail.com                                                            #
# Date:     November 2019                                                                   #
#                                                                                           #
#############################################################################################

# Create a window for plot seismic inline-crossline-z slices in 3D


from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
import sys, os
#
sys.path.append(os.path.dirname(__file__)[:-4][:-4][:-13])
from cognitivegeo.src.basic.data import data as basic_data
from cognitivegeo.src.core.settings import settings as core_set
from cognitivegeo.src.seismic.analysis import analysis as seis_ays
from cognitivegeo.src.seismic.visualization import visualization as seis_vis
from cognitivegeo.src.vis.colormap import colormap as vis_cmap
from cognitivegeo.src.gui.configplayer import configplayer as gui_configplayer
from cognitivegeo.src.vis.messager import messager as vis_msg

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class plotvis3dseisinlxlz(object):

    survinfo = {}
    seisdata = {}
    plotstyle = core_set.Visual['Image']
    fontstyle = core_set.Visual['Font']
    playerconfiginl = core_set.Viewer['Player']
    playerconfigxl = core_set.Viewer['Player']
    playerconfigz = core_set.Viewer['Player']
    viewerconfig = core_set.Viewer['Viewer3D']['ViewFrom']
    viewerconfig['Home'] = core_set.Viewer['Viewer3D']['GoHome']
    #
    iconpath = os.path.dirname(__file__)
    dialog = None
    vispyscene = None

    def setupGUI(self, PlotVis3DSeisInlXlZ):
        PlotVis3DSeisInlXlZ.setObjectName("PlotVis3DSeisInlXlZ")
        PlotVis3DSeisInlXlZ.setFixedSize(500, 490)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(os.path.join(self.iconpath, "icons/box.png")),
                       QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        PlotVis3DSeisInlXlZ.setWindowIcon(icon)
        #
        self.lwgattrib = QtWidgets.QListWidget(PlotVis3DSeisInlXlZ)
        self.lwgattrib.setObjectName("lwgattrib")
        self.lwgattrib.setGeometry(QtCore.QRect(10, 10, 230, 410))
        self.lwgattrib.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        #
        self.lblinlslice = QtWidgets.QLabel(PlotVis3DSeisInlXlZ)
        self.lblinlslice.setObjectName("lblinlslice")
        self.lblinlslice.setGeometry(QtCore.QRect(260, 50, 150, 30))
        self.slbinlslice = QtWidgets.QScrollBar(PlotVis3DSeisInlXlZ)
        self.slbinlslice.setObjectName("slbinlslice")
        self.slbinlslice.setOrientation(QtCore.Qt.Horizontal)
        self.slbinlslice.setGeometry(QtCore.QRect(290, 80, 140, 30))
        self.ldtinlslice = QtWidgets.QLineEdit(PlotVis3DSeisInlXlZ)
        self.ldtinlslice.setObjectName("ldtinlslice")
        self.ldtinlslice.setGeometry(QtCore.QRect(440, 80, 50, 30))
        self.ldtinlslice.setAlignment(QtCore.Qt.AlignCenter)
        self.cbxinlslice = QtWidgets.QCheckBox(PlotVis3DSeisInlXlZ)
        self.cbxinlslice.setObjectName("cbxinlslice")
        self.cbxinlslice.setGeometry(QtCore.QRect(260, 80, 30, 30))
        #
        self.lblxlslice = QtWidgets.QLabel(PlotVis3DSeisInlXlZ)
        self.lblxlslice.setObjectName("lblxlslice")
        self.lblxlslice.setGeometry(QtCore.QRect(260, 120, 150, 30))
        self.slbxlslice = QtWidgets.QScrollBar(PlotVis3DSeisInlXlZ)
        self.slbxlslice.setObjectName("slbxlslice")
        self.slbxlslice.setOrientation(QtCore.Qt.Horizontal)
        self.slbxlslice.setGeometry(QtCore.QRect(290, 150, 140, 30))
        self.ldtxlslice = QtWidgets.QLineEdit(PlotVis3DSeisInlXlZ)
        self.ldtxlslice.setObjectName("ldtxlslice")
        self.ldtxlslice.setGeometry(QtCore.QRect(440, 150, 50, 30))
        self.ldtxlslice.setAlignment(QtCore.Qt.AlignCenter)
        self.cbxxlslice = QtWidgets.QCheckBox(PlotVis3DSeisInlXlZ)
        self.cbxxlslice.setObjectName("cbxxlslice")
        self.cbxxlslice.setGeometry(QtCore.QRect(260, 150, 30, 30))
        #
        self.lblzslice = QtWidgets.QLabel(PlotVis3DSeisInlXlZ)
        self.lblzslice.setObjectName("lblzslice")
        self.lblzslice.setGeometry(QtCore.QRect(260, 190, 150, 30))
        self.slbzslice = QtWidgets.QScrollBar(PlotVis3DSeisInlXlZ)
        self.slbzslice.setObjectName("slbzslice")
        self.slbzslice.setOrientation(QtCore.Qt.Horizontal)
        self.slbzslice.setGeometry(QtCore.QRect(290, 220, 140, 30))
        self.ldtzslice = QtWidgets.QLineEdit(PlotVis3DSeisInlXlZ)
        self.ldtzslice.setObjectName("ldtzslice")
        self.ldtzslice.setGeometry(QtCore.QRect(440, 220, 50, 30))
        self.ldtzslice.setAlignment(QtCore.Qt.AlignCenter)
        self.cbxzslice = QtWidgets.QCheckBox(PlotVis3DSeisInlXlZ)
        self.cbxzslice.setObjectName("cbxzslice")
        self.cbxzslice.setGeometry(QtCore.QRect(260, 220, 30, 30))
        #
        self.lblcmap = QtWidgets.QLabel(PlotVis3DSeisInlXlZ)
        self.lblcmap.setObjectName("lblcmap")
        self.lblcmap.setGeometry(QtCore.QRect(260, 350, 60, 30))
        self.cbbcmap = QtWidgets.QComboBox(PlotVis3DSeisInlXlZ)
        self.cbbcmap.setObjectName("cbbcmap")
        self.cbbcmap.setGeometry(QtCore.QRect(320, 350, 120, 30))
        self.cbxflip = QtWidgets.QCheckBox(PlotVis3DSeisInlXlZ)
        self.cbxflip.setObjectName("cbxflip")
        self.cbxflip.setGeometry(QtCore.QRect(450, 350, 40, 30))
        #
        self.lblrange = QtWidgets.QLabel(PlotVis3DSeisInlXlZ)
        self.lblrange.setObjectName("lblrange")
        self.lblrange.setGeometry(QtCore.QRect(260, 270, 40, 30))
        self.ldtmin = QtWidgets.QLineEdit(PlotVis3DSeisInlXlZ)
        self.ldtmin.setObjectName("ldtmin")
        self.ldtmin.setGeometry(QtCore.QRect(300, 270, 70, 30))
        self.ldtmin.setAlignment(QtCore.Qt.AlignCenter)
        self.ldtmax = QtWidgets.QLineEdit(PlotVis3DSeisInlXlZ)
        self.ldtmax.setObjectName("ldtmax")
        self.ldtmax.setGeometry(QtCore.QRect(420, 270, 70, 30))
        self.ldtmax.setAlignment(QtCore.Qt.AlignCenter)
        self.lblrangeto = QtWidgets.QLabel(PlotVis3DSeisInlXlZ)
        self.lblrangeto.setObjectName("lblrangeto")
        self.lblrangeto.setGeometry(QtCore.QRect(370, 270, 50, 30))
        self.lblrangeto.setAlignment(QtCore.Qt.AlignCenter)
        #
        self.lblzscale = QtWidgets.QLabel(PlotVis3DSeisInlXlZ)
        self.lblzscale.setObjectName("lblzscale")
        self.lblzscale.setGeometry(QtCore.QRect(260, 390, 40, 30))
        self.ldtzscale = QtWidgets.QLineEdit(PlotVis3DSeisInlXlZ)
        self.ldtzscale.setObjectName("ldtzscale")
        self.ldtzscale.setGeometry(QtCore.QRect(300, 390, 50, 30))
        self.ldtzscale.setAlignment(QtCore.Qt.AlignCenter)
        #
        self.cbxsrvbox = QtWidgets.QCheckBox(PlotVis3DSeisInlXlZ)
        self.cbxsrvbox.setObjectName("cbxsrvbox")
        self.cbxsrvbox.setGeometry(QtCore.QRect(400, 390, 90, 30))

        #
        self.btnconfigplayer = QtWidgets.QPushButton(PlotVis3DSeisInlXlZ)
        self.btnconfigplayer.setObjectName("btnconfigplayer")
        self.btnconfigplayer.setGeometry(QtCore.QRect(390, 10, 100, 30))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(os.path.join(self.iconpath, "icons/video.png")),
                       QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        self.btnconfigplayer.setIcon(icon)
        #
        self.btnplotslice = QtWidgets.QPushButton(PlotVis3DSeisInlXlZ)
        self.btnplotslice.setObjectName("btnplotslice")
        self.btnplotslice.setGeometry(QtCore.QRect(170, 440, 160, 30))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(os.path.join(self.iconpath, "icons/box.png")),
                       QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        self.btnplotslice.setIcon(icon)
        #
        self.msgbox = QtWidgets.QMessageBox(PlotVis3DSeisInlXlZ)
        self.msgbox.setObjectName("msgbox")
        _center_x = PlotVis3DSeisInlXlZ.geometry().center().x()
        _center_y = PlotVis3DSeisInlXlZ.geometry().center().y()
        self.msgbox.setGeometry(QtCore.QRect(_center_x - 150, _center_y - 50, 300, 100))
        #
        self.retranslateGUI(PlotVis3DSeisInlXlZ)
        QtCore.QMetaObject.connectSlotsByName(PlotVis3DSeisInlXlZ)



    def retranslateGUI(self, PlotVis3DSeisInlXlZ):
        self.dialog = PlotVis3DSeisInlXlZ
        #
        _translate = QtCore.QCoreApplication.translate
        PlotVis3DSeisInlXlZ.setWindowTitle(_translate("PlotVis3DSeisInlXlZ", "3D Window: Seismic"))
        if self.checkSurvInfo() is True:
            _firstattrib = None
            for i in sorted(self.seisdata.keys()):
                if self.checkSeisData(i):
                    item = QtWidgets.QListWidgetItem(self.lwgattrib)
                    item.setText(_translate("PlotVis3DSeisInlXlZ", i))
                    self.lwgattrib.addItem(item)
                    if _firstattrib is None:
                        _firstattrib = item
            self.lwgattrib.setCurrentItem(_firstattrib)
        self.lwgattrib.itemSelectionChanged.connect(self.changeLwgAttrib)
        #
        self.lblinlslice.setText(_translate("PlotVis3DSeisInlXlZ", "@ inline:"))
        if (self.checkSurvInfo() is True):
            _slices = self.survinfo['ILRange'].astype(int)
            _slicemin = np.min(_slices)
            _slicemax = np.max(_slices)
        else:
            _slicemin = 0
            _slicemax = 0
        self.slbinlslice.setMinimum(_slicemin)
        self.slbinlslice.setMaximum(_slicemax)
        self.slbinlslice.setValue(_slicemin)
        if (self.checkSurvInfo() is True):
            self.ldtinlslice.setText(_translate("PlotVis3DSeisInlXlZ", str(_slicemin)))
        else:
            self.ldtinlslice.setText(_translate("PlotVis3DSeisInlXlZ", ''))
        self.slbinlslice.valueChanged.connect(self.changeSlbInlSlice)
        self.ldtinlslice.textChanged.connect(self.changeLdtInlSlice)
        self.cbxinlslice.setChecked(True)
        self.cbxinlslice.stateChanged.connect(self.changeCbxInlSlice)
        #
        self.lblxlslice.setText(_translate("PlotVis3DSeisInlXlZ", "@ crossline:"))
        if (self.checkSurvInfo() is True):
            _slices = self.survinfo['XLRange'].astype(int)
            _slicemin = np.min(_slices)
            _slicemax = np.max(_slices)
        else:
            _slicemin = 0
            _slicemax = 0
        self.slbxlslice.setMinimum(_slicemin)
        self.slbxlslice.setMaximum(_slicemax)
        self.slbxlslice.setValue(_slicemin)
        if (self.checkSurvInfo() is True):
            self.ldtxlslice.setText(_translate("PlotVis3DSeisInlXlZ", str(_slicemin)))
        else:
            self.ldtxlslice.setText(_translate("PlotVis3DSeisInlXlZ", ''))
        self.slbxlslice.valueChanged.connect(self.changeSlbXlSlice)
        self.ldtxlslice.textChanged.connect(self.changeLdtXlSlice)
        self.cbxxlslice.setChecked(True)
        self.cbxxlslice.stateChanged.connect(self.changeCbxXlSlice)
        #
        self.lblzslice.setText(_translate("PlotVis3DSeisInlXlZ", "@ time/depth:"))
        if (self.checkSurvInfo() is True):
            _slices = self.survinfo['ZRange'].astype(int)
            _slicemin = np.min(_slices)
            _slicemax = np.max(_slices)
        else:
            _slicemin = 0
            _slicemax = 0
        self.slbzslice.setMinimum(_slicemin)
        self.slbzslice.setMaximum(_slicemax)
        self.slbzslice.setValue(_slicemin)
        if (self.checkSurvInfo() is True):
            self.ldtzslice.setText(_translate("PlotVis3DSeisInlXlZ", str(_slicemin)))
        else:
            self.ldtzslice.setText(_translate("PlotVis3DSeisInlXlZ", ''))
        self.slbzslice.valueChanged.connect(self.changeSlbZSlice)
        self.ldtzslice.textChanged.connect(self.changeLdtZSlice)
        self.cbxzslice.setChecked(True)
        self.cbxzslice.stateChanged.connect(self.changeCbxZSlice)
        #
        self.lblcmap.setText(_translate("Plot2DXlSlice", "Color map:"))
        self.cbbcmap.addItems(vis_cmap.ColorMapList)
        for _i in range(len(vis_cmap.ColorMapList)):
            self.cbbcmap.setItemIcon(_i, QtGui.QIcon(
                QtGui.QPixmap(os.path.join(self.iconpath, "icons/cmap_" + vis_cmap.ColorMapList[_i] + ".png")).scaled(80, 30)))
        self.cbbcmap.setCurrentIndex(list.index(vis_cmap.ColorMapList, self.plotstyle['Colormap']))
        #
        self.cbxflip.setText(_translate("PlotVis3DSeisInlXlZ", ""))
        self.cbxflip.setIcon(QtGui.QIcon(
            QtGui.QPixmap(os.path.join(self.iconpath, "icons/flip.png")).scaled(80, 80)))
        #
        self.lblrange.setText(_translate("PlotVis3DSeisInlXlZ", "Range:"))
        self.lblrangeto.setText(_translate("PlotVis3DSeisInlXlZ", "~~~"))
        if (self.checkSurvInfo() is True) \
                and (self.lwgattrib.currentItem() is not None) \
                and (self.checkSeisData(self.lwgattrib.currentItem().text()) is True):
            _min, _max = self.getAttribRange(self.lwgattrib.currentItem().text())
            self.ldtmin.setText(_translate("PlotVis3DSeisInlXlZ", str(_min)))
            self.ldtmax.setText(_translate("PlotVis3DSeisInlXlZ", str(_max)))
        #
        self.lblzscale.setText(_translate("PlotVis3DSeisInlXlZ", "Z-scale:"))
        self.ldtzscale.setText(_translate("PlotVis3DSeisInlXlZ", '1.0'))
        #
        self.cbxsrvbox.setText(_translate("PlotVis3DSeisInlXlZ", "Survey box"))
        self.cbxsrvbox.setChecked(True)
        #
        self.btnconfigplayer.setText(_translate("PlotVis3DSeisInlXlZ", "Slice Player"))
        self.btnconfigplayer.clicked.connect(self.clickBtnConfigPlayer)
        #
        self.btnplotslice.setText(_translate("PlotVis3DSeisInlXlZ", "3D Seismic Viewer"))
        self.btnplotslice.setDefault(True)
        self.btnplotslice.clicked.connect(self.clickBtnPlotSlice)

        self.dialog.show()


    def changeLwgAttrib(self):
        if len(self.lwgattrib.selectedItems()) > 0:
            # if len(self.lwgattrib.selectedItems()) > 1:
            #     self.ldtmin.setEnabled(False)
            #     self.ldtmax.setEnabled(False)
            # else:
            #     self.ldtmin.setEnabled(True)
            #     self.ldtmax.setEnabled(True)
            _slices = self.survinfo['ILRange'].astype(int)
            _slicemin = np.min(_slices)
            _slicemax = np.max(_slices)
            self.slbinlslice.setMinimum(_slicemin)
            self.slbinlslice.setMaximum(_slicemax)
            self.ldtinlslice.setText(str(self.slbinlslice.value()))
            #
            _slices = self.survinfo['XLRange'].astype(int)
            _slicemin = np.min(_slices)
            _slicemax = np.max(_slices)
            self.slbxlslice.setMinimum(_slicemin)
            self.slbxlslice.setMaximum(_slicemax)
            self.ldtxlslice.setText(str(self.slbxlslice.value()))
            #
            _slices = self.survinfo['ZRange'].astype(int)
            _slicemin = np.min(_slices)
            _slicemax = np.max(_slices)
            self.slbzslice.setMinimum(_slicemin)
            self.slbzslice.setMaximum(_slicemax)
            self.ldtzslice.setText(str(self.slbzslice.value()))
            #
            _min, _max = self.getAttribRange(self.lwgattrib.currentItem().text())
            self.ldtmin.setText(str(_min))
            self.ldtmax.setText(str(_max))
        else:
            self.slbinlslice.setMinimum(0)
            self.slbinlslice.setMaximum(0)
            self.ldtinlslice.setText('')
            #
            self.slbxlslice.setMinimum(0)
            self.slbxlslice.setMaximum(0)
            self.ldtxlslice.setText('')
            #
            self.slbzslice.setMinimum(0)
            self.slbzslice.setMaximum(0)
            self.ldtzslice.setText('')
            #
            self.ldtmin.setText('')
            self.ldtmax.setText('')


    def changeSlbInlSlice(self):
        self.ldtinlslice.setText(str(self.slbinlslice.value()))


    def changeLdtInlSlice(self):
        if len(self.ldtinlslice.text()) > 0:
            _val = basic_data.str2int(self.ldtinlslice.text())
            if _val >= self.slbinlslice.minimum() and _val <= self.slbinlslice.maximum():
                self.slbinlslice.setValue(_val)


    def changeCbxInlSlice(self):
        if self.cbxinlslice.isChecked():
            self.ldtinlslice.setEnabled(True)
            self.slbinlslice.setEnabled(True)
        else:
            self.ldtinlslice.setEnabled(False)
            self.slbinlslice.setEnabled(False)
    
    
    def changeSlbXlSlice(self):
        self.ldtxlslice.setText(str(self.slbxlslice.value()))


    def changeLdtXlSlice(self):
        if len(self.ldtxlslice.text()) > 0:
            _val = basic_data.str2int(self.ldtxlslice.text())
            if _val >= self.slbxlslice.minimum() and _val <= self.slbxlslice.maximum():
                self.slbxlslice.setValue(_val)


    def changeCbxXlSlice(self):
        if self.cbxxlslice.isChecked():
            self.ldtxlslice.setEnabled(True)
            self.slbxlslice.setEnabled(True)
        else:
            self.ldtxlslice.setEnabled(False)
            self.slbxlslice.setEnabled(False)
    
    
    def changeSlbZSlice(self):
        self.ldtzslice.setText(str(self.slbzslice.value()))


    def changeLdtZSlice(self):
        if len(self.ldtzslice.text()) > 0:
            _val = basic_data.str2int(self.ldtzslice.text())
            if _val >= self.slbzslice.minimum() and _val <= self.slbzslice.maximum():
                self.slbzslice.setValue(_val)


    def changeCbxZSlice(self):
        if self.cbxzslice.isChecked():
            self.ldtzslice.setEnabled(True)
            self.slbzslice.setEnabled(True)
        else:
            self.ldtzslice.setEnabled(False)
            self.slbzslice.setEnabled(False)


    def clickBtnConfigPlayer(self):
        _config = QtWidgets.QDialog()
        _gui = gui_configplayer()
        _gui.playerconfig = {}
        _gui.playerconfig['Inline'] = self.playerconfiginl
        _gui.playerconfig['Crossline'] = self.playerconfigxl
        _gui.playerconfig['Time/depth'] = self.playerconfigz
        _gui.setupGUI(_config)
        _config.exec()
        self.playerconfiginl = _gui.playerconfig['Inline']
        self.playerconfigxl = _gui.playerconfig['Crossline']
        self.playerconfigz = _gui.playerconfig['Time/depth']
        _config.show()


    def clickBtnPlotSlice(self):
        self.refreshMsgBox()
        #
        _attriblist = self.lwgattrib.selectedItems()
        if len(_attriblist) < 1:
            vis_msg.print("ERROR in PlotVis3DSeisInlXlZ: No property selected for plot", type='error')
            QtWidgets.QMessageBox.critical(self.msgbox,
                                           '3D Window: Seismic',
                                           'No property selected for plot')
            return
        #
        _inlsls = None
        if self.cbxinlslice.isChecked():
            _inlsls = self.slbinlslice.value()
        _xlsls = None
        if self.cbxxlslice.isChecked():
            _xlsls = self.slbxlslice.value()
        _zsls = None
        if self.cbxzslice.isChecked():
            _zsls = self.slbzslice.value()
        #
        _cmap = self.cbbcmap.currentIndex()
        _flip = self.cbxflip.isChecked()
        _min = basic_data.str2float(self.ldtmin.text())
        _max = basic_data.str2float(self.ldtmax.text())
        if _min is False or _max is False:
            vis_msg.print("ERROR in PlotVis3DSeisInlXlZ: Non-float range specified for plot", type='error')
            QtWidgets.QMessageBox.critical(self.msgbox,
                                           '3D Window: Seismic',
                                           'Non-float range specified for plot')
            return

        _zscale = basic_data.str2float(self.ldtzscale.text())
        if _zsls is False or _zscale <= 0.0:
            vis_msg.print("ERROR in PlotVis3DSeisInlXlZ: z-scale > 0.0 required", type='error')
            QtWidgets.QMessageBox.critical(self.msgbox,
                                           '3D Window: Seismic',
                                           'z-scale > 0.0 required')
            return
        #
        _srvbox = self.cbxsrvbox.isChecked()
        #
        for i in range(len(_attriblist)):
            print("PlotVis3DSeisInlXlZ: Plot %d of %d properties: %s" % (i + 1, len(_attriblist), _attriblist[i].text()))
            _data = self.seisdata[_attriblist[i].text()]
            seis_vis.plotSeisILXLZSlicePlayerFrom3DMat(_data, seisinfo=self.survinfo,
                                                       initinlsl=_inlsls, initxlsl=_xlsls, initzsl=_zsls,
                                                       valuemax=_max, valuemin=_min, zscale=_zscale,
                                                       colormap=vis_cmap.ColorMapList[_cmap], flipcmap=_flip,
                                                       surveyboxon=_srvbox,
                                                       interpolation=self.plotstyle['Interpolation'].lower(),
                                                       viewerconfig=self.viewerconfig,
                                                       playerconfiginl=self.playerconfiginl,
                                                       playerconfigxl=self.playerconfigxl,
                                                       playerconfigz=self.playerconfigz,
                                                       qicon=QtGui.QIcon(os.path.join(self.iconpath, "icons/logo.png")),
                                                       )
        #
        # QtWidgets.QMessageBox.information(self.msgbox,
        #                                   "Plot Inline",
        #                                   str(len(_attriblist)) + " properties plotted successfully")
        # self.dialog.close()
        return


    def getAttribRange(self, f):
        _min = -1
        _max = 1
        if (self.checkSurvInfo() is True) \
                and (f in self.seisdata.keys()) \
                and (self.checkSeisData(f) is True):
            _min = np.min(self.seisdata[f])
            _max = np.max(self.seisdata[f])
        return _min, _max


    def refreshMsgBox(self):
        _center_x = self.dialog.geometry().center().x()
        _center_y = self.dialog.geometry().center().y()
        self.msgbox.setGeometry(QtCore.QRect(_center_x - 150, _center_y - 50, 300, 100))


    def checkSurvInfo(self):
        self.refreshMsgBox()
        #
        if seis_ays.checkSeisInfo(self.survinfo) is False:
            # print("PlotVis3DSeisInlXlZ: Survey not found")
            # QtWidgets.QMessageBox.critical(self.msgbox,
            #                                'Plot Seismic Inline',
            #                                'Survey not found')
            return False
        return True


    def checkSeisData(self, f):
        self.refreshMsgBox()
        #
        return seis_ays.isSeis3DMatConsistentWithSeisInfo(self.seisdata[f], self.survinfo)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    PlotVis3DSeisInlXlZ = QtWidgets.QWidget()
    gui = plotvis3dseisinlxlz()
    gui.setupGUI(PlotVis3DSeisInlXlZ)
    PlotVis3DSeisInlXlZ.show()
    sys.exit(app.exec_())