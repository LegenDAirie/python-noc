import sys
sys.path.append("../../../lib")

from random import randint, random
from vector import Vector
from sketchy import Sketchy
from physics import limit
import math

class Ball(object):
    def __init__(self, width, height, angle, x, angleUpdate):
        # angle stuff
        self.amp = 150
        self.angle = angle
        self.angleUpdate = angleUpdate

        # movement stuff
        self.location = Vector(x, 0)

    def update(self):
        """updates the objects"""

        #updates the angle
        self.location.y = self.amp * math.sin(self.angle)
        self.angle += self.angleUpdate


    def draw(self, g, width, height):
        """ draws objects to the screen """

        # sets the color and opacity of the objects outline
        g.stroke(0, 0, 0, 1)

        # sets the thickness of the outline
        g.strokeWeight(1)

        # sets the color fill of the object
        g.fill(0, 0, 0, 0.1)

        # draws a cirlce
        g.circle(self.location.x, self.location.y + height / 2, 24)
