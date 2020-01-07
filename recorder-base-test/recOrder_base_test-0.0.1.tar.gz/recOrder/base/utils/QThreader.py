from PyQt5.QtCore import QRunnable, QThreadPool, QThread
from multiprocessing import Pool, Process


class ProcessRunnable(QRunnable):
    def __init__(self, target, args):
        super().__init__()
        self.t = target
        self.args = args

    def run(self):
        self.t(*self.args)

    def start(self):
        QThreadPool.globalInstance().start(self)


class ThreadRandom(QThread):

    def __init__(self, target, args):
        QThread.__init__(self)
        self.t = target
        self.args = args

    def run(self):
        self.t(*self.args)


class MultiProcessor:

    def __init__(self, target, args):
        self.t = target
        self.args = args

    def launch(self):
        p = Process(target=self.t, args=(self.args,))
        p.start()
