from random import randint, random
from vector import Vector
from physics import *
from confetti import Confetti
import math

class Squares(Confetti):

    def draw(self, g):
        """ draws objects to the screen """

        # sets the color and opacity of the objects outline
        g.stroke(0, 0, 0, self.lifeSpan / 50)

        # sets the thickness of the outline
        g.strokeWeight(1)

        # sets the color fill of the object
        g.fill(1, 0, 0, self.lifeSpan / 50)

        # draws a cirlce
        g.rect(self.location.x, self.location.y, 5, 5)
