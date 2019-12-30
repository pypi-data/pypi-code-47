#############################################################################################
#                                                                                           #
# Author:   GeoPy Team                                                                      #
# Email:    geopy.info@gmail.com                                                            #
# Date:     March 2018                                                                      #
#                                                                                           #
#############################################################################################

# Create a window for plot seismic time/depth slices


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


class plotvis2dseisz(object):

    survinfo = {}
    seisdata = {}
    plotstyle = core_set.Visual['Image']
    playerconfig = core_set.Viewer['Player']
    fontstyle = core_set.Visual['Font']
    #
    iconpath = os.path.dirname(__file__)
    dialog = None

    cmaps = vis_cmap.ColorMapList

    def setupGUI(self, PlotVis2DSeisZ):
        PlotVis2DSeisZ.setObjectName("PlotVis2DSeisZ")
        PlotVis2DSeisZ.setFixedSize(500, 320)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(os.path.join(self.iconpath, "icons/visz.png")),
                       QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        PlotVis2DSeisZ.setWindowIcon(icon)
        #
        self.lwgattrib = QtWidgets.QListWidget(PlotVis2DSeisZ)
        self.lwgattrib.setObjectName("lwgattrib")
        self.lwgattrib.setGeometry(QtCore.QRect(10, 10, 230, 240))
        self.lwgattrib.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        #
        self.lblslice = QtWidgets.QLabel(PlotVis2DSeisZ)
        self.lblslice.setObjectName("lblslice")
        self.lblslice.setGeometry(QtCore.QRect(260, 50, 150, 30))
        self.slbslice = QtWidgets.QScrollBar(PlotVis2DSeisZ)
        self.slbslice.setObjectName("slbslice")
        self.slbslice.setOrientation(QtCore.Qt.Horizontal)
        self.slbslice.setGeometry(QtCore.QRect(260, 80, 170, 30))
        self.ldtslice = QtWidgets.QLineEdit(PlotVis2DSeisZ)
        self.ldtslice.setObjectName("ldtslice")
        self.ldtslice.setGeometry(QtCore.QRect(440, 80, 50, 30))
        self.ldtslice.setAlignment(QtCore.Qt.AlignCenter)
        #
        self.lblcmap = QtWidgets.QLabel(PlotVis2DSeisZ)
        self.lblcmap.setObjectName("lblcmap")
        self.lblcmap.setGeometry(QtCore.QRect(260, 220, 60, 30))
        self.cbbcmap = QtWidgets.QComboBox(PlotVis2DSeisZ)
        self.cbbcmap.setObjectName("cbbcmap")
        self.cbbcmap.setGeometry(QtCore.QRect(320, 220, 120, 30))
        self.cbxflip = QtWidgets.QCheckBox(PlotVis2DSeisZ)
        self.cbxflip.setObjectName("cbxflip")
        self.cbxflip.setGeometry(QtCore.QRect(450, 220, 40, 30))
        #
        self.lblrange = QtWidgets.QLabel(PlotVis2DSeisZ)
        self.lblrange.setObjectName("lblrange")
        self.lblrange.setGeometry(QtCore.QRect(260, 130, 40, 30))
        self.ldtmin = QtWidgets.QLineEdit(PlotVis2DSeisZ)
        self.ldtmin.setObjectName("ldtmin")
        self.ldtmin.setGeometry(QtCore.QRect(300, 130, 70, 30))
        self.ldtmin.setAlignment(QtCore.Qt.AlignCenter)
        self.ldtmax = QtWidgets.QLineEdit(PlotVis2DSeisZ)
        self.ldtmax.setObjectName("ldtmax")
        self.ldtmax.setGeometry(QtCore.QRect(420, 130, 70, 30))
        self.ldtmax.setAlignment(QtCore.Qt.AlignCenter)
        self.lblrangeto = QtWidgets.QLabel(PlotVis2DSeisZ)
        self.lblrangeto.setObjectName("lblrangeto")
        self.lblrangeto.setGeometry(QtCore.QRect(370, 130, 50, 30))
        self.lblrangeto.setAlignment(QtCore.Qt.AlignCenter)
        #
        self.btnconfigplayer = QtWidgets.QPushButton(PlotVis2DSeisZ)
        self.btnconfigplayer.setObjectName("btnconfigplayer")
        self.btnconfigplayer.setGeometry(QtCore.QRect(390, 10, 100, 30))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(os.path.join(self.iconpath, "icons/video.png")),
                       QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        self.btnconfigplayer.setIcon(icon)
        #
        self.btnplotslice = QtWidgets.QPushButton(PlotVis2DSeisZ)
        self.btnplotslice.setObjectName("btnplotsliceinl")
        self.btnplotslice.setGeometry(QtCore.QRect(170, 270, 160, 30))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(os.path.join(self.iconpath, "icons/visz.png")),
                       QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        self.btnplotslice.setIcon(icon)
        #
        self.msgbox = QtWidgets.QMessageBox(PlotVis2DSeisZ)
        self.msgbox.setObjectName("msgbox")
        _center_x = PlotVis2DSeisZ.geometry().center().x()
        _center_y = PlotVis2DSeisZ.geometry().center().y()
        self.msgbox.setGeometry(QtCore.QRect(_center_x - 150, _center_y - 50, 300, 100))
        #
        self.retranslateGUI(PlotVis2DSeisZ)
        QtCore.QMetaObject.connectSlotsByName(PlotVis2DSeisZ)



    def retranslateGUI(self, PlotVis2DSeisZ):
        self.dialog = PlotVis2DSeisZ
        #
        _translate = QtCore.QCoreApplication.translate
        PlotVis2DSeisZ.setWindowTitle(_translate("PlotVis2DSeisZ", "2D Window: Seismic Time/depth"))
        if self.checkSurvInfo() is True:
            _firstattrib = None
            for i in sorted(self.seisdata.keys()):
                if self.checkSeisData(i):
                    item = QtWidgets.QListWidgetItem(self.lwgattrib)
                    item.setText(_translate("PlotVis2DSeisZ", i))
                    self.lwgattrib.addItem(item)
                    if _firstattrib is None:
                        _firstattrib = item
            self.lwgattrib.setCurrentItem(_firstattrib)
        self.lwgattrib.itemSelectionChanged.connect(self.changeLwgAttrib)
        #
        self.lblslice.setText(_translate("PlotVis2DSeisZ", "@ time/depth:"))
        if (self.checkSurvInfo() is True) :
            _slices = self.survinfo['ZRange'].astype(int)
            _slicemin = np.min(_slices)
            _slicemax = np.max(_slices)
        else:
            _slicemin = 0
            _slicemax = 0
        self.slbslice.setMinimum(_slicemin)
        self.slbslice.setMaximum(_slicemax)
        self.slbslice.setValue(_slicemin)
        if (self.checkSurvInfo() is True):
            self.ldtslice.setText(_translate("PlotVis2DSeisZ", str(_slicemin)))
        else:
            self.ldtslice.setText(_translate("PlotVis2DSeisZ", ''))
        self.slbslice.valueChanged.connect(self.changeSlbSlice)
        self.ldtslice.textChanged.connect(self.changeLdtSlice)
        #
        self.lblcmap.setText(_translate("Plot2DXlSlice", "Color map:"))
        self.cbbcmap.addItems(vis_cmap.ColorMapList)
        for _i in range(len(vis_cmap.ColorMapList)):
            self.cbbcmap.setItemIcon(_i, QtGui.QIcon(
                QtGui.QPixmap(os.path.join(self.iconpath, "icons/cmap_" + vis_cmap.ColorMapList[_i] + ".png")).scaled(80, 30)))
        self.cbbcmap.setCurrentIndex(list.index(vis_cmap.ColorMapList, self.plotstyle['Colormap']))
        #
        self.cbxflip.setText(_translate("PlotVis2DSeisZ", ""))
        self.cbxflip.setIcon(QtGui.QIcon(
            QtGui.QPixmap(os.path.join(self.iconpath, "icons/flip.png")).scaled(80, 80)))
        #
        self.lblrange.setText(_translate("PlotVis2DSeisZ", "Range:"))
        self.lblrangeto.setText(_translate("PlotVis2DSeisZ", "~~~"))
        if (self.checkSurvInfo() is True) \
                and (self.lwgattrib.currentItem() is not None) \
                and (self.checkSeisData(self.lwgattrib.currentItem().text()) is True):
            _min, _max = self.getAttribRange(self.lwgattrib.currentItem().text())
            self.ldtmin.setText(_translate("PlotVis2DSeisZ", str(_min)))
            self.ldtmax.setText(_translate("PlotVis2DSeisZ", str(_max)))
        #
        self.btnconfigplayer.setText(_translate("PlotVis2DSeisZ", "Slice Player"))
        self.btnconfigplayer.clicked.connect(self.clickBtnConfigPlayer)
        #
        self.btnplotslice.setText(_translate("PlotVis2DSeisZ", "Seismic Time/depth Viewer"))
        self.btnplotslice.setDefault(True)
        self.btnplotslice.clicked.connect(self.clickBtnPlotSlice)


    def changeLwgAttrib(self):
        if len(self.lwgattrib.selectedItems()) > 0:
            # if len(self.lwgattrib.selectedItems()) > 1:
            #     self.ldtmin.setEnabled(False)
            #     self.ldtmax.setEnabled(False)
            # else:
            #     self.ldtmin.setEnabled(True)
            #     self.ldtmax.setEnabled(True)
            _slices = self.survinfo['ZRange'].astype(int)
            _slicemin = np.min(_slices)
            _slicemax = np.max(_slices)
            self.slbslice.setMinimum(_slicemin)
            self.slbslice.setMaximum(_slicemax)
            self.ldtslice.setText(str(self.slbslice.value()))
            _min, _max = self.getAttribRange(self.lwgattrib.currentItem().text())
            self.ldtmin.setText(str(_min))
            self.ldtmax.setText(str(_max))
        else:
            self.slbslice.setMinimum(0)
            self.slbslice.setMaximum(0)
            self.ldtslice.setText('')
            self.ldtmin.setText('')
            self.ldtmax.setText('')


    def changeSlbSlice(self):
        self.ldtslice.setText(str(self.slbslice.value()))


    def changeLdtSlice(self):
        if len(self.ldtslice.text()) > 0:
            _val = basic_data.str2int(self.ldtslice.text())
            if _val >= self.slbslice.minimum() and _val <= self.slbslice.maximum():
                self.slbslice.setValue(_val)


    def clickBtnConfigPlayer(self):
        _config = QtWidgets.QDialog()
        _gui = gui_configplayer()
        _gui.playerconfig = {}
        _gui.playerconfig['Time/depth'] = self.playerconfig
        _gui.setupGUI(_config)
        _config.exec()
        self.playerconfig = _gui.playerconfig['Time/depth']
        _config.show()


    def clickBtnPlotSlice(self):
        self.refreshMsgBox()
        #
        _attriblist = self.lwgattrib.selectedItems()
        if len(_attriblist) < 1:
            vis_msg.print("ERROR in PlotVis2DSeisZ: No property selected for plot", type='error')
            QtWidgets.QMessageBox.critical(self.msgbox,
                                           '2D Window: Seismic Time/depth',
                                           'No property selected for plot')
            return
        _sls = self.slbslice.value()
        _cmap = self.cbbcmap.currentIndex()
        _flip = self.cbxflip.isChecked()
        _min = basic_data.str2float(self.ldtmin.text())
        _max = basic_data.str2float(self.ldtmax.text())
        if _min is False or _max is False:
            vis_msg.print("ERROR in PlotVis2DSeisZ: Non-float range specified for plot", type='error')
            QtWidgets.QMessageBox.critical(self.msgbox,
                                           '2D Window: Seismic Time/depth',
                                           'Non-float range specified for plot')
            return
        #
        for i in range(len(_attriblist)):
            print("Plot %d of %d properties: %s" % (i + 1, len(_attriblist), _attriblist[i].text()))
            _data = self.seisdata[_attriblist[i].text()]
            # if len(_attriblist) > 1:
            #     _min, _max = self.getAttribRange(_attriblist[i].text())
            seis_vis.plotSeisZSlicePlayerFrom3DMat(_data, initzsl=_sls, seisinfo=self.survinfo,
                                                   titlesurf=': ' + _attriblist[i].text(),
                                                   valuemin=_min,
                                                   valuemax=_max,
                                                   colormap=vis_cmap.ColorMapList[_cmap],
                                                   flipcmap=_flip, colorbaron=True,
                                                   interpolation=self.plotstyle['Interpolation'].lower(),
                                                   playerconfig=self.playerconfig,
                                                   fontstyle=self.fontstyle,
                                                   qicon=QtGui.QIcon(os.path.join(self.iconpath, "icons/logo.png"))
                                                   )
        #
        # QtWidgets.QMessageBox.information(self.msgbox,
        #                                   "Plot Time/depth",
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
            # print("PlotVis2DSeisZ: Survey not found")
            # QtWidgets.QMessageBox.critical(self.msgbox,
            #                                'Plot Seismic Time/depth',
            #                                'Survey not found')
            return False
        return True


    def checkSeisData(self, f):
        self.refreshMsgBox()
        #
        return seis_ays.isSeis3DMatConsistentWithSeisInfo(self.seisdata[f], self.survinfo)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    PlotVis2DSeisZ = QtWidgets.QWidget()
    gui = plotvis2dseisz()
    gui.setupGUI(PlotVis2DSeisZ)
    PlotVis2DSeisZ.show()
    sys.exit(app.exec_())