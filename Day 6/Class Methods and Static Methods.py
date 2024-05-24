# Create a class called MathOperations with class methods for basic mathematical operations like addition, subtraction, multiplication, and a static method to find the factorial of a number.

class MathOperations:
    @classmethod
    def add(cls, a, b):
        return a + b

    @classmethod
    def subtract(cls, a, b):
        return a - b

    @classmethod
    def multiply(cls, a, b):
        return a * b

    @staticmethod
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * MathOperations.factorial(n - 1)

# Testing class methods and static method
print("Addition:", MathOperations.add(5, 3))
print("Subtraction:", MathOperations.subtract(10, 4))
print("Multiplication:", MathOperations.multiply(6, 7))
print("Factorial:", MathOperations.factorial(5))
