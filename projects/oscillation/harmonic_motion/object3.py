import sys
sys.path.append("../../../lib")

from random import randint, random
from vector import Vector
from sketchy import Sketchy
from physics import limit
import math
import random

class Oscillator(object):
    def __init__(self, width, height):
        # oscillation stuff
        self.angle = Vector(0, 0)
        self.angleVelocity = Vector(random.uniform(-.05, .05), random.uniform(-.05, .05))
        self.amplitude = Vector(randint(0, width / 2), randint(0, height / 2))

        self.location = Vector(0, 0)

    def update(self):
        self.angle += self.angleVelocity

        self.location.x = math.sin(self.angle.x) * self.amplitude.x
        self.location.y = math.sin(self.angle.y) * self.amplitude.y

    def draw(self, g, width, height):
        # sets the color and opacity of the objects outline
        g.stroke(0, 0, 0, 1)
        # sets the color fill of the object
        g.fill(0, 1, 1, 0.75)

        g.push()
        g.translate(width / 2, height / 2)
        g.line(0, 0, self.location.x, self.location.y)
        g.circle(self.location.x, self.location.y, 20)
        g.pop()
