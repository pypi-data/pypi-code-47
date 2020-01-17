
import os
import re
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from tool.device.library.nvme import NVMe
from .library.nvme_cmd import SmartHealth, NamespaceDataStructure
from utils.buf import Malloc
from utils.system import execute


class NVME(object):

    def __init__(self, dev_index=0):
        self.dev_index = dev_index

    def list_dev(self):
        dev_list = list()
        cmd = "lsblk"
        _, outs = execute(cmd)
        rets = re.findall("((nexus|nvme)\w+)", outs, re.DOTALL)
        if rets:
            for item in rets:
                ret_index = re.findall("(nexus|nvme)(\d+)n", item[0])
                if ret_index:
                    dev_index = ret_index[0][1]
                    dev = {"index": dev_index, "name": item[0]}
                    dev_list.append(dev)
        return dev_list

    def getlog(self, lid=0x01, numd=100, numdu=0, lpol=0, lpou=0, nsid=0, type_=SmartHealth):
        dev_name = "/dev/nvme{}".format(self.dev_index)
        nvme_device = NVMe(dev_name)
        ret, prp = None, None
        if lid == 0x02:
            prp = Malloc(length=1, types=type_)
            ret = nvme_device.nvme_smart_log(nsid, prp.buffer())
        return ret, prp

    def identify(self, cns, cntid, nsid, types):
        dev_name = "/dev/nvme{}".format(self.dev_index)
        nvme_device = NVMe(dev_name)
        prp = Malloc(types=types)
        ret = -1
        if cns == 0x1:
            ret = nvme_device.nvme_identify_ctrl(prp.buffer())
        elif cns == 0x11:
            ret = nvme_device.nvme_identify_ns(nsid, False, prp.buffer())
        return ret, prp

    def upgrade_fw(self, fw_path, device_index, slot):
        dev_name = "/dev/nvme{}".format(device_index)
        nvme_device = NVMe(dev_name)
        length, pdata = self.get_firmware_buf(fw_path)
        ret = nvme_device.nvme_fw_download(0, length, pdata)
        if ret == 0:
            ret = nvme_device.nvme_fw_commit(slot, 1, bpid=0)
            if ret == 0:
                ret = nvme_device.nvme_reset_controller()
        result = True if ret == 0 else False
        return result, ""

    def get_firmware_buf(self, fw_path):
        size = os.path.getsize(fw_path)
        ndw = size / 4
        fw_file = open(fw_path, "rb")
        fw_data = fw_file.read()
        return ndw, id(fw_data)
