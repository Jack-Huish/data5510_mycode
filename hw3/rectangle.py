class Rectangle ():
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def calc_area(self):
        return self.length * self.width
first_rectangle = Rectangle(5,3)
print(first_rectangle.calc_area())