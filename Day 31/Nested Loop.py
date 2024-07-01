# A nested loop means a loop inside the loop. In python, you can create a loop inside a loop.

# Example 1
str=""
for Row in range(0,7):
    for Col in range(0,7): 
        if (((Col == 1 or Col == 5) and Row != 0) or ((Row == 0 or Row == 3) and (Col > 1 and Col < 5))): 
            str=str+"*" 
        else: 
         str=str+" " 
    str=str+"\n" 
print(str)

# Example 2
str=""
for Row in range(0,7):
    for Col in range(0,7): 
        if (Col == 1 or ((Row == 0 or Row == 3 or Row == 6) and (Col < 5 and Col > 1)) or (Col == 5 and (Row != 0 and Row != 3 and Row != 6))) :
            str=str+"*" 
        else: 
         str=str+" " 
    str=str+"\n"
print(str)