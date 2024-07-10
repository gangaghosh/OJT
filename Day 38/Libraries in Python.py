# Example
# Importing math library
import math
A = 16
print(math.sqrt(A))

# Create a NumPy ndarray Object
import numpy as np
arr=np.array([1,2,3,4,5])
print(arr)
print (type (arr))

# Min, Max & Everything in between
import numpy as np

# Creating a numpy array of integers
arr = np.array([13, 5, -4, 83, 3, 7])

# Finding the maximum and minimum elements in the array
max_element = np.max(arr)
min_element = np.min(arr)

# Printing the results
print("Maximum element in the array:", max_element)
print("Minimum element in the array:", min_element)

# Random Number Generator
from numpy import random
x =random. randint(100,size=(5))
print(x)

# Ex: Generate a 2-D array with 3 rows, each row containing 5 random integers from 0 to 100
from numpy import random
y = random.randint(100, 5)
print(y)


# Creating scalars in NumPy

# Python program explaining
# numpy.asscalar() function

import numpy as np

# Creating an array of size 1
in_arr = np.array([8])

print("Input array:", in_arr)

# Using the item() method to get the scalar value
out_scalar = in_arr.item()
print("Output scalar from input array:", out_scalar)

# Creating Vector in NumPy
# Importing numpy
import numpy as np

# Creating a 1-D list (Horizontal)
list1 = [1, 2, 3]

# Creating a 1-D list (Vertical)
list2 = [[10],
         [20],
         [30]]

# Creating vector1, vector as row
vector1 = np.array(list1)

# Creating vector2, vector as column
vector2 = np.array(list2)

print("Vector 1 (Row vector):", vector1)
print("Vector 2 (Column vector):")
print(vector2)

# Creating Matrix in NumPy
import numpy as np

# Creating a 2x2 matrix
matrix_2x2 = np.array([[1, 2],
                       [3, 4]])

print("2x2 Matrix:")
print(matrix_2x2)

# Matrix Multiplication in NumPy
import numpy as np

# Creating two matrices
A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

# Matrix multiplication using np.dot()
result_dot = np.dot(A, B)

print("Matrix A:")
print(A)
print("\nMatrix B:")
print(B)
print("\nMatrix multiplication (A dot B):")
print(result_dot)
