from collections import OrderedDict
import re

from . import object_info as oi
from . import CONFIG


class SourceFileInfo(object):
    def __init__(self, src):
        self.src = src
        # TODO might be better to store all these as dicts
        #      of mapping - name : ObjectInfo
        self.classes = OrderedDict()
        self.enums = OrderedDict()
        self.dataclasses = OrderedDict()
        self.methods = {}  # {classname : {methname : MethodInfo}}
        self.functions = OrderedDict()

    def public(self, objtype=None, include_functions=False):
        if objtype is None:
            public = {}

            pclasses = self.public("classes")
            if pclasses:
                public["classes"] = pclasses

            penums = self.public("enums")
            if penums:
                public["enums"] = penums

            pdcs = self.public("dataclasses")
            if pdcs:
                public["dataclasses"] = pdcs

            if include_functions:
                pfuncs = self.public("functions")
                if pfuncs:
                    public["functions"] = pfuncs

            return public

        objects = getattr(self, objtype)

        return {k: v for k, v in objects.items() if v.is_public}

    def get_class_data(self, classname: str):
        if classname not in self.classes:
            raise ValueError("%s not in self.classes" % classname)

        all_methods = self.methods.get(classname, {})
        methods = {}
        properties = {}
        constructor = None
        for method_name, method_info in all_methods.items():
            if method_info.mtype == oi.MethodType.METHOD and method_info.is_public:
                methods[method_name] = method_info
            elif method_info.mtype == oi.MethodType.PROPERTY and method_info.is_public:
                properties[method_name] = method_info
            elif method_info.mtype == oi.MethodType.CONSTRUCTOR:
                if constructor is not None:
                    raise Exception(
                        "BUG: class %s somehow has multiple constructors." % classname
                    )
                constructor = method_name, method_info

        return ClassData(classname, methods, constructor, properties)


class ClassData(object):
    def __init__(self, name, methods=None, constructor=None, properties=None):
        self.name = name
        self.methods = methods
        self.properties = properties
        self.constructor = constructor


def strip_base_args_whitespace(line):
    if "(" not in line or ")" not in line:
        return line.split(":")[0]

    start_paren_idx = line.index("(")
    end_paren_idx = line.index(")")

    bases = line[(1 + start_paren_idx) : end_paren_idx]
    reformed_bases = bases.replace(" ", "")

    return line.split("(")[0] + f"({reformed_bases})"


def is_class(line):
    return line.startswith("class") or line.startswith("cdef class")


def is_method(line, stripped):
    return (
        (stripped.startswith("def") or stripped.startswith("cpdef"))
        and "(" in line
        and len(line) - len(stripped) == 4
    )


def is_free_function(line):
    return (line.startswith("def") or line.startswith("cpdef")) and "(" in line


class Parser(object):
    def __init__(self, src):
        self.src = src
        self.sfi = SourceFileInfo(self.src)
        self.line = ""
        self.prev_line = ""

    def _parse_class(self, streampos):
        line = strip_base_args_whitespace(self.line)

        split = line.split(" ")
        if "cdef" in line:
            if len(split) > 3:
                split = split[:3]
            _, _, name_with_bases = split
        else:
            if len(split) > 2:
                split = split[:2]
            _, name_with_bases = split

        tmp = name_with_bases.split("(")
        if len(tmp) > 1:
            bases = tmp[1]
        else:
            bases = ""
        name = tmp[0].split(":")[0]

        if "Enum" in bases or "Flag" in bases:
            if all(re.search(p, name) is None for p in CONFIG.exclude_enums):
                self.sfi.enums[name] = oi.EnumInfo(name, self.src, streampos)
        elif "dataclass" in self.prev_line:
            if all(re.search(p, name) is None for p in CONFIG.exclude_dataclasses):
                self.sfi.dataclasses[name] = oi.DataClassInfo(name, self.src, streampos)
        else:
            if all(re.search(p, name) is None for p in CONFIG.exclude_classes):
                self.sfi.classes[name] = oi.ClassInfo(
                    name, self.src, streampos, "ABC" in bases
                )

    def _parse_free_function(self, streampos):
        line = strip_base_args_whitespace(self.line)

        split = line.split(" ")
        if "cpdef" in line:
            if len(split) == 2:
                _, name_with_args = split
            else:
                if len(split) > 3:
                    split = split[:3]
                _, _type, name_with_args = split
        else:
            if len(split) > 2:
                split = split[:2]
            _, name_with_args = split

        tmp = name_with_args.split("(")
        name = tmp[0]

        if all(re.search(p, name) is None for p in CONFIG.exclude_functions):
            self.sfi.functions[name] = oi.FunctionInfo(name, self.src, streampos)

    def _parse_methods(self, src_handle):
        class_info_list = list(self.sfi.classes.values())
        for i, (classname, class_info) in enumerate(self.sfi.classes.items()):
            src_handle.seek(class_info.streampos)

            self.sfi.methods[classname] = OrderedDict()

            if class_info.streampos == class_info_list[-1].streampos:
                allclass = src_handle.read()
            else:
                allclass = src_handle.read(
                    class_info_list[i + 1].streampos - class_info.streampos
                )

            class_lines = allclass.splitlines()
            for j, line in enumerate(class_lines):
                stripped = line.strip()

                if is_method(line, stripped):
                    line = strip_base_args_whitespace(stripped)

                    split = line.split(" ")
                    if "cpdef" in line:
                        if len(split) == 2:
                            _, name_with_args = split
                        else:
                            if len(split) > 3:
                                split = split[:3]
                            _, _type, name_with_args = split
                    else:
                        if len(split) > 2:
                            split = split[:2]
                        _, name_with_args = split

                    tmp = name_with_args.split("(")
                    method_name = tmp[0]

                    if any(
                        re.search(p, method_name) is not None
                        for p in CONFIG.exclude_methods
                    ):
                        continue

                    is_property = class_lines[j - 1].lstrip().startswith("@property")
                    is_constructor = method_name == "__init__"

                    if is_property:
                        mtype = oi.MethodType.PROPERTY
                    elif is_constructor:
                        mtype = oi.MethodType.CONSTRUCTOR
                    else:
                        mtype = oi.MethodType.METHOD

                    self.sfi.methods[classname][method_name] = oi.MethodInfo(
                        method_name, self.src, src_handle.tell(), mtype, class_info
                    )

    def parse(self):
        with open(self.src) as f:
            self.line = f.readline()
            in_module_docstrings = False

            while self.line:
                if self.line.startswith('"""') and not in_module_docstrings:
                    in_module_docstrings = True
                elif self.line.startswith('"""') and in_module_docstrings:
                    in_module_docstrings = False

                if is_class(self.line) and not in_module_docstrings:
                    self._parse_class(f.tell())

                elif is_free_function(self.line) and not in_module_docstrings:
                    self._parse_free_function(f.tell())

                self.prev_line = self.line
                self.line = f.readline()

            self._parse_methods(f)

        return self.sfi
