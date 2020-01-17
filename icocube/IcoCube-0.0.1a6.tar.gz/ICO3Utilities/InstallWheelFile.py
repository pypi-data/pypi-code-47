#  Copyright (c) $Gille PREVOT, Guillaume PREVOT, Anne-Delphine PREVOT

import pip

class InstallWheelFile:

    @staticmethod
    def install_whl(path):
        pip.main(['install', path])


if __name__ == '__main__':
    wpath = r"C:\Users\Gilles\PycharmProjects\IcoCube\dist\IcoCube-0.0.1a2-py3-none-any.whl"
    InstallWheelFile.install_whl(wpath)
