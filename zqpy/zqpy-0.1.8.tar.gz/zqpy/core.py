# Insert your code here. 
print(" Init zqpy core By ZhouQing")
from pkg import *       # 直接可以调用Class, 因为init里面注册了

class BasePyClass(object):

    def __init__(self, *args, **kwargs):
        Log = LogServiceClass(tag=self.vGetLogTag())
        self.LogD = Log.LogD
        self.LogW = Log.LogW
        self.LogE = Log.LogE

        self.FileService = FileServiceClass()
        self.HttpService = HttpServiceClass()
        self.RegexService = RegexServiceClass()
        self.ThreadService = ThreadServiceClass()
        self.TimeService = TimeServiceClass()
        self.VideoDownloadService = VideoDownloadServiceClass()
        self.LocalizeService = LocallizeServiceClass(path=kwargs.get("LocallizePath", None))
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

base = BasePyClass()