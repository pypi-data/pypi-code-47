from WasuTvTest.public import appium_config

if __name__ == '__main__':
    # station = platform.platform()
    # adb_cmd = adb(station)
    # adb_cmd.adb_devices()
    # adb_cmd.start_appium(ip_address=data.appium_start_ip, start_port=data.appium_start_port)
    # case = get_case()
    # case_name = case.get_case_name()
    # case_action = case.get_case_action()
    # print(case_name)
    path = '../config/appium_config.yaml'
    config = appium_config(path).get_config()
    print(config['appium_config']['desired_caps'])
