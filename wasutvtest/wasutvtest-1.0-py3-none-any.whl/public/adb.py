import os
import platform
import sys


class adb:

    def __init__(self, station):
        self.platform = station

    def adb_devices(self):
        if 'Windows' in self.platform:
            os.system('adb devices')

    def adb_connect(self, ip):
        if self.platform == 'Windows':
            os.system('adb connect' + ip)

    def adb_install(self, apk_package):
        if self.platform == 'Windows':
            os.system('adb install' + apk_package)

    def adb_uninstall(self, apk_package):
        if self.platform == 'Windows':
            os.system('adb uninstall' + apk_package)

    def adb_shell(self):
        if self.platform == 'Windows':
            os.system('adb shell')

    def adb_log(self):
        if self.platform == 'Windows':
            os.system('adb logcat')

    def adb_startActivity(self, options='n', activity=None):
        if self.platform == 'Windows':
            os.system('adb shell am start' + options + activity)

    def start_appium(self, ip_address=None, start_port=None):
        if self.platform == 'Windows':
            os.system('appium -a ' + ip_address + ' -p ' + start_port + ' --session-override')

    def send_key(self, key_code):
        if self.platform == 'Windows':
            os.system('adb shell input keyevent '+key_code)
