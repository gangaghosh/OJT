# iteration
import numpy as np

# for-in loop
# 1D Array
array_1d=np.array([1,2,3,4,5,6])
# iterate the elements in this array
print("Array_1d: ",array_1d)

for elements in array_1d:
    print(elements)

array_2D=np.array([[1,2,3],[4,5,6],[7,8,9]])
print("2D array : ",array_2D)

# iterate 2D Array
# for rows in array_2D:
#     print(rows)
    
#     for elements in rows:
#          print(elements)

# iterate the elements without nested lopp
for elements in np.nditer(array_2D):
    print(elements)


# iterate the elements with index
for index, element in np.ndenumerate(array_2D):
    print(f"index: {index}, Element: {element}")