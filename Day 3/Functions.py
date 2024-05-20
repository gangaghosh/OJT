# 1.   Write a Python function to calculate the area of a circle given its radius.
import math

def calculate_area_circle(radius):
    return math.pi * radius ** 2

circle_radius = 5
area = calculate_area_circle(circle_radius)
print("Area of the circle:", area)



# 2.  Write a Python program to reverse a list using a function.
def reverse_list(input_list):
    return input_list[::-1]

original_list = [1, 2, 3, 4, 5]
reversed_list = reverse_list(original_list)
print("Reversed list:", reversed_list)


# 3. Write a Python program to check if a string is a palindrome using a function.
def is_palindrome(input_str):
    input_str = input_str.lower().replace(" ", "")  
    return input_str == input_str[::-1]

test_string = "Malayalam"
if is_palindrome(test_string):
    print(f"{test_string} is a palindrome")
else:
    print(f"{test_string} is not a palindrome")


# 4. Write a Python program to count the number of even and odd numbers in a list using functions.
def count_even_odd(numbers_list):
    even_count = sum(1 for num in numbers_list if num % 2 == 0)
    odd_count = sum(1 for num in numbers_list if num % 2 != 0)
    return even_count, odd_count

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even, odd = count_even_odd(numbers)
print("Number of even numbers:", even)
print("Number of odd numbers:", odd)
