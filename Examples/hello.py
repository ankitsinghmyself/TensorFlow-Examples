# -*- coding: utf-8 -*-
'''
HelloWorld example using TensorFlow library.
Author: Ankit Singh
Project: https://github.com/ankitsinghmyself/TensorFlow/
'''
import tensorflow as tf
# Simple hello world using TensorFlow

# Create a Constant op
# The op is added as a node to the default graph.
# The value returned by the constructor represents the output of the Constant op.
hello = tf.constant('Hello, TensorFlow!')
#start session tf
sess = tf.Session()
# Run the op
print(sess.run(hello))
