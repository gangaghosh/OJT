# Write a python program to Delete a file

import os

# Check if file exists before deleting
if os.path.exists('file.txt'):
    os.remove('file.txt')
    print("File deleted successfully")
else:
    print("File not found")
