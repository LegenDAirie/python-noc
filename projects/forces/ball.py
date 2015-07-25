import sys
sys.path.append("../../lib")

from random import randint, random
from vector import Vector
from sketchy import Sketchy
from physics import applyFroce
import math

class Ball(object):
    def __init__(self, width, height):
        self.location = Vector(randint(0, width), randint(0, height))
        self.velocity = Vector(0, 0)
        self.acceleration = Vector(0, 0)
        self.red = randint(0,1)
        self.green = randint(0,1)
        self.blue = randint(0,1)
        self.mass = randint(1,10)

        # force vectors
        self.wind = Vector(.01, 0)
        self.gravity = Vector(0, .1)

    def update(self, width, height):
        """updates the objects"""
        applyFroce(self.acceleration, self.mass, self.wind, self.gravity)

        self.velocity += self.acceleration
        self.checkEdges(width, height)
        self.location += self.velocity
        self.acceleration *= 0

    def draw(self, g):
        """ draws objects to the screen """

        # sets the color and opacity of the objects outline
        g.stroke(0, 0, 0, 1)

        # sets the thickness of the outline
        g.strokeWeight(1)

        # sets the color fill of the object
        g.fill(self.red, self.green, self.blue, 0.75)

        # draws a cirlce
        g.circle(self.location.x, self.location.y, 20)

    def checkEdges(self, width, height):
        if self.location.x > width or self.location.x < 0:
            self.velocity.x *= -1
        if self.location.y > height or self.location.y < 0:
            self.velocity.y *= -1
