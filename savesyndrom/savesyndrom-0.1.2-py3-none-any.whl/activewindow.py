import re
import subprocess
import sys


def linux():
    process = subprocess.Popen(["xprop", "-root", "_NET_ACTIVE_WINDOW"], stdout=subprocess.PIPE)
    output = process.stdout.readline()
    window_id = re.findall(b"0x[abcdef\d]+", output)[0].decode("utf-8")
    process = subprocess.Popen(["xprop", "-id", window_id, "WM_NAME"], stdout=subprocess.PIPE)
    output = process.stdout.readline()
    name = re.search(b"WM_NAME\(\w+\) = (.*)$", output).group(1).decode("utf-8")
    return name


def windows():
    import win32gui
    window = win32gui.GetForegroundWindow()
    return win32gui.GetWindowText(window)


def mac():
    from AppKit import NSWorkspace
    return NSWorkspace.sharedWorkspace().activeApplication()["NSApplicationName"]


def get_active_window():
    if sys.platform in ("linux", "linux2"):
        return linux()
    elif sys.platform in ("Windows", "win32", "cygwin"):
        return windows()
    elif sys.platfrom in ("Mac", "darwin", "os2", "os2emx"):
        return mac()
