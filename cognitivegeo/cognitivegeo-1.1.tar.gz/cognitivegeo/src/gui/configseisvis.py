#############################################################################################
#                                                                                           #
# Author:   GeoPy Team                                                                      #
# Email:    geopy.info@gmail.com                                                            #
# Date:     November 2019                                                                   #
#                                                                                           #
#############################################################################################

# Create a GUI for configuring seismic visualization

from PyQt5 import QtCore, QtGui, QtWidgets
import os, sys
#
sys.path.append(os.path.dirname(__file__)[:-4][:-4][:-13])
from cognitivegeo.src.basic.data import data as basic_data
from cognitivegeo.src.vis.image import image as vis_image
from cognitivegeo.src.vis.colormap import colormap as vis_cmap

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class configseisvis(object):

    seisvisconfig = {}
    #
    iconpath = os.path.dirname(__file__)
    dialog = None


    def setupGUI(self, ConfigSeisVis):
        ConfigSeisVis.setObjectName("ConfigSeisVis")
        ConfigSeisVis.setFixedSize(620, 280)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(os.path.join(self.iconpath, "icons/settings.png")),
                       QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        ConfigSeisVis.setWindowIcon(icon)
        #
        self.twgseis = QtWidgets.QTableWidget(ConfigSeisVis)
        self.twgseis.setObjectName("twgseis")
        self.twgseis.setGeometry(QtCore.QRect(10, 10, 600, 200))
        self.twgseis.setColumnCount(7)
        self.twgseis.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.twgseis.verticalHeader().hide()
        self.twgseis.setColumnWidth(2, 40)
        #
        self.btnapply = QtWidgets.QPushButton(ConfigSeisVis)
        self.btnapply.setObjectName("btnapply")
        self.btnapply.setGeometry(QtCore.QRect(160, 230, 100, 30))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(os.path.join(self.iconpath, "icons/ok.png")),
                       QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        self.btnapply.setIcon(icon)
        #
        self.msgbox = QtWidgets.QMessageBox(ConfigSeisVis)
        self.msgbox.setObjectName("msgbox")
        _center_x = ConfigSeisVis.geometry().center().x()
        _center_y = ConfigSeisVis.geometry().center().y()
        self.msgbox.setGeometry(QtCore.QRect(_center_x - 150, _center_y - 50, 300, 100))
        #
        self.retranslateGUI(ConfigSeisVis)
        QtCore.QMetaObject.connectSlotsByName(ConfigSeisVis)


    def retranslateGUI(self, ConfigSeisVis):
        self.dialog = ConfigSeisVis
        #
        _translate = QtCore.QCoreApplication.translate
        ConfigSeisVis.setWindowTitle(_translate("ConfigSeisVis", "Seismic Visualization Configuration"))
        #
        self.twgseis.clear()
        self.twgseis.setHorizontalHeaderLabels(["Seismic", "Colormap", '', 'Opacity', 'Interpolation', 'Maximum', 'Minimum'])
        self.twgseis.setRowCount(len(self.seisvisconfig.keys()))
        _idx = 0
        for seis in sorted(self.seisvisconfig.keys()):
            item = QtWidgets.QTableWidgetItem()
            item.setText(seis)
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.twgseis.setItem(_idx, 0, item)
            #
            item = QtWidgets.QComboBox()
            item.addItems(vis_cmap.ColorMapList)
            for _i in range(len(vis_cmap.ColorMapList)):
                item.setItemIcon(_i, QtGui.QIcon(
                    QtGui.QPixmap(
                        os.path.join(self.iconpath, "icons/cmap_" + vis_cmap.ColorMapList[_i] + ".png")).scaled(80,
                                                                                                                40)))
            item.setCurrentIndex(list.index(vis_cmap.ColorMapList,
                                            self.seisvisconfig[seis]['Colormap']))
            self.twgseis.setCellWidget(_idx, 1, item)
            #
            item = QtWidgets.QCheckBox()
            item.setIcon(QtGui.QIcon(QtGui.QPixmap(os.path.join(self.iconpath, "icons/flip.png")).scaled(40, 40)))
            item.setChecked(self.seisvisconfig[seis]['Flip'])
            self.twgseis.setCellWidget(_idx, 2, item)
            #
            item = QtWidgets.QComboBox()
            item.addItems(vis_cmap.OpacityList)
            item.setCurrentIndex(list.index(vis_cmap.OpacityList,
                                            self.seisvisconfig[seis]['Opacity']))
            self.twgseis.setCellWidget(_idx, 3, item)
            #
            item = QtWidgets.QComboBox()
            item.addItems(vis_image.InterpolationList)
            for _i in range(len(vis_image.InterpolationList)):
                item.setItemIcon(_i, QtGui.QIcon(
                    QtGui.QPixmap(
                        os.path.join(self.iconpath, "icons/interp_" + vis_image.InterpolationList[_i] + ".png")).scaled(
                        80, 40)))
            item.setCurrentIndex(list.index(vis_image.InterpolationList,
                                            self.seisvisconfig[seis]['Interpolation']))
            self.twgseis.setCellWidget(_idx, 4, item)
            #
            item = QtWidgets.QTableWidgetItem()
            item.setText(str(self.seisvisconfig[seis]['Maximum']))
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.twgseis.setItem(_idx, 5, item)
            #
            item = QtWidgets.QTableWidgetItem()
            item.setText(str(self.seisvisconfig[seis]['Minimum']))
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.twgseis.setItem(_idx, 6, item)
            #
            _idx = _idx + 1
        #
        self.btnapply.setText(_translate("ConfigSeisVis", "Apply"))
        self.btnapply.clicked.connect(self.clickBtnApply)


    def clickBtnApply(self):
        self.refreshMsgBox()
        #
        for seis in sorted(self.seisvisconfig.keys()):
            _idx = list.index(sorted(self.seisvisconfig.keys()), seis)
            _config = {}
            _config['Colormap'] = vis_cmap.ColorMapList[self.twgseis.cellWidget(_idx, 1).currentIndex()]
            _config['Flip'] = self.twgseis.cellWidget(_idx, 2).isChecked()
            _config['Opacity'] = vis_cmap.OpacityList[self.twgseis.cellWidget(_idx, 3).currentIndex()]
            _config['Interpolation'] = vis_image.InterpolationList[self.twgseis.cellWidget(_idx, 4).currentIndex()]
            _max = basic_data.str2float(self.twgseis.item(_idx, 5).text())
            _min = basic_data.str2float(self.twgseis.item(_idx, 6).text())
            if _max is not False and _min is not False and _max >= _min:
                _config['Maximum'] = _max
                _config['Minimum'] = _min
            self.seisvisconfig[seis] = _config
        #
        self.dialog.close()


    def refreshMsgBox(self):
        _center_x = self.dialog.geometry().center().x()
        _center_y = self.dialog.geometry().center().y()
        self.msgbox.setGeometry(QtCore.QRect(_center_x - 150, _center_y - 50, 300, 100))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ConfigSeisVis = QtWidgets.QWidget()
    gui = configseisvis()
    _seis = {}
    _seis['seismic'] = {}
    _seis['seismic']['Colormap'] = 'Seismic'
    _seis['seismic']['Flip'] = True
    _seis['seismic']['Opacity'] = '100%'
    _seis['seismic']['Interpolation'] = 'Bicubic'
    _seis['seismic']['Maximum'] = 100.0
    _seis['seismic']['Minimum'] = -100.0
    gui.seisvisconfig = _seis
    gui.setupGUI(ConfigSeisVis)
    ConfigSeisVis.show()
    sys.exit(app.exec_())