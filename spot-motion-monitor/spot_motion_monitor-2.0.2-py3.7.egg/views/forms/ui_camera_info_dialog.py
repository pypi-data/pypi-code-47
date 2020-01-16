# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms/camera_info_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CameraInformationDialog(object):
    def setupUi(self, CameraInformationDialog):
        CameraInformationDialog.setObjectName("CameraInformationDialog")
        CameraInformationDialog.resize(174, 164)
        self.verticalLayout = QtWidgets.QVBoxLayout(CameraInformationDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.cameraInfoTextBrowser = QtWidgets.QTextBrowser(CameraInformationDialog)
        self.cameraInfoTextBrowser.setMinimumSize(QtCore.QSize(150, 100))
        self.cameraInfoTextBrowser.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.cameraInfoTextBrowser.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.cameraInfoTextBrowser.setObjectName("cameraInfoTextBrowser")
        self.verticalLayout.addWidget(self.cameraInfoTextBrowser)
        self.buttonBox = QtWidgets.QDialogButtonBox(CameraInformationDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(CameraInformationDialog)
        self.buttonBox.accepted.connect(CameraInformationDialog.accept)
        QtCore.QMetaObject.connectSlotsByName(CameraInformationDialog)

    def retranslateUi(self, CameraInformationDialog):
        _translate = QtCore.QCoreApplication.translate
        CameraInformationDialog.setWindowTitle(_translate("CameraInformationDialog", "Camera Info"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CameraInformationDialog = QtWidgets.QDialog()
    ui = Ui_CameraInformationDialog()
    ui.setupUi(CameraInformationDialog)
    CameraInformationDialog.show()
    sys.exit(app.exec_())
