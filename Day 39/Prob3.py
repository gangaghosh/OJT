# Write a  Python program that removes and prints every third number from a list of numbers until the list is empty
# Define a function named 'remove_nums' that takes a list 'int_list' as a parameter.
def remove_nums(int_list):
    # Set the starting position for removal to the 3rd element (0-based index).
    position = 3 - 1
    # Initialize the index variable to 0.
    idx = 0
    # Get the length of the input list.
    len_list = len(int_list)
    
    # Continue removing elements until the list is empty.
    while len_list > 0:
        # Calculate the new index based on the starting position and current index.
        idx = (position + idx) % len_list
        # Print and remove the element at the calculated index.
        print(int_list.pop(idx))
        # Decrement the length of the list.
        len_list -= 1

# Create a list of numbers.
nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]

# Call the 'remove_nums' function with the list of numbers.
remove_nums(nums)