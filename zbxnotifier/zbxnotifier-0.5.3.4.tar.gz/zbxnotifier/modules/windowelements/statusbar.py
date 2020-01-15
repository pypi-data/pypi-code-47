from PyQt5.QtWidgets import QLabel, QPushButton, QDialog, QFormLayout, QVBoxLayout, QLineEdit, QDialogButtonBox, QComboBox
from PyQt5.QtWidgets import QStatusBar
from zbxnotifier.modules.zabbix.zabbix import ZabbixConnection
from zbxnotifier.modules.settings import Settings
from zbxnotifier.modules.zabbix.hostgroups import HostGroups
from PyQt5.QtCore import QRunnable, pyqtSlot, pyqtSignal, QObject


class StatusSignals(QObject):
    finished = pyqtSignal()
    error = pyqtSignal(tuple)
    result = pyqtSignal(object)


class StatusWorker(QRunnable):
    def __init__(self):
        super(StatusWorker, self).__init__()
        self.signals = StatusSignals()

    @pyqtSlot()
    def run(self):
        connection_status = ZabbixConnection.get_status_desc()
        self.signals.result.emit(connection_status)


class Statusbar(QStatusBar):
    def __init__(self):
        super().__init__()
        self.status_widget = QLabel("ZBX Status: " + ZabbixConnection.get_status_desc())
        self.settings_button = QPushButton("SETTINGS")
        self.filtering_button = QPushButton("FILTERING")
        self.settings_button.clicked.connect(self.settings_clicked)
        self.filtering_button.clicked.connect(self.filtering_clicked)

        # Create elements
        self.settings_dialog = None

        self.qline_zbx_server = None
        self.qline_zbx_username = None
        self.qline_zbx_password = None

        # Initializing elements
        self.setup_settings_dialog()
        # self.setup_filtering_dialog()
        self.init_elements()

    def setup_filtering_dialog(self):
        self.filtering_dialog = QDialog()
        self.settings_dialog.setWindowTitle("Alert Filtering")

        dialog_layout = QVBoxLayout()
        form_layout = QFormLayout()

        # self.qline_exclude_tags = QLineEdit(Settings.config.get('AlertFilter', 'exclude-tags'))
        # form_layout.addRow('Tags to exclude (comma separated list)', self.qline_exclude_tags)

        self.cbox_severity = QComboBox()
        self.cbox_severity.addItem("Not classified")
        self.cbox_severity.addItem("Information")
        self.cbox_severity.addItem("Warning")
        self.cbox_severity.addItem("Average")
        self.cbox_severity.addItem("High")
        self.cbox_severity.addItem("Disaster")
        self.cbox_severity.setCurrentIndex(int(Settings.config.get('AlertFilter', 'min-severity')))

        form_layout.addRow('Minimum severity', self.cbox_severity)

        self.cbox_group = QComboBox()
        self.cbox_group.addItem("-->NO FILTER<--")
        for group in HostGroups.groups:
            self.cbox_group.addItem(group.name)
        form_layout.addRow('Group to filter on', self.cbox_group)

        dialog_layout.addLayout(form_layout)

        buttons = QDialogButtonBox(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        buttons.clicked.connect(self.filtering_dialog.accept)
        buttons.accepted.connect(self.filtering_ok_clicked)

        dialog_layout.addWidget(buttons)

        self.filtering_dialog.setLayout(dialog_layout)

    def setup_settings_dialog(self):
        self.settings_dialog = QDialog()
        self.settings_dialog.setWindowTitle("Settings")

        dialog_layout = QVBoxLayout()

        self.qline_zbx_server = QLineEdit(Settings.config.get('ZabbixSettings', 'server'))
        self.qline_zbx_username = QLineEdit(Settings.config.get('ZabbixSettings', 'username'))

        password_input = QLineEdit(Settings.config.get('ZabbixSettings', 'password'))
        password_input.setEchoMode(QLineEdit.Password)
        self.qline_zbx_password = password_input
        form_layout = QFormLayout()

        form_layout.addRow('Zabbix Server URL', self.qline_zbx_server)
        form_layout.addRow('Zabbix Username', self.qline_zbx_username)
        form_layout.addRow('Zabbix Password', self.qline_zbx_password)

        buttons = QDialogButtonBox(QDialogButtonBox.Cancel | QDialogButtonBox.Ok )

        buttons.clicked.connect(self.settings_dialog.accept)
        buttons.accepted.connect(self.settings_ok_clicked)

        dialog_layout.addLayout(form_layout)
        dialog_layout.addWidget(QLabel("Clickin 'OK' will re-initialize the connection!"))
        dialog_layout.addWidget(buttons)

        dialog_layout.addWidget(QLabel("Your password will be stored on your keyring!"))

        self.settings_dialog.setLayout(dialog_layout)

    def settings_clicked(self):
        self.settings_dialog.show()

    def filtering_clicked(self):
        self.setup_filtering_dialog()
        self.filtering_dialog.show()

    def settings_ok_clicked(self):
        Settings.config.set('ZabbixSettings', 'username', self.qline_zbx_username.text())
        Settings.config.set('ZabbixSettings', 'server', self.qline_zbx_server.text())
        Settings.config.set('ZabbixSettings', 'password', self.qline_zbx_password.text())
        Settings.save_running_config()
        ZabbixConnection.re_init()

    def filtering_ok_clicked(self):

        # Set tag filter list
        # Settings.config.set('AlertFilter', 'exclude-tags', str(self.qline_exclude_tags.text()))

        # Set min-severity
        Settings.config.set('AlertFilter', 'min-severity', str(self.cbox_severity.currentIndex()))

        # Set group filter
        if self.cbox_group.currentIndex() == 0:
            Settings.config.set('AlertFilter', 'group', "")
        else:
            Settings.config.set('AlertFilter', 'group', self.cbox_group.currentText())

        Settings.save_running_config()

    def update_elements(self):
        self.status_widget.setText("ZBX Status: " + ZabbixConnection.get_status_desc())
        self.status_widget.update()

    def init_elements(self):
        self.addWidget(self.settings_button)
        self.addWidget(self.filtering_button)
        self.addWidget(self.status_widget)




