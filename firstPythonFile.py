import tensorflow as tf

a = tf.constant(1)
b = tf.constant(2)

c = a + b 
d = a * b 
# vector 1 dimensional
V1 = tf.constant([1.,2.])
V2 = tf.constant([3.,4.])
# matrix 2 d
M = tf.constant([[1.,2.]])
N = tf.constant([[1.,2.],[3.,4.]])
# tensor 3d+
K = tf.constant([[[1.,2.],[3.,4.]]])