import numpy as np

array=np.array([10,20,12,15,14,17])
# np.where (array==20)
# where(): use to check the particular condition for filter and condition

# element greater than 15 for the above array

element=np.where(array > 15, 0, array)
print(element)
# print(array[element])