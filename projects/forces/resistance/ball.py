import sys
sys.path.append("../../../lib")

from random import randint, random
from vector import Vector
from sketchy import Sketchy
from physics import *
import math

class Ball(object):
    def __init__(self, width, height):
        self.location = Vector(randint(0, width), height/2)
        self.velocity = Vector(0, 0)
        self.acceleration = Vector(0, 0)
        self.red = randint(0,1)
        self.green = randint(0,1)
        self.blue = randint(0,1)
        self.mass = randint(1,5)

        # force vectors
        self.wind = Vector(.01, 0)
        # scaling gravity by mass to be more accurate
        self.gravity = Vector(0, .1*self.mass)

    def update(self, width, height):
        """updates the objects"""
        # self.friction = Vector(self.velocity.x, self.velocity.y)
        # self.friction.normalize
        # self.friction *= -.01
        applyFroce(self.acceleration, self.mass, self.wind, self.gravity)

        self.velocity += self.acceleration
        self.location += self.velocity
        checkEdges(self, width, height)
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
        g.circle(self.location.x, self.location.y, self.mass*10)
