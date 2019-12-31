import tensorflow as tf
opt = tf.GPUOptions(allow_growth=True)
config = tf.ConfigProto(gpu_options=opt)
