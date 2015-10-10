from random import randint, random
import math

class Vector(object):
    """ a basic vector class used for creating 2D vectors"""
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
        """ adds 2 vectors and ruturns a new one """
        return Vector(self.x + b.x, self.y + b.y)

    # a + b
    def __add__(self, b):
        """ adds 2 vectors and ruturns a new one using oporators """
        return self.add(b)

    # addAccumulate(b)
    def addAccumulate(self, b):
        """ returns the current vector after the specified one has been added to it"""
        self.x += b.x
        self.y += b.y
        return self

    # a += b
    def __iadd__(self, b):
        """ returns the current vector after the specified one has been added to it using oporators"""
        return self.addAccumulate(b)

    # sub(b)
    def sub(self, b):
        """ subtracts the specified vector from the current """
        return Vector(self.x - b.x, self.y - b.y)

    # a - b
    def __sub__(self, b):
        """ subtracts the specified vector from the current using oporators """
        return self.sub(b)

    # subAccumulate(b)
    def subAccumulate(self, b):
        """ returns the current vector after the specified one has been subtracted from it"""
        self.x -= b.x
        self.y -= b.y
        return self

    # a -= b
    def __isub__(self, b):
        """ returns the current vector after the specified one has been subtracted from it using oporators"""
        return self.subAccumulate(b)

    # mul(scalar)
    def mul(self, scalar):
        """ returns a new vector that is the product of the current vector and a scalar """
        return Vector(self.x * scalar, self.y * scalar)

    # a * scalar
    def __mul__(self, other):
        """ returns a new vector that is the product of the current vector and a scalar using oporators"""
        if type(other) == int:
            return self.mul(other)
        elif type(other) == type(Vector(0, 0)):
            return self.dot(other)
        else:
            print("not a value type to multiply a vector against")

    # a *= scalar
    def mulAccumulate(self, scalar):
        """ returns the current vector after it has been multiplied by a scalar"""
        self.x *= scalar
        self.y *= scalar
        return self

    # a *= scalar
    def __imul__(self, scalar):
        """ returns the current vector after it has been multiplied by a scalar using oporators """
        return self.mulAccumulate(scalar)

    # div(scalar)
    def div(self, scalar):
        """ returns a new vector that is the quotiant of the curent and a scalar """
        return Vector(self.x / scalar, self.y / scalar)

    # a / scalar
    def __div__(self, scalar):
        """ returns a new vector that is the quotiant of the curent and a scalar using oporators """
        return self.div(scalar)

    # divAccumulate(scalar)
    def devAccumulate(self, scalar):
        """ returns the current vector after it has been devided by a scalar """
        self.x /= scalar
        self.y /= scalar
        return self

    # a /= scalar
    def __idiv__(self, scalar):
        """ returns the current vector after it has been devided by a scalar using oporators """
        return self.divAccumulate(scalar)

    # get_mag()
    def magnitude(self):
        """ tells you the magnitude of a vector """
        hypotenuse = math.sqrt((self.x ** 2) + (self.y ** 2))
        return hypotenuse

    def distanceBetween(self, vector):
        return math.sqrt(((self.x - vector.x)**2) + ((self.y - vector.y)**2))

    # normalize()
    def normalize(self):
        """ reduces the vector to unit vector form, a magnitude of 1 """
        hypotenuse = self.magnitude()
        if hypotenuse != 0:
            return Vector(self.x / hypotenuse, self.y / hypotenuse)
        else:
            return Vector(0, 0)

    def setMag(self, value):
        """ changes the magnitude of the current vector to a number specified """
        mag = self.magnitude()
        self.x *= value / mag
        self.y *= value / mag
        return Vector(self.x, self.y)

    def dot(self, b):
        """finds the dot product of two vectors and returns that value"""
        return self.x * b.x + self.y * b.y

    def angleBetween(self, vector):
        """finds the angle between two vectors, if one vector has no magnitude
        returns 0"""
        if vector.magnitude() != 0 and self.magnitude() != 0:
            return math.acos(self.dot(vector) / (self.magnitude() * vector.magnitude()))
        else:
            print("Vector has no magnitude")
            return 0
