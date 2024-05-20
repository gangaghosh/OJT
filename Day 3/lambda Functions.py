# 1. Write a Python program to calculate the square of a number using a lambda function.

square = lambda x: x**2
num = 5
print("Square of", num, "is", square(num))


# 2. Write a Python program to calculate the factorial of a number using a lambda function and reduce function.

from functools import reduce

f = 5
factorial = reduce(lambda x, y: x * y, range(1, num+1))
print("Factorial of", f, "is", factorial)


# 3. Write a Python program to filter even numbers from a list using a lambda function.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers in the list:", even_numbers)
