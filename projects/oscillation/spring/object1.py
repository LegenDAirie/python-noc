import sys
sys.path.append("../../../lib")

from random import randint, random
from vector import Vector
from sketchy import Sketchy
from physics import limit
from object2 import Ball
import math

class Spring(object):
    # hooke's law constant
    constant = .1
    def __init__(self, width, height):
        # location stuff
        self.anchor = Vector(width / 2, height / 2)
        self.location = Vector(0, 0)
        # self.velocity = Vector(0, 0)
        # self.acceleration = Vector(0, 0)

        # properties
        self.restLength = 100
        self.currentLength = 100
        self.force = 0



    def update(self):
        """updates the objects"""
        self.dir = (self.location - self.anchor)
        self.currentLength = self.dir.magnitude()
        self.force = self.restLength - self.currentLength
        self.dir = self.dir.normalize() * self.force * self.constant

        # self.velocity += self.acceleration
        # self.location += self.velocity

    def draw(self, g, balls):
        """ draws objects to the screen """

        # draws a cirlce
        g.line(self.anchor.x, self.anchor.y, balls.location.x, balls.location.y)
