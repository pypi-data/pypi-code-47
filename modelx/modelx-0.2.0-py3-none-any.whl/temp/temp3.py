import os

tmp_path = here = os.path.abspath(os.path.dirname(__file__))
os.chdir(here)

import modelx as mx
m = mx.new_model()
SpaceA = m.new_space('SpaceA', formula=lambda t: None)

@mx.defcells
def foo(x):
    return x

m.new_space('SpaceB', refs={'RefA': m.SpaceA[0]})
SpaceA[1].foo[2] = 3

mx.write_model(m, "testdir")
m2 = mx.read_model("testdir")

m2.SpaceA[1].foo[2]     # => 3
m2.SpaceB.RefA is m2.SpaceA[0]   # => True