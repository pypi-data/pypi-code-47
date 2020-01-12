import os.path
import pathlib
import modelx as mx
import sys

def testmodel():
    m, s = mx.new_model("TestModel"), mx.new_space(name='TestSpace')

    @mx.defcells
    def foo(x):
        # Comment
        return x # Comment

    s.formula = lambda a: None

    m.x = [1, "2"]

    s.m = 1
    s.n = "abc"
    s.o = [1, "2"]
    s.t = (1, 2, "藍上夫", (3, 4.33), [5, None, (7, 8, [9, 10], "ABC")])
    s.u = {3: '4',
           '5': ['6', 7]}
    s.j = "藍上夫"
    s.v = m
    s.w = foo

    # modelx objects as refs
    an = m.new_space(name="Another")
    s.s = [an]
    an.s2 = s[2]

    # same objects
    an.ou = [s.o, s.u]

    return m


def simplelife():
    import lifelib
    from lifelib.projects.solvency2 import solvency2

    path = os.path.dirname(lifelib.projects.solvency2.__file__)
    os.chdir(path)

    try:
        sys.path.insert(0, path)
        m = solvency2.build()
    finally:
        sys.path.pop(0)

    return m


def t_arg(t):
    pass


def dynmodel():
    m = mx.new_model()
    s1 = m.new_space('s1', formula=t_arg)
    @mx.defcells
    def foo(x):
        return x
    m.new_space('s2', refs={'s1': m.s1(0)})
    s1[1].foo[2] = 3
    return m


tmp_path = here = os.path.abspath(os.path.dirname(__file__))
os.chdir(here)


def write_model(testmodel):

    path_ = pathlib.Path(tmp_path) / "testdir"
    mx.write_model(testmodel, path_, version=3)


if __name__ == "__main__":
    # write_model(dynmodel())
    m2 = mx.read_model(pathlib.Path(tmp_path) / "testdir")
    # pass
