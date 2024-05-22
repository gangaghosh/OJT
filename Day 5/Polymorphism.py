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
        super().__init__(side_length, side_length)

    def calculate_diagonal(self):
        return (self.length ** 2 + self.width ** 2) ** 0.5
def display_info(shape):
    if isinstance(shape, Square):
        print("Square Area:", shape.calculate_area())
        print("Square Perimeter:", shape.calculate_perimeter())
        print("Square Diagonal:", shape.calculate_diagonal())
    elif isinstance(shape, Rectangle):
        print("Rectangle Area:", shape.calculate_area())
        print("Rectangle Perimeter:", shape.calculate_perimeter())
    else:
        print("Invalid shape provided.")

# Testing the display_info function
rectangle3 = Rectangle(4, 9)
square2 = Square(5)

display_info(rectangle3)
print()
display_info(square2)
