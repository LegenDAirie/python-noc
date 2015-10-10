import sys
sys.path.append("../../lib")

from random import randint, random
from vector import Vector
from sketchy import Sketchy
from physics import limit
import math

class Ball(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.location = Vector(1, 0)
        self.place = Vector(1, 0)
        self.constant = Vector(1, 0)
        self.acceleration = Vector(0, 0)

    def update(self, mouseX, mouseY):
        """updates the objects"""
        self.place = Vector(mouseX - (self.width / 2), mouseY - (self.height / 2))
        self.location = Vector(mouseX - (self.width / 2), mouseY - (self.height / 2))
        print(self.location.angleBetween(self.constant) * 180 / math.pi, "degrees")
        self.place = self.place.normalize() * 50
        print(self.place.magnitude())
        self.location = self.location.normalize() * 50


    def draw(self, g):
        """ draws objects to the screen """

        # sets the color and opacity of the objects outline
        g.stroke(0, 0, 0, .25)

        # sets the thickness of the outline
        g.strokeWeight(5)

        # sets the color fill of the object
        g.fill(0, 1, 1, 0.75)

        g.circle(self.width / 2, self.height / 2, 50)

        # draws a cirlce
        # g.circle(self.location.x, self.location.y, 20)
        g.push()
        g.translate(self.width / 2, self.height / 2)
        g.line(0, 0, self.location.x, self.location.y)
        g.line(0, 0, self.place.x, self.place.y)
        g.pop()
