#############################################################################################
#                                                                                           #
# Author:   GeoPy Team                                                                      #
# Email:    geopy.info@gmail.com                                                            #
# Date:     March 2018                                                                      #
#                                                                                           #
#############################################################################################

# Create a window for managing seismic properties


from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
import os, sys
#
sys.path.append(os.path.dirname(__file__)[:-4][:-4][:-13])
from cognitivegeo.src.seismic.analysis import analysis as seis_ays
from cognitivegeo.src.gui.editseispointset import editseispointset as gui_editseispointset
from cognitivegeo.src.vis.messager import messager as vis_msg

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class manageseis(object):

    survinfo = {}
    seisdata = {}
    rootpath = ''
    #
    iconpath = os.path.dirname(__file__)
    dialog = None


    def setupGUI(self, ManageSeis):
        ManageSeis.setObjectName("ManageSeis")
        ManageSeis.setFixedSize(320, 420)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(os.path.join(self.iconpath, "icons/seismic.png")),
                       QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        ManageSeis.setWindowIcon(icon)
        #
        self.lblseis = QtWidgets.QLabel(ManageSeis)
        self.lblseis.setObjectName("lblattrib")
        self.lblseis.setGeometry(QtCore.QRect(10, 10, 150, 30))
        self.twgseis = QtWidgets.QTableWidget(ManageSeis)
        self.twgseis.setObjectName("twgseis")
        self.twgseis.setGeometry(QtCore.QRect(10, 50, 300, 300))
        self.twgseis.setColumnCount(5)
        self.twgseis.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.twgseis.verticalHeader().hide()
        self.btnedit = QtWidgets.QPushButton(ManageSeis)
        self.btnedit.setObjectName("btnedit")
        self.btnedit.setGeometry(QtCore.QRect(210, 360, 100, 30))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(os.path.join(self.iconpath, "icons/pen.png")),
                       QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        self.btnedit.setIcon(icon)
        #
        self.msgbox = QtWidgets.QMessageBox(ManageSeis)
        self.msgbox.setObjectName("msgbox")
        _center_x = ManageSeis.geometry().center().x()
        _center_y = ManageSeis.geometry().center().y()
        self.msgbox.setGeometry(QtCore.QRect(_center_x - 150, _center_y - 50, 300, 100))
        #
        self.retranslateGUI(ManageSeis)
        QtCore.QMetaObject.connectSlotsByName(ManageSeis)


    def retranslateGUI(self, ManageSeis):
        self.dialog = ManageSeis
        #
        _translate = QtCore.QCoreApplication.translate
        ManageSeis.setWindowTitle(_translate("ManageSeis", "Manage Seismic"))
        self.lblseis.setText(_translate("ManageSeis", "Seismic properties:"))
        self.refreshTwgSeis()
        self.btnedit.setText(_translate("ManageSeis", "Edit"))
        self.btnedit.setToolTip("Edit seismic properties")
        self.btnedit.clicked.connect(self.clickBtnEdit)


    def clickBtnEdit(self):
        _editseis = QtWidgets.QDialog()
        _gui = gui_editseispointset()
        _gui.seispointdata = {}
        # add info
        if self.checkSurvInfo():
            _survinfo = seis_ays.convertSeisInfoTo2DMat(self.survinfo)
            _gui.seispointdata['Inline'] = _survinfo[:, 0:1]
            _gui.seispointdata['Crossline'] = _survinfo[:, 1:2]
            _gui.seispointdata['Z'] = _survinfo[:, 2:3]
        # reshape data
        for key in self.seisdata.keys():
            if self.checkSeisData(key):
                _gui.seispointdata[key] = np.reshape(np.transpose(self.seisdata[key], [2, 1, 0]), [-1, 1])
        _gui.rootpath = self.rootpath
        _gui.setupGUI(_editseis)
        _editseis.exec()
        #
        self.seisdata = {}
        # reshape data
        for key in _gui.seispointdata.keys():
            if key != 'Inline' and key != 'Crossline' and key != 'Z' \
                    and (np.shape(_gui.seispointdata[key])[0] == self.survinfo['ILNum'] * self.survinfo['XLNum'] * self.survinfo['ZNum']):
                self.seisdata[key] = np.transpose(np.reshape(_gui.seispointdata[key], [self.survinfo['ILNum'],
                                                                                       self.survinfo['XLNum'],
                                                                                       self.survinfo['ZNum']]),
                                                  [2, 1, 0])
        _editseis.show()
        #
        self.refreshTwgSeis()


    def refreshTwgSeis(self):
        self.twgseis.clear()
        self.twgseis.setHorizontalHeaderLabels(["Property", "Maximum", "Minimum", "Mean", "Std"])
        if self.checkSurvInfo() is True:
            _idx = 0
            self.twgseis.setRowCount(len(self.seisdata.keys()))
            for i in sorted(self.seisdata.keys()):
                if self.checkSeisData(i):
                    self.twgseis.setRowCount(_idx+1)
                    #
                    item = QtWidgets.QTableWidgetItem()
                    item.setText(i)
                    item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                    self.twgseis.setItem(_idx, 0, item)
                    item = QtWidgets.QTableWidgetItem()
                    item.setText(str(np.max(self.seisdata[i])))
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                    item.setFlags(QtCore.Qt.ItemIsEditable)
                    self.twgseis.setItem(_idx, 1, item)
                    item = QtWidgets.QTableWidgetItem()
                    item.setText(str(np.min(self.seisdata[i])))
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                    item.setFlags(QtCore.Qt.ItemIsEditable)
                    self.twgseis.setItem(_idx, 2, item)
                    item = QtWidgets.QTableWidgetItem()
                    item.setText(str(np.mean(self.seisdata[i])))
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                    item.setFlags(QtCore.Qt.ItemIsEditable)
                    self.twgseis.setItem(_idx, 3, item)
                    item = QtWidgets.QTableWidgetItem()
                    item.setText(str(np.std(self.seisdata[i])))
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                    item.setFlags(QtCore.Qt.ItemIsEditable)
                    self.twgseis.setItem(_idx, 4, item)
                    _idx = _idx + 1


    def refreshMsgBox(self):
        _center_x = self.dialog.geometry().center().x()
        _center_y = self.dialog.geometry().center().y()
        self.msgbox.setGeometry(QtCore.QRect(_center_x - 150, _center_y - 50, 300, 100))


    def checkSurvInfo(self):
        self.refreshMsgBox()
        #
        if seis_ays.checkSeisInfo(self.survinfo) is False:
            # print("ManageSeis: Survey not found")
            # QtWidgets.QMessageBox.critical(self.msgbox,
            #                                'Manage Seismic',
            #                                'Survey not found')
            return False
        return True


    def checkSeisData(self, f):
        self.refreshMsgBox()
        #
        return seis_ays.isSeis3DMatConsistentWithSeisInfo(self.seisdata[f], self.survinfo)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ManageSeis = QtWidgets.QWidget()
    gui = manageseis()
    gui.setupGUI(ManageSeis)
    ManageSeis.show()
    sys.exit(app.exec_())