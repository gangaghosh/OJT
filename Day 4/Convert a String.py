
# Write a Python program with a function that converts a string to an integer. Handle exceptions within the function and print appropriate error messages.

def string_to_int(s):
    try:
        return int(s)
    except ValueError:
        return None

# Test the function
num_str = input("Enter a number as a string: ")
result = string_to_int(num_str)
if result is not None:
    print("Integer value:", result)
else:
    print("Invalid input: Please enter a valid integer")

