import sys
sys.path.append("../../../lib")

from random import randint, random
from vector import Vector
from sketchy import Sketchy
from physics import limit
import math


class Rectangle(object):
    def __init__(self, width, height):
        #oscillation stuff
        self.amplitude = 100
        self.period = 120
        self.frameCount = 0

        #location stuff
        self.location = Vector(0,0)

    def update(self):
        """updates the object"""

        self.frameCount += 1
        self.location.x = self.amplitude * math.cos(2 * math.pi * self.frameCount / self.period)

    def draw(self,g, width, height):
        """draws the object"""
        # sets the color and opacity of the objects outline
        g.stroke(0, 0, 0, 1)
        # sets the color fill of the object
        g.fill(0, 1, 1, 0.75)
        g.translate(width/2, height/2)

        g.line(0, 0, self.location.x, 0)
        g.circle(self.location.x, 0, 20)
