import sys
sys.path.append("../../../lib")

from random import randint, random
from vector import Vector
from sketchy import Sketchy
from physics import limit
import math

class Path(object):
    def __init__(self, width, height):
        self.start = Vector(randint(0, width / 8), randint(0, height))
        self.end = Vector(randint(width * 4 / 5, width), randint(0, height))
        self.radius = 20
        self.path = self.start - self.end
        self.length = self.path.magnitude()
        self.slopeNeg = self.path.x > 0 and self.path.y > 0 or self.path.x < 0\
         and self.path.y < 0
        # print("slope is pos: ", self.slopeNeg)

    def update(self):
        """updates the objects"""

    def draw(self, g):
        """ draws objects to the screen """

        # sets the color and opacity of the objects outline
        # g.strokeWeight(50)
        # g.stroke(0, 0, 0, .2)
        # g.line(self.start.x, self.start.y, self.end.x, self.end.y)

        g.strokeWeight(1)
        g.stroke(0, 0, 0, 1)
        g.line(self.start.x, self.start.y, self.end.x, self.end.y)
        # sets the thickness of the outline

        # sets the color fill of the object
        g.push()
        g.translate(self.start.x, self.start.y)
        if self.slopeNeg:
            g.rotate(math.pi - self.path.angleBetween(Vector(1,0)))
        else:
            g.rotate(math.pi + self.path.angleBetween(Vector(1,0)))
        g.fill(0, 0, 0, 0.5)
        g.rect(0, -self.radius, self.length, self.radius * 2)
        g.pop()

        g.strokeWeight(1)
        g.stroke(0, 0, 0, 1)
        g.fill(0, 0, 0, 0.4)
        g.circle(self.start.x, self.start.y, self.radius)
        g.circle(self.end.x, self.end.y, self.radius)
        # draws a cirlce
