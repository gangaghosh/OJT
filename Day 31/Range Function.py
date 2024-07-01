# for using range function, in which we will decide range inside the function

# Syntax of range function 
# range([start],end,[step])

# # Example 1 
# for val in range(11): 
#     print(val)
    
# # Example 2 
# for val in range(1,11):
#     print(val)
    
# Example 3
# for val in range(1,11,2):
#     print(val)    


# For loop with else condition

#program to check weather the given number is prime number or not 
num = int(input("Enter a Number : ")) 
for i in range(2,num): 
    if(num%i==0): 
        print("%d is not a prime number.."%num)  
        break
else: 
    print("%d is a prime number..."%num)

# %d: This is a placeholder for a decimal integer. When used in a string, Python expects a corresponding integer value to be inserted at that position in the string.

# %num: Here, num is a variable holding an integer value. When used in conjunction with %d in a formatted string, %num tells Python to insert the value of the variable num into the string at that %d placeholder position.

