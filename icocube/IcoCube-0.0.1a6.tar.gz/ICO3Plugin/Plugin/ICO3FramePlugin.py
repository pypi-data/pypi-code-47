
from ICO3Plugin.Plugin.ico3plugin import ICO3Plugin

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True


class ICO3FramePlugin(tk.Toplevel, ICO3Plugin):         #tk.Tk,
    pass


class ICO3XXXPlugin( ICO3Plugin):         #tk.Toplevel,

    def __init__(self, xMainFrame = None, XY = None) :
        pass
