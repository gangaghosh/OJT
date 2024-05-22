# Create a class called FileProcessor with methods to read data from a file, write data to a file, and append data to an existing file.

class FileProcessor:
    @staticmethod
    def read_file(filename):
        with open(filename, 'r') as file:
            return file.read()

    @staticmethod
    def write_file(filename, data):
        with open(filename, 'w') as file:
            file.write(data)

    @staticmethod
    def append_file(filename, data):
        with open(filename, 'a') as file:
            file.write(data + '\n')

# Testing file processing methods
FileProcessor.write_file("test.txt", "Hello, this is a test.")
print(FileProcessor.read_file("test.txt"))

FileProcessor.append_file("test.txt", "This is an appended line.")
print(FileProcessor.read_file("test.txt"))
