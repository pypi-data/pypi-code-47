# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms/data_config.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DataConfigForm(object):
    def setupUi(self, DataConfigForm):
        DataConfigForm.setObjectName("DataConfigForm")
        DataConfigForm.resize(311, 253)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DataConfigForm.sizePolicy().hasHeightForWidth())
        DataConfigForm.setSizePolicy(sizePolicy)
        DataConfigForm.setStyleSheet("")
        self.gridLayout = QtWidgets.QGridLayout(DataConfigForm)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pixelScaleLabel = QtWidgets.QLabel(DataConfigForm)
        self.pixelScaleLabel.setObjectName("pixelScaleLabel")
        self.horizontalLayout.addWidget(self.pixelScaleLabel)
        self.pixelScaleLineEdit = QtWidgets.QLineEdit(DataConfigForm)
        self.pixelScaleLineEdit.setObjectName("pixelScaleLineEdit")
        self.horizontalLayout.addWidget(self.pixelScaleLineEdit)
        self.pixelScaleUnitsLabel = QtWidgets.QLabel(DataConfigForm)
        self.pixelScaleUnitsLabel.setObjectName("pixelScaleUnitsLabel")
        self.horizontalLayout.addWidget(self.pixelScaleUnitsLabel)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.fullFrameGroupBox = QtWidgets.QGroupBox(DataConfigForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fullFrameGroupBox.sizePolicy().hasHeightForWidth())
        self.fullFrameGroupBox.setSizePolicy(sizePolicy)
        self.fullFrameGroupBox.setObjectName("fullFrameGroupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.fullFrameGroupBox)
        self.verticalLayout.setContentsMargins(-1, 12, -1, 15)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.sigmaScaleLabel = QtWidgets.QLabel(self.fullFrameGroupBox)
        self.sigmaScaleLabel.setObjectName("sigmaScaleLabel")
        self.horizontalLayout_2.addWidget(self.sigmaScaleLabel)
        self.sigmaScaleLineEdit = QtWidgets.QLineEdit(self.fullFrameGroupBox)
        self.sigmaScaleLineEdit.setObjectName("sigmaScaleLineEdit")
        self.horizontalLayout_2.addWidget(self.sigmaScaleLineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.minimumNumPixelsLabel = QtWidgets.QLabel(self.fullFrameGroupBox)
        self.minimumNumPixelsLabel.setObjectName("minimumNumPixelsLabel")
        self.horizontalLayout_3.addWidget(self.minimumNumPixelsLabel)
        self.minimumNumPixelsLineEdit = QtWidgets.QLineEdit(self.fullFrameGroupBox)
        self.minimumNumPixelsLineEdit.setObjectName("minimumNumPixelsLineEdit")
        self.horizontalLayout_3.addWidget(self.minimumNumPixelsLineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.gridLayout.addWidget(self.fullFrameGroupBox, 1, 0, 1, 1)
        self.roiFrameGroupBox = QtWidgets.QGroupBox(DataConfigForm)
        self.roiFrameGroupBox.setObjectName("roiFrameGroupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.roiFrameGroupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.thresholdFactorLabel = QtWidgets.QLabel(self.roiFrameGroupBox)
        self.thresholdFactorLabel.setObjectName("thresholdFactorLabel")
        self.horizontalLayout_4.addWidget(self.thresholdFactorLabel)
        self.thresholdFactorLineEdit = QtWidgets.QLineEdit(self.roiFrameGroupBox)
        self.thresholdFactorLineEdit.setObjectName("thresholdFactorLineEdit")
        self.horizontalLayout_4.addWidget(self.thresholdFactorLineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.gridLayout.addWidget(self.roiFrameGroupBox, 2, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 3, 0, 1, 1)
        self.pixelScaleLabel.setBuddy(self.pixelScaleLineEdit)

        self.retranslateUi(DataConfigForm)
        QtCore.QMetaObject.connectSlotsByName(DataConfigForm)

    def retranslateUi(self, DataConfigForm):
        _translate = QtCore.QCoreApplication.translate
        DataConfigForm.setWindowTitle(_translate("DataConfigForm", "Form"))
        self.pixelScaleLabel.setToolTip(_translate("DataConfigForm", "Pixel scale in arcseconds per pixel of the optical system in front of the camera."))
        self.pixelScaleLabel.setText(_translate("DataConfigForm", "Pixel Scale:"))
        self.pixelScaleLineEdit.setToolTip(_translate("DataConfigForm", "Valid Range: 0 to 1e200 with a precision of 5"))
        self.pixelScaleUnitsLabel.setText(_translate("DataConfigForm", "arcsec/pixel"))
        self.fullFrameGroupBox.setTitle(_translate("DataConfigForm", "Full Frame"))
        self.sigmaScaleLabel.setToolTip(_translate("DataConfigForm", "Multiplier for the frame standard deviation."))
        self.sigmaScaleLabel.setText(_translate("DataConfigForm", "Sigma Scale:"))
        self.minimumNumPixelsLabel.setToolTip(_translate("DataConfigForm", "The minimum number of pixels that must be in a center-of-mass object."))
        self.minimumNumPixelsLabel.setText(_translate("DataConfigForm", "Min Num Pixels:"))
        self.roiFrameGroupBox.setTitle(_translate("DataConfigForm", "ROI Frame"))
        self.thresholdFactorLabel.setToolTip(_translate("DataConfigForm", "The scale factor multiplied by the frame max and then subtracted from the frame."))
        self.thresholdFactorLabel.setText(_translate("DataConfigForm", "Threshold Factor:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DataConfigForm = QtWidgets.QWidget()
    ui = Ui_DataConfigForm()
    ui.setupUi(DataConfigForm)
    DataConfigForm.show()
    sys.exit(app.exec_())
