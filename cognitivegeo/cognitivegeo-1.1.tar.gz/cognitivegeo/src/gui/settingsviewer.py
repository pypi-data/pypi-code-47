#############################################################################################
#                                                                                           #
# Author:   GeoPy Team                                                                      #
# Email:    geopy.info@gmail.com                                                            #
# Date:     November 2019                                                                   #
#                                                                                           #
#############################################################################################

# Create a GUI for settings (3d viewer)

from PyQt5 import QtCore, QtGui, QtWidgets
import os, sys
#
sys.path.append(os.path.dirname(__file__)[:-4][:-4][:-13])
from cognitivegeo.src.core.settings import settings as core_set
from cognitivegeo.src.vis.viewer3d import viewer3d as vis_viewer3d
from cognitivegeo.src.vis.player import player as vis_player

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class settingsviewer(object):

    settings = core_set.Viewer
    #
    iconpath = os.path.dirname(__file__)
    dialog = None


    def setupGUI(self, SettingsViewer):
        SettingsViewer.setObjectName("SettingsViewer")
        SettingsViewer.setFixedSize(840, 310)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(os.path.join(self.iconpath, "icons/dice.png")),
                       QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        SettingsViewer.setWindowIcon(icon)
        #
        self.lblviewer3d = QtWidgets.QLabel(SettingsViewer)
        self.lblviewer3d.setObjectName("lblviewer3d")
        self.lblviewer3d.setGeometry(QtCore.QRect(10, 20, 50, 30))
        #
        self.lblgohome = QtWidgets.QLabel(SettingsViewer)
        self.lblgohome.setObjectName("lblgohome")
        self.lblgohome.setGeometry(QtCore.QRect(30, 60, 60, 30))
        self.cbbgohome = QtWidgets.QComboBox(SettingsViewer)
        self.cbbgohome.setObjectName("cbbgohome")
        self.cbbgohome.setGeometry(QtCore.QRect(100, 60, 100, 30))
        #
        self.lblviewfrom = QtWidgets.QLabel(SettingsViewer)
        self.lblviewfrom.setObjectName("lblviewfrom")
        self.lblviewfrom.setGeometry(QtCore.QRect(450, 60, 60, 30))
        self.twgviewfrom = QtWidgets.QTableWidget(SettingsViewer)
        self.twgviewfrom.setObjectName("twgplayer")
        self.twgviewfrom.setGeometry(QtCore.QRect(520, 60, 310, 50))
        self.twgviewfrom.setColumnCount(3)
        self.twgviewfrom.setRowCount(1)
        self.twgviewfrom.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.twgviewfrom.verticalHeader().hide()
        #
        self.lblplayer = QtWidgets.QLabel(SettingsViewer)
        self.lblplayer.setObjectName("lblplayer")
        self.lblplayer.setGeometry(QtCore.QRect(10, 130, 160, 30))
        self.twgplayer = QtWidgets.QTableWidget(SettingsViewer)
        self.twgplayer.setObjectName("twgplayer")
        self.twgplayer.setGeometry(QtCore.QRect(30, 170, 800, 70))
        self.twgplayer.setColumnCount(8)
        self.twgplayer.setRowCount(1)
        self.twgplayer.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.twgplayer.verticalHeader().hide()
        #
        self.btnapply = QtWidgets.QPushButton(SettingsViewer)
        self.btnapply.setObjectName("btnapply")
        self.btnapply.setGeometry(QtCore.QRect(370, 260, 100, 30))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(os.path.join(self.iconpath, "icons/ok.png")),
                       QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        self.btnapply.setIcon(icon)
        #
        self.msgbox = QtWidgets.QMessageBox(SettingsViewer)
        self.msgbox.setObjectName("msgbox")
        _center_x = SettingsViewer.geometry().center().x()
        _center_y = SettingsViewer.geometry().center().y()
        self.msgbox.setGeometry(QtCore.QRect(_center_x - 150, _center_y - 50, 300, 100))
        #
        self.retranslateGUI(SettingsViewer)
        QtCore.QMetaObject.connectSlotsByName(SettingsViewer)


    def retranslateGUI(self, SettingsViewer):
        self.dialog = SettingsViewer
        #
        _translate = QtCore.QCoreApplication.translate
        SettingsViewer.setWindowTitle(_translate("SettingsViewer", "Viewer Settings"))
        self.lblviewer3d.setText(_translate("SettingsViewer", "3-D:"))
        self.lblgohome.setText(_translate("SettingsViewer", "Go Home:"))
        self.cbbgohome.addItems(vis_viewer3d.GoHomeKeyList)
        #
        self.lblviewfrom.setText(_translate("SettingsViewer", "View from:"))
        self.twgviewfrom.setHorizontalHeaderLabels(['Inline', "Crossline", 'Time/depth'])
        for _i in vis_viewer3d.ViewFromPropertyList:
            _idx = list.index(vis_viewer3d.ViewFromPropertyList, _i)
            item = QtWidgets.QComboBox()
            item.addItems(vis_viewer3d.ViewFromKeyList)
            self.twgviewfrom.setCellWidget(0, _idx, item)
        #
        self.lblplayer.setText(_translate("SettingsViewer", "Player:"))
        self.twgplayer.setHorizontalHeaderLabels(['|<--', "<<--", '<<<<', '>>||',
                                                  '>>>>', '-->>', '-->|', 'Interval'])
        for _i in vis_player.PlayerPropertyList[:-1]:
            _idx = list.index(vis_player.PlayerPropertyList, _i)
            item = QtWidgets.QComboBox()
            item.addItems(vis_player.PlayerKeyList)
            self.twgplayer.setCellWidget(0, _idx, item)
        _idx = list.index(vis_player.PlayerPropertyList, vis_player.PlayerPropertyList[-1])
        item = QtWidgets.QComboBox()
        item.addItems([str(t) for t in vis_player.PlayerIntervalList])
        self.twgplayer.setCellWidget(0, _idx, item)
        #
        self.btnapply.setText(_translate("SettingsViewer", "Apply"))
        self.btnapply.clicked.connect(self.clickBtnApply)
        #
        self.cbbgohome.setCurrentIndex(list.index(vis_viewer3d.GoHomeKeyList, self.settings['Viewer3D']['GoHome']))
        #
        for _i in vis_viewer3d.ViewFromPropertyList:
            _idx = list.index(vis_viewer3d.ViewFromPropertyList, _i)
            self.twgviewfrom.cellWidget(0, _idx).setCurrentIndex(list.index(vis_viewer3d.ViewFromKeyList,
                                                                            self.settings['Viewer3D']['ViewFrom'][_i]))
        #
        for _i in vis_player.PlayerPropertyList[:-1]:
            _idx = list.index(vis_player.PlayerPropertyList, _i)
            self.twgplayer.cellWidget(0, _idx).setCurrentIndex(list.index(vis_player.PlayerKeyList,
                                                                          self.settings['Player'][_i]))
        _i = vis_player.PlayerPropertyList[-1]
        _idx = list.index(vis_player.PlayerPropertyList, _i)
        self.twgplayer.cellWidget(0, _idx).setCurrentIndex(list.index(vis_player.PlayerIntervalList,
                                                                      self.settings['Player'][_i]))


    def clickBtnApply(self):
        self.refreshMsgBox()
        #
        self.settings['Viewer3D']['GoHome'] = vis_viewer3d.GoHomeKeyList[self.cbbgohome.currentIndex()]
        #
        for _prop in vis_viewer3d.ViewFromPropertyList:
            _idx = list.index(vis_viewer3d.ViewFromPropertyList, _prop)
            self.settings['Viewer3D']['ViewFrom'][_prop] = \
                vis_viewer3d.ViewFromKeyList[self.twgviewfrom.cellWidget(0, _idx).currentIndex()]
        #
        for _prop in vis_player.PlayerPropertyList[:-1]:
            _idx = list.index(vis_player.PlayerPropertyList, _prop)
            self.settings['Player'][_prop] = \
                vis_player.PlayerKeyList[self.twgplayer.cellWidget(0, _idx).currentIndex()]
        _prop = vis_player.PlayerPropertyList[-1]
        _idx = list.index(vis_player.PlayerPropertyList, _prop)
        self.settings['Player'][_prop] = \
            vis_player.PlayerIntervalList[self.twgplayer.cellWidget(0, _idx).currentIndex()]
        #
        self.dialog.close()


    def refreshMsgBox(self):
        _center_x = self.dialog.geometry().center().x()
        _center_y = self.dialog.geometry().center().y()
        self.msgbox.setGeometry(QtCore.QRect(_center_x - 150, _center_y - 50, 300, 100))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SettingsViewer = QtWidgets.QWidget()
    gui = settingsviewer()
    gui.setupGUI(SettingsViewer)
    SettingsViewer.show()
    sys.exit(app.exec_())