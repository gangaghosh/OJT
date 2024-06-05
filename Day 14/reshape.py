# convert 1D into 2D
# #.reshape() is the method which is used for reshaping the arrays

import numpy as np

# create a 1D Array
array_1D=np.array([1,2,3,4,5,6])
print('array 1D : ',array_1D)
print("shape of the array1D :",array_1D.shape)
# identifying the shape of the particular array that you have been provided, we will use shape.

# reshape the 1D array to 2D array
array_2D=array_1D.reshape((2,3))
print("2D array:\n ",array_2D)
print("shape of array_2D",array_2D.shape)

# reshape the 1D array to 3D array
array_3D=array_2D.reshape((3,2))
print("3D array:\n ",array_3D)
print("shape of array_3D",array_3D.shape)

# reshape the 2D array to 1D array
array1_D=array_2D.reshape(-1)  # 6 also we can give
print("1D array back:",array1_D)
print("shape of array1_D back",array1_D.shape)

