from pathlib import Path
import os
import time
import pandas as pd
import numpy as np
from collections.abc import Iterable

# To change the color of some elements in the dataframe under some condition, do:
#  dff is some dataframe. In this example, negative values are set to red
#    dff = dff.mask(dff < 0, TableWriter.set_color_dataframe(dff, "red"))
#    dff = pd.DataFrame(columns=dff.columns,
#                       index=dff.index,
#                       data=dff.values.astype(str))
#    dff = dff.mask(dff == "nan", "")
#    writer = TableWriter(data=dff,
#                     caption="Slippage analysis",
#                     escape_special_chars=True)

class TableWriter:
    
    VERBOSE = 0
    @classmethod
    def set_verbose(cls, v):
        TableWriter.VERBOSE = v
    @classmethod
    def printv(cls, s):
        if TableWriter.VERBOSE > 0:
            print(s)
    
    def __init__(self, **kwargs):
    
        self.__header = ""
        self.__body = ""
        self.__footer = ""
        
        expected = ["data", "path", "label", "caption", "col_names", "row_names",
                    "packages_commands", "load", "escape_special_chars",
                    "paperwidth", "paperheight", "number"]
        for name in kwargs:
            if not name in expected:
                raise ValueError("Unexpected argument " + name)
        self.__data = kwargs.get("data", pd.DataFrame())
        self.__path = kwargs.get("path", "")
        self.__label = kwargs.get("label", "")
        self.__caption = kwargs.get("caption", "")
        self.__paperwidth = kwargs.get("paperwidth", 0)
        self.__paperheight = kwargs.get("paperheight", 0)
        self.__ndecimals = kwargs.get("ndecimals", 4)
        self.__number = kwargs.get("number", "0")
        if not isinstance(self.__number, str):
            self.__number = str(int(self.__number))
        self.__escape_special_chars = kwargs.get("escape_special_chars", False)
        col_names = kwargs.get("col_names", [])
        row_names = kwargs.get("row_names", [])
        load = kwargs.get("load", False)
        self.__packages_commands = kwargs.get("packages_commands", [])
        self.__special_char = ["_", "^", "%", "&"]
        if not type(self.__path) == Path:
            self.__path = Path(self.__path)
        if load:
            if not self.load_from_file():
                sys.exit(0)
        else:
            if type(self.__data) != pd.DataFrame:
                self.__data = pd.DataFrame(columns=col_names,
                                           index=row_names,
                                           data=self.__data.astype(str))
            else:
                self.__data = self.__data.astype(str)

# setters
    def set_data(self, data):
        if type(data) != pd.DataFrame:
            data = pd.DataFrame(data=data)
        self.__data = data
    def set_label(self, label):
        self.__label = label
    def set_caption(self, caption):
        self.__caption = caption
    def set_packages_commands(self, packages_commands):
        self.__packages_commands = packages_commands
    def set_path(self, path):
        self.__path = path
    def set_col_names(self, col_names):
        self.__data.columns = col_names
    def set_row_names(self, row_names):
        self.__data.index = row_names
    def set_item(self, index, column, value):
        self.__data.at[index, column] = value
    def set_number(self, number):
        self.__number = number
        if not isinstance(self.__number, str):
            self.__number = str(int(self.__number))
    
    def rename(self, dick, axis=0):
        if axis == 0:
            self.__data.rename(index=dick, inplace=True)
        if axis == 1:
            self.__data.rename(columns=dick, inplace=True)

#getters
    def get_ncols(self):
        return len(self.__data.columns)
    def get_nrows(self):
        return len(self.__data.index)
    def get_data(self, df = False):
        if df:
            return self.__data
        else:
            return self.__data.values
    def get_path(self):
        return self.__path
    def get_label(self):
        return self.__label
    def get_caption(self):
        return self.__caption
    def get_col_names(self):
        return self.__data.columns
    def get_row_names(self):
        return self.__data.index
    def get_number(self):
        return self.__number
    
    def escape_special_chars(self, s):
        """ Will add '\\' before special characters outside of mathmode
        """
        if isinstance(s, Iterable) and type(s) != str:
            for i in range(len(s)):
                s[i] = self.escape_special_chars(s[i])
        if type(s) != str:
            return s
        in_math = False
        previous_c = ""
        s2 = ""
        for c in s:
            if c == "$":
                in_math = not in_math
            if in_math:
                s2 += c
                previous_c = c
                continue
            if c in self.__special_char and not previous_c == "\\":
                c =  "\\" + c
            previous_c = c
            s2 += c
        return s2

