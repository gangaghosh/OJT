# Write a Python program that renames a file named ‘old_name.txt to’ ‘new_name.txt’.

import os

# Check if file exists before renaming
if os.path.exists('old_name.txt'):
    os.rename('old_name.txt', 'new_name.txt')
    print("File renamed successfully")
else:
    print("File not found")
