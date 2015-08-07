import sys
sys.path.append("../../../lib")

from random import randint, random
from vector import Vector
from sketchy import Sketchy
from physics import limit
import math

class ParticleSystem(object):
    def __init__(self):
        pass
        # self.velocity = Vector(0, 0)
        # self.acceleration = Vector(0, 0)

    def update(self, mouseX, mouseY):
        """updates the objects"""
        self.origin = Vector(mouseX, mouseY)

        # self.velocity += self.acceleration
        # self.origin += self.velocity

    def draw(self, g):
        """ draws objects to the screen """

        # sets the color and opacity of the objects outline
        # g.stroke(0, 0, 0, 1)

        # sets the thickness of the outline
        # g.strokeWeight(1)

        # sets the color fill of the object
        # g.fill(0, 1, 1, 0.75)

        # draws a cirlce
        # g.circle(self.origin.x, self.origin.y, 20)
