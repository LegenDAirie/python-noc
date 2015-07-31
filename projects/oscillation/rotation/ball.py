import sys
sys.path.append("../../../lib")

from random import randint, random
from vector import Vector
from sketchy import Sketchy
from physics import limit
import math

class Ball(object):
    def __init__(self, width, height):
        self.angle = 0
        self.angleVelocity = 0
        self.angleAcceleration = 0.05
        self.width = 50
        self.height = 50
        self.location = Vector(randint(0, width - self.width), randint(0, height - self.height))
        # self.location = Vector(width/2, height/2)
        self.velocity = Vector(0, 0)
        self.acceleration = Vector(0, 0)

    def update(self):
        """updates the objects"""

        self.velocity += self.acceleration
        self.location += self.velocity
        self.angle += self.angleVelocity
        self.angleVelocity += self.angleAcceleration
        self.angleAcceleration *= 0

    def draw(self, g, width, height):
        """ draws objects to the screen """
        # sets the color and opacity of the objects outline
        g.stroke(0, 0, 0, 1)
        # sets the thickness of the outline
        g.strokeWeight(1)
        # sets the color fill of the object
        g.fill(0, 1, 1, 0.25)

        g.push()

        #translates the origin
        g.translate(self.location.x + self.width/2, self.location.y + self.height/2)
        # g.translate(width/2, height/2)

        #rotates with the origin at the axis
        g.rotate(self.angle)

        # draws a cirlce
        g.rect(-self.width/2, -self.height/2, self.width, self.height)
        g.pop()
        # g.rect(self.location.x, self.location.y, self.width, self.height)
