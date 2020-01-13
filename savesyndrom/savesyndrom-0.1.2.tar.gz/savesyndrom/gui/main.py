import re

from PyQt5 import QtCore, QtGui, QtWidgets

from ..keylogger import KeyLogger
from ..settings import Settings
from .show import ShowWindow, TestWindow


class ShowMessage(QtCore.QObject):
    show_message = QtCore.pyqtSignal(frozenset)

    def __init__(self, show_window: ShowWindow):
        super().__init__()

        self.show_message.connect(show_window.show_text)

    def emit(self, keys):
        self.show_message.emit(keys)


class MainWindow(QtWidgets.QMainWindow):
    MINUTE = 60
    HOUR = MINUTE * 60
    DAY = HOUR * 24
    YEAR = DAY * 365

    FONTS = {
        "Times New Roman": "Times",
    }

    def __init__(self, application: QtWidgets.QApplication, settings=Settings):
        super().__init__()

        self.application = application
        self.settings = settings
        self.translate = QtCore.QCoreApplication.translate
        self.show_window = ShowWindow(settings=settings)
        self.show_message = ShowMessage(show_window=self.show_window)
        self.test_window = TestWindow(settings=settings)

        self.tray_icon = QtWidgets.QSystemTrayIcon(self)
        self.tray_icon.setIcon(self.style().standardIcon(QtWidgets.QStyle.SP_ComputerIcon))

        self.tray_startstop_action = QtWidgets.QAction(self.translate("MainWindow", "Start"), self)
        self.tray_show_action = QtWidgets.QAction(self.translate("MainWindow", "Show"), self)
        self.tray_quit_action = QtWidgets.QAction(self.translate("MainWindow", "Exit"), self)
        self.tray_menu = QtWidgets.QMenu()
        self.tray_menu.addAction(self.tray_startstop_action)
        self.tray_menu.addAction(self.tray_show_action)
        self.tray_menu.addAction(self.tray_quit_action)
        self.tray_icon.setContextMenu(self.tray_menu)
        self.tray_icon.show()

        self.setObjectName("MainWindow")
        self.setWindowTitle(self.translate("MainWindow", "savesyndrom"))
        self.setGeometry(*self.settings.get_window_position(), *self.settings.get_window_size())

        self.central_widget = QtWidgets.QWidget(self)
        self.central_widget.setObjectName("central_widget")
        self.central_layout = QtWidgets.QGridLayout(self.central_widget)
        self.central_layout.setObjectName("central_layout")

        self.settings_listwidget = QtWidgets.QListWidget(self.central_widget)
        self.settings_listwidget.setObjectName("settings_listwidget")
        self.settings_listwidget.setFixedWidth(250)
        font = QtGui.QFont("Times", 20)
        item = QtWidgets.QListWidgetItem(self.translate("MainWindow", "General"))
        item.setFont(font)
        self.settings_listwidget.addItem(item)
        item = QtWidgets.QListWidgetItem(self.translate("MainWindow", "Statistic"))
        item.setFont(font)
        self.settings_listwidget.addItem(item)

        self.general_frame = QtWidgets.QFrame(self.central_widget)
        self.general_frame.setObjectName("general_frame")
        self.general_layout = QtWidgets.QGridLayout(self.general_frame)
        self.general_layout.setObjectName("general_layout")
        self.language_label = QtWidgets.QLabel(self.general_frame)
        self.language_label.setText(self.translate("MainWindow", "Language:"))
        self.language_combobox = QtWidgets.QComboBox(self.general_frame)
        self.language_combobox.addItems(self.settings.LANGUAGES.values())
        self.show_checkbox = QtWidgets.QCheckBox(self.general_frame)
        self.show_checkbox.setText(self.translate("MainWindow", "Show"))
        combinations = self.settings.get_combinations()
        combination = frozenset(("ctrl", "s"))
        self.show_checkbox.setChecked(
            combinations[combination] if combination in combinations else False
        )
        self.text_frame = QtWidgets.QFrame(self.general_frame)
        self.text_frame.setEnabled(
            combinations[combination] if combination in combinations else False
        )
        self.text_layout = QtWidgets.QGridLayout(self.text_frame)
        self.text_test_button = QtWidgets.QPushButton(self.text_frame)
        self.text_test_button.setText(self.translate("MainWindow", "Show test window"))
        self.text_font_label = QtWidgets.QLabel(self.text_frame)
        self.text_font_label.setText(self.translate("MainWindow", "Font"))
        self.text_font_combobox = QtWidgets.QComboBox(self.text_frame)
        fonts = self.FONTS.items()
        self.text_font_combobox.addItems(map(lambda x: x[0], fonts))
        for index, font in enumerate(fonts):
            if self.settings.text_font == font[1]:
                self.text_font_combobox.setCurrentIndex(index)
        self.text_fontsize_label = QtWidgets.QLabel(self.text_frame)
        self.text_fontsize_label.setText(self.translate("MainWindow", "Font size"))
        self.text_fontsize_lineedit = QtWidgets.QLineEdit(self.text_frame)
        self.text_fontsize_lineedit.setText(str(self.settings.text_fontsize))
        self.text_color_label = QtWidgets.QLabel(self.text_frame)
        self.text_color_label.setText(
            self.translate("MainWindow", "Current color: ") + str(self.settings.get_text_color()),
        )
        self.text_color_button = QtWidgets.QPushButton(self.text_frame)
        self.text_color_button.setText(self.translate("MainWindow", "Change text color"))
        self.text_time_label = QtWidgets.QLabel(self.text_frame)
        self.text_time_label.setText(self.translate("MainWindow", "Show time"))
        self.text_time_lineedit = QtWidgets.QLineEdit(self.text_frame)
        self.text_time_lineedit.setText(str(self.settings.text_time))
        self.text_layout.addWidget(self.text_test_button, 0, 0, 1, 2)
        self.text_layout.addWidget(self.text_font_label, 1, 0, 1, 1)
        self.text_layout.addWidget(self.text_font_combobox, 1, 1, 1, 1)
        self.text_layout.addWidget(self.text_fontsize_label, 2, 0, 1, 1)
        self.text_layout.addWidget(self.text_fontsize_lineedit, 2, 1, 1, 1)
        self.text_layout.addWidget(self.text_color_label, 3, 0, 1, 1)
        self.text_layout.addWidget(self.text_color_button, 3, 1, 1, 1)
        self.text_layout.addWidget(self.text_time_label, 4, 0, 1, 1)
        self.text_layout.addWidget(self.text_time_lineedit, 4, 1, 1, 1)
        self.general_layout.addWidget(self.language_label, 0, 0, 1, 1)
        self.general_layout.addWidget(self.language_combobox, 0, 1, 1, 1)
        self.general_layout.addWidget(self.show_checkbox, 1, 0, 1, 1)
        self.general_layout.addWidget(self.text_frame, 2, 0, 1, 2)

        self.statistic_frame = QtWidgets.QFrame(self.central_widget)
        self.statistic_frame.setObjectName("statistic_frame")
        self.statistic_layout = QtWidgets.QGridLayout(self.statistic_frame)
        self.statistic_layout.setObjectName("statistic_layout")
        self.statistic_label = QtWidgets.QLabel(self.statistic_frame)
        self.calcstat_button = QtWidgets.QPushButton(self.statistic_frame)
        self.calcstat_button.setText(self.translate("MainWindow", "Calculate statistic"))
        self.statistic_layout.addWidget(self.statistic_label, 0, 0, 1, 1)
        self.statistic_layout.addWidget(self.calcstat_button, 1, 0, 1, 1)

        self.settings_frames = (
            self.general_frame,
            self.statistic_frame,
        )

        self.button_frame = QtWidgets.QFrame(self.central_widget)
        self.button_frame.setObjectName("button_frame")
        self.button_layout = QtWidgets.QGridLayout(self.button_frame)
        self.startstop_button = QtWidgets.QPushButton(self.button_frame)
        self.startstop_button.setText(self.translate("MainWindow", "Start"))
        self.startstop_button.setObjectName("startstop_button")
        self.apply_button = QtWidgets.QPushButton(self.button_frame)
        self.apply_button.setText(self.translate("MainWindow", "Apply"))
        self.apply_button.setObjectName("apply_button")
        self.minimize_button = QtWidgets.QPushButton(self.button_frame)
        self.minimize_button.setText(self.translate("MainWindow", "Minimize"))
        self.minimize_button.setObjectName("minimize_button")
        self.exit_button = QtWidgets.QPushButton(self.button_frame)
        self.exit_button.setText(self.translate("MainWindow", "Exit"))
        self.exit_button.setObjectName("exit_button")
        self.button_layout.addWidget(self.startstop_button, 0, 0, 1, 1)
        self.button_layout.addWidget(self.apply_button, 0, 1, 1, 1)
        self.button_layout.addWidget(self.minimize_button, 0, 2, 1, 1)
        self.button_layout.addWidget(self.exit_button, 0, 3, 1, 1)

        self.central_layout.addWidget(self.settings_listwidget, 0, 0, 1, 1)
        for frame in self.settings_frames:
            self.central_layout.addWidget(frame, 0, 1, 1, 1)
        self.central_layout.addWidget(self.button_frame, 1, 0, 1, 2)

        self.setCentralWidget(self.central_widget)

        self.tray_startstop_action.triggered.connect(self.start_keylogger)
        self.tray_show_action.triggered.connect(self.show)
        self.tray_quit_action.triggered.connect(self.exit)
        self.settings_listwidget.currentItemChanged.connect(self.show_settings)
        self.show_checkbox.toggled.connect(self.show_toggled)
        self.text_test_button.clicked.connect(self.test_window.show)
        self.text_fontsize_lineedit.textChanged.connect(self.text_fontsize_changed)
        self.text_color_button.clicked.connect(self.open_text_color_dialog)
        self.calcstat_button.clicked.connect(self.calc_statistic)
        self.startstop_button.clicked.connect(self.start_keylogger)
        self.minimize_button.clicked.connect(self.close)
        self.apply_button.clicked.connect(self.apply)
        self.exit_button.clicked.connect(self.exit)

        QtCore.QMetaObject.connectSlotsByName(self)
        
        self.init_keylogger()
        self.calc_statistic()

    def closeEvent(self, event):
        event.ignore()
        self.hide()

    def init_keylogger(self):
        self.keylogger = KeyLogger(
            filename="savesyndrom.log",
            show=lambda *keys: self.show_message.emit(*keys),
        )
        self.keylogger.all_processes = True
        combination = frozenset(("ctrl", "s"))
        combinations = self.settings.get_combinations()
        self.keylogger.add_combination(
            combination=("ctrl", "s"),
            show=combinations[combination] if combination in combinations else False,
        )

    def show_settings(self, last_item: QtWidgets.QListWidgetItem,
                      current_item: QtWidgets.QListWidgetItem):
        for frame in self.settings_frames:
            frame.hide()
        self.settings_frames[self.settings_listwidget.currentRow()].show()

    def show_toggled(self, value: bool):
        self.text_frame.setEnabled(value)

    def text_fontsize_changed(self, text: str):
        font = self.test_window.label.font()
        font.setPointSize(int(text) if text else 0)
        self.test_window.label.setFont(font)

    def open_text_color_dialog(self):
        color = QtWidgets.QColorDialog.getColor()

        if color.isValid():
            red, green, blue, alpha = color.getRgb()
            self.test_window.label.setStyleSheet(f"color: rgba({red}, {green}, {blue}, {alpha})")

    def calc_statistic(self):
        statistic = self.keylogger.get_statistic()
        count = 0
        for record, c in statistic["pressed"].items():
            if record[1] == frozenset(("ctrl", "s")):
                count += c
        text = f"Pressed ctrl+s {count} for "
        time = statistic["time"]
        if time > self.YEAR:
            text += f"{time // self.YEAR} years "
            time %= self.YEAR
        if time > self.DAY:
            text += f"{time // self.DAY} days "
            time %= self.DAY
        if time > self.HOUR:
            text += f"{time // self.HOUR} hours "
            time %= self.HOUR
        if time > self.MINUTE:
            text += f"{time // self.MINUTE} minutes"
            time %= self.MINUTE
        if time:
            text += f"{time} seconds"
        count = count if count else 1
        if count:
            text += f"\nFrequency: one time in "
            time = statistic["time"] // count
            if time > self.YEAR:
                text += f"{time // self.YEAR} years "
                time %= self.YEAR
            if time > self.DAY:
                text += f"{time // self.DAY} days "
                time %= self.DAY
            if time > self.HOUR:
                text += f"{time // self.HOUR} hours "
                time %= self.HOUR
            if time > self.MINUTE:
                text += f"{time // self.MINUTE} minutes"
                time %= self.MINUTE
            if time:
                text += f"{time} seconds"
        self.statistic_label.setText(text)

    def start_keylogger(self):
        self.keylogger.start()

        self.startstop_button.setText(self.translate("MainWindow", "Stop"))
        self.startstop_button.clicked.disconnect()
        self.startstop_button.clicked.connect(self.stop_keylogger)

    def stop_keylogger(self):
        self.keylogger.stop()
        self.init_keylogger()

        self.startstop_button.setText(self.translate("MainWindow", "Start"))
        self.startstop_button.clicked.disconnect()
        self.startstop_button.clicked.connect(self.start_keylogger)

    def apply(self):
        self.settings.all_processes = True
        self.settings.all_combinations = False
        self.settings.clear_processes()
        self.settings.clear_combinations()
        self.settings.add_combination(
            combination=("ctrl", "s"),
            show=self.show_checkbox.checkState() == QtCore.Qt.Checked,
        )
        self.keylogger.add_combination(
            combination=("ctrl", "s"),
            show=self.show_checkbox.checkState() == QtCore.Qt.Checked,
        )
        language = self.language_combobox.currentText()
        for l, code in self.settings.LANGUAGES.items():
            if language == l:
                self.settings.language = code
                break
        text_fontsize = self.text_fontsize_lineedit.text()
        text_fontsize = int(text_fontsize) if text_fontsize else 0
        self.settings.text_fontsize = text_fontsize
        text_font = self.FONTS[self.text_font_combobox.currentText()]
        self.settings.text_font = text_font
        self.show_window.label.setFont(QtGui.QFont(text_font, text_fontsize))
        red, green, blue, alpha = map(int, re.findall("\d+", self.test_window.label.styleSheet()))
        self.text_color_label.setText(
            self.translate("MainWindow", "Current color: ") + str((red, green, blue, alpha)),
        )
        self.settings.set_text_color(red=red, green=green, blue=blue, alpha=alpha)
        self.show_window.label.setStyleSheet(f"color: rgba({red}, {green}, {blue}, {alpha})")
        text_position = self.test_window.pos()
        text_position = (text_position.x(), text_position.y())
        self.settings.set_text_position(*text_position)
        text_size = self.test_window.size()
        text_size = (text_size.width(), text_size.height())
        self.settings.set_text_size(*text_size)
        self.show_window.setGeometry(*text_position, *text_size)
        text_time = self.text_time_lineedit.text()
        self.settings.text_time = int(text_time) if text_time else 0
        window_position = self.pos()
        self.settings.set_window_position(x=window_position.x(), y=window_position.y())
        window_size = self.size()
        self.settings.set_window_size(width=window_size.width(), height=window_size.height())

        self.settings.save("settings.json")

    def exit(self):
        self.application.quit()
