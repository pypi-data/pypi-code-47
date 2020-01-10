"""
 Project: coraline_eda
 Desctiption: Main file for Coraline EDA Tool
 Created by Jiranun J. at 2019/10/02 2:16 PM
"""

from PyQt5.QtWidgets import (
    QMainWindow, QApplication, QHBoxLayout, QVBoxLayout, QLabel,
    QWidget, QFileDialog, QLineEdit, QPushButton, QMessageBox, QProgressBar,
    QStatusBar,QTableWidget,QTableWidgetItem,QHeaderView, QComboBox)
from PyQt5.QtCore import Qt, pyqtSignal, pyqtSlot
from coraline_eda.eda_utils import read_and_gen_report
import sys
from os import listdir
from os.path import splitext
import threading
import matplotlib
matplotlib.use('Qt5Agg')
import time


class CoralineEDAWindow(QMainWindow):
    update_progress = pyqtSignal(int, name="update_progress")
    update_label = pyqtSignal(str, name="update_label")
    enable_buttons = pyqtSignal(bool, name="enable_buttons")

    def __init__(self, *args, **kwargs):
        super(CoralineEDAWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle("Coraline EDA Tool")
        self.initUI()
        self.setConnections()
        self.connectSignals()
        self.files_list = []
        self.delimiterOptions = {
            ", (Comma)" : "," ,
            "  (Tab)"   : "\t" ,
            ": (Colon)" : ":" ,
            "| (Pipe)"  : "|" ,
        }

    def initUI(self):
        """
        Initial All UI including field and buttons
        """
        main_widget = QWidget(self)
        main_layout = QVBoxLayout(main_widget)

        # Create Browse layout
        browse_layout = QHBoxLayout()
        browse_layout.addWidget(QLabel("Folder: "))
        self.selected_folder = QLineEdit()
        self.selected_folder.setEnabled(False)
        browse_layout.addWidget(self.selected_folder)
        self.browse_folder_button = QPushButton("Browse")
        browse_layout.addWidget(self.browse_folder_button)

        # Add Browse Layout to Main Layout
        main_layout.addLayout(browse_layout)

        # Add File List Table
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(['Filename','Type','Delimiter'])
        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)
        main_layout.addWidget(self.tableWidget)

        # Add Generate button to main layout
        self.gen_button = QPushButton("Generate EDA Reports")
        main_layout.addWidget(self.gen_button)

        # Add current file label to status bar (left)
        self.current_file = QLabel("")
        self.status_bar = QStatusBar(self)
        self.setStatusBar(self.status_bar)
        self.status_bar.addWidget(self.current_file)

        # Add progress bar to status bar (right)
        self.progress = QProgressBar(self)
        self.progress.setRange(0, 100)
        self.progress.setHidden(True)
        self.status_bar.addPermanentWidget(self.progress)

        # Set Central Widget and resize
        self.setCentralWidget(main_widget)
        self.setMinimumSize(500, 100)

    def setConnections(self):
        """
        Set All Event Handler
        """
        self.browse_folder_button.clicked.connect(self.on_browse_clicked)
        self.gen_button.clicked.connect(self.on_generate_clicked)

    def connectSignals(self):
        """
        Set Signal for GUI Updates through thread
        """
        self.update_progress.connect(self.progress.setValue)
        self.update_label.connect(self.current_file.setText)
        self.enable_buttons.connect(self.setButtonsEnabled)

    def on_browse_clicked(self, e):
        """
        Popup Folder Selection Dialog
        """
        selected_path = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.selected_folder.setText(selected_path)

        # Check if the selected folder contains at least 1 table files (csv, tsv, xlsx) and not a hidden file
        if selected_path != '':
            all_files = listdir(selected_path)
            all_files = [fn for fn in all_files if (splitext(fn)[1] == '.csv' or splitext(fn)[1] == '.xlsx' or splitext(fn)[1] == '.tsv')and not fn.startswith('.')]
            if len(all_files) == 0:
                msg_box = QMessageBox()
                msg_box.setText("Please select a folder that contains at least one table file e.g csv or excel(xlsx)")
                msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box.exec_()
            all_files.sort()
        else:
            all_files = []
            msg_box = QMessageBox()
            msg_box.setText("Please select a folder to generate EDA reports")
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.exec_()

        # Update UI (tableWidget) and Update files_list
        self.files_list = []
        self.tableWidget.setRowCount(len(all_files))
        for id in range(len(all_files)):
            file_dict = {
                'filename'  : all_files[id],
                'filetype'  : splitext(all_files[id])[1],
                'delimiter' : None
            }
            self.files_list.append(file_dict)
            self.tableWidget.setItem(id,0,QTableWidgetItem(file_dict['filename']))
            self.tableWidget.setItem(id,1,QTableWidgetItem(file_dict['filetype'].replace('.','').upper()))
            delimiter_combobox = QComboBox()
            if file_dict['filetype'] == '.csv' or file_dict['filetype'] == '.tsv':
                for option in self.delimiterOptions.keys():
                    delimiter_combobox.addItem(option)
                if file_dict['filetype'] == '.tsv':
                    delimiter_combobox.setCurrentIndex(1)
                self.tableWidget.setCellWidget(id,2,delimiter_combobox)
                
            self.tableWidget.setItem(id,2,QTableWidgetItem("-"))

    @pyqtSlot(bool)
    def setButtonsEnabled(self, is_enabled):
        """Set Enable Flag for buttons -- Generate and Browse Buttons

        Parameters
        ----------
        is_enabled : bool
            is enable flag
        """
        self.browse_folder_button.setEnabled(is_enabled)
        self.gen_button.setEnabled(is_enabled)

    def process_files(self, file_path):
        """
        Process all files in the list
        """
        if file_path == "" or len(self.files_list) == 0:
            return

        n_files = len(self.files_list)
        self.enable_buttons.emit(False)
        for i, file in enumerate(self.files_list):
            curr_label = f" Processing: {file['filename']} ({i+1}/{n_files})"
            self.update_label.emit(curr_label)
            prog_val = int((i+1)*100/n_files)
            self.update_progress.emit(prog_val)
            read_and_gen_report(file_path, file['filename'], file['delimiter'])

        self.enable_buttons.emit(True)
        self.update_label.emit(" Done :)")

    def on_generate_clicked(self, e):
        """
        Event handling when Generate Reports button is clicked
        """
        # Check if a folder is selected
        selected_path = self.selected_folder.text()
        if selected_path == '':
            msg_box = QMessageBox()
            msg_box.setText("Please select a folder to generate EDA reports")
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.exec_()
            return

        # Check if the selected folder contains at least 1 table files (csv, tsv, xlsx) and not a hidden file
        if selected_path != '':
            all_files = listdir(selected_path)
        else:
            all_files = []
        all_files = [fn for fn in all_files if (splitext(fn)[1] == '.csv' or splitext(fn)[1] == '.xlsx' or splitext(fn)[1] == '.tsv')and not fn.startswith('.')]
        if len(all_files) == 0:
            msg_box = QMessageBox()
            msg_box.setText("Please select a folder that contains at least one table file e.g csv or excel(xlsx)")
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.exec_()
            return
        all_files.sort()

        # Get Delimiter from UI
        for id in range(len(self.files_list)):
            if self.files_list[id]['filetype'] == '.csv' or self.files_list[id]['filetype'] == '.tsv':
                delimiter = self.tableWidget.cellWidget(id,2).currentText()
            else:
                delimiter = ''
            self.files_list[id]['delimiter'] = self.delimiterOptions.get(delimiter,None)
            
        # Pop confirmation dialog
        msg_box = QMessageBox()
        msg = """This folder contains %d files. Including \n\n - %s
        \nThis might take long. Are you sure you want to process this folder?
        """ % (len(all_files), "\n - ".join(all_files))
        msg_box.setText(msg)
        msg_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        ret = msg_box.exec_()

        if ret == QMessageBox.Ok:
            self.progress.setHidden(False)
            print("\nEDA REPORT GENERATOR HAS BEEN STARTED\n")
            x = threading.Thread(target=self.process_files, args=(selected_path, ))
            x.start()

    def keyPressEvent(self, e):
        """
        Set Event handling for button pressed
        """
        if e.key() == Qt.Key_Escape:
            self.close()


def run():
    app = QApplication(sys.argv)
    window = CoralineEDAWindow()
    window.show()
    app.exec_()


if __name__ == "__main__":
    run()
