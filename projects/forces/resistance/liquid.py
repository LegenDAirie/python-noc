import sys
sys.path.append("../../../lib")

from vector import Vector

class Liquid(object):
    """representing liquid"""
    def __init__(self, x, y, w, h):
        self.x, self.y, self.w, self.h = x, y, w, h
        self.dragStrength = -.01

    def resist(self, other):
        self.speed = other.velocity.magnitude()
        self.dragMagnitude = self.dragStrength * (self.speed ** 2)
        self.drag = Vector(other.velocity.x, other.velocity.y)
        self.drag.normalize
        self.drag *= self.dragMagnitude
        return self.drag


    def isInside(self, other):
        """checks to see if the object is inside the liquid"""
        if other.location.x > self.x and other.location.y > self.y and other.location.x < self.w and other.location.y < self.h:
            return True
        else:
            return False

    def draw(self, g):
        g.fill(0, 0, 0, .75)
        g.rect(self.x, self.y, self.w, self.h)
