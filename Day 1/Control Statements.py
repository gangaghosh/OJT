# Write a Python program to print numbers from 1 to 10, but skip printing the number 5 using a for loop and the continue statement
print("Numbers from 1 to 10 (skipping 5):")
for i in range(1, 11):
    if i == 5:
        continue     
    # 'continue' skips the current iteration of the loop and moves on to the next number if i is equal to 5.
    print(i)
