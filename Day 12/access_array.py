import numpy as np
# create an array
array_2D=np.array(
    [         # 2*3
        [1,2,3],   #0 index
        [4,5,6]    #1 index
        ]
    )

# accessing a single element
element=array_2D[0,1]
print("element at the index of [0,1]: ",element)


# Access by 1 row
# :symbol refers to entire rows
row=array_2D[0,:]
print("first row :",row)

# fetch out the value from the second column
column=array_2D[:,1]
print("second column: ",column)


# slicing
# access the subarray with row of 0 and 1, column of 1 and 2
slice_array=array_2D[0:2,1:3]
print("subarray : ",slice_array)

