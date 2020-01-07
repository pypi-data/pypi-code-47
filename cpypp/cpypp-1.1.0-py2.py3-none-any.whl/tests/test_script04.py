import sys
from cpypp import py_preprocessor
PYPP = py_preprocessor()
PYPP.parse(__file__, __name__)

# This is just a comment
#define NUMPY_E __import__("numpy").e

numpy_e = NUMPY_E
print("numpy_e ", numpy_e)

