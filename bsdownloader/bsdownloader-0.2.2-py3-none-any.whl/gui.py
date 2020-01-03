import wx
import wx.richtext
import sys
from types import SimpleNamespace

from .config import Config
from .download import WorkerThread, clear_cache
from .timed_progress import TimedProgressBar


def wx_after(func):
    def after_fun(*args, **kwargs):
        wx.CallAfter(lambda: func(*args, **kwargs))

    return after_fun


class AppGui(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(640, 480))
        self.config = Config()
        self.worker = None

        app_panel = wx.Panel(self)
        main_box = wx.BoxSizer(wx.VERTICAL)

        # settings
        settings_box = wx.StaticBoxSizer(wx.VERTICAL, app_panel, "Settings")

        # path picker
        path_box = wx.BoxSizer(wx.HORIZONTAL)
        label = wx.StaticText(settings_box.GetStaticBox(), label="Game path: ")
        self.dir_picker = wx.DirPickerCtrl(settings_box.GetStaticBox(), path=self.config.path)
        path_box.Add(label, 0, wx.ALL | wx.ALIGN_CENTER, 2)
        path_box.Add(self.dir_picker, 1, wx.ALL | wx.EXPAND, 2)

        # count picker
        count_box = wx.BoxSizer(wx.HORIZONTAL)
        label = wx.StaticText(settings_box.GetStaticBox(), label="Song count: ")
        self.count_picker = wx.SpinCtrl(
            settings_box.GetStaticBox(), style=wx.ALIGN_RIGHT, min=1, max=1000, initial=self.config.count
        )
        count_box.Add(label, 0, wx.ALL | wx.ALIGN_CENTER, 2)
        count_box.Add(self.count_picker, 1, wx.ALL | wx.EXPAND, 2)

        settings_box.Add(path_box, 0, wx.ALL | wx.EXPAND, 2)
        settings_box.Add(count_box, 0, wx.ALL | wx.EXPAND, 2)

        # progress
        progress_box = wx.StaticBoxSizer(wx.VERTICAL, app_panel, "Progress")
        self.progress1 = TimedProgressBar(progress_box.GetStaticBox())
        self.progress2 = wx.Gauge(progress_box.GetStaticBox())

        # text & start button
        text_box = wx.BoxSizer(wx.HORIZONTAL)
        self.progress_label = wx.StaticText(progress_box.GetStaticBox(), label="Waiting for start")
        self.start_button = wx.Button(progress_box.GetStaticBox(), label="Start")
        text_box.Add(self.progress_label, 1, wx.ALL | wx.EXPAND, 2)
        text_box.Add(self.start_button, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 2)

        progress_box.Add(self.progress1, 0, wx.ALL | wx.EXPAND, 2)
        progress_box.Add(self.progress2, 0, wx.ALL | wx.EXPAND, 2)
        progress_box.Add(text_box, 0, wx.ALL | wx.EXPAND, 2)

        # log
        log_box = wx.StaticBoxSizer(wx.VERTICAL, app_panel, "Log")
        self.log_text = wx.richtext.RichTextCtrl(
            log_box.GetStaticBox(), style=wx.richtext.RE_MULTILINE | wx.richtext.RE_READONLY
        )
        log_box.Add(self.log_text, 1, wx.ALL | wx.EXPAND, 0)

        # main panel
        main_box.Add(settings_box, 0, wx.ALL | wx.EXPAND, 2)
        main_box.Add(progress_box, 0, wx.ALL | wx.EXPAND, 2)
        main_box.Add(log_box, 1, wx.ALL | wx.EXPAND, 2)
        app_panel.SetSizer(main_box)

        # bindings
        self.Bind(wx.EVT_CLOSE, self.on_close)
        self.dir_picker.Bind(wx.EVT_DIRPICKER_CHANGED, self.on_path)
        self.count_picker.Bind(wx.EVT_SPINCTRL, self.on_count)
        self.start_button.Bind(wx.EVT_BUTTON, self.on_start)

        # redirect stdout to logging
        self.bind_stdout()
        # redirect stderr to error box
        self.bind_stderr()

        # add top menu
        self.make_menu()

        # show window
        self.Show(True)

    def bind_stdout(self):
        log_class = SimpleNamespace()

        @wx_after
        def _print_log(log: str):
            self.log_text.BeginTextColour(wx.Colour(25, 125, 25))
            self.log_text.WriteText(log)
            self.log_text.EndTextColour()
            self.log_text.ShowPosition(self.log_text.LastPosition)
            self.log_text.Update()

        log_class.write = _print_log
        sys.stdout = log_class

    def bind_stderr(self):
        err_class = SimpleNamespace()

        @wx_after
        def _show_err(err: str):
            if not err.strip():
                return
            self.log_text.BeginTextColour(wx.Colour(200, 50, 50))
            self.log_text.WriteText(err)
            self.log_text.EndTextColour()
            self.log_text.ShowPosition(self.log_text.LastPosition)
            self.log_text.Update()
            wx.MessageBox(err, "Error", style=wx.ICON_ERROR | wx.OK)

        err_class.write = _show_err
        sys.stderr = err_class

    def make_menu(self):
        menu_bar = wx.MenuBar()
        file_menu = wx.Menu()
        file_quit = file_menu.Append(wx.ID_EXIT, "Quit", "Quit application")
        file_clear = file_menu.Append(wx.ID_CLEAR, "Clear cache", "Clear cache folder")
        menu_bar.Append(file_menu, "&File")

        # binds
        self.Bind(wx.EVT_MENU, lambda e: self.Close(), file_quit)
        self.Bind(wx.EVT_MENU, lambda e: clear_cache(), file_clear)

        self.SetMenuBar(menu_bar)

    def on_close(self, event):
        if self.worker is not None:
            self.worker.stop()
            self.worker.join()

        self.dir_picker.Destroy()
        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__
        self.Destroy()

    def on_start(self, event):
        # stop
        if self.worker is not None and self.worker.working:
            self.worker.stop()
            self.worker.join()
            self.progress1.stop()
            print("Stopped!")
            self.start_button.SetLabel("Start")
        # start
        else:
            self.progress1.reset()
            self.worker = WorkerThread(self, self.config)
            self.start_button.SetLabel("Stop")
            self.log_text.Clear()
            self.worker.start()

    def on_path(self, event):
        self.config.path = event.GetPath()
        self.config.save()

    def on_count(self, event):
        self.config.count = event.GetPosition()
        self.config.save()

    @wx_after
    def on_done(self):
        self.start_button.SetLabel("Start")
        wx.MessageBox("Done!", self.GetTitle())

    @wx_after
    def set_progress1(self, value: int) -> None:
        self.progress1.SetValue(value)

    @wx_after
    def set_progress2(self, value: int) -> None:
        self.progress2.SetValue(value)

    @wx_after
    def set_label(self, value: str) -> None:
        self.progress_label.SetLabel(value)
        self.log_text.BeginTextColour(wx.Colour(0, 0, 0))
        self.log_text.WriteText(value + "\n")
        self.log_text.EndTextColour()
        self.log_text.ShowPosition(self.log_text.LastPosition)
        self.log_text.Update()


class GuiIter:
    def __init__(self, collection, p_fun, p_from=0, p_to=100):
        self.size = len(collection)
        self.pos = 0
        self.p_fun = p_fun
        self.iter = iter(collection)
        self.p_start = p_from
        self.p_diff = p_to - p_from

    def __iter__(self):
        return self

    def __next__(self):
        self.p_fun(self.p_start + self.pos / self.size * self.p_diff)
        self.pos += 1
        return next(self.iter)
