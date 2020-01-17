import re
import subprocess

from dataclasses import dataclass
from typing import Set as PySet, Dict as PyDict, Tuple as PyTuple, List as PyList


class AbstractTestType:
    def compile_expr(self, expr: str) -> str:
        return expr

    def compile(self):
        return re.sub(r"\n +", " ", re.sub(r" +", " ", self.compile_expr(self.__repr__())))


@dataclass
class Unit(AbstractTestType):
    def get_type(self):
        return "unit"

    def __repr__(self):
        return f"""Unit"""


@dataclass
class Address(AbstractTestType):
    value: str

    def get_type(self):
        return "address"

    def __repr__(self):
        return f"""("{self.value}" : address)"""

    def __hash__(self):
        return hash(self.value)


@dataclass
class String(AbstractTestType):
    value: str

    def get_type(self):
        return "string"

    def __repr__(self):
        return f'"{self.value}"'

    def __hash__(self):
        return hash(self.value)

@dataclass
class Timestamp(AbstractTestType):
    value: str

    def get_type(self):
        return "timestamp"

    def __repr__(self):
        return self.value

@dataclass
class List(AbstractTestType):
    value: PyList
    type: str = ""  # Not necessary when self.value is not empty

    def get_type(self):
        type = self.type if not len(self.value) else self.value[0].get_type()
        return f'{type} list'

    def __repr__(self):
        result = ""
        for v in self.value:
            result += f"{v} ; "
        return f'([{result}] : {self.get_type()})'

    def __getitem__(self, key):
        return self.value[key]

    def __setitem__(self, key, value):
        self.value[key] = value

    def __hash__(self):
        return hash(self.value.__repr__())

    def __len__(self):
        return len(self.value)


@dataclass
class Bool(AbstractTestType):
    value: bool

    def get_type(self):
        return 'bool'

    def __repr__(self):
        if self.value:
            return "true"
        else:
            return "false"

    def __eq__(self, other: "Bool"):
        return self.value == other.value

class AbstractRecord(AbstractTestType):
    def get_type(self):
        result = ""
        for k, v in self.__dict__.items():
            result += f"""{k} : {v.get_type()} ; """
        return f"""({{ {result} }})"""

    def __repr__(self):
        result = ""
        for k, v in self.__dict__.items():
            result += f"""{k} = {v} ; """
        return f"""{{ {result} }}"""


@dataclass
class Tuple(AbstractTestType):
    value: PyTuple[any]

    def get_type(self):
        content = ""
        for v in self.value:
            content += f"{v.get_type()} * "
        if len(self.value):
            # remove trailing star if non empty list
            content = content[:-3]
        return f"""({content})"""

    def __repr__(self):
        content = ""
        for v in self.value:
            content += f"{v} ,"
        if len(self.value):
            # remove trailing comma if non empty list
            content = content[:-1]
        return f"""({content})"""

    def __hash__(self):
        return hash(self.value)

@dataclass
class Bytes(AbstractTestType):
    value: AbstractTestType

    def get_type(self):
        return "bytes"

    def __repr__(self):
        return f"""(Bytes.pack {self.value})"""

    def __hash__(self):
        return hash(self.value)

@dataclass
class Sha256(AbstractTestType):
    value: AbstractTestType

    def get_type(self):
        return "bytes"

    def __repr__(self):
        return f"""(Crypto.sha256 {self.value})"""

    def __hash__(self):
        return hash(self.value)

@dataclass
class Nat(AbstractTestType):
    value: int

    def get_type(self):
        return "nat"

    def __repr__(self):
        return str(self.value) + "n"

    def __add__(self, other):
        return Nat(self.value + other.value)

    def __sub__(self, other):
        return Nat(self.value - other.value)

    def __hash__(self):
        return hash(self.value)

@dataclass
class Map(AbstractTestType):
    value: PyDict[any, any]
    key_type: str = ""    # not necessary when len(self.value) is not 0
    value_type: str = ""  # not necessary when len(self.value) is not 0

    def get_type(self):
        if len(self.value):
            key = list(self.value.keys())[0]
            value = self.value[key]
            return f'({key.get_type()}, {value.get_type()}) map'
        return f'({self.key_type}, {self.value_type}) map'

    def __repr__(self):
        result = ""
        for k, v in self.value.items():
            result += f"({k},{v});"
        return f"(Map.literal [{result}] : {self.get_type()})"

    def __getitem__(self, key):
        return self.value[key]

    def __setitem__(self, key, value):
        self.value[key] = value

    def __len__(self):
        return len(self.value)


@dataclass
class Set(AbstractTestType):
    value: PySet[any]
    type: str = ""  # Infered used when self.value is not empty

    def get_type(self):
        if len(self.value):
            el = tuple(self.value)[0]
            return f'{el.get_type()} set'
        return f'{self.type} set'

    def union(self, s: "Set[any]"):
        return Set(self.value.union(s.value))

    def remove(self, el):
        self.value.remove(el)

    def remove_subset(self, subset: "Set[any]"):
        for el in subset.value:
            self.value.remove(el)

    def __repr__(self):
        result = f"(Set.empty: {self.get_type()})"
        for v in self.value:
            result = f"(Set.add {v} {result})"
        return result

    def __hash__(self):
        return hash(self.value.__repr__())

    def __len__(self):
        return len(self.value)
