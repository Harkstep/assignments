class shape:
    def init(self, name):
        self.name = name

    def area(self):
        pass
    def perimeter(self):
        pass

class square(shape):
    def __init__(self, name, length, width):
        self.length = length
        self.width = width
        self.name = "square"

    def area(self):
        return (self.length * self.width)

class circle(shape):
    def __init__(self, name, diam, pi):
        self.diam = diam
        self.pi = pi
        self.name = "circle"

    def circumference(self):
        return (self.diam * self.pi)
