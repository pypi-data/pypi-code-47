#############################################################################################
#                                                                                           #
# Author:   GeoPy Team                                                                      #
# Email:    geopy.info@gmail.com                                                            #
# Date:     March 2018                                                                      #
#                                                                                           #
#############################################################################################

# Create a window for view information about GeoPy


from PyQt5 import QtCore, QtGui, QtWidgets
import sys, os
#
sys.path.append(os.path.dirname(__file__)[:-4][:-4][:-13])

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

class about(object):

    rootpath = ''
    #
    iconpath = os.path.dirname(__file__)

    def setupGUI(self, About):
        About.setObjectName("About")
        About.setFixedSize(430, 230)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(os.path.join(self.iconpath, "icons/about.png")),
                       QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        About.setWindowIcon(icon)
        self.lblicon = QtWidgets.QLabel(About)
        self.lblicon.setObjectName("lblicon")
        self.lblicon.setGeometry(QtCore.QRect(30, 30, 100, 100))
        self.lbltitle = QtWidgets.QLabel(About)
        self.lbltitle.setObjectName("lbltitle")
        self.lbltitle.setGeometry(QtCore.QRect(150, 30, 320, 40))
        self.lbldate = QtWidgets.QLabel(About)
        self.lbldate.setObjectName("lbldate")
        self.lbldate.setGeometry(QtCore.QRect(150, 70, 320, 60))
        self.lblcopyright = QtWidgets.QLabel(About)
        self.lblcopyright.setObjectName("lblcopyright")
        self.lblcopyright.setGeometry(QtCore.QRect(150, 130, 320, 60))
        self.lbllink = QtWidgets.QLabel(About)
        self.lbllink.setObjectName("lbllink")
        self.lbllink.setGeometry(QtCore.QRect(275, 131, 70, 30))
        self.lblqr = QtWidgets.QLabel(About)
        self.lblqr.setObjectName("lblqr")
        self.lblqr.setGeometry(QtCore.QRect(340, 140, 80, 80))
        #
        self.retranslateGUI(About)
        QtCore.QMetaObject.connectSlotsByName(About)


    def retranslateGUI(self, About):
        _translate = QtCore.QCoreApplication.translate
        About.setWindowTitle(_translate("About", "About Cognitive Geo"))
        self.lblicon.setPixmap(QtGui.QPixmap(os.path.join(self.iconpath, "icons/logo.png")).scaled(80, 80, QtCore.Qt.KeepAspectRatio))
        self.lblicon.setAlignment(QtCore.Qt.AlignCenter)
        self.lbltitle.setText(_translate("About", "Cognitive Geo"))
        self.lbltitle.setFont(QtGui.QFont("Helvetica", 16, QtGui.QFont.Bold))
        self.lbltitle.setAlignment(QtCore.Qt.AlignTop)
        self.lbldate.setText(_translate("About", "Version 1.1\nBuilt on PyQt5, Vispy, Numpy, Matlibplot, Scipy"))
        self.lblcopyright.setText(_translate("About", "Copyright (C) 2018-2020          \n\n\tMore information? Scan me"))
        self.lbllink.setText(_translate("About", '<a href="https://www.linkedin.com/in/geopy-team-182b27185/">GeoPy Team</a>'))
        self.lbllink.setOpenExternalLinks(True)
        self.lblqr.setPixmap(
            QtGui.QPixmap(os.path.join(self.iconpath, "icons/qrcode.png")).scaled(80, 80, QtCore.Qt.KeepAspectRatio))
        self.lblqr.setAlignment(QtCore.Qt.AlignCenter)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    About = QtWidgets.QWidget()
    gui = about()
    gui.setupGUI(About)
    About.show()
    sys.exit(app.exec_())