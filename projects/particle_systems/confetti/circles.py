from random import randint, random
from vector import Vector
from physics import *
from confetti import Confetti
import math

class Circles(Confetti):
    # def __init__(self, width, height, origin):
    #     pass
    # def update(self):
    #     pass
    # def draw(self, g):
    #     pass
    def draw(self, g):
        """ draws objects to the screen """

        # sets the color and opacity of the objects outline
        g.stroke(0, 0, 0, self.lifeSpan / 50)

        # sets the thickness of the outline
        g.strokeWeight(1)

        # sets the color fill of the object
        g.fill(0, 1, 1, self.lifeSpan / 50)

        # draws a cirlce
        g.circle(self.location.x, self.location.y, 2)
