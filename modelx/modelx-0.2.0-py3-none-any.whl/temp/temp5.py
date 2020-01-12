import modelx as mx
from modelx.tests.testdata import XL_TESTDATA
import os
import pathlib

# tmp_path = here = os.path.abspath(os.path.dirname(__file__))
# os.chdir(here)

tmp_path = here = pathlib.Path(os.path.abspath(os.path.dirname(__file__)))
os.chdir(here)

model, space = mx.new_model(), mx.new_space()
space.new_cells_from_excel(
    book=XL_TESTDATA,
    range_="C9:E25",
    sheet="TestTables",
    names_row=0,
    param_cols=[0],
    param_order=[0],
    transpose=False,
)

mx.write_model(model, here / "testdir")

m = mx.read_model(here / "testdir")
mx.write_model(m, here / "testdir")
m2 = mx.read_model(here / "testdir")