def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)

def check_strong_number(num):
    return num == sum([factorial(int(digit)) for digit in str(num)])

# Testing the function
num = 145
if check_strong_number(num):
    print(f"{num} is a strong number")
else:
    print(f"{num} is not a strong number")
