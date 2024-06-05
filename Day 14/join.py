import numpy as np
array1=np.array([1,2,3])
array2=np.array([4,5,6])

concat_array=np.concatenate((array1,array2))
print("concat_array : ",concat_array)

# create multidimensional or 2D array here
array2d_1=np.array([[1,2,3],[4,5,6]])
array2d_2=np.array([[7,8,9],[10,11,12]])

# verticaly and horizontaly 
# vstack  - for vertical joining
# hstack - for horizontal

# vertically
vstack_array=np.vstack((array2d_1,array2d_2))
print("vertical stacked array is:\n ",vstack_array)

# horizontal
hstack_array=np.hstack((array2d_1,array2d_2))
print("horizontal array is:",hstack_array)

