import sys
sys.path.append("../../../lib")

from random import randint, random
from vector import Vector
from sketchy import Sketchy
from physics import *
# from object1 import Spring
import math

class Ball(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.location = Vector(100 * math.cos(randint(1, 5) * math.pi / 5) + (width / 2), 100 * math.sin(randint(1, 5) * math.pi / 5) + (height /2))
        self.velocity = Vector(0, 0)
        self.acceleration = Vector(0, 0)

        # forces
        self.mass = 3
        self.gravity = Vector(0, 1 * self.mass)

    def update(self):
        """updates the location of the object"""

        applyForce(self, self.gravity)
        self.velocity += self.acceleration

        # using this as a kind of friction so it doesn't bounce forever
        self.velocity *= .99

        self.location += self.velocity

        self.acceleration *= 0

    def draw(self, g):
        # sets the color and opacity of the objects outline
        g.stroke(0, 0, 0, 1)

        # sets the thickness of the outline
        g.strokeWeight(1)

        # sets the color fill of the object
        g.fill(0, 1, 1, 0.75)

        g.circle(self.location.x, self.location.y, 20)
