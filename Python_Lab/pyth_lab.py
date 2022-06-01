class Rectangle():
    def __init__(self, l, w):
        self.length = l
        self.width = w

    def rectangle_area(self):
        return self.length*self.width

    def perimeter(self):
        return 2*(self.length+self.width)

    def isSquare(self):
        return self.length == self.width


length = int(input())
width = int(input())
newRectangle = Rectangle(length, width)
print(newRectangle.rectangle_area())
print(newRectangle.isSquare())
print(newRectangle.perimeter())
