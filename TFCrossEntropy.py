# Solution is available in the other "solution.py" tab
import tensorflow as tf

softmax_data = [0.7, 0.2, 0.1]
one_hot_data = [1.0, 0.0, 0.0]

softmax = tf.placeholder(tf.float32)
one_hot = tf.placeholder(tf.float32)

# TODO: Print cross entropy from session
#x = tf.reduce_sum([1, 2, 3, 4, 5])  # 15
#x = tf.log(100.0)  # 4.60517
cross_entropy = -tf.reduce_sum(tf.multiply(tf.log(softmax),one_hot))

with tf.Session() as sess:
    output = sess.run(cross_entropy,   feed_dict = {softmax: softmax_data, one_hot: one_hot_data} )
    print(output)
