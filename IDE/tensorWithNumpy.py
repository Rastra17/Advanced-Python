#Some other ways to create tensors

#Importing tensorflow
import tensorflow as tf

#Printing the version of tensorflow library
print("The version of current tensorflow is: "+tf.__version__)

#Creating a tensor of all 1's
tf.ones([10,7])

#Creating a tensor of all 0's
tf.ones(shape=(3,4))