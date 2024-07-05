def sum_of_proper_divisors(n):
    return sum([i for i in range(1, n) if n % i == 0])

def check_amicable_numbers(num1, num2):
    return sum_of_proper_divisors(num1) == num2 and sum_of_proper_divisors(num2) == num1

# Testing the function
num1, num2 = 220, 284
if check_amicable_numbers(num1, num2):
    print(f"{num1} and {num2} are amicable numbers")
else:
    print(f"{num1} and {num2} are not amicable numbers")
