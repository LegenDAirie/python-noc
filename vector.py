from random import randint, random
import math

class Vector(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # str(a)
    def __str__(self):
        return "[" + str(self.x) + ", " + str(self.y) + "]"

    # repr(a) or print(a)
    def __repr__(self):
        return self.__str__()

    # add(b)
    def add(self, b):
        return Vector(self.x + b.x, self.y + b.y)

    # a + b
    def __add__(self, b):
        return self.add(b)

    # addAccumulate(b)
    def addAccumulate(self, b):
        self.x += b.x
        self.y += b.y
        return self

    # a += b
    def __iadd__(self, b):
        return self.addAccumulate(b)

    # sub(b)
    def sub(self, b):
        return Vector(self.x - b.x, self.y - b.y)

    # a - b
    def __sub__(self, b):
        return self.sub(b)

    # subAccumulate(b)
    def subAccumulate(self, b):
        self.x -= b.x
        self.y -= b.y
        return self

    # a -= b
    def __isub__(self, b):
        return self.subAccumulate(b)

    # mul(scalar)
    def mul(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    # a * scalar
    def __mul__(self, scalar):
        return self.mul(scalar)

    # a *= scalar
    def mulAccumulate(self, scalar):
        self.x *= x
        self.y *= y
        return self

    # a *= scalar
    def __imul__(self, scalar):
        return self.mulAccumulate(scalar)

    # div(scalar)
    def div(self, scalar):
        return Vector(self.x / scalar, self.y / scalar)

    # a / scalar
    def __div__(self, scalar):
        return self.div(scalar)

    # divAccumulate(scalar)
    def devAccumulate(self, scalar):
        self.x /= scalar
        self.y /= scalar
        return self

    # a /= scalar
    def __idiv__(self, scalar):
        return self.divAccumulate(scalar)

    # get_mag()
    def magnitude(self):
        hypotenuse = math.sqrt((self.x ** 2) + (self.y ** 2))
        return hypotenuse

    # normalize()
    def normalize(self):
        hypotenuse = self.magnitude()
        if hypotenuse != 0:
            self.x /= hypotenuse
            self.y /= hypotenuse
            return Vector(self.x, self.y)

    def setMag(self, value):
        mag = self.magnitude()
        self.x *= value / mag
        self.y *= value / mag
        return Vector(self.x, self.y)

    def limit(self, topSpeed):
        if self.magnitude() > topSpeed:
            return self.setMag(topSpeed)
        else:
            return self
