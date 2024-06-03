import numpy as np

# Create a NumPy array
original_array = np.array([1, 2, 3, 4, 5, 6])
print("Original array:", original_array)

# Create a view for the array
view_array = original_array.view()
print("View of the original array:", view_array)

view_array[2] = 30
print("Modified view of the array:", view_array)
print("Original array after modifying the view:", original_array)

# create copy of the array
copy_array=original_array.copy()
print("copy Array: ",copy_array)

# modify element in copy array
copy_array[0]=10
print("modified copy of the array: ",copy_array)
print("original array after modifying the copy array:",original_array)