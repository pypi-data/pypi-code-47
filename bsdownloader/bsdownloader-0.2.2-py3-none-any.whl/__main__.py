import wx
from .gui import AppGui


def main():
    app = wx.App(False)
    AppGui(None, "Beat Saber - Downloader")
    app.MainLoop()


if __name__ == "__main__":
    main()
