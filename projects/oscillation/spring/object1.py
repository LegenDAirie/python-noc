import sys
sys.path.append("../../../lib")

from random import randint, random
from vector import Vector
from sketchy import Sketchy
from physics import *
from object2 import Ball
import math

class Spring(object):
    # hooke's law constant
    constant = .1
    def __init__(self, width, height):
        # location stuff
        self.anchor = Vector(width / 2, height / 2)
        self.location = Vector(0, 0)

        # properties
        self.restLength = 100
        self.currentLength = 100
        self.force = 1



    def update(self, ball):
        """updates the objects"""
        self.dir = ball.location - self.anchor
        self.currentLength = self.dir.magnitude()
        self.force = self.restLength - self.currentLength
        self.dir = self.dir.normalize() * self.force * self.constant
        applyForce(ball, self.dir)

    def draw(self, g, ball):
        """ draws objects to the screen """

        g.line(self.anchor.x, self.anchor.y, ball.location.x, ball.location.y)
