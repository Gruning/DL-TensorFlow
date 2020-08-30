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

#basic operations
V3 = V1 + V2 
M2 = N * M

#matrix multiplicatio 
NN = tf.matmul(N,N)

#create a TF session 
#sess = tf.Sesion()
#compatibility v1 for that command
tf.compat.v1.Session() 


output = sess.run(NN)

print('NN is: ' )
print(NN)
