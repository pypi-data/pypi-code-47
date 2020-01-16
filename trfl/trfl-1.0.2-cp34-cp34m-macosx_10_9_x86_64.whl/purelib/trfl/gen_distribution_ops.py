import os.path
import tensorflow as tf
_op_lib = tf.load_op_library(os.path.join(os.path.dirname(__file__), "_gen_distribution_ops.so"))
project_distribution = _op_lib.project_distribution
del _op_lib, tf
