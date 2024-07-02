# Function 
# A function in programming terms can be defined as “a block of the reusable, managed code block that is used to perform any certain single operation.”

# Structure
# def funcname (parameters):
     # “func_docstring” [func_suite]
     # return [expression]
     
     
# Example 
# Creating several basic functions

# Function: Add
def add(a, b):
    print ("Adding : %d + %d" % (a, b)) 
    return a + b

# Function: Subtract 
def subtract(a, b): 
    print ("Subtracting : %d - %d" % (a,b))       
    return a - b 
    
    # Function: Multiply 
def multiply(a, b): 
    print ("Multiplying : %d * %d" % (a, b)) 
    return a * b 

# Function: Divide 
def divide(a, b):
    print ("Dividing : %d / %d" % (a, b))
    return a / b 
print ("Let's use the functions created by us")
# Calling Functions
A = add(5, 5) 
B = subtract(5, 6)
C = multiply(6, 5) 
D = divide(5, 5) 
print ("A : %d | B : %d | C : %d | D : %d" % (A, B, C, D))


# Default Arguments
# As the name suggests, a default argument always assumes a default value in case there is no value provided in the function call for a specific argument.
# Example 
def emp_info(designation,name="ABC"): 
    print ("Name : ", name)
    print ("Designation : ", designation) 
    return
emp_info( designation = "Dev" )

# Example 2
def empinfo(designation,name = "XYZ"):
    print ("Name : ", name)
    print ("Designation : ", designation) 
    return
empinfo( name = "ABC", designation = "Dev" ) 
empinfo( designation = "Dev" )

# Required Arguments
# Required arguments are those that are passed to a function in a proper positional/hierarchical order. In Python, the number of arguments in the function call should be exactly the same as the function definition
# Example 
def callme( str ): 
    # "This prints a passed string into this function" 
    print (str)
    return
callme("hello")

# Keyword Arguments
# Keyword arguments are somehow similar to the function calls. Whenever you use keyword arguments in a function call, it is identified by the parameter name directly.
# Example 
def callme( str ): 
    print (str) 
    return
callme( str = "Calling that function")

# Example 2
def empinfo(name , designation):
    print ("Name : ", name)
    print ("Designation : ", designation)
    return
empinfo( name = "ABC", designation = "Dev" )

# Variable Length Arguments 
# All the three above specified arguments are enough to perform any operation, but still, you may need to process a function for more arguments than you specified. For that, here comes the concept of Variable Length Arguments
# Example 
def callme( arg, *vartuple ): 
    print ("India??")
    print (arg) 
    for var in vartuple:
        print (var) 
    return
callme( "Democracy", "or", "Gerontocracy")