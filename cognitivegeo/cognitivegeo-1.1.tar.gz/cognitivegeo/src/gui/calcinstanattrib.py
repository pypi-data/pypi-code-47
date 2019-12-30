#############################################################################################
#                                                                                           #
# Author:   GeoPy Team                                                                      #
# Email:    geopy.info@gmail.com                                                            #
# Date:     September 2018                                                                  #
#                                                                                           #
#############################################################################################

# Create a window for calculating seismic attribute (instantaneous)


from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
import os, sys
#
sys.path.append(os.path.dirname(__file__)[:-4][:-4][:-13])
from cognitivegeo.src.seismic.analysis import analysis as seis_ays
from cognitivegeo.src.seismic.attribute import attribute as seis_attrib
from cognitivegeo.src.vis.messager import messager as vis_msg

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class calcinstanattrib(object):

    survinfo = {}
    seisdata = {}
    rootpath = ''
    #
    iconpath = os.path.dirname(__file__)
    dialog = None
    #
    instanattriblist = ['Envelop', 'Quadrature', 'Phase', 'Frequency', 'Cosine of Phase']


    def setupGUI(self, CalcInstanAttrib):
        CalcInstanAttrib.setObjectName("CalcInstanAttrib")
        CalcInstanAttrib.setFixedSize(500, 420)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(os.path.join(self.iconpath, "icons/hilbert.png")),
                       QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        CalcInstanAttrib.setWindowIcon(icon)
        #
        self.lblproperty = QtWidgets.QLabel(CalcInstanAttrib)
        self.lblproperty.setObjectName("lblproperty")
        self.lblproperty.setGeometry(QtCore.QRect(10, 10, 150, 30))
        self.lwgproperty = QtWidgets.QListWidget(CalcInstanAttrib)
        self.lwgproperty.setObjectName("lwgproperty")
        self.lwgproperty.setGeometry(QtCore.QRect(10, 50, 480, 200))
        self.lwgproperty.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.lblattrib = QtWidgets.QLabel(CalcInstanAttrib)
        self.lblattrib.setObjectName("lblattrib")
        self.lblattrib.setGeometry(QtCore.QRect(10, 270, 230, 30))
        self.cbbattrib = QtWidgets.QComboBox(CalcInstanAttrib)
        self.cbbattrib.setObjectName("cbbattrib")
        self.cbbattrib.setGeometry(QtCore.QRect(10, 310, 230, 30))
        self.lblname = QtWidgets.QLabel(CalcInstanAttrib)
        self.lblname.setObjectName("lblname")
        self.lblname.setGeometry(QtCore.QRect(310, 310, 80, 30))
        self.ldtname = QtWidgets.QLineEdit(CalcInstanAttrib)
        self.ldtname.setObjectName("ldtname")
        self.ldtname.setGeometry(QtCore.QRect(390, 310, 100, 30))
        self.btnapply = QtWidgets.QPushButton(CalcInstanAttrib)
        self.btnapply.setObjectName("btnapply")
        self.btnapply.setGeometry(QtCore.QRect(200, 370, 100, 30))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(os.path.join(self.iconpath, "icons/ok.png")),
                       QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        self.btnapply.setIcon(icon)
        #
        self.msgbox = QtWidgets.QMessageBox(CalcInstanAttrib)
        self.msgbox.setObjectName("msgbox")
        _center_x = CalcInstanAttrib.geometry().center().x()
        _center_y = CalcInstanAttrib.geometry().center().y()
        self.msgbox.setGeometry(QtCore.QRect(_center_x - 150, _center_y - 50, 300, 100))
        #
        self.retranslateGUI(CalcInstanAttrib)
        QtCore.QMetaObject.connectSlotsByName(CalcInstanAttrib)


    def retranslateGUI(self, CalcInstanAttrib):
        self.dialog = CalcInstanAttrib
        #
        _translate = QtCore.QCoreApplication.translate
        CalcInstanAttrib.setWindowTitle(_translate("CalcInstanAttrib", "Calculate Instantaneous Attribute"))
        self.lblproperty.setText(_translate("CalcInstanAttrib", "Select target property:"))
        self.lblattrib.setText(_translate("CalcInstanAttrib", "Select attribute:"))
        self.cbbattrib.addItems(self.instanattriblist)
        self.cbbattrib.currentIndexChanged.connect(self.changeCbbAttrib)
        self.lblname.setText(_translate("CalcInstanAttrib", "Output name:"))
        self.ldtname.setText(_translate("CalcInstanAttrib", "Envelop"))
        self.btnapply.setText(_translate("CalcInstanAttrib", "Apply"))
        self.btnapply.clicked.connect(self.clickBtnCalcInstanAttrib)
        #
        self.refreshLwgProperty()


    def changeCbbAttrib(self):
        if self.cbbattrib.currentIndex() == 0:
            self.ldtname.setText('Envelop')
        if self.cbbattrib.currentIndex() == 1:
            self.ldtname.setText('Quadrature')
        if self.cbbattrib.currentIndex() == 2:
            self.ldtname.setText('Phase')
        if self.cbbattrib.currentIndex() == 3:
            self.ldtname.setText('Frequency')
        if self.cbbattrib.currentIndex() == 4:
            self.ldtname.setText('CosPhase')


    def clickBtnCalcInstanAttrib(self):
        self.refreshMsgBox()
        #
        _propertylist = self.lwgproperty.selectedItems()
        if len(_propertylist) < 1:
            vis_msg.print("Error in CalcInstanAttrib: No property selected for attribute analysis", type='error')
            QtWidgets.QMessageBox.critical(self.msgbox,
                                           'Calculate Instantaneous Attribute',
                                           'No property selected for attribute analysis')
            return
        if len(self.ldtname.text()) < 1:
            vis_msg.print("Error in CalcInstanAttrib: No name specified for output attribute", type='error')
            QtWidgets.QMessageBox.critical(self.msgbox,
                                           'Calculate Instantaneous Attribute',
                                           'No name specified for output attribute')
            return
        if self.ldtname.text() in self.seisdata.keys() and self.checkSeisData(self.ldtname.text()):
            reply = QtWidgets.QMessageBox.question(self.msgbox, 'Calculate Instantaneous Attribute',
                                                   self.ldtname.text() + ' already exists. Overwrite?',
                                                   QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                   QtWidgets.QMessageBox.No)

            if reply == QtWidgets.QMessageBox.No:
                return
        #
        _seisdata = self.seisdata[_propertylist[0].text()]
        #
        _attrib = np.zeros(np.shape(_seisdata))
        if self.cbbattrib.currentIndex() == 0:
            _attrib = seis_attrib.calcInstanEnvelop(_seisdata)
        if self.cbbattrib.currentIndex() == 1:
            _attrib = seis_attrib.calcInstanQuadrature(_seisdata)
        if self.cbbattrib.currentIndex() == 2:
            _attrib = seis_attrib.calcInstanPhase(_seisdata)
        if self.cbbattrib.currentIndex() == 3:
            _attrib = seis_attrib.calcInstanFrequency(_seisdata)
        if self.cbbattrib.currentIndex() == 4:
            _attrib = seis_attrib.calcInstanCosPhase(_seisdata)
        self.seisdata[self.ldtname.text()] = _attrib
        #
        self.refreshLwgProperty()
        #
        QtWidgets.QMessageBox.information(self.msgbox,
                                          "Calculate Instantaneous Attribute",
                                          self.instanattriblist[self.cbbattrib.currentIndex()] + " calculated successfully")
        return


    def refreshLwgProperty(self):
        self.lwgproperty.clear()
        if self.checkSurvInfo() is True:
            for i in sorted(self.seisdata.keys()):
                if self.checkSeisData(i) is True:
                    item = QtWidgets.QListWidgetItem(self.lwgproperty)
                    item.setText(i)
                    self.lwgproperty.addItem(item)


    def refreshMsgBox(self):
        _center_x = self.dialog.geometry().center().x()
        _center_y = self.dialog.geometry().center().y()
        self.msgbox.setGeometry(QtCore.QRect(_center_x - 150, _center_y - 50, 300, 100))


    def checkSurvInfo(self):
        self.refreshMsgBox()
        #
        if seis_ays.checkSeisInfo(self.survinfo) is False:
            # print("CalcInstanAttrib: Survey not found")
            # QtWidgets.QMessageBox.critical(self.msgbox,
            #                                'Calculate Math Attribute from Single Property',
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
    CalcInstanAttrib = QtWidgets.QWidget()
    gui = calcinstanattrib()
    gui.setupGUI(CalcInstanAttrib)
    CalcInstanAttrib.show()
    sys.exit(app.exec_())