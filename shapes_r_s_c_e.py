# practical no 9
from abc import ABC
import math


# Abstract class
class Shape(ABC):

    # Abstract method
    def no_of_sides(self):
        pass

    # Abstract method
    def calculate_area(self):
        pass

    # Abstract method
    def calculate_perimeter(self):
        pass


class Rectangle(Shape):

    # overriding abstract method
    def no_of_sides(self, length, breadth):
        print("Length = 40\nBreadth = 30")
        self.length = length
        self.breadth = breadth

    # overriding abstract method
    def calculate_area(self):
        print("Area of rectangle: ", self.length * self.breadth)

    # overriding abstract method
    def calculate_perimeter(self):
        print
        ("Perimeter of rectangle: ", 2 * (self.length + self.breadth), "\n")


class Square(Shape):
    # overriding abstract method
    def no_of_sides(self, side):
        print("Side = 10")
        self.side = side

    # overriding abstract method
    def calculate_area(self):
        print("Area of square: ", self.side ** 2)

    # overriding abstract method
    def calculate_perimeter(self):
        print("Perimeter of square: ", 4 * self.side, "\n")


class Circle(Shape):
    # overriding abstract method
    def no_of_sides(self, radius):
        print("Radius = 10")
        self.radius = radius

    # overriding abstract method
    def calculate_area(self):
        print("Area of circle : ", (22/7) * self.radius ** 2)

    # overriding abstract method
    def calculate_perimeter(self):
        print("Perimeter of circle: ", 2 * (22/7) * self.radius, "\n")


class Ellipse(Shape):

    # overriding abstract method
    def no_of_sides(self, semiMajorAxis, semiMinorAxis):
        print("semi Major Axis = 2 \n semi Minor Axis =2")
        self.semiMajorAxis = semiMajorAxis
        self.semiMinorAxis = semiMinorAxis

    # overriding abstract method
    def calculate_area(self):
        print
        ("Area of ellipse: ", (22/7) * self.semiMajorAxis * self.semiMinorAxis)

    # overriding abstract method
    def calculate_perimeter(self):
        print
        ("Perimeter of ellipse: ", 2 * (22/7) ** math.sqrt
         ((self.semiMajorAxis + self.semiMinorAxis) / 2))


objrect = Rectangle()
objrect.no_of_sides(40, 30)
objrect.calculate_area()
objrect.calculate_perimeter()

objSquare = Square()
objSquare.no_of_sides(10)
objSquare.calculate_area()
objSquare.calculate_perimeter()

objCircle = Circle()
objCircle.no_of_sides(7)
objCircle.calculate_area()
objCircle.calculate_perimeter()

objEllipse = Ellipse()
objEllipse.no_of_sides(40, 30)
objEllipse.calculate_area()
objEllipse.calculate_perimeter()
