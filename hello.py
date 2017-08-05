"""
HelloWorld example using Tensorfloaw library 

Author : Issam Boutaib 

"""


import tensorflow as tf 

# Simple Hello World using Tensorfloaw
# Create a Constant operation
# The operation is added as a node to the default Computaional graph
# 
# The value returned  by the constructor represents the outpout 
# of the constant operation.
#


hello = tf.constant("Hallo Leute ! Ich Benutze Tensorflow")

# Creating a session 
sess = tf.Session()

# Launching our model
print (sess.run(hello))