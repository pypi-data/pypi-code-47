
import os
from ctypes import windll
from utils.buf import Malloc
from tool.device.library.nvme_cmd import SmartHealth


class NVME(object):

    def __init__(self, dev_index):
        self.dev_index = dev_index
        path = os.path.realpath(os.path.join(os.path.dirname(__file__), "library", "nvme_ioctl.dll"))
        self.__dll = windll.LoadLibrary(path)

    def getlog(self, lid=0x01, numd=100, numdu=0, lpol=0, lpou=0, nsid=0, type_=SmartHealth):
        ret, prp = None, None
        if lid == 0x02:
            ret, prp = self.get_smart_log()
        return ret, prp

    def get_smart_log(self):
        prp = Malloc(types=SmartHealth)
        ret = self.__dll.get_smartlog(self.dev_index, prp.buffer())
        if ret != 0:
            print("get smart log failed")
        return ret, prp

    def identify(self, cns, cntid, nsid, types):
        prp = Malloc(types=types)
        ret = -1
        if cns == 0x1:
            ret = self.__dll.identify_controller(self.dev_index, prp.buffer())
        elif cns == 0x11:
            ret = self.__dll.identify_namespace(self.dev_index, prp.buffer())
        return ret, prp

    def upgrade_fw(self, fw_path, device_index, slot):
        ret = self.__dll.upgrade_fw(device_index, slot, fw_path)
        return ret
