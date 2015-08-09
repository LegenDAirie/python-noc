from random import randint, random
from vector import Vector
from physics import *
from confetti import Confetti
import math

class Particle(object):
    gravity = Vector(0, .1)
    def __init__(self, width, height, origin):
        self.width = width
        self.height = height
        self.location = Vector(origin.x, origin.y)
        self.velocity = Vector(randint(-2, 2), randint(-2, 2))
        self.acceleration = Vector(0, 0)
        self.lifeSpan = float(15)
        self.mass = 1

    def update(self):
        """updates the objects"""
        applyForce(self, self.gravity)
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
