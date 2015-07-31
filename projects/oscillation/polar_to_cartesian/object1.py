import sys
sys.path.append("../../../lib")

from random import randint, random
from vector import Vector
from sketchy import Sketchy
from physics import limit
import math

class Square(object):
    def __init__(self, width, height):

        # sets how long i want the vector to be
        self.vectorLength = 75
        self.theta = math.pi / 4

        self.location = Vector(randint(0, width), randint(0, height))
        # self.velocity = Vector(0, 0)
        # self.acceleration = Vector(0, 0)

    def update(self):
        """updates the objects"""

        # translates the position the object should be on the circle into cartesian coordinates
        self.location.x = self.vectorLength * math.cos(self.theta)
        self.location.y = self.vectorLength * math.sin(self.theta)
        self.theta += .1
        # self.velocity += self.acceleration
        # self.location += self.velocity



    def draw(self, g, width, height):
        """ draws objects to the screen """

        # sets the color and opacity of the objects outline
        g.stroke(0, 0, 0, 1)

        # sets the thickness of the outline
        g.strokeWeight(1)

        # sets the color fill of the object
        g.fill(0, 1, 1, 0.75)

        # draws a cirlce
        g.rect(self.location.x + (width/2), self.location.y + (height/2), 20, 20)
