import tensorflow as tf

hello_constant = tf.constant('Hello World!')
x = tf.placeholder(tf.string)

##x = tf.add(5, 2)
##y = tf.multiply(2, 5)

a = 10
b = 2
c = a/b -1
a = tf.constant(10)
b = tf.constant(2)
c = tf.subtract(tf.divide(a,b),tf.cast(tf.constant(1), tf.float64))

n_features = 120
n_labels = 5
w = tf.Variable(120,5)
weights = tf.Variable(tf.truncated_normal((n_features, n_labels)))

with tf.Session() as sess:
    # Run the tf.constant operation in the session
    sess.run(tf.global_variables_initializer())
    #output = sess.run(hello_constant)
    #output = sess.run(x, feed_dict = {x:'test123'})
    output = sess.run(c)
    print(output)
