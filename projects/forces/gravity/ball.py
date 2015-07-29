import sys
sys.path.append("../../../lib")

from random import randint, random
from vector import Vector
from sketchy import Sketchy
from physics import *
import math
import random

class Ball(object):
    def __init__(self, width, height):
        self.location = Vector(randint(0, width), randint(0, height))
        self.velocity = Vector(random.uniform(-1, 1), random.uniform(-1, 1))
        self.acceleration = Vector(0, 0)
        self.mass = randint(1,5)

    def update(self, width, height):
        """updates the objects"""

        self.velocity += self.acceleration
        self.location += self.velocity
        self.acceleration *= 0

    def draw(self, g):
        """ draws objects to the screen """

        # sets the color and opacity of the objects outline
        g.stroke(0, 0, 0, 1)

        # sets the thickness of the outline
        g.strokeWeight(1)

        # sets the color fill of the object
        g.fill(0, 1, 1, 0.2)

        # draws a cirlce
        g.circle(self.location.x, self.location.y, 4*self.mass)
