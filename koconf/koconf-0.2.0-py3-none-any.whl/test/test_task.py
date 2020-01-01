from koconf.task import BashManager, CronManager


class TestCronManager():
    def setup_class(self):
        self.__command = ': this is nop command :'

    def teardown_class(self):
        with CronManager() as cron:
            cron.unset_reboot_task(self.__command)

    def test_cron_task_set(self):
        with CronManager() as cron:
            cron.set_reboot_task(self.__command)

        with CronManager() as cron:
            assert cron.check_reboot_task(self.__command)

    def test_cron_task_unset(self):
        with CronManager() as cron:
            cron.unset_reboot_task(self.__command)

        with CronManager() as cron:
            assert not cron.check_reboot_task(self.__command)


class TestBashManager():
    def setup_class(self):
        self.__command = ': this is nop command :'

    def teardown_class(self):
        with BashManager() as bash:
            bash.unset_terminal_task(self.__command)

    def test_bash_task_set(self):
        with BashManager() as bash:
            bash.set_terminal_task(self.__command)

        with BashManager() as bash:
            assert bash.check_terminal_task(self.__command)

    def test_bash_task_unset(self):
        with BashManager() as bash:
            bash.unset_terminal_task(self.__command)

        with BashManager() as bash:
            assert not bash.check_terminal_task(self.__command)
