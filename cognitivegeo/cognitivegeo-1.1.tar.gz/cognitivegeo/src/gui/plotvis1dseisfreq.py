#############################################################################################
#                                                                                           #
# Author:   GeoPy Team                                                                      #
# Email:    geopy.info@gmail.com                                                            #
# Date:     April 2019                                                                      #
#                                                                                           #
#############################################################################################

# Create a window for plot seismic spectrum


from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
import sys, os
#
sys.path.append(os.path.dirname(__file__)[:-4][:-4][:-13])
from cognitivegeo.src.basic.data import data as basic_data
from cognitivegeo.src.core.settings import settings as core_set
from cognitivegeo.src.seismic.analysis import analysis as seis_ays
from cognitivegeo.src.seismic.attribute import attribute as seis_attrib
from cognitivegeo.src.pointset.visualization import visualization as point_vis
from cognitivegeo.src.gui.configlineplotting import configlineplotting as gui_configlineplotting
from cognitivegeo.src.vis.messager import messager as vis_msg

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class plotvis1dseisfreq(object):

    survinfo = {}
    seisdata = {}
    linestyle = core_set.Visual['Line']
    fontstyle = core_set.Visual['Font']
    #
    iconpath = os.path.dirname(__file__)
    dialog = None
    #
    lineplottingconfig = {}


    def setupGUI(self, PlotVis1DSeisFreq):
        PlotVis1DSeisFreq.setObjectName("PlotVis1DSeisFreq")
        PlotVis1DSeisFreq.setFixedSize(500, 320)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(os.path.join(self.iconpath, "icons/plotcurve.png")),
                       QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        PlotVis1DSeisFreq.setWindowIcon(icon)
        #
        self.lwgattrib = QtWidgets.QListWidget(PlotVis1DSeisFreq)
        self.lwgattrib.setObjectName("lwgattrib")
        self.lwgattrib.setGeometry(QtCore.QRect(10, 10, 230, 240))
        self.lwgattrib.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        #
        self.lblrange = QtWidgets.QLabel(PlotVis1DSeisFreq)
        self.lblrange.setObjectName("lblrange")
        self.lblrange.setGeometry(QtCore.QRect(260, 10, 150, 30))
        self.ldtmin = QtWidgets.QLineEdit(PlotVis1DSeisFreq)
        self.ldtmin.setObjectName("ldtmin")
        self.ldtmin.setGeometry(QtCore.QRect(260, 40, 90, 30))
        self.ldtmin.setAlignment(QtCore.Qt.AlignCenter)
        self.ldtmax = QtWidgets.QLineEdit(PlotVis1DSeisFreq)
        self.ldtmax.setObjectName("ldtmax")
        self.ldtmax.setGeometry(QtCore.QRect(400, 40, 90, 30))
        self.ldtmax.setAlignment(QtCore.Qt.AlignCenter)
        self.lblrangeto = QtWidgets.QLabel(PlotVis1DSeisFreq)
        self.lblrangeto.setObjectName("lblrangeto")
        self.lblrangeto.setGeometry(QtCore.QRect(350, 40, 50, 30))
        self.lblrangeto.setAlignment(QtCore.Qt.AlignCenter)
        #
        self.cbxlegend = QtWidgets.QCheckBox(PlotVis1DSeisFreq)
        self.cbxlegend.setObjectName("cbxlegend")
        self.cbxlegend.setGeometry(QtCore.QRect(430, 220, 60, 30))
        #
        self.btnconfigline = QtWidgets.QPushButton(PlotVis1DSeisFreq)
        self.btnconfigline.setObjectName("btnconfigline")
        self.btnconfigline.setGeometry(QtCore.QRect(260, 220, 160, 30))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(os.path.join(self.iconpath, "icons/settings.png")),
                       QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        self.btnconfigline.setIcon(icon)
        #
        self.btnplot = QtWidgets.QPushButton(PlotVis1DSeisFreq)
        self.btnplot.setObjectName("btnplot")
        self.btnplot.setGeometry(QtCore.QRect(170, 270, 160, 30))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(os.path.join(self.iconpath, "icons/plotcurve.png")),
                       QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        self.btnplot.setIcon(icon)
        #
        self.msgbox = QtWidgets.QMessageBox(PlotVis1DSeisFreq)
        self.msgbox.setObjectName("msgbox")
        _center_x = PlotVis1DSeisFreq.geometry().center().x()
        _center_y = PlotVis1DSeisFreq.geometry().center().y()
        self.msgbox.setGeometry(QtCore.QRect(_center_x - 150, _center_y - 50, 300, 100))
        #
        self.retranslateGUI(PlotVis1DSeisFreq)
        QtCore.QMetaObject.connectSlotsByName(PlotVis1DSeisFreq)



    def retranslateGUI(self, PlotVis1DSeisFreq):
        self.dialog = PlotVis1DSeisFreq
        #
        _translate = QtCore.QCoreApplication.translate
        PlotVis1DSeisFreq.setWindowTitle(_translate("PlotVis1DSeisFreq", "1D Window: Seismic Spectrum"))
        if self.checkSurvInfo() is True:
            _firstattrib = None
            for i in sorted(self.seisdata.keys()):
                if self.checkSeisData(i):
                    item = QtWidgets.QListWidgetItem(self.lwgattrib)
                    item.setText(_translate("PlotVis1DSeisFreq", i))
                    self.lwgattrib.addItem(item)
                    if _firstattrib is None:
                        _firstattrib = item
            self.lwgattrib.setCurrentItem(_firstattrib)
        self.lwgattrib.itemSelectionChanged.connect(self.changeLwgAttrib)
        #
        self.lblrange.setText(_translate("PlotVis1DSeisFreq", "Frequency range:"))
        self.lblrangeto.setText(_translate("PlotVis1DSeisFreq", "~~~"))
        if (self.checkSurvInfo() is True):
            _min = 0.0
            _max = abs(500.0 / float(self.survinfo['ZStep']))
            self.ldtmin.setText(_translate("PlotVis1DSeisFreq", str(_min)))
            self.ldtmax.setText(_translate("PlotVis1DSeisFreq", str(_max)))
        #
        self.cbxlegend.setText(_translate("Plot2DSeisXl", "Legend"))
        self.cbxlegend.setChecked(True)
        #
        self.btnconfigline.setText(_translate("PlotVis1DSeisFreq", "Spectrum Configuration"))
        self.btnconfigline.clicked.connect(self.clickBtnConfigLine)
        if (self.checkSurvInfo() is True) \
                and (self.lwgattrib.currentItem() is not None) \
                and (self.checkSeisData(self.lwgattrib.currentItem().text()) is True):
            _config = self.linestyle
            self.lineplottingconfig[self.lwgattrib.currentItem().text()] = _config
        #
        self.btnplot.setText(_translate("PlotVis1DSeisFreq", "Seismic Spectrum Viewer"))
        self.btnplot.setDefault(True)
        self.btnplot.clicked.connect(self.clickBtnPlot)


    def changeLwgAttrib(self):
        if len(self.lwgattrib.selectedItems()) > 0:
            _config = {}
            for _attrib in self.lwgattrib.selectedItems():
                if _attrib.text() in self.lineplottingconfig.keys():
                    _config[_attrib.text()] = self.lineplottingconfig[_attrib.text()]
                else:
                    _config[_attrib.text()] = self.linestyle
            self.lineplottingconfig = _config
        else:
            self.lineplottingconfig = {}


    def clickBtnConfigLine(self):
        _config = QtWidgets.QDialog()
        _gui = gui_configlineplotting()
        _gui.lineplottingconfig = self.lineplottingconfig
        _gui.setupGUI(_config)
        _config.exec()
        self.lineplottingconfig = _gui.lineplottingconfig
        _config.show()


    def clickBtnPlot(self):
        self.refreshMsgBox()
        #
        _attriblist = self.lwgattrib.selectedItems()
        if len(_attriblist) < 1:
            vis_msg.print("ERROR in PlotVis1DSeisFreq: No property selected for plot", type='error')
            QtWidgets.QMessageBox.critical(self.msgbox,
                                           '1D Window: Seismic Spectrum',
                                           'No property selected for plot')
            return
        #
        _freqmin = basic_data.str2float(self.ldtmin.text())
        _freqmax = basic_data.str2float(self.ldtmax.text())
        if _freqmin is False or _freqmax is False:
            vis_msg.print("ERROR in PlotVis1DSeisFreq: Non-float range specified for plot", type='error')
            QtWidgets.QMessageBox.critical(self.msgbox,
                                           '1D Window: Seismic Spectrum',
                                           'Non-float range specified for plot')
            return
        #
        _legendon = self.cbxlegend.isChecked()
        #
        _freqdict = {}
        _markerstylelist = []
        _markersizelist = []
        _colorlist = []
        _linestylelist = []
        _linewidthlist = []
        _specmin = 1e+10
        _specmax = 0
        for i in range(len(_attriblist)):
            print("PlotVis1DSeisFreq: Plot %d of %d property spectrum: %s"
                  % (i+1, len(_attriblist), _attriblist[i].text()))
            _data = self.seisdata[_attriblist[i].text()]
            #
            _freq = seis_attrib.calcPowerSpectrum(_data, self.survinfo['ZStep'])
            _freqdict[_attriblist[i].text()] = {}
            _freqdict[_attriblist[i].text()]['Frequency'] = _freq[:, 0]
            _freqdict[_attriblist[i].text()]['Power spectrum'] = _freq[:, 1]
            if np.min(_freq[:, 1]) < _specmin:
                _specmin = np.min(_freq[:, 1])
            if np.max(_freq[:, 1]) > _specmax:
                _specmax = np.max(_freq[:, 1])
            #
            _colorlist.append(self.lineplottingconfig[_attriblist[i].text()]['Color'].lower())
            _linewidthlist.append(self.lineplottingconfig[_attriblist[i].text()]['Width'])
            _linestylelist.append(self.lineplottingconfig[_attriblist[i].text()]['Style'].lower())
            _markerstylelist.append(self.lineplottingconfig[_attriblist[i].text()]['MarkerStyle'])
            _markersizelist.append(self.lineplottingconfig[_attriblist[i].text()]['MarkerSize'])
        #
        point_vis.crossplot2D(_freqdict,
                              colorlist=_colorlist, linestylelist=_linestylelist,
                              linewidthlist=_linewidthlist,
                              markerstylelist=_markerstylelist,
                              markersizelist=_markersizelist,
                              xfeature='Frequency', yfeature='Power spectrum',
                              xlim=[_freqmin, _freqmax], ylim=[_specmin, _specmax],
                              xlabel='Frequency', ylabel='Power spectrum', legendon=_legendon,
                              fontstyle=self.fontstyle,
                              title='Spectrum',
                              qicon=QtGui.QIcon(os.path.join(self.iconpath, "icons/logo.png")),
                              qtitle='1D Window: Seismic Spectrum')
        #
        # self.dialog.close()
        return


    def refreshMsgBox(self):
        _center_x = self.dialog.geometry().center().x()
        _center_y = self.dialog.geometry().center().y()
        self.msgbox.setGeometry(QtCore.QRect(_center_x - 150, _center_y - 50, 300, 100))


    def checkSurvInfo(self):
        self.refreshMsgBox()
        #
        if seis_ays.checkSeisInfo(self.survinfo) is False:
            # print("PlotVis1DSeisFreq: Survey not found")
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
    PlotVis1DSeisFreq = QtWidgets.QWidget()
    gui = plotvis1dseisfreq()
    gui.setupGUI(PlotVis1DSeisFreq)
    PlotVis1DSeisFreq.show()
    sys.exit(app.exec_())