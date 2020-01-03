import wx
from datetime import datetime, timedelta


class TimedProgressBar(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        # widgets
        sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.progress = wx.Gauge(self)
        self.label = wx.StaticText(self, label=" 0:00:00 / 0:00:00")

        sizer.Add(self.progress, 1, wx.EXPAND)
        sizer.Add(self.label, 0, wx.ALIGN_CENTER_VERTICAL)

        self.SetSizer(sizer)

        # data
        self.started = False
        self.done = False
        self.last_update = datetime.now()
        self.finish_time = datetime.now()
        self.start_time = datetime.now()
        self.last_value = 0.0
        self.speeds = []

        # timer
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.update, self.timer)
        self.timer.Start(1000)

    def reset(self):
        self.started = False
        self.done = False
        self.last_update = datetime.now()
        self.finish_time = datetime.now()
        self.start_time = datetime.now()
        self.last_value = 0.0
        self.speeds = []

    def SetValue(self, value: float):
        self.progress.SetValue(int(value))
        if not self.started:
            self.start_time = datetime.now()
            self.started = True
        if value >= 99.9:
            self.done = True
        if value - self.last_value > 0.25:
            delta = value - self.last_value
            self.last_value = value
            dt = (datetime.now() - self.last_update).total_seconds()
            dt = 0.01 if dt < 0.01 else dt
            self.last_update = datetime.now()

            self.speeds.append(delta / dt)
            speeds = self.speeds[-3:]
            speed = sum(speeds) / len(speeds)

            self.finish_time = datetime.now() + timedelta(seconds=(100.0 - value) / speed)

    def update(self, event):
        if not self.started or self.done:
            return
        elapsed = datetime.now() - self.start_time
        if self.finish_time > datetime.now():
            finish = self.finish_time - datetime.now()
        else:
            finish = timedelta()
        self.label.SetLabel(f" {str(elapsed).split('.')[0]} / {str(finish).split('.')[0]}")

    def stop(self):
        self.done = True
