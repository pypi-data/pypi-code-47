# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(964, 600)
        Form.setStyleSheet("QPushButton#pushButton_min,QPushButton#pushButton_max,QPushButton#pushButton_restore,QPushButton#pushButton_close{\n"
"background-color: #2db7f5;\n"
"border-top-left-radius:0px;\n"
"border-top-right-radius:0px;\n"
"border-bottom-right-radius:4px;\n"
"border-bottom-left-radius:4px;\n"
"border:1px solid #2db7f5;\n"
"}\n"
"QPushButton#pushButton_min{\n"
"image: url(:/image/resources/image/minimize.png);\n"
"}\n"
"\n"
"QPushButton#pushButton_max{\n"
"image: url(:/image/resources/image/maximize.png);\n"
"}\n"
"\n"
"QPushButton#pushButton_restore{\n"
"image: url(:/image/resources/image/restore.png);\n"
"}\n"
"\n"
"QPushButton#pushButton_close{\n"
"image: url(:/image/resources/image/close.png);\n"
"background-color: #ed4014;\n"
"border-color: #ed4014;\n"
"\n"
"}\n"
"\n"
"QPushButton#pushButton_min:hover,QPushButton#pushButton_max:hover,QPushButton#pushButton_restore:hover{\n"
"background-color: #57c5f7;\n"
"}\n"
"\n"
"QPushButton#pushButton_close:hover{\n"
"background-color: #f16643;\n"
"border-color: #f16643;\n"
"\n"
"}\n"
"\n"
"QWidget#title{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.403409 rgba(45, 140, 240, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QLabel#label_icon{\n"
"image: url(:/image/resources/image/frog.png);\n"
"}\n"
"")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.title = QtWidgets.QWidget(Form)
        self.title.setMinimumSize(QtCore.QSize(0, 25))
        self.title.setMaximumSize(QtCore.QSize(16777215, 25))
        self.title.setStyleSheet("")
        self.title.setObjectName("title")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.title)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(10, -1, -1, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, 1)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_icon = QtWidgets.QLabel(self.title)
        self.label_icon.setMinimumSize(QtCore.QSize(15, 15))
        self.label_icon.setMaximumSize(QtCore.QSize(15, 15))
        self.label_icon.setText("")
        self.label_icon.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_icon.setObjectName("label_icon")
        self.horizontalLayout_3.addWidget(self.label_icon)
        self.label = QtWidgets.QLabel(self.title)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(0, 0, 5, 5)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_min = QtWidgets.QPushButton(self.title)
        self.pushButton_min.setMinimumSize(QtCore.QSize(35, 20))
        self.pushButton_min.setMaximumSize(QtCore.QSize(16777215, 20))
        self.pushButton_min.setStyleSheet("")
        self.pushButton_min.setText("")
        self.pushButton_min.setObjectName("pushButton_min")
        self.horizontalLayout.addWidget(self.pushButton_min)
        self.pushButton_restore = QtWidgets.QPushButton(self.title)
        self.pushButton_restore.setMinimumSize(QtCore.QSize(35, 20))
        self.pushButton_restore.setMaximumSize(QtCore.QSize(16777215, 20))
        self.pushButton_restore.setText("")
        self.pushButton_restore.setObjectName("pushButton_restore")
        self.horizontalLayout.addWidget(self.pushButton_restore)
        self.pushButton_max = QtWidgets.QPushButton(self.title)
        self.pushButton_max.setMinimumSize(QtCore.QSize(35, 20))
        self.pushButton_max.setMaximumSize(QtCore.QSize(16777215, 20))
        self.pushButton_max.setText("")
        self.pushButton_max.setObjectName("pushButton_max")
        self.horizontalLayout.addWidget(self.pushButton_max)
        self.pushButton_close = QtWidgets.QPushButton(self.title)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_close.sizePolicy().hasHeightForWidth())
        self.pushButton_close.setSizePolicy(sizePolicy)
        self.pushButton_close.setMinimumSize(QtCore.QSize(35, 20))
        self.pushButton_close.setMaximumSize(QtCore.QSize(16777215, 20))
        self.pushButton_close.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_close.setStyleSheet("")
        self.pushButton_close.setText("")
        self.pushButton_close.setObjectName("pushButton_close")
        self.horizontalLayout.addWidget(self.pushButton_close)
        self.horizontalLayout_4.addLayout(self.horizontalLayout)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)
        self.verticalLayout_2.addWidget(self.title)
        self.menu_widget = QtWidgets.QWidget(Form)
        self.menu_widget.setMinimumSize(QtCore.QSize(0, 25))
        self.menu_widget.setObjectName("menu_widget")
        self.verticalLayout_2.addWidget(self.menu_widget)
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setMinimumSize(QtCore.QSize(0, 43))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        self.tabWidget.setFont(font)
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Python Tool"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "首页"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Tab 2"))

