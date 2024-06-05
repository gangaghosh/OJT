import numpy as np
# split will work in numpy

array=np.array([1,2,3,4,5,6,7,8,9])

split_array=np.split(array,3)
print("original array: ",array)
print("split array:",split_array)

# multidimensional
# horizontally and vertically

# vertical 
array1_2d=np.array([[1,2,3,4],[4,5,6,7]])
vsplit_array=np.vsplit(array1_2d,2)
print("vsplited array:",vsplit_array)

# horizontal
array2_2d=np.array([[1,2,3,4],[4,5,6,7]])
vsplit_array=np.hsplit(array2_2d,2)
print("hsplited array:",vsplit_array)