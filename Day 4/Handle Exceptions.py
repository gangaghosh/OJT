# Write a Python program that reads a file and prints its content. Handle ‘FileNotFoundError’ and ‘PermissionError’ exceptions.

def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            print("File content:")
            print(content)
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    except PermissionError:
        print(f"Error: Permission denied for file '{file_name}'.")

# Test the function with a file name
file_name = input("Enter the file name to read: ")
read_file(file_name)

