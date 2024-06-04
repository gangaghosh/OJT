import numpy as np


# 1. Counts the number of non-zero values in the array

arr = np.array([1, 2, 0, 6, 8])
# count non-zero values
non_zero = np.count_nonzero(arr)
# count_nonzero function in NumPy is used to count the number of non-zero elements
print("Non zero values in the array:", non_zero)



# 2. How to create an empty and a full NumPy array?

# # Create an empty array
empty_array = np.empty((3, 3))
# empty creates an uninitialized array of specified shape and data type
print("Empty array:\n", empty_array)

# Create a full array with all elements as a specific value
full_array = np.full((3, 3), 5)
# full creates a new array of specified shape and data type, filled with a specified value
print("Full array:\n", full_array)



# 3. Find the number of rows and columns of a given matrix using NumPy

matrix = np.array([[1, 2, 3], [4, 5, 6]])

rows, cols = matrix.shape
# shape attribute in NumPy is used to get the dimensions of an array
print("Number of rows:", rows)
print("Number of columns:", cols)



# 4. Find the sum of values in a matrix
matrix_array = np.array([[1, 2, 3], [4, 5, 6]])
matrix_sum = np.sum(matrix_array)
# sum function is used to compute the sum of array elements over a specified axis
print("Sum of values in the matrix:", matrix_sum)



# 5. Calculate the sum of the diagonal elements of a NumPy array 3*3 and 4*4
# create 3x3 matrix
matrix_3x3 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 10]])

print("\n", matrix_3x3)

sum_diagonal_matrix_3x3 = np.trace(matrix_3x3)
# The trace of a matrix is defined as the sum of its diagonal elements

print("Sum of diagonal elements in 3x3 matrix:", sum_diagonal_matrix_3x3)

# create 4x4 matrix
matrix_4x4 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])

print("\n", matrix_4x4)

sum_diagonal_matrix_4x4 = np.trace(matrix_4x4)
print("Sum of diagonal elements in 4x4 matrix:", sum_diagonal_matrix_4x4)



# (?) Extracting Diagonal Elements
import numpy as np

# Example 3x3 matrix
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Extract the diagonal elements
diagonal_elements = np.diag(matrix)
# NumPy provides an easy way to extract the diagonal elements of a matrix using the np.diag function.
print("Diagonal elements:", diagonal_elements)



# 6. How to inverse a matrix using NumPy
matrix_i=np.array([[1,2],[3,4]])

# calculate the inverse of a matrix
inverse_matrix=np.linalg.inv(matrix_i)
# linalg.inv function in NumPy is used to compute the inverse of a given square matrix
print("original matrix:\n",matrix_i)
print("inverse of the matrix:\n",inverse_matrix)



# 7. Matrix Multiplication in NumPy
matrix1=np.array([[1,2],[3,4]])
matrix2=np.array([[5,6],[7,8]])

# matrix multiplication
result=np.dot(matrix1,matrix2)
# dot function in NumPy is used for matrix multiplication or dot product of two arrays
print("multiplication of the matrix:\n",result)



# 8. Get the maximum and minimum value from given matrix

matrix_m = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Get the maximum and minimum values
max_m=np.max(matrix_m)
min_m=np.min(matrix_m)
print("Maximum value in the matrix:", max_m)
print("Minimum m in the matrix:", min_m)


# 9. Adding and Subtracting Matrices in Python

matrix_1 = np.array([[1, 2], [3, 4]])
matrix_2 = np.array([[5, 6], [7, 8]])

# Adding matrices
add_matrix=np.add(matrix_1,matrix_2)
print("Addition of matrices:\n", add_matrix)

# Subtracting matrices
substract_matrix=np.subtract(matrix_1,matrix_2)



# 10. How to count the frequency of unique values in NumPy array?
array = np.array([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])

# Count the frequency of unique values
unique,counts=np.unique(array,return_counts=True)
print("unique:",unique)
print("count:",counts)
frequency=dict(zip(unique,counts))
print("Frequency of unique values:", frequency)
