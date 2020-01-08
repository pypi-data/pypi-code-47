'''
 Copyright (c) 2019, UChicago Argonne, LLC
 See LICENSE file.
'''
#from PyQt5 import uic
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton,\
    QLabel, QFileDialog, QComboBox, QSpacerItem, QGroupBox, QMessageBox
from PyQt5.QtCore import pyqtSlot, QRegExp, QSize
from PyQt5.Qt import QMainWindow, QVBoxLayout, QHBoxLayout, Qt, QTextEdit
from PyQt5.QtGui import QRegExpValidator
from s33specimagesum.srange import srange
import logging
from spec2nexus.spec import SpecDataFile, NotASpecDataFile, SpecDataFileNotFound
import os
import cv2

logger = logging.getLogger(__name__)
MAX_WIDTH = 2000
#Form, Window = uic.loadUiType("main.ui")
EMPTY_STR = ''
METHOD_ENTER_STR = "Entering %s"
METHOD_EXIT_STR = "Exiting %s"
SCAN_LIST_EXAMPLE = "ex 1-5, 7-10"
TSAM = 'Temp_sp'
SAMZ = 'samZ'

class MainWindow(QMainWindow):
    #SCAN_LIST_REGEXP = "((\d)+(-(\d)+)?\,( )?)*"
    SCAN_LIST_REGEXP = "(?:\d+(?:-\d+)?)(?:,(?:\d+(-\d+)?))*"
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        
        mainWidget = QWidget()
        vLayout = QVBoxLayout()
        hLayout1 =  QHBoxLayout()
        self.setMaximumWidth(MAX_WIDTH)
        label = QLabel("SpecFileName", minimumSize=QSize(80,0))
        self.specFileNameTxt = QLineEdit(minimumSize=QSize(200,0))
        self.browseFileNameButton = QPushButton("Browse", minimumSize=QSize(70,0))
        self.specFileNameTxt.editingFinished.connect(self.handleFileNameChanged)
        self.browseFileNameButton.clicked.connect(self.handleBrowseFile)
        hLayout1.addWidget(label)
        hLayout1.addWidget(self.specFileNameTxt)
        hLayout1.addWidget(self.browseFileNameButton)
        vLayout.addLayout(hLayout1)
        ######################
        self.scanListGroupBox = QGroupBox()
        scanVLayout = QVBoxLayout()
        hLayout2 = QHBoxLayout()
        label = QLabel("Scans", minimumSize=QSize(80,0))
        self.scanListTxt = QLineEdit()
        rx = QRegExp(self.SCAN_LIST_REGEXP)
        self.scanListTxt.editingFinished.connect(self.handleScanChanged)
        self.scanListTxt.setValidator(QRegExpValidator(rx, self.scanListTxt))
        self.exampleTxt=QLabel(SCAN_LIST_EXAMPLE, minimumSize=QSize(100,0))
        self.exampleTxt.setEnabled(False)
        hLayout2.addWidget(label)
        hLayout2.addWidget(self.scanListTxt)
        hLayout2.addWidget(self.exampleTxt)
        scanVLayout.addLayout(hLayout2)
        self.scanListGroupBox.setLayout(scanVLayout)
        self.scanListGroupBox.setEnabled(False)
        vLayout.addWidget(self.scanListGroupBox)
        #################
        self.param1GroupBox = QGroupBox()
        self.param1GroupBox.setMaximumWidth(MAX_WIDTH)
        param1VLayout = QVBoxLayout()
        hLayout3 = QHBoxLayout()
        label = QLineEdit("Parameter 1", minimumSize=QSize(80,0))
        label.setReadOnly(True)
        self.param1Selector = QComboBox()
        self.param1Selector.currentIndexChanged[str].connect(self.handleSelector1Changed)
        hLayout3.addWidget(label)
        hLayout3.addWidget(self.param1Selector)
        param1VLayout.addLayout(hLayout3)
        #selectedValues
        hLayout3a = QHBoxLayout()
        self.selectedP1Values = QLabel() 
        self.selectedP1Values.setEnabled(False)
        hLayout3a.addWidget(self.selectedP1Values)
        param1VLayout.addLayout(hLayout3a)
        #selectionRange
        hLayout3b = QHBoxLayout()
        label = QLabel("Range", minimumSize=QSize(80,0))
        self.param1Txt = QLineEdit()
        self.param1Txt.editingFinished.connect(self.handleParam1RangeChanged)
        hLayout3b.addWidget(label)
        hLayout3b.addWidget(self.param1Txt)
        param1VLayout.addLayout(hLayout3b)
        self.param1GroupBox.setLayout(param1VLayout)
        self.param1GroupBox.setEnabled(False)
        vLayout.addWidget(self.param1GroupBox)
        ###################
        self.param2GroupBox = QGroupBox()
        self.param2GroupBox.setMaximumWidth(MAX_WIDTH)
        param2VLayout = QVBoxLayout()
        hLayout4 = QHBoxLayout()
        label = QLineEdit("Parameter 2", minimumSize=QSize(80,0))
        label.setReadOnly(True)
        self.param2Selector = QComboBox()
        self.param2Selector.currentIndexChanged[str].connect(self.handleSelector2Changed)
        hLayout4.addWidget(label)
        hLayout4.addWidget(self.param2Selector)
        param2VLayout.addLayout(hLayout4)
        # selected values
        hLayout4a = QHBoxLayout()
        self.selectedP2Values = QLabel() 
        self.selectedP2Values.setEnabled(False)
        hLayout4a.addWidget(self.selectedP2Values)
        param2VLayout.addLayout(hLayout4a)
        hLayout4b = QHBoxLayout()
        label = QLabel("Range")
        self.param2Txt = QLineEdit()
        self.param2Txt.editingFinished.connect(self.handleParam2RangeChanged)
        hLayout4b.addWidget(label)
        hLayout4b.addWidget(self.param2Txt)
        param2VLayout.addLayout(hLayout4b)
        self.param2GroupBox.setLayout(param2VLayout)
        self.param2GroupBox.setEnabled(False)
        vLayout.addWidget(self.param2GroupBox)
        ###############
        hLayout5 = QHBoxLayout()
        self.runButton = QPushButton("Run")
        self.exitButton = QPushButton("Exit")
        hLayout5.addWidget(self.runButton, alignment=Qt.AlignRight)
        hLayout5.addWidget(self.exitButton, alignment=Qt.AlignRight)
        vLayout.addLayout(hLayout5)
        mainWidget.setLayout(vLayout)
        
        self.exitButton.clicked.connect(self.close)
        self.runButton.clicked.connect(self.runScans)
        mainWidget.show()
        #self.w
        self.specFile = None
        self.setCentralWidget(mainWidget)
        
    def findSelectedParameterRanges(self):
        logger.debug("self.scanListTxt %s" % str(self.scanListTxt.text()))
        scans = srange(str(self.scanListTxt.text()))
        scanList = scans.list()
        logger.debug("scans %s" % scanList)
        param1List = set()
        param2List = set()
        maxScans = int(self.specDataFile.getMaxScanNumber())
        for scanNum in scanList:
            logger.debug("Scan %s" % scanNum)
            if scanNum > maxScans:
                QMessageBox.warning(self, "SCAN OUT OF RANGE", "Scan %s is out of range.  MaxScan=%s" % (scanNum, maxScans))
                break
            scan = self.specDataFile.scans[str(scanNum)]
            if len(scan.data_lines) != 0:
                logger.debug("data size = %s" % scan.data)
                param1Name = self.param1Selector.currentText()
                logger.debug("param1Name %s" % param1Name)
                for param1 in scan.data[param1Name]:
                    param1List.add(param1)
                    #logger.debug (samZ)
                param2Name = self.param2Selector.currentText()
                logger.debug("param2Name %s" % param2Name)
                for param2 in scan.data[param2Name]:
                    param2List.add(param2)
