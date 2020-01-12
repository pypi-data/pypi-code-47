


import modelx as mx
import os, pathlib

class Tot_func:
    def __init__(self, space, cell):
        self.cell = cell
        self.space = space

    def Sum(self, *args):
        return sum([self.space(id).cells[self.cell](*args) for id in range(0, 10)])


def s_arg(id):
    if id == -1:
        refs = {cell: m.Tot_func(m.s_base, cell).Sum for cell in m.s_base.cells}
    else:
        refs = {cell: m.s_base(id).cells[cell] for cell in m.s_base.cells}
    return {'refs': refs}


def dyntotal():
    """
    Model-----s_base[id]-----a(i)
           |              +--b(i, j)
           +--s[id]
           |
           +--Tot_func
           |
           +--m
    """
    m = mx.new_model()
    s_base = mx.new_space('s_base', formula=lambda id: None)

    @mx.defcells
    def a(i):
        return i

    @mx.defcells
    def b(i, j):
        return i * j

    m.Tot_func = Tot_func
    m.m = m

    s = mx.new_space('s', formula=s_arg)
    return m


tmp_path = here = os.path.abspath(os.path.dirname(__file__))
os.chdir(here)


def write_model(testmodel):

    path_ = pathlib.Path(tmp_path) / "testdir"
    mx.write_model(testmodel, path_, version=3)


if __name__ == "__main__":
    write_model(dyntotal())
    m2 = mx.read_model(pathlib.Path(tmp_path) / "testdir")
    # pass

# s(-1).a(2)
# s(0).a(2)
# s(-1).b(2, 3)
# s(0).b(2, 3)