#############################################################################################
#                                                                                           #
# Author:   GeoPy Team                                                                      #
# Email:    geopy.info@gmail.com                                                            #
# Date:     March 2018                                                                      #
#                                                                                           #
#############################################################################################

# Create a window for retrieving seismic properties from a given numpy dictionary


from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
import os, sys
#
sys.path.append(os.path.dirname(__file__)[:-4][:-4][:-13])
from cognitivegeo.src.seismic.analysis import analysis as seis_ays
from cognitivegeo.src.pointset.analysis import analysis as point_ays
from cognitivegeo.src.basic.data import data as basic_data
from cognitivegeo.src.basic.matdict import matdict as basic_mdt
from cognitivegeo.src.vis.messager import messager as vis_msg

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class rtrvseisprop(object):

    pointdata = {}
    rootpath = ''
    #
    iconpath = os.path.dirname(__file__)
    dialog = None
    #
    npydata = None
    npyinfo = {}


    def setupGUI(self, RtrvSeisProp):
        RtrvSeisProp.setObjectName("RtrvSeisProp")
        RtrvSeisProp.setFixedSize(400, 390)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(os.path.join(self.iconpath, "icons/retrieve.png")),
                       QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        RtrvSeisProp.setWindowIcon(icon)
        #
        self.lblfrom = QtWidgets.QLabel(RtrvSeisProp)
        self.lblfrom.setObjectName("lblfrom")
        self.lblfrom.setGeometry(QtCore.QRect(10, 10, 150, 30))
        self.ldtfrom = QtWidgets.QLineEdit(RtrvSeisProp)
        self.ldtfrom.setObjectName("ldtfrom")
        self.ldtfrom.setGeometry(QtCore.QRect(160, 10, 160, 30))
        self.btnfrom = QtWidgets.QPushButton(RtrvSeisProp)
        self.btnfrom.setObjectName("btnfrom")
        self.btnfrom.setGeometry(QtCore.QRect(330, 10, 60, 30))
        self.lblattrib = QtWidgets.QLabel(RtrvSeisProp)
        self.lblattrib.setObjectName("lblattrib")
        self.lblattrib.setGeometry(QtCore.QRect(10, 50, 150, 30))
        self.lwgattrib = QtWidgets.QListWidget(RtrvSeisProp)
        self.lwgattrib.setObjectName("lwgattrib")
        self.lwgattrib.setGeometry(QtCore.QRect(160, 50, 230, 200))
        self.lwgattrib.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.lbldims = QtWidgets.QLabel(RtrvSeisProp)
        self.lbldims.setObjectName("lbldims")
        self.lbldims.setGeometry(QtCore.QRect(10, 270, 150, 30))
        self.ldtdimsinl = QtWidgets.QLineEdit(RtrvSeisProp)
        self.ldtdimsinl.setObjectName("ldtdimsinl")
        self.ldtdimsinl.setGeometry(QtCore.QRect(160, 270, 60, 30))
        self.ldtdimsxl = QtWidgets.QLineEdit(RtrvSeisProp)
        self.ldtdimsxl.setObjectName("ldtdimsxl")
        self.ldtdimsxl.setGeometry(QtCore.QRect(245, 270, 60, 30))
        self.ldtdimsz = QtWidgets.QLineEdit(RtrvSeisProp)
        self.ldtdimsz.setObjectName("ldtdimsz")
        self.ldtdimsz.setGeometry(QtCore.QRect(330, 270, 60, 30))
        self.btnrtrvprop = QtWidgets.QPushButton(RtrvSeisProp)
        self.btnrtrvprop.setObjectName("btnrtrvprop")
        self.btnrtrvprop.setGeometry(QtCore.QRect(120, 330, 160, 30))
        self.btnrtrvprop.setIcon(icon)
        #
        self.msgbox = QtWidgets.QMessageBox(RtrvSeisProp)
        self.msgbox.setObjectName("msgbox")
        _center_x = RtrvSeisProp.geometry().center().x()
        _center_y = RtrvSeisProp.geometry().center().y()
        self.msgbox.setGeometry(QtCore.QRect(_center_x - 150, _center_y - 50, 300, 100))
        #
        self.retranslateGUI(RtrvSeisProp)
        QtCore.QMetaObject.connectSlotsByName(RtrvSeisProp)


    def retranslateGUI(self, RtrvSeisProp):
        self.dialog = RtrvSeisProp
        #
        _translate = QtCore.QCoreApplication.translate
        RtrvSeisProp.setWindowTitle(_translate("RtrvSeisProp", "Retrieve Seismic Property"))
        self.lblfrom.setText(_translate("RtrvSeisProp", "Select Seismic NumPy:"))
        self.ldtfrom.setText(_translate("RtrvSeisProp", ""))
        self.ldtfrom.textChanged.connect(self.changeLdtFrom)
        self.btnfrom.setText(_translate("RtrvSeisProp", "Browse"))
        self.btnfrom.clicked.connect(self.clickBtnFrom)
        self.lblattrib.setText(_translate("RtrvSeisProp", "Select target properties:"))
        self.lbldims.setText(_translate("RtrvSeisProp", "Retrieval radius (IL/XL/Z):"))
        self.ldtdimsinl.setText(_translate("RtrvSeisProp", "0"))
        self.ldtdimsinl.setAlignment(QtCore.Qt.AlignCenter)
        self.ldtdimsxl.setText(_translate("RtrvSeisProp", "0"))
        self.ldtdimsxl.setAlignment(QtCore.Qt.AlignCenter)
        self.ldtdimsz.setText(_translate("RtrvSeisProp", "0"))
        self.ldtdimsz.setAlignment(QtCore.Qt.AlignCenter)
        self.btnrtrvprop.setText(_translate("RtrvSeisProp", "Retrieve Property"))
        self.btnrtrvprop.clicked.connect(self.clickBtnRtrvSeisProp)


    def changeLdtFrom(self):
        self.refreshMsgBox()
        #
        self.lwgattrib.clear()
        #
        if os.path.exists(self.ldtfrom.text()) is False:
            vis_msg.print("ERROR in RtrvSeisProp: No NumPy selected for retrieval", type='error')
            return
        #
        try:
            self.npydata = np.load(self.ldtfrom.text()).item()
            if ('SeisInfo' not in self.npydata.keys())\
                    or (seis_ays.checkSeisInfo(self.npydata['SeisInfo']) is False):
                vis_msg.print("ERROR in RtrvSeisProp: NumPy dictionary contains no information about seismic survey",
                              type='error')
                QtWidgets.QMessageBox.critical(self.msgbox,
                                               'Retrieve Seismic Property',
                                               'NumPy dictionary contains no inforamtion about seismic')
                return
            self.npyinfo = self.npydata['SeisInfo']
            self.npydata.pop('SeisInfo')
            for key in self.npydata.keys():
                if checkSeisData(self.npydata[key], self.npyinfo) is False:
                    self.npydata.pop(key)
        except ValueError:
            _npydata = np.load(self.ldtfrom.text())
            _filename = os.path.splitext(os.path.basename(self.ldtfrom.text()))[0]
            if np.ndim(_npydata)<=1 or np.ndim(_npydata)>=4:
                vis_msg.print("ERROR in RtrvSeisProp: NumPy matrix shall be 2D or 3D", type='error')
                QtWidgets.QMessageBox.critical(self.msgbox,
                                               'Retrieve Seismic Property',
                                               'NumPy matrix shall be 2D or 3D')
                return
            if np.ndim(_npydata) == 2:
                if np.shape(_npydata)[1] < 4:
                    vis_msg.print("ERROR in RtrvSeisProp: 2D NumPy matrix shall contain at least 4 columns",
                                  type='error')
                    QtWidgets.QMessageBox.critical(self.msgbox,
                                                   'Retrieve Seismic Property',
                                                   '2D NumPy matrix shall contain at least 4 columns')
                    return
                self.npyinfo = seis_ays.getSeisInfoFrom2DMat(_npydata)
                _npydata = np.transpose(np.reshape(_npydata[:, 3:4], [self.npyinfo['ILNum'],
                                                                      self.npyinfo['XLNum'],
                                                                      self.npyinfo['ZNum']]), [2, 1, 0])
            if np.ndim(_npydata) == 3:
                self.npyinfo = seis_ays.createSeisInfoFrom3DMat(_npydata)
                _npydata = _npydata

            self.npydata = {}
            self.npydata[_filename] = _npydata
        #
        if seis_ays.checkSeisInfo(self.npyinfo) is False:
            vis_msg.print("ERROR in RtrvSeisProp: Selected not seismic numpy", type='error')
            QtWidgets.QMessageBox.critical(self.msgbox,
                                           'Retrieve Seismic Property',
                                           'Selected not seismic numpy')
            return
        #
        _firstattrib = None
        for i in sorted(self.npydata.keys()):
            item = QtWidgets.QListWidgetItem(self.lwgattrib)
            item.setText(i)
            self.lwgattrib.addItem(item)
            if _firstattrib is None:
                _firstattrib = item
        self.lwgattrib.setCurrentItem(_firstattrib)


    def clickBtnFrom(self):
        self.refreshMsgBox()
        #
        _dialog = QtWidgets.QFileDialog()
        _file = _dialog.getOpenFileName(None, 'Select Seismic NumPy', self.rootpath,
                                        filter="NumPy files (*.npy);; All files (*.*)")
        if len(_file[0]) > 0:
            self.ldtfrom.setText(_file[0])



    def clickBtnRtrvSeisProp(self):
        self.refreshMsgBox()
        #
        _attriblist = self.lwgattrib.selectedItems()
        if len(_attriblist) < 1:
            vis_msg.print("ERROR in RtrvSeisProb: No property selected for retrieval", type='error')
            QtWidgets.QMessageBox.critical(self.msgbox,
                                           'Retrieve Seismic Property',
                                           'No property selected for export')
            return
        if self.checkPointData() is False:
            vis_msg.print("ERROR in RtrvSeisProp: No point loaded for retrieval", type='error')
            QtWidgets.QMessageBox.critical(self.msgbox,
                                           'Retrieve Seismic Property',
                                           'No point loaded for retrieval')
            return
        #
        _wdinl = basic_data.str2int(self.ldtdimsinl.text())
        _wdxl = basic_data.str2int(self.ldtdimsxl.text())
        _wdz = basic_data.str2int(self.ldtdimsz.text())
        if _wdinl is False or _wdxl is False or _wdz is False:
            vis_msg.print("ERROR in RtrvSeisProp: Non-integer retrieval window", type='error')
            QtWidgets.QMessageBox.critical(self.msgbox,
                                           'Retrieve Seismic Property',
                                           'Non-integer retrieval window')
            return
        if _wdinl < 0 or _wdxl < 0 or _wdz < 0:
            vis_msg.print("ERROR in RtrvSeisProp: Non-positive retrieval window", type='error')
            QtWidgets.QMessageBox.critical(self.msgbox,
                                           'Retrieve Seismic Property',
                                           'Non-positive retrieval window')
            return
        #
        _wdsize = (2*_wdinl+1)*(2*_wdxl+1)*(2*_wdz+1)
        #
        # Progress dialog
        _pgsdlg = QtWidgets.QProgressDialog()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(os.path.join(self.iconpath, "icons/retrieve.png")),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        _pgsdlg.setWindowIcon(icon)
        _pgsdlg.setWindowTitle('Retrieve Seismic Property')
        _pgsdlg.setCancelButton(None)
        _pgsdlg.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        _pgsdlg.forceShow()
        _pgsdlg.setFixedWidth(400)
        #
        _targetdata = basic_mdt.exportMatDict(self.pointdata, ['Inline', 'Crossline', 'Z'])
        #
        for i in range(len(_attriblist)):
            #
            _pgsdlg.setWindowTitle('Retrieve ' + str(i + 1) + ' of ' + str(len(_attriblist)) + ' Property')
            #
            print("RtrvSeisProp: Retrieve %d of %d Properties: %s" % (i + 1, len(_attriblist), _attriblist[i].text()))
            _npydata = self.npydata[_attriblist[i].text()]
            _data = seis_ays.retrieveSeisWindowFrom3DMat(_npydata, _targetdata, seisinfo=self.npyinfo,
                                                         wdinl=_wdinl, wdxl=_wdxl, wdz=_wdz,
                                                         verbose=False, qpgsdlg=_pgsdlg)
            _data = _data[:, 3:3+_wdsize]
            _data = np.mean(_data, axis=1)
            _data = np.reshape(_data, [-1, 1])
            self.pointdata[_attriblist[i].text()] = np.reshape(_data, [-1, 1])
            #
            # _pgsdlg.setValue(i + 1)
            #
        #
        QtWidgets.QMessageBox.information(self.msgbox,
                                          "Retrieve Seismic Property",
                                          str(len(_attriblist)) + " properties retrieved successfully")
        return


    def refreshMsgBox(self):
        _center_x = self.dialog.geometry().center().x()
        _center_y = self.dialog.geometry().center().y()
        self.msgbox.setGeometry(QtCore.QRect(_center_x - 150, _center_y - 50, 300, 100))


    def checkPointData(self):
        return point_ays.checkPoint(self.pointdata)


def checkSeisData(seisdata, survinfo={}):
    return seis_ays.isSeis3DMatConsistentWithSeisInfo(seisdata, survinfo)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RtrvSeisProp = QtWidgets.QWidget()
    gui = rtrvseisprop()
    gui.setupGUI(RtrvSeisProp)
    RtrvSeisProp.show()
    sys.exit(app.exec_())