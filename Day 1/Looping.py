#  Write a Python program to print the multiplication table of a number using a for loop
num = int(input("Enter a number to print its multiplication table: "))

print(f"Multiplication table of {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
