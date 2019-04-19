# -*- coding: utf-8 -*-
'''
HelloWorld example using TensorFlow library.
Author: Ankit Singh
Project: https://github.com/ankitsinghmyself/TensorFlow/
'''
import tensorflow as tf
hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
print(sess.run(hello))
