import sys
sys.path.append("../../../lib")

from sketchy import Sketchy
from vector import Vector
from ball import Ball
from attractor import Attractor
from physics import *

class MyDrawing(Sketchy):

    def setup(self):
        width, height = [600, 400]

        self.a = Attractor(width, height)

        self.balls = []
        for i in range(0, 15):
            self.balls.append(Ball(width,height))

        self.size(width, height)

    def update(self):
        for i in range(len(self.balls)):
            self.force = self.a.attract(self.balls[i])
            applyForce(self.balls[i], self.force)
            self.balls[i].update(600, 400)

    def draw(self, g):
        g.background(1, 1, 1)
        for i in range(len(self.balls)):
            self.balls[i].draw(g)
        self.a.draw(g)

MyDrawing()
