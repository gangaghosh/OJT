def is_palindrome(num):
    str_num = str(num)
    return str_num == str_num[::-1]

# Testing the function
num = 12321
if is_palindrome(num):
    print(f"Given number {num} is a palindrome")
else:
    print(f"Given number {num} is not a palindrome")

num = 12345
if is_palindrome(num):
    print(f"Given number {num} is a palindrome")
else:
    print(f"Given number {num} is not a palindrome")
