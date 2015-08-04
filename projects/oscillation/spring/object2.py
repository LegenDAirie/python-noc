import sys
sys.path.append("../../../lib")

from random import randint, random
from vector import Vector
from sketchy import Sketchy
from physics import limit
# from object1 import Spring
import math

class Ball(object):
    def __init__(self, width, height):
        self.location = Vector(0, 0)
        self.velocity = Vector(0, 0)
        self.acceleration = Vector(0, 0)

        # forces
        self.gravity = Vector(0, 1)

    def update(self):
        """updates the location of the object"""

        applyForce(self, self.gravity, self.Spring)
        self.velocity += self.acceleration
        self.location += self.velocity

    def draw(self, g):
        # sets the color and opacity of the objects outline
        g.stroke(0, 0, 0, 1)

        # sets the thickness of the outline
        g.strokeWeight(1)

        # sets the color fill of the object
        g.fill(0, 1, 1, 0.75)

        g.circle(self.location.x, self.location.y, 20)
