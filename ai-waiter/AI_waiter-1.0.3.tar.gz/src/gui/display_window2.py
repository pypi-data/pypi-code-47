import pandas as pd
import sys
import qdarkstyle
import sqlalchemy
import textwrap
from PySide2.QtCore import (QAbstractTableModel, QModelIndex, Slot, QPersistentModelIndex, Qt)
from PySide2.QtWidgets import (QDesktopWidget, QAction, QApplication, QHBoxLayout, QHeaderView, QMainWindow,
                               QSizePolicy, QTableView, QWidget, QCheckBox, QTableWidgetItem)
from PySide2.QtGui import QFont
sys.path.append('../')
from configs.config import filenames

final_orders = filenames.final_orders

def read_sql_server():
    engine = sqlalchemy.create_engine(
        "mssql+pyodbc://altius:alt.ius01@demodatasets.database.windows.net/DemoDatasets?driver=SQL+Server")
    query = textwrap.dedent('''
                SELECT *
                FROM orders''')
    df = pd.read_sql_query(query, engine)
    order = df["OrderID"]
    itemid = df["ItemID"]
    table = df["TableNo"]
    item = df["Item"]
    quantity = df["Quantity"]
    number = df["Number"]
    time = df["Time"]
    return order, itemid,table, item, quantity, number, time

# def read_data(fname):
#     df = pd.read_csv(fname)
#     table = df["Table"]
#     order = df["Order"]
#     time = df["Time"]
#     return table, order, time

class MainWindow(QMainWindow):
    def __init__(self, widget):
        super().__init__()
        #QMainWindow.__init__(self)
        self.setWindowTitle("AI Waiter Orders")

        # Menu
        self.menu = self.menuBar()
        self.file_menu = self.menu.addMenu("File")

        # Exit QAction
        exit_action = QAction("Exit", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(self.close)

        self.file_menu.addAction(exit_action)

        # Status Bar
        self.status = self.statusBar()
        self.status.showMessage("Orders")

        # Window dimensions
        # geometry = QDesktopWidget().availableGeometry(self)
        # self.setFixedSize(geometry.width() * 1, geometry.height() * 1)
        self.setGeometry(0, 0, 1550, 800)
        self.setCentralWidget(widget)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        #Font
        self.setFont(QFont('SansSerif', 14))

    # @Slot()
    # def exit_app(self, checked):
    #     sys.exit()

class CustomTableModel(QAbstractTableModel):
    def __init__(self, data=None):
        QAbstractTableModel.__init__(self)
        self.load_data(data)
        self.checks = {}

    def checkState(self, index):
        if index in self.checks.keys():
            return self.checks[index]
        else:
            return Qt.Unchecked

    def load_data(self, data):
        self.input_order = data[0].values
        self.input_itemid = data[1].values
        self.input_table = data[2].values
        self.input_item = data[3].values
        self.input_quantity = data[4].values
        self.input_number = data[5].values
        self.input_time = data[6].values

        self.column_count = 8
        self.row_count = len(self.input_order)

    def rowCount(self, parent=QModelIndex()):
        return self.row_count

    def columnCount(self, parent=QModelIndex()):
        return self.column_count

    def headerData(self, section, orientation, role):
        if role != Qt.DisplayRole:
            return None
        if orientation == Qt.Horizontal:
            return ("Served", "OrderID", "ItemID", "TableNo", "Item", "Quantity", "Number", "Time")[section]
        else:
            return "{}".format(section)

    def data(self, index, role = Qt.DisplayRole):
        column = index.column()
        row = index.row()
        if role == Qt.DisplayRole or role == Qt.EditRole:
            if column == 1:
                raw_date = self.input_order[row]
                date = "{}".format(raw_date)
                return date
            elif column == 2:
                return "{}".format(self.input_itemid[row])
            elif column == 3:
                return "{}".format(self.input_table[row])
            elif column == 4:
                return "{}".format(self.input_item[row])
            elif column == 5:
                return "{}".format(self.input_quantity[row])
            elif column == 6:
                return "{}".format(self.input_number[row])
            elif column == 7:
                return "{}".format(self.input_time[row])
            else:
                return QCheckBox('')
        elif role == Qt.CheckStateRole and column == 0:
            return self.checkState(QPersistentModelIndex(index))
        elif role == Qt.TextAlignmentRole:
            return Qt.AlignCenter

        return None

    def setData(self, index, value, role=Qt.EditRole):
        if not index.isValid():
            return False
        if role == Qt.CheckStateRole:
            self.checks[QPersistentModelIndex(index)] = value
            return True
        return False

    def flags(self, index):
        fl = QAbstractTableModel.flags(self, index)
        if index.column() == 0:
            fl |= Qt.ItemIsEditable | Qt.ItemIsUserCheckable
        return fl

class Widget(QWidget):
    def __init__(self, data):
        super().__init__()
        #QWidget.__init__(self)

        # Getting the Model
        self.model = CustomTableModel(data)

        # Creating a QTableView
        self.table_view = QTableView()
        self.table_view.setModel(self.model)

        # QTableView Headers
        self.horizontal_header = self.table_view.horizontalHeader()
        self.vertical_header = self.table_view.verticalHeader()
        self.horizontal_header.setSectionResizeMode(0,QHeaderView.ResizeToContents)
        self.horizontal_header.setSectionResizeMode(1,QHeaderView.ResizeToContents)
        self.horizontal_header.setSectionResizeMode(2,QHeaderView.ResizeToContents)
        self.horizontal_header.setSectionResizeMode(3,QHeaderView.ResizeToContents)
        self.horizontal_header.setSectionResizeMode(4,QHeaderView.Stretch)
        self.horizontal_header.setSectionResizeMode(5,QHeaderView.ResizeToContents)
        self.horizontal_header.setSectionResizeMode(6,QHeaderView.ResizeToContents)
        self.horizontal_header.setSectionResizeMode(7,QHeaderView.ResizeToContents)
        self.vertical_header.setSectionResizeMode(QHeaderView.Interactive)
        self.horizontal_header.setStyleSheet("QHeaderView { font-size: 18pt; font: bold 24px;}")

        # QWidget Layout
        self.main_layout = QHBoxLayout()
        size = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.main_layout.setContentsMargins(0,0,0,0)

        #Align Checkbox
        self.main_layout.setContentsMargins(0,0,0,0)

        ## Left layout
        size.setHorizontalStretch(1)
        self.table_view.setSizePolicy(size)
        self.main_layout.addWidget(self.table_view)

        # Set the layout to the QWidget
        self.setLayout(self.main_layout)

def main(final_orders):
    data = read_sql_server()
    #app2 = QApplication()
    widget = Widget(data)
    window2 = MainWindow(widget)
    #app.setStyleSheet(qdarkstyle.load_stylesheet_pyside2())
    #window2.show()
    #sys.exit(app2.exec_())
    return window2

if __name__ == "__main__":
    data = read_sql_server()

    # Qt Application
    app = QApplication()
    # QWidget
    widget = Widget(data)
    # QMainWindow using QWidget as central widget
    window = MainWindow(widget)
    # setup stylesheet
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyside2())

    window.show()
    sys.exit(app.exec_())