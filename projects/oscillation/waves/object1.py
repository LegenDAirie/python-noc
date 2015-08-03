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
        self.tan = 0

        # movement stuff
        self.location = Vector(x, 0)
        self.oldLocation = Vector(x, 0)
        self.velocity = Vector(0, 0)
        self.heading = 0

    def update(self):
        """updates the objects"""

        #updates the angle
        self.oldLocation.y = self.location.y
        self.location.y = self.amp * math.sin(self.angle)
        self.angle += self.angleUpdate
        self.velocity.y = self.location.y - self.oldLocation.y
        # self.tan = math.tan(self.angle)
        print self.velocity.y
        self.heading = math.atan2(self.velocity.y, 5)

    def draw(self, g, width, height):
        """ draws objects to the screen """

        # sets the color and opacity of the objects outline
        g.stroke(0, 0, 0, 1)

        # sets the thickness of the outline
        g.strokeWeight(1)

        # sets the color fill of the object
        g.fill(0, 0, 0, 0.1)

        # draws a cirlce
        # g.rect(self.location.x, self.location.y + height / 2, 24, 10)

        g.push()
        g.translate(self.location.x + 12, self.location.y + 5 + (height / 2))
        g.rotate(self.heading)

        # draws a cirlce
        g.rect(-12, -5, 24, 10)
        g.pop()
