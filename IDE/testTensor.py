#Creating a program with TensorFlow

#Importing TensorFlow
import tensorflow as tf

print(tf.__version__)

#Creating tensors with tf.constant()
scalar=tf.constant(10)

#Printing the essence of scalar variable
print(scalar)

#Check the dimensions of a scalar tensor (ndim stands for number of dimensions)
print("The dimensions of a scalar tensor is:",scalar.ndim)

#Creating a vector
vector=tf.constant([10,20])

#Printing the essence of vector variable
print(vector)

#Check the dimensions of a vector tensor (ndim stands for number of dimensions)
print("The dimensions of a vector tensor is:",vector.ndim)

#Creating a matrix which is a data structure having more than 1 element
matrix=tf.constant([
[10,20],
[20,10]
])

#Printing the essence of a matrix variable
print(matrix)

#Check the dimensions of a matrix tensor (ndim stands for number of dimensions)
print("The dimensions of a matrix tensor is:",matrix.ndim)

#Creating another matrix
anotherMatrix=tf.constant([
[40.,50.],
[60.,70.],
[80.,90.]
],dtype=tf.float16) #Specifying the datatype with dtype parameter

#Printing the essence of a specific matrix variable
print(anotherMatrix)

#Check the dimensions of a matrix tensor (ndim stands for number of dimensions)
print("The dimensions of a specific matrix tensor is:",anotherMatrix.ndim)

#Creating an original tensor
tensor=tf.constant([
[[1,2,3],
[4,5,6]],

[[7,8,9],
[10,11,12]],

[[13,14,15],
[16,17,18]]
])

#Printing the essence of an original tensor
print(tensor)

#Check the dimensions of a tensor (ndim stands for number of dimensions)
print("The dimensions of an original tensor is:",tensor.ndim)

#What we have created so far
#1. Scalar: Single number
#2. Vector: A number with direction
#3. Matrix: A two dimensional array of numbers
#4. Tensor: An n-dimensional array of numbers

#Creating a tensor variable
changeableTensor=tf.Variable([10,20])

#Creating a tensor constant
unchangeableTensor=tf.constant([70,80])

#Printing the essence values of the tensor variables
print(changeableTensor)
print(unchangeableTensor)

#Let's try changing the values within the changeableTensor variable
changeableTensor[0].assign(30)
print(changeableTensor)

#Rarely in practice will you need to decide whether to use tf.constant
#or tf.variable to create tensors, as TensorFlow does this for you.
#However, when in doubt, use tf.constant and change it later if needed.

#Creating random tensors which has some arbitiary size and random numbers.
random1=tf.random.Generator.from_seed(40) #Set seed for same results
random1=random1.normal(shape=(3,2))

random2=tf.random.Generator.from_seed(40) #Set seed for same results
random2=random2.normal(shape=(3,2))

#Checking if the two tensors above is equal or not
print(random1==random2)

#Printing the essence values of random1 and random2 variables
print(random1)
print(random2)

#Shuffle the elements within a tensor to help make the machine learn efficiently
notShuffled=tf.constant([
[10,7],
[3,4],
[2,5]
])

#Check the dimensions of a matrix tensor (ndim stands for number of dimensions)
print("The dimensions of an unshuffled matrix tensor is:",notShuffled.ndim)

#Printing the essence values of notShuffled variable
print(notShuffled)

#Shuffling the notShuffled tensor
shuffled=tf.random.shuffle(notShuffled,seed=40)

#Check the dimensions of a matrix tensor (ndim stands for number of dimensions)
print("The dimensions of a shuffled matrix tensor is:",shuffled.ndim)

#Printing the essence values of shuffled varaible
print(shuffled)
