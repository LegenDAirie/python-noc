from vector import *
from physics import *
import math

class Repeller(object):

    def __init__(self, width, height):

        self.location = Vector(width / 2, height / 2)
        self.mass = 10
        self.gravStr = 2

    def repel(self, particle):
        """calcules a vector for repulsion"""

        self.dir = self.location - particle.location
        self.distance = self.dir.magnitude()
        self.dir.normalize()
        self.strength = -1 * self.gravStr * self.mass * particle.mass / (self.distance ** 2)
        self.dir *= self.strength
        return self.dir

    def draw(self, g):
        """ draws objects to the screen """

        # sets the color and opacity of the objects outline
        g.stroke(0, 0, 0, 1)

        # sets the thickness of the outline
        g.strokeWeight(1)

        # sets the color fill of the object
        g.fill(0, 0, 0, .25)

        # draws a cirlce
        g.circle(self.location.x, self.location.y, 20)
