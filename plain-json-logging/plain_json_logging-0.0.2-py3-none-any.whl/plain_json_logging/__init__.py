import datetime
import json
import sys

class PlainJsonLogging:

    def __init__(self,
      file=sys.stderr,
      strftime='%Y-%m-%dT%H:%M:%S.%f',
      timedelta=0,
      timestampname='timestamp',
      levelname='level',
      messagename='message',
      inforname='INFO',
      warnname='WARNNING',
      errorname='ERROR'):
        self.file = file
        self.strftime = strftime
        self.timedelta = datetime.timedelta(minutes=timedelta)
        self.timestampname = timestampname
        self.levelname = levelname
        self.messagename = messagename
        self.inforname = inforname
        self.warnname = warnname
        self.errorname = errorname

    def __dump(self, log):
        self.file.write(json.dumps(log, ensure_ascii=False) + u'\n')

    def __timestamp(self):
        now = datetime.datetime.now() + self.timedelta
        return now.strftime(self.strftime)

    def __log(self, level, message, extend=None):
        log = {}
        if extend is not None:
            log.update(extend)
        log[self.timestampname] = self.__timestamp()
        log[self.levelname] = level
        log[self.messagename] = message
        self.__dump(log)

    def error(self, message, extend=None):
        self.__log(self.errorname, message, extend)

    def warn(self, message, extend=None):
        self.__log(self.warnname, message, extend)

    def info(self, message, extend=None):
        self.__log(self.inforname, message, extend)
