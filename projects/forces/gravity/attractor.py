import sys
sys.path.append("../../../lib")

from random import randint, random
from vector import Vector
from sketchy import Sketchy
from physics import *
import math

class Attractor(object):
    def __init__(self, width, height):
        self.location = Vector(width/2, height/2)
        self.mass = 15
        self.g = .1

    def attract(self, ball):
        self.force = self.location - ball.location
        self.distance = self.force.magnitude()
        self.force.normalize()
        self.strength = (self.g * self.mass * ball.mass) / (self.distance ** 2)
        self.force *= self.strength
        return self.force

    def draw(self, g):
        g.stroke(0, 0, 0, 1)

        # sets the thickness of the outline
        g.strokeWeight(1)

        # sets the color fill of the object
        g.fill(0, 0, 0, .65)

        # draws a cirlce
        g.circle(self.location.x, self.location.y, 15 * math.sqrt(self.mass/math.pi))
