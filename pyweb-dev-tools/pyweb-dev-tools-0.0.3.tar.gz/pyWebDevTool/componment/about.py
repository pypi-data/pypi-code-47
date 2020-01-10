# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(500, 300)
        Dialog.setMinimumSize(QtCore.QSize(500, 300))
        Dialog.setMaximumSize(QtCore.QSize(500, 300))
        Dialog.setStyleSheet("QDialog{\n"
"background-color: #F0F0F0;\n"
"border: 1px solid #edeff0;\n"
"}\n"
"QPushButton{\n"
"    color: #515a6e;\n"
"    background-color: #fff;\n"
"    border: 1px solid transparent;\n"
"    border-color: #dcdee2;\n"
"    height: 32px;\n"
"    padding: 0 15px;\n"
"    font-size: 14px;\n"
"    border-radius: 4px;\n"
"    display: inline-block;\n"
"    margin-bottom: 0;\n"
"    font-weight: 400;\n"
"    text-align: center;\n"
"    vertical-align: middle;\n"
"    min-width:60px;\n"
"    transition: color .2s linear,background-color .2s linear,border .2s linear,box-shadow .2s linear;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: #57a3f3;\n"
"    background-color: #fff;\n"
"    border-color: #57a3f3;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: #fff;\n"
"    border-color: #2b85e4;\n"
"}")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(50, 40, 50, 20)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setMinimumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMaximumSize(QtCore.QSize(150, 16777215))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.setStretch(0, 5)
        self.verticalLayout.setStretch(1, 1)
        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">pyweb-dev-tool工具套件</p><p align=\"center\">版本号:v1.0.0 </p><p align=\"center\">作者：尼罗河的赠礼</p><p align=\"center\">QQ:250985725</p><p align=\"center\">博客地址: <a href=\"https://blog.csdn.net/v2sking\"><span style=\" text-decoration: underline; color:#0000ff;\">https://blog.csdn.net/v2sking</span></a></p><p align=\"center\">项目地址：<a href=\"https://gitee.com/luanhaoyu_admin/pyqt-destop-app\"><span style=\" text-decoration: underline; color:#0000ff;\">https://gitee.com/luanhaoyu_admin/pyqt-destop-app</span></a></p><p align=\"center\"><br/></p><p align=\"center\"><br/></p></body></html>"))
        self.pushButton.setText(_translate("Dialog", "确定"))