#   Table makers
    def set_line(self, line, name = ""):
        """Adds or updates a line
        """
        
        TableWriter.printv("Adding/changing line in table.")
        if name != "":
            self.__data.loc[name] = line
            return
        else:
            self.__data.loc[str(len(self.__data.index))] = line
            return
    
    def set_column(self, column, name = ""):
        """Adds or updates a column
        """
        
        TableWriter.printv("Adding/changing column in table.")
        if name != "":
            self.__data[name] = column
            return
        else:
            self.__data[str(len(self.__data.columns))] = column
            return
    
    def load_from_file(self):
        """Loads a table from a tex file
        
        NOT WORKING IF TEXFILE HAS PACKAGES
        """
        
        self.__data = []
        row_names = []
        col_names = []
        if not self.__path.is_file():
            raise ValueError("Tex file " + str(self.__path) + " not found.")
    
        lines = []
        with open(self.__path, "r") as ifile:
            lines = [line.split("\n")[0].split(" ") for line in ifile.readlines()]
        self.__header = ""
        nlines_header = 9
        for iline in range(len(lines)):
            #  Reads Header if iline inferior to number of lines in header
            if iline <= nlines_header:
                #  Fetchs caption and label if any
                for item in lines[iline]:
                    if item != "":
                        if "caption{" in item:
                            nlines_header += 1
                            for item2 in lines[iline]:
                                self.__caption += item2 + " "
                            self.__caption = self.__caption[
                                self.__caption.find("{")+1:][:-2]
                        
                        if "label{" in item:
                            nlines_header += 1
                            for item2 in lines[iline]:
                                self.__label += item2 + " "
                            self.__label = self.__label[
                                self.__label.find("{")+1:][:-2]
                        break
            
            #  Reads table content if iline is superior to number of line in header
            if iline >= nlines_header:
                #  Reads column names if __has_col_names is True and col_names empty
                if len(col_names) == 0:
                    name = ""
                    for item in lines[iline]:
                        if item == "":
                            continue
                        if item == "&" or item == "\\\\":
                            if name != "":
                                name = name[:-1] if name[-1] == " " else name
                                col_names.append(name)
                                name = ""
                        else:
                            name += item + " "
                else:
                    #  Reads data
                    self.__data.append([])
                    name = ""
                    first_found = False
                    for item in lines[iline]:
                        if item == "":
                            continue
                        if item == "&" or item == "\\\\":
                            #  Reads row name if first item and rows have names
                            if not first_found:
                                name = name[:-1] if name[-1] == " " else name
                                row_names.append(name)
                                name = ""
                                first_found = True
                                continue
                            if name != "":
                                name = name[:-1] if name[-1] == " " else name
                                self.__data[-1].append(name)
                                name = ""
                        else:
                            name += item + " "
                    
        self.__data = (self.__data[:-1] if len(self.__data[-1]) == 0
                                        else self.__data)
        self.__data = pd.DataFrame(columns=col_names,
                                   index=row_names,
                                   data=self.__data)
        return True
    
    def make_header(self):
        TableWriter.printv("Making Header...")
        if self.__paperwidth == 0:
            charswidth = (len("".join(list(self.__data.columns)))
                    + len(str(self.__data.index[0])))*0.178
            self.__paperwidth = charswidth + 0.8*(len(self.__data.columns))+1  # pifometre!
            if self.__paperwidth < 9:
                self.__paperwidth = 9
        if self.__paperheight == 0:
            self.__paperheight = 3.5+(len(self.__data.index))*0.45  # pifometre!
            if self.__paperheight < 4:
                self.__paperheight = 4 
            if self.__paperheight > 24:
                self.__paperheight = 24  # Limit page height to A4's 24 cm
        self.__header = "\\documentclass{article}\n"
        self.__header += ("\\usepackage[margin=0.5cm, paperwidth="
                        + str(self.__paperwidth) + "cm, paperheight="
                        + str(self.__paperheight) + "cm]{geometry}\n")
        self.__header += ("\\usepackage{longtable}\n\\usepackage[dvipsnames]{xcolor}\n"
                        + "\\usepackage{booktabs}\n\\usepackage[utf8]{inputenc}\n")
        for package in self.__packages_commands:
            self.__header += package + "\n"
        
        self.__header += ("\\begin{document}\n\\nonstopmode\n\setcounter{table}{"
                             + self.__number + "}\n")
        
        TableWriter.printv("...done")
    
    def make_body(self):
        TableWriter.printv("Making Body...")
        column_format = "|l|" + len(self.__data.columns)*"c" + "|"
        self.__body = self.__data.to_latex(
                               longtable=True,
                               escape=False,
                               column_format=column_format)
        append_newline = False
        if self.__caption != "":
            in_table = self.__body.find("\\toprule")
            pre_table = self.__body[:in_table]
            post_table = self.__body[in_table:]
            pre_table += "\\caption{" + self.__caption + "}\n"
            self.__body = pre_table + post_table
            append_newline = True
        
        if self.__label != "":
            in_table = self.__body.find("\\toprule")
            pre_table = self.__body[:in_table]
            post_table = self.__body[in_table:]
            pre_table += "\\label{" + self.__label + "}\n"
            self.__body = pre_table + post_table
            append_newline = True
        if append_newline:
            self.__body = self.__body.replace("\n\\toprule","\\\\\n\\toprule")
        TableWriter.printv("...done")
    
    def make_footer(self):
        TableWriter.printv("Making Footer...")
        self.__footer = ("\\end{document}\n")
        TableWriter.printv("...done")

