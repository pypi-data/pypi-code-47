from koconf.scripts import SetupManager


class TestScriptManager():
    def setup_class(self):
        with SetupManager() as setup:
            self.__status = setup.check_need_setup()

    def teardown_class(self):
        with SetupManager() as setup:
            if self.__status:
                setup.set_need_setup()
            else:
                setup.unset_need_setup()

    @staticmethod
    def test_setup_true():
        with SetupManager() as setup:
            setup.set_need_setup()
            assert setup.check_need_setup()

    @staticmethod
    def test_setup_false():
        with SetupManager() as setup:
            setup.unset_need_setup()
            assert not setup.check_need_setup()
