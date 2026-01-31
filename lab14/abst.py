from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

class Square(Rectangle):
    def __init__(self, side):
        # A square is a special case of a rectangle where all sides are equal
        super().__init__(side, side)

# Example usage
shapes = [Circle(10), Rectangle(15, 20), Square(5)]

for shape in shapes:
    print(f"The area of the {shape.__class__.__name__} is {shape.area():.2f}")
    print(f"The perimeter of the {shape.__class__.__name__} is {shape.perimeter():.2f}")
