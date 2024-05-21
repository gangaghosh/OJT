# Write a Python program to Read/Write to a File 

# Writing to a file
with open('file.txt', 'w') as f:
    f.write('Hello, this is a test!')

# Reading from a file
with open('file.txt', 'r') as f:
    content = f.read()
    print(content)