#  Write and compile
    def create_tex_file(self):
        if self.__path == "":
            raise ValueError("Must specify a file path.")
        
        with open(self.__path, "w") as outfile:
            if self.__escape_special_chars:
                self.__data.index = [self.escape_special_chars(s)
                                     for s in self.__data.index]
                self.__data.columns = [self.escape_special_chars(s)
                                       for s in self.__data.columns]
                self.__data = self.__data.apply(self.escape_special_chars, axis=1)
            self.make_header()
            outfile.write(self.__header)
            self.make_body()
            outfile.write(self.__body)
            self.make_footer()
            outfile.write(self.__footer)
        return True
    
    def compile_pdf_file(self, silenced = True, recreate = True):
        if self.__path == "":
            raise ValueError("Must specify a file path.")
        
        if recreate or not self.__path.is_file():
            if not self.create_tex_file():
                raise ValueError("Failed to create tex file.")
        
        if not self.__path.is_file():
            raise ValueError("Tex file " + str(self.__path) + " not found.")
        
        command = "pdflatex -synctex=1 -interaction=nonstopmode "
        parent = self.__path.parents[0]
        if parent != ".":
            command = command + "-output-directory=\"" + str(parent) + "\" "
        
        command = command + "\"" + str(self.__path) + "\""
        if silenced:
            if os.name == "posix":
                command = command + " > /dev/null"
            else:
                command = command + " > NUL"
        
        TableWriter.printv(command)
        x = os.system(command)
        time.sleep(0.5)
        x = os.system(command)
        time.sleep(0.5)
        x = os.system(command)
        if x != 0:
            raise ValueError("Failed to compile pdf")
        return True
    
    def remove_color(self, obj):
        has_color = "textcolor" in obj
        if not "\\textcolor{" in obj:
            return obj
        to_find = "\\textcolor{"
        before_color = obj[:obj.find(to_find)]
        after_color = obj[obj.find("textcolor")+10:]
        no_color = after_color[after_color.find("{")+1:].replace("}","",1)
        return before_color + no_color
    
    def set_color(s, color):
        return "\\textcolor{" + color + "}{" + str(s) + "}"
    
    def set_color_dataframe(df, color):
        data = df.values.astype(str)
        data = [["\\textcolor{" + color + "}{" + s + "}"
                 for s in col] for col in data]
        return pd.DataFrame(columns=df.columns,
                           index=df.index,
                           data=data)
