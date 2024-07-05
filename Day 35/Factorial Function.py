def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)

# Testing the function
print(factorial(5))  # Output: 120
