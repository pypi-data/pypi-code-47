from crontab import CronTab
from pathlib import Path


class CronManager():
    def __init__(self):
        self.__cron = CronTab(user=True)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.__cron.write()

    def set_reboot_task(self, command):
        if not self.check_reboot_task(command):
            self.__cron.new(command).every_reboot()

    def unset_reboot_task(self, command):
        # TODO : Check 'check and remove' is better way
        self.__cron.remove(self.__cron.find_command(command))

    def check_reboot_task(self, command):
        for _ in self.__cron.find_command(command):
            return True
        return False


class BashManager():
    def __init__(self):
        path = str(Path.home().joinpath('.bashrc'))
        self.__file = open(path, mode='r+')

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.__file.close()

    def set_terminal_task(self, command):
        if not self.check_terminal_task(command):
            self.__file.write(command + '\n')

    def unset_terminal_task(self, command):
        # TODO : Check 'check and remove' is better way
        lines = self.__file.readlines()
        self.__file.seek(0)
        for line in lines:
            if command != line.strip():
                self.__file.write(line)
        self.__file.truncate()

    def check_terminal_task(self, command):
        for line in self.__file:
            if command == line.strip():
                return True
        return False
