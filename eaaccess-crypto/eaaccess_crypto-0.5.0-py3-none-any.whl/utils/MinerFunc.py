from shinehope.utils.definitions import EAACCESS_DIR
from shinehope.utils.mylogger import appLog
import os

# FileAccessKey= "shinehope/configs/mineraccesskey"

class MinerFunc:
    @staticmethod
    def GetMinerUniqueId() -> int:
        baseNumber = 1000000000
        procID = baseNumber + os.getpid()

        return procID

    @staticmethod
    def GetMachineAccessKey() -> str:
        configPath = os.path.join(EAACCESS_DIR, 'configs', 'mineraccesskey')

        line = ""
        try:
            with open(configPath, "r", encoding="utf-8") as fileObj:
                tmpSeri = fileObj.readline()
                line = tmpSeri.strip()
        except Exception as ex:
            appLog.error(str(ex))

        return line