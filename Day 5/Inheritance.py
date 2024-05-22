# Create a class Square that inherits from the Rectangle class. Add a method calculate_diagonal() to calculate the diagonal of the square.


class Rectangle:
    def __init__(self, length, width):
        if length < 0 or width < 0:
            raise ValueError("Length and width must be positive.")
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)
class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)  # Square has equal length and width

    def calculate_diagonal(self):
        return (self.length ** 2 + self.width ** 2) ** 0.5

# Testing the Square class
square = Square(5)
print("Area:", square.calculate_area())  # Output: Area: 25
print("Perimeter:", square.calculate_perimeter())  # Output: Perimeter: 20
print("Diagonal:", square.calculate_diagonal())  # Output: Diagonal: 7.0710678118654755

