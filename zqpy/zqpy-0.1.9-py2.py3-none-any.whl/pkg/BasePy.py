import os, sys
sys.path.append(os.path.dirname(__file__))

from LogService import LogServiceClass
from FileService import FileServiceClass
from HttpService import HttpServiceClass
from RegexService import RegexServiceClass
from ThreadService import ThreadServiceClass
from TimeService import TimeServiceClass
from VideoDownloadService import VideoDownloadServiceClass
from LocallizeService import LocallizeServiceClass

from WaitExecutService import WaitExecutServiceClass
from QrCodeService import QrCodeServiceClass
from ToolsService import ToolsServiceClass

from MailService import MailServiceClass

class BasePyClass(object):
    def __init__(self, *args, **kwargs):
        Log = LogServiceClass(tag=self.vGetLogTag())
        self.LogD = Log.LogD
        self.LogW = Log.LogW
        self.LogE = Log.LogE

        self.File = FileServiceClass()
        self.Http = HttpServiceClass()
        self.Regex = RegexServiceClass()
        self.Thread = ThreadServiceClass()
        self.Time = TimeServiceClass()
        self.VideoDownload = VideoDownloadServiceClass()
        self.Localize = LocallizeServiceClass(path=kwargs.get("LocallizePath", None))
        self.WaitExecutService = WaitExecutServiceClass()

        self.QrCodeService = QrCodeServiceClass()

        self.ToolsService = ToolsServiceClass()

        self.MailService = MailServiceClass()

    ############################################通用方法##########################################
    def GetLocalize(self, key):
        return self.Localize.Get(key)

    ############################################子类可重写##########################################
    def vGetLogTag(self):
        return "BasePyClass"

BasePy = BasePyClass(LocallizePath='{}{}'.format(os.path.dirname(__file__), '/Locallize.txt'))