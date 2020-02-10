class Shape:

    def __init__(self, side, length, breadth):
        self.side = side
        self.length = length
        self.breadth = breadth

    def display(self):
        print("SIDE:", self.side)
        print("LENGTH:", self.length)
        print("BREADTH:", self.breadth)

    def square(self, side, lenght, breadth):
        self.square = (side * side)
        print("area of square: ", self.square)
        self.area_of_square = (4 * side)
        print("perimeter of square: ", self.square)
        self.square = (length * breadth)
        print("area of rectangle : ", self.square)
        self.square = 2 * (length + breadth)
        print("perimeter of rectangle: ", self.square)
side = int(input("Please enter your side: "))
length = int(input("Please enter your length: "))
breadth = int(input("Please enter your breadth: "))

S1 = Shape(side, length, breadth)
S1.display()
S1.square(side, length, breadth)
