import sys
sys.path.append("../../../lib")

from random import randint, random
from vector import Vector
from sketchy import Sketchy
from physics import limit
import math

class Pendulum(object):
    def __init__(self, width, height):
        #location stuff
        self.location = Vector(0, 0)
        # self.velocity = Vector(0, 0)
        # self.acceleration = Vector(0, 0)
        self.origin = Vector(width / 2, height / 2)
        self.armLength = 100

        # angle stuff
        self.angle = math.pi / 2
        # self.penArmAngle = 0
        self.angleVelocity = 0
        self.angleAcceleration = 0

        # forces
        self.gravity = .4

    def update(self):
        """updates the objects"""
        self.angleAcceleration = -self.gravity * math.sin(self.angle) / self.armLength
        self.angleVelocity += self.angleAcceleration
        self.angle += self.angleVelocity
        self.angleVelocity *= .999

        # converting to cartesian coordinates
        self.location = Vector(self.armLength * math.sin(self.angle), self.armLength * math.cos(self.angle))
        self.location += self.origin

    def draw(self, g):
        """ draws objects to the screen """

        # sets the color and opacity of the objects outline
        g.stroke(0, 0, 0, 1)

        # sets the thickness of the outline
        g.strokeWeight(1)

        # sets the color fill of the object
        g.fill(0, 1, 1, 0.75)

        # draws a cirlce
        g.line(self.origin.x, self.origin.y, self.location.x, self.location.y)
        g.circle(self.location.x, self.location.y, 20)
