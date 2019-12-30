#############################################################################################
#                                                                                           #
# Author:   GeoPy Team                                                                      #
# Email:    geopy.info@gmail.com                                                            #
# Date:     Movember 2018                                                                   #
#                                                                                           #
#############################################################################################

# Create a window for plot seismic traces


from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
import sys, os
#
sys.path.append(os.path.dirname(__file__)[:-4][:-4][:-13])
from cognitivegeo.src.basic.data import data as basic_data
from cognitivegeo.src.core.settings import settings as core_set
from cognitivegeo.src.seismic.analysis import analysis as seis_ays
from cognitivegeo.src.seismic.visualization import visualization as seis_vis
from cognitivegeo.src.gui.configlineplotting import configlineplotting as gui_configlineplotting
from cognitivegeo.src.gui.configplayer import configplayer as gui_configplayer
from cognitivegeo.src.vis.messager import messager as vis_msg

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class plotvis1dseisz(object):

    survinfo = {}
    seisdata = {}
    linestyle = core_set.Visual['Line']
    playerconfiginl = core_set.Viewer['Player']
    playerconfigxl = core_set.Viewer['Player']
    fontstyle = core_set.Visual['Font']
    #
    iconpath = os.path.dirname(__file__)
    dialog = None
    #
    lineplottingconfig = {}


    def setupGUI(self, PlotVis1DSeisZ):
        PlotVis1DSeisZ.setObjectName("PlotVis1DSeisZ")
        PlotVis1DSeisZ.setFixedSize(500, 370)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(os.path.join(self.iconpath, "icons/waveform.png")),
                       QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        PlotVis1DSeisZ.setWindowIcon(icon)
        #
        self.lwgattrib = QtWidgets.QListWidget(PlotVis1DSeisZ)
        self.lwgattrib.setObjectName("lwgattrib")
        self.lwgattrib.setGeometry(QtCore.QRect(10, 10, 230, 290))
        self.lwgattrib.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        #
        self.lblinl = QtWidgets.QLabel(PlotVis1DSeisZ)
        self.lblinl.setObjectName("lblinl")
        self.lblinl.setGeometry(QtCore.QRect(260, 50, 150, 30))
        self.slbinl = QtWidgets.QScrollBar(PlotVis1DSeisZ)
        self.slbinl.setObjectName("slbinl")
        self.slbinl.setOrientation(QtCore.Qt.Horizontal)
        self.slbinl.setGeometry(QtCore.QRect(260, 80, 170, 30))
        self.ldtinl = QtWidgets.QLineEdit(PlotVis1DSeisZ)
        self.ldtinl.setObjectName("ldtinl")
        self.ldtinl.setGeometry(QtCore.QRect(440, 80, 50, 30))
        self.ldtinl.setAlignment(QtCore.Qt.AlignCenter)
        #
        self.lblxl = QtWidgets.QLabel(PlotVis1DSeisZ)
        self.lblxl.setObjectName("lblxl")
        self.lblxl.setGeometry(QtCore.QRect(260, 120, 150, 30))
        self.slbxl = QtWidgets.QScrollBar(PlotVis1DSeisZ)
        self.slbxl.setObjectName("slbxl")
        self.slbxl.setOrientation(QtCore.Qt.Horizontal)
        self.slbxl.setGeometry(QtCore.QRect(260, 150, 170, 30))
        self.ldtxl = QtWidgets.QLineEdit(PlotVis1DSeisZ)
        self.ldtxl.setObjectName("ldtxl")
        self.ldtxl.setGeometry(QtCore.QRect(440, 150, 50, 30))
        self.ldtxl.setAlignment(QtCore.Qt.AlignCenter)
        #
        self.lblrange = QtWidgets.QLabel(PlotVis1DSeisZ)
        self.lblrange.setObjectName("lblrange")
        self.lblrange.setGeometry(QtCore.QRect(260, 200, 40, 30))
        self.ldtmin = QtWidgets.QLineEdit(PlotVis1DSeisZ)
        self.ldtmin.setObjectName("ldtmin")
        self.ldtmin.setGeometry(QtCore.QRect(300, 200, 70, 30))
        self.ldtmin.setAlignment(QtCore.Qt.AlignCenter)
        self.ldtmax = QtWidgets.QLineEdit(PlotVis1DSeisZ)
        self.ldtmax.setObjectName("ldtmax")
        self.ldtmax.setGeometry(QtCore.QRect(420, 200, 70, 30))
        self.ldtmax.setAlignment(QtCore.Qt.AlignCenter)
        self.lblrangeto = QtWidgets.QLabel(PlotVis1DSeisZ)
        self.lblrangeto.setObjectName("lblrangeto")
        self.lblrangeto.setGeometry(QtCore.QRect(370, 200, 50, 30))
        self.lblrangeto.setAlignment(QtCore.Qt.AlignCenter)
        #
        self.btnconfigline = QtWidgets.QPushButton(PlotVis1DSeisZ)
        self.btnconfigline.setObjectName("btnconfigline")
        self.btnconfigline.setGeometry(QtCore.QRect(330, 270, 160, 30))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(os.path.join(self.iconpath, "icons/plotcurve.png")),
                       QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        self.btnconfigline.setIcon(icon)
        #
        self.btnconfigplayer = QtWidgets.QPushButton(PlotVis1DSeisZ)
        self.btnconfigplayer.setObjectName("btnconfigplayer")
        self.btnconfigplayer.setGeometry(QtCore.QRect(370, 10, 120, 30))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(os.path.join(self.iconpath, "icons/video.png")),
                       QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        self.btnconfigplayer.setIcon(icon)
        #
        self.btnplot = QtWidgets.QPushButton(PlotVis1DSeisZ)
        self.btnplot.setObjectName("btnplot")
        self.btnplot.setGeometry(QtCore.QRect(170, 320, 160, 30))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(os.path.join(self.iconpath, "icons/waveform.png")),
                       QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        self.btnplot.setIcon(icon)
        #
        self.msgbox = QtWidgets.QMessageBox(PlotVis1DSeisZ)
        self.msgbox.setObjectName("msgbox")
        _center_x = PlotVis1DSeisZ.geometry().center().x()
        _center_y = PlotVis1DSeisZ.geometry().center().y()
        self.msgbox.setGeometry(QtCore.QRect(_center_x - 150, _center_y - 50, 300, 100))
        #
        self.retranslateGUI(PlotVis1DSeisZ)
        QtCore.QMetaObject.connectSlotsByName(PlotVis1DSeisZ)



    def retranslateGUI(self, PlotVis1DSeisZ):
        self.dialog = PlotVis1DSeisZ
        #
        _translate = QtCore.QCoreApplication.translate
        PlotVis1DSeisZ.setWindowTitle(_translate("PlotVis1DSeisZ", "1D Window: Seismic Waveform"))
        if self.checkSurvInfo() is True:
            _firstattrib = None
            for i in sorted(self.seisdata.keys()):
                if self.checkSeisData(i):
                    item = QtWidgets.QListWidgetItem(self.lwgattrib)
                    item.setText(_translate("PlotVis1DSeisZ", i))
                    self.lwgattrib.addItem(item)
                    if _firstattrib is None:
                        _firstattrib = item
            self.lwgattrib.setCurrentItem(_firstattrib)
        self.lwgattrib.itemSelectionChanged.connect(self.changeLwgAttrib)
        #
        self.lblinl.setText(_translate("PlotVis1DSeisZ", "@ Inline:"))
        if (self.checkSurvInfo() is True):
            _slices = self.survinfo['ILRange'].astype(int)
            _slicemin = np.min(_slices)
            _slicemax = np.max(_slices)
        else:
            _slicemin = 0
            _slicemax = 0
        self.slbinl.setMinimum(_slicemin)
        self.slbinl.setMaximum(_slicemax)
        self.slbinl.setValue(_slicemin)
        if (self.checkSurvInfo() is True):
            self.ldtinl.setText(_translate("PlotVis1DSeisZ", str(_slicemin)))
        else:
            self.ldtinl.setText(_translate("PlotVis1DSeisZ", ''))
        self.slbinl.valueChanged.connect(self.changeSlbInl)
        self.ldtinl.textChanged.connect(self.changeLdtInl)
        #
        self.lblxl.setText(_translate("PlotVis1DSeisZ", "@ crossline:"))
        if (self.checkSurvInfo() is True):
            _slices = self.survinfo['XLRange'].astype(int)
            _slicemin = np.min(_slices)
            _slicemax = np.max(_slices)
        else:
            _slicemin = 0
            _slicemax = 0
        self.slbxl.setMinimum(_slicemin)
        self.slbxl.setMaximum(_slicemax)
        self.slbxl.setValue(_slicemin)
        if (self.checkSurvInfo() is True):
            self.ldtxl.setText(_translate("PlotVis1DSeisZ", str(_slicemin)))
        else:
            self.ldtxl.setText(_translate("PlotVis1DSeisZ", ''))
        self.slbxl.valueChanged.connect(self.changeSlbXl)
        self.ldtxl.textChanged.connect(self.changeLdtXl)
        #
        self.lblrange.setText(_translate("PlotVis1DSeisZ", "Range:"))
        self.lblrangeto.setText(_translate("PlotVis1DSeisZ", "~~~"))
        if (self.checkSurvInfo() is True) \
                and (self.lwgattrib.currentItem() is not None) \
                and (self.checkSeisData(self.lwgattrib.currentItem().text()) is True):
            _min, _max = self.getAttribRange(self.lwgattrib.currentItem().text())
            self.ldtmin.setText(_translate("PlotVis1DSeisZ", str(_min)))
            self.ldtmax.setText(_translate("PlotVis1DSeisZ", str(_max)))
        #
        self.btnconfigline.setText(_translate("PlotVis1DSeisZ", "Waveform Configuration"))
        self.btnconfigline.clicked.connect(self.clickBtnConfigLine)
        if (self.checkSurvInfo() is True) \
                and (self.lwgattrib.currentItem() is not None) \
                and (self.checkSeisData(self.lwgattrib.currentItem().text()) is True):
            _config = self.linestyle
            self.lineplottingconfig[self.lwgattrib.currentItem().text()] = _config
        #
        self.btnconfigplayer.setText(_translate("PlotVis1DSeisZ", "Waveform Player"))
        self.btnconfigplayer.clicked.connect(self.clickBtnConfigPlayer)
        #
        self.btnplot.setText(_translate("PlotVis1DSeisZ", "Seismic Waveform Viewer"))
        self.btnplot.setDefault(True)
        self.btnplot.clicked.connect(self.clickBtnPlot)


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
            self.slbinl.setMinimum(_slicemin)
            self.slbinl.setMaximum(_slicemax)
            self.ldtinl.setText(str(self.slbinl.value()))
            _slices = self.survinfo['XLRange'].astype(int)
            _slicemin = np.min(_slices)
            _slicemax = np.max(_slices)
            self.slbxl.setMinimum(_slicemin)
            self.slbxl.setMaximum(_slicemax)
            self.ldtxl.setText(str(self.slbxl.value()))
            _min, _max = self.getAttribRange(self.lwgattrib.selectedItems()[0].text())
            self.ldtmin.setText(str(_min))
            self.ldtmax.setText(str(_max))
            #
            _config = {}
            for _attrib in self.lwgattrib.selectedItems():
                if _attrib.text() in self.lineplottingconfig.keys():
                    _config[_attrib.text()] = self.lineplottingconfig[_attrib.text()]
                else:
                    _config[_attrib.text()] = self.linestyle
            self.lineplottingconfig = _config
        else:
            self.slbinl.setMinimum(0)
            self.slbinl.setMaximum(0)
            self.ldtinl.setText('')
            self.slbxl.setMinimum(0)
            self.slbxl.setMaximum(0)
            self.ldtxl.setText('')
            self.ldtmin.setText('')
            self.ldtmax.setText('')
            self.lineplottingconfig = {}


    def changeSlbInl(self):
        self.ldtinl.setText(str(self.slbinl.value()))


    def changeLdtInl(self):
        if len(self.ldtinl.text()) > 0:
            _val = basic_data.str2int(self.ldtinl.text())
            if _val >= self.slbinl.minimum() and _val <= self.slbinl.maximum():
                self.slbinl.setValue(_val)


    def changeSlbXl(self):
        self.ldtxl.setText(str(self.slbxl.value()))


    def changeLdtXl(self):
        if len(self.ldtxl.text()) > 0:
            _val = basic_data.str2int(self.ldtxl.text())
            if _val >= self.slbxl.minimum() and _val <= self.slbxl.maximum():
                self.slbxl.setValue(_val)


    def clickBtnConfigLine(self):
        _config = QtWidgets.QDialog()
        _gui = gui_configlineplotting()
        _gui.lineplottingconfig = self.lineplottingconfig
        _gui.setupGUI(_config)
        _config.exec()
        self.lineplottingconfig = _gui.lineplottingconfig
        _config.show()


    def clickBtnConfigPlayer(self):
        _config = QtWidgets.QDialog()
        _gui = gui_configplayer()
        _gui.playerconfig = {}
        _gui.playerconfig['Inline'] = self.playerconfiginl
        _gui.playerconfig['Crossline'] = self.playerconfigxl
        _gui.setupGUI(_config)
        _config.exec()
        self.playerconfiginl = _gui.playerconfig['Inline']
        self.playerconfigxl = _gui.playerconfig['Crossline']
        _config.show()


    def clickBtnPlot(self):
        self.refreshMsgBox()
        #
        _attriblist = self.lwgattrib.selectedItems()
        if len(_attriblist) < 1:
            vis_msg.print("ERROR in PlotVis1DSeisZ: No property selected for plot", type='error')
            QtWidgets.QMessageBox.critical(self.msgbox,
                                           '1D Window: Seismic Waveform',
                                           'No property selected for plot')
            return
        #
        _inls = self.slbinl.value()
        _xls = self.slbxl.value()
        _min = basic_data.str2float(self.ldtmin.text())
        _max = basic_data.str2float(self.ldtmax.text())
        if _min is False or _max is False:
            vis_msg.print("ERROR in PlotVis1DSeisZ: Non-float range specified for plot", type='error')
            QtWidgets.QMessageBox.critical(self.msgbox,
                                           '1D Window: Seismic Waveform',
                                           'Non-float range specified for plot')
            return

        for i in range(len(_attriblist)):
            print("PlotVis1DSeisZ: Plot %d of %d properties: %s" % (i + 1, len(_attriblist), _attriblist[i].text()))
            _data = self.seisdata[_attriblist[i].text()]
            # if len(_attriblist) > 1:
            #     _min, _max = self.getAttribRange(_attriblist[i].text())
            #
            _color = self.lineplottingconfig[_attriblist[i].text()]['Color'].lower()
            _linewidth = self.lineplottingconfig[_attriblist[i].text()]['Width']
            _linestyle = self.lineplottingconfig[_attriblist[i].text()]['Style'].lower()
            _markerstyle = self.lineplottingconfig[_attriblist[i].text()]['MarkerStyle']
            _markersize = self.lineplottingconfig[_attriblist[i].text()]['MarkerSize']
            #
            seis_vis.plotSeisZTracePlayerFrom3DMat(_data, initinltc=_inls, initxltc=_xls, seisinfo=self.survinfo,
                                                   titlesurf=_attriblist[i].text() + ' at ',
                                                   valuemin=_min, valuemax=_max,
                                                   color=_color, markerstyle=_markerstyle, markersize=_markersize,
                                                   linewidth=_linewidth, linestyle=_linestyle,
                                                   playerconfiginl=self.playerconfiginl,
                                                   playerconfigxl=self.playerconfigxl,
                                                   fontstyle=self.fontstyle,
                                                   qicon=QtGui.QIcon(os.path.join(self.iconpath, "icons/logo.png")))
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
            # print("PlotVis1DSeisZ: Survey not found")
            # QtWidgets.QMessageBox.critical(self.msgbox,
            #                                'Plot Seismic Waveform',
            #                                'Survey not found')
            return False
        return True


    def checkSeisData(self, f):
        self.refreshMsgBox()
        #
        return seis_ays.isSeis3DMatConsistentWithSeisInfo(self.seisdata[f], self.survinfo)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    PlotVis1DSeisZ = QtWidgets.QWidget()
    gui = plotvis1dseisz()
    gui.setupGUI(PlotVis1DSeisZ)
    PlotVis1DSeisZ.show()
    sys.exit(app.exec_())