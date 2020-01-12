from PyQt5.QtWidgets import QLabel, QPushButton, QDialog, QFormLayout, QVBoxLayout, QLineEdit, QDialogButtonBox
from PyQt5.QtWidgets import QStatusBar
from zbxnotifier.modules.zabbix.zabbix import ZabbixConnection
from zbxnotifier.modules.settings import Settings
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
        self.settings_button.clicked.connect(self.settings_clicked)
        self.setup_settings_dialog()
        self.init_elements()

    def setup_settings_dialog(self):
        self.settings_dialog = QDialog()
        self.settings_dialog.setWindowTitle("Settings")

        dialog_layout = QVBoxLayout()

        self.qline_zbx_server = QLineEdit(Settings.config.get('ZabbixSettings', 'server'))
        self.qline_zbx_username = QLineEdit(Settings.config.get('ZabbixSettings', 'username'))
        form_layout = QFormLayout()
        form_layout.addRow('Zabbix Server URL', self.qline_zbx_server)
        form_layout.addRow('Zabbix Username', self.qline_zbx_username)


        buttons = QDialogButtonBox(QDialogButtonBox.Cancel | QDialogButtonBox.Ok )

        buttons.clicked.connect(self.settings_dialog.accept, )
        buttons.accepted.connect(self.settings_ok_clicked)

        dialog_layout.addLayout(form_layout)
        dialog_layout.addWidget(QLabel("Clickin 'OK' will re-initialize the connection!"))
        dialog_layout.addWidget(buttons)

        dialog_layout.addWidget(QLabel("The supplied username must exist in the Windows Credential store under the 'zabbix' service!"))

        self.settings_dialog.setLayout(dialog_layout)

    def settings_ok_clicked(self):
        Settings.config.set('ZabbixSettings', 'username', self.qline_zbx_username.text())
        Settings.config.set('ZabbixSettings', 'server', self.qline_zbx_server.text())
        Settings.save_running_config()
        ZabbixConnection.re_init()

    def settings_clicked(self):
        self.settings_dialog.show()

    def update_elements(self):
        self.status_widget.setText("ZBX Status: " + ZabbixConnection.get_status_desc())
        self.status_widget.update()

    def init_elements(self):
        self.addWidget(self.settings_button)
        self.addWidget(self.status_widget)




