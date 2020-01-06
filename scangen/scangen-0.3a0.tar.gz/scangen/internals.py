import ctypes
import json

libregexp = ctypes.CDLL("libregexp.so")
libregexp.regexp_open.argtypes = [ctypes.c_char_p]
libregexp.regexp_open.restype = ctypes.POINTER(ctypes.c_char)
libregexp.regexp_close.argtypes = [ctypes.c_void_p]
libregexp.regexp_close.restype = None

class DFA:
    def __init__(self, s):
        self.regex = s
        re = libregexp.regexp_open(s.encode("utf-8"))
        js = json.loads(ctypes.cast(re, ctypes.c_char_p).value)
        libregexp.regexp_close(re)
        self.start = js["start"]
        self.accepts = set(js["accepts"])
        self.transitions = {}
        for q, dq in enumerate(js["transitions"]):
            self.transitions[q] = dq[:]
        self.error = js["error"]