#             else:    
#                 QMessageBox.warning(self, "SCAN IS EMPTY", "Scan %s is empty."  % scanNum)
                
        self.selectedP1Values.setText(str(param1List))        
        self.selectedP2Values.setText(str(param2List))        
        self.runButton.setEnabled(True)

    def getScanList(self):
        '''
        return a list of scans to be used for loading data
        '''
        logger.debug(METHOD_ENTER_STR)
        scanList = None
        if str(self.scanListTxt.text()) == EMPTY_STR:
            scanList = None
        else:
            scans = srange(str(self.scanNumsTxt.text()))
            scanList = scans.list() 
        logger.debug(METHOD_EXIT_STR)
        return scanList
        
    
    @pyqtSlot()
    def close(self):
        sys.exit()
        
    @pyqtSlot()
    def handleFileNameChanged(self):
        logger.debug(METHOD_ENTER_STR % "FileChanged")
        filename=str(self.specFileNameTxt.text())
        logger.debug("evaluating %s" % filename)
        if (filename != ""):
            try:
                self.specDataFile = SpecDataFile(filename)
                numberOfScans = self.specDataFile.getMaxScanNumber()
                self.exampleTxt.setText((SCAN_LIST_EXAMPLE + 
                                         "limits [1:%d]") % int(numberOfScans))
                self.scanListGroupBox.setEnabled(True)
                self.setParameterListChoices()
                if str(self.scanListTxt.text()) == "":
                    self.param1GroupBox.setEnabled(False)
                    self.param2GroupBox.setEnabled(False)
                else:
                    scans = srange(str(self.scanListTxt.text()))
                    self.param1GroupBox.setEnabled(True)
                    self.param2GroupBox.setEnabled(True)
            except NotASpecDataFile:
                QMessageBox.warning(self, "Not a Spec File", "%s is not a Specfile" % filename)
            except SpecDataFileNotFound:
                QMessageBox.warning(self, "File Not Found", "%s does not seem to exist" % filename)
        
    @pyqtSlot()
    def handleBrowseFile(self):
        logger.debug(METHOD_ENTER_STR)
        if self.specFileNameTxt.text() == EMPTY_STR:
            filename = QFileDialog.getOpenFileName(None, 
                                                   'Spec File Name', 
                                                   filter="")[0]
        else:
            fileDirectory = os.path.dirname(self.specFileNameTxt.text())
            filename = QFileDialog.getOpenFileName(None, 
                                                   "Spec File Name",
                                                   directory= fileDirectory,
                                                   filter="")[0]
        if filename != EMPTY_STR:
            self.specFileNameTxt.setText(filename)
            self.specFileNameTxt.editingFinished.emit()
            
        
    @pyqtSlot()
    def handleParam2RangeChanged(self):
        logger.debug (METHOD_ENTER_STR % "handleParam2RangeChanged")
        
    @pyqtSlot()
    def handleParam1RangeChanged(self):
        logger.debug(METHOD_ENTER_STR % "handleParam1RangeChanged")

    @pyqtSlot(str)
    def handleSelector1Changed(self, choice):
        logger.debug (METHOD_ENTER_STR % "handleSelector1Changed")
        if choice == '':
            return
        self.findSelectedParameterRanges()
                
    @pyqtSlot(str)
    def handleSelector2Changed(self, choice):
        logger.debug (METHOD_ENTER_STR % "handleSelector2Changed")
        if choice == '':
            return
        self.findSelectedParameterRanges()
                
    @pyqtSlot()
    def handleScanChanged(self):
        logger.debug(METHOD_ENTER_STR % "handleScanChanged")
        if str(self.scanListTxt.text()) == '' and \
           str(self.specFileNameTxt.text()) == '':
            self.param1GroupBox.setEnabled(False)
            self.param2GroupBox.setEnabled(False)
            return
        self.param1GroupBox.setEnabled(True)
        self.param2GroupBox.setEnabled(True)
        self.setParameterListChoices()
        self.findSelectedParameterRanges()
