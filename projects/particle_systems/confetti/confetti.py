from random import randint, random
from vector import Vector
from physics import *
import math

class Confetti(object):
    """docstring for Confetti"""

    gravity = Vector(0, .1)
    wind = Vector(.2, 0)

    def __init__(self, width, height, origin):
        self.width = width
        self.height = height
        self.location = Vector(origin.x, origin.y)
        self.velocity = Vector(randint(-2, 2), randint(-2, 2))
        self.acceleration = Vector(0, 0)
        self.lifeSpan = float(30)
        self.mass = 1

    def update(self):
        """updates the objects"""
        applyForce(self, self.gravity, self.wind)
        self.velocity += self.acceleration
        self.location += self.velocity
        self.lifeSpan -= 1
        reflectEdges(self, self.width, self.height)

        # dampening/ reseting
        self.velocity *= .99
        self.acceleration *= 0

    def draw(self, g):
        """ draws objects to the screen """

        # sets the color and opacity of the objects outline
        g.stroke(0, 0, 0, self.lifeSpan / 50)

        # sets the thickness of the outline
        g.strokeWeight(1)

        # sets the color fill of the object
        g.fill(0, 1, 1, self.lifeSpan / 50)

        # draws a cirlce
        g.circle(self.location.x, self.location.y, 2)


    def isDead(self):
        if self.lifeSpan < 0:
            return True
        else:
            return False
