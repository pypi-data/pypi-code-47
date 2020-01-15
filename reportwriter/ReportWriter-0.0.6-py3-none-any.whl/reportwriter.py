from typing import Iterable, Dict
from pathlib import Path
from io import StringIO

class ReportWriter:
    data: StringIO
    delim: str

    default_delim = "\t"
    default_newline = "\n"

    def __init__(self, data="", delim: str = default_delim):
        self.data = StringIO(data)
        self.delim = delim

    def indentation(self, indent: int) -> str:
        return self.delim * indent

    def writeindent(self, indent: int):
        self.data.write(self.indentation(indent))

    def write(self, val, indent: int = 0):
        val_str = str(val)
        val_str_indented = val_str.replace(ReportWriter.default_newline, f"{ReportWriter.default_newline}{self.indentation(indent)}")
        self.writeindent(indent)
        self.data.write(val_str_indented)

    def writeline(self, val="", indent: int = 0):
        self.write(val, indent)
        self.write(ReportWriter.default_newline)

    def writedelim(self):
        self.write(self.delim)

    def writecols(self, vals: Iterable[str], indent: int = 0):
        self.writeindent(indent)
        for val in vals:
            self.write(val)
            self.writedelim()

    def writevals(self, *vals, indent: int = 0, newline: bool = True):
        self.writeindent(indent)
        for val in list(vals):
            self.write(val)
            self.writedelim()
        if newline:
            self.writeline()

    def writerows(self, vals: Iterable[str], indent: int = 0):
        for val in vals:
            self.writeline(val, indent)

    def writedicts(self, dicts: Iterable[Dict]):
        dicts_list = list(dicts)
        self.writecols(dicts_list[0].keys())
        self.writeline()
        for dict_ in dicts_list:
            self.writecols(dict_.values())
            self.writeline()

    @property
    def value(self):
        return self.data.getvalue()

    def __str__(self):
        return self.value

    def writeto(self, path: Path):
        path.write_text(self.value)
