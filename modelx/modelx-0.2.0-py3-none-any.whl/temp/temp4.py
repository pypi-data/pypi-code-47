
import os
import pandas as pd
import numpy as np
import modelx as mx
from modelx.testing.testutil import compare_model
import pathlib

tmp_path = here = pathlib.Path(os.path.abspath(os.path.dirname(__file__)))

arrays = [['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux'],
          ['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two']]


index = pd.MultiIndex.from_tuples(
    tuple(zip(*arrays)),
    names=['first', 'second'])

testdf = pd.DataFrame(np.random.randn(8, 4), index=index)
testdf.columns = ["Foo", "Bar", "Baz", "Qux"]
modelpath = tmp_path / "testdir"

doc = """\
Sample DocString
This is a sample docstring\
"""

def write_cells_from_pandas():

    m, space = mx.new_model(), mx.new_space()
    type(m).doc.fset(m, doc) # = doc
    space.new_cells_from_pandas(testdf)

    mx.write_model(m, modelpath)
    # m2 = mx.read_model(modelpath)
    #
    # compare_model(m, m2)
    #
    # assert space.frame.equals(m2.spaces[space.name].frame)


if __name__ == "__main__":
    # write_cells_from_pandas()
    # m = mx.read_model(model_path=modelpath)
    # mx.write_model(m, modelpath)
    m2 = mx.read_model(modelpath)