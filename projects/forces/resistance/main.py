import sys
sys.path.append("../../../lib")

from sketchy import Sketchy
from vector import Vector
from ball import Ball
from liquid import Liquid
from physics import *

class Resistance(Sketchy):

    def setup(self):
        width, height = [600, 400]
        self.liquid = Liquid(width/2, height/2, width, height)
        self.balls = []
        for i in range(0, 10):
            self.balls.append(Ball(width, height))
        self.size(width, height)

    def update(self):
        width, height = [600, 400]
        for i in range(len(self.balls)):
            if self.liquid.isInside(self.balls[i]):
                self.balls[i].friction = self.liquid.resist(self.balls[i])
                applyForce(self.balls[i], self.balls[i].wind, self.balls[i].gravity, self.balls[i].friction)
            else:
                applyForce(self.balls[i], self.balls[i].wind, self.balls[i].gravity)
            self.balls[i].update(width, height)
            reflectEdges(self.balls[i], width, height)

    def draw(self, g):
        g.background(1, 1, 1)

        self.liquid.draw(g)

        for i in range(len(self.balls)):
            self.balls[i].draw(g)

Resistance()