#         logger.debug ("param1List %s" % param1List)
#         logger.debug ("param2List %s" % param2List)
        
    def runScans(self):
        scans = srange(str(self.scanListTxt.text()))
        
        param1Name = str(self.param1Selector.currentText())
        param2Name = str(self.param2Selector.currentText())
        for scanNum in scans.list():
            scan = self.specDataFile.scans[str(scanNum)]
            numLinesInScan = len(scan.data_lines)
            if numLinesInScan == 0:
                QMessageBox.warning(self, "SCAN IS EMPTY", "Scan %s is empty."  % scanNum)
            else:
                param1Vals = scan.data[param1Name]
                param2Vals = scan.data[param2Name]
                specFileName = str(self.specFileNameTxt.text())
                fileDirectory, fileName = os.path.split(specFileName)
                fileNameBase,fileExtension = os.path.splitext(fileName)
                imageSum = None
                    
                for point in range(numLinesInScan):
                    imageFile = "%s_S%.3d_%.5d.tif" % \
                        (fileNameBase, scanNum, point)
                    fullFileName = os.path.join(fileDirectory, 'images', 
                                                fileNameBase, "S%.3d"%scanNum, 
                                                imageFile)
                    logger.debug("Filename %s" % fullFileName)
                    if point == 0:
                        imageSum = cv2.imread(fullFileName, -1)
                    imageSum += cv2.imread(fullFileName,-1)
                outFileName = "%s_S%.3d_%s_%f_%s_%f.tif" % (fileNameBase, scanNum,
                                                         param1Name, param1Vals[0],
                                                         param2Name, param2Vals[0])
                outBaseDirectory = os.path.join(fileDirectory, 'analysis_runtime', fileNameBase, "S%.3d" % scanNum)
                if not os.path.exists(outBaseDirectory):
                    os.makedirs(outBaseDirectory)
                fullOutName = os.path.join(outBaseDirectory, outFileName)
                cv2.imwrite(fullOutName, imageSum)
                    
 
    
    def setParameterListChoices(self):
        scansText = str(self.scanListTxt.text())
        self.param1Selector.clear()
        self.param2Selector.clear()
        if scansText != "":
            scans = srange(scansText)
            firstScan = scans.list()[0]
            logger.debug("firstScan %s" % firstScan)
            columns = self.specDataFile.scans[str(firstScan)].L
            logger.debug("scansText %s Columns %s" % (scansText, columns))
            self.param1Selector.currentIndexChanged[str].disconnect(self.handleSelector1Changed)
            self.param2Selector.currentIndexChanged[str].disconnect(self.handleSelector2Changed)
            self.param1Selector.addItems(columns)
            self.param2Selector.addItems(columns)
            self.param1Selector.currentIndexChanged[str].connect(self.handleSelector1Changed)
            self.param2Selector.currentIndexChanged[str].connect(self.handleSelector2Changed)
        else:
            columns = self.specDataFile.scans[str(1)].L
            logger.debug("scansText %s Columns %s" % (scansText, columns))
            self.param1Selector.addItems(columns)
            self.param2Selector.addItems(columns)
        self.param1Selector.setCurrentIndex(0)
        self.param2Selector.setCurrentIndex(0)
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec_()