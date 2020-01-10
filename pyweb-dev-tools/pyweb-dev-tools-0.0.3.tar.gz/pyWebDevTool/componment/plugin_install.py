# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'plugin_install.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(450, 217)
        Dialog.setMinimumSize(QtCore.QSize(450, 217))
        Dialog.setMaximumSize(QtCore.QSize(450, 217))
        Dialog.setStyleSheet("QDialog{\n"
"background-color: #F0F0F0;\n"
"border: 1px solid #edeff0;\n"
"}\n"
"\n"
"QPushButton{\n"
"    color: #fff;\n"
"    background-color: gray;\n"
"    height: 32px;\n"
"    padding: 0 15px;\n"
"    font-size: 14px;\n"
"    border-radius: 4px;\n"
"    border: 1px solid transparent;\n"
"    display: inline-block;\n"
"    margin-bottom: 0;\n"
"    font-weight: 400;\n"
"    text-align: center;\n"
"    vertical-align: middle;\n"
"    border-radius:5px;\n"
"    transition: color .2s linear,background-color .2s linear,border .2s linear,box-shadow .2s linear;\n"
"}\n"
"\n"
"QPushButton#pushButton_ok{\n"
"    color: #fff;\n"
"    background-color: #2d8cf0;\n"
"    border-color: #2d8cf0;\n"
"}\n"
"\n"
"QPushButton#pushButton_ok:pressed{\n"
"    background-color: #2b85e4;\n"
"    border-color: #2b85e4;\n"
"}\n"
"\n"
"QPushButton#pushButton_ok:hover{\n"
"    background-color: #57a3f3;\n"
"    border-color: #57a3f3;\n"
"}\n"
"\n"
"QPushButton#pushButton_cancel,QPushButton#pushButton_choose_file{\n"
"    color: #515a6e;\n"
"    background-color: #fff;\n"
"    border-color: #dcdee2;\n"
"}\n"
"\n"
"QPushButton#pushButton_cancel:hover,QPushButton#pushButton_choose_file:hover{\n"
"    color: #57a3f3;\n"
"    background-color: #fff;\n"
"    border-color: #57a3f3;\n"
"}\n"
"\n"
"QPushButton#pushButton_cancel:pressed,QPushButton#pushButton_choose_file:pressed{\n"
"    background-color: #fff;\n"
"    border-color: #2b85e4;\n"
"}")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(0, -1, 0, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButton_file = QtWidgets.QRadioButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.radioButton_file.setFont(font)
        self.radioButton_file.setChecked(True)
        self.radioButton_file.setObjectName("radioButton_file")
        self.buttonGroup = QtWidgets.QButtonGroup(Dialog)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.radioButton_file)
        self.horizontalLayout.addWidget(self.radioButton_file)
        self.radioButton_addr = QtWidgets.QRadioButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.radioButton_addr.setFont(font)
        self.radioButton_addr.setObjectName("radioButton_addr")
        self.buttonGroup.addButton(self.radioButton_addr)
        self.horizontalLayout.addWidget(self.radioButton_addr)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setMinimumSize(QtCore.QSize(50, 100))
        self.widget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.widget.setObjectName("widget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_5.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.edit = QtWidgets.QLineEdit(self.widget)
        self.edit.setMinimumSize(QtCore.QSize(0, 32))
        self.edit.setAccessibleName("")
        self.edit.setInputMask("")
        self.edit.setText("")
        self.edit.setObjectName("edit")
        self.horizontalLayout_4.addWidget(self.edit)
        self.pushButton_choose_file = QtWidgets.QPushButton(self.widget)
        self.pushButton_choose_file.setMinimumSize(QtCore.QSize(0, 27))
        self.pushButton_choose_file.setObjectName("pushButton_choose_file")
        self.horizontalLayout_4.addWidget(self.pushButton_choose_file)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.verticalLayout_2.setStretch(0, 1)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)
        self.verticalLayout.addWidget(self.widget)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_ok = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_ok.setFont(font)
        self.pushButton_ok.setObjectName("pushButton_ok")
        self.horizontalLayout_2.addWidget(self.pushButton_ok)
        self.pushButton_cancel = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_cancel.setFont(font)
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.horizontalLayout_2.addWidget(self.pushButton_cancel)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 2)
        self.verticalLayout.setStretch(3, 1)
        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "安装插件"))
        self.radioButton_file.setText(_translate("Dialog", "上传插件包"))
        self.radioButton_addr.setText(_translate("Dialog", "输入插件地址"))
        self.edit.setPlaceholderText(_translate("Dialog", "选择插件包"))
        self.pushButton_choose_file.setText(_translate("Dialog", "选择"))
        self.pushButton_ok.setText(_translate("Dialog", "确定"))
        self.pushButton_cancel.setText(_translate("Dialog", "取消"))

