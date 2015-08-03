import sys
sys.path.append("../../../lib")

from sketchy import Sketchy
from vector import Vector
from object1 import Ball
import math

class Wave(Sketchy):

    def setup(self):
        width, height = [600, 400]
        self.balls = []
        angle = 0
        angleInc = .2
        angleUpdate = .05
        x = 0
        for i in range(0, 25):
            self.balls.append(Ball(width, height, angle, x, angleUpdate))
            angle += angleInc
            x += 25
        self.size(width, height)

    def update(self):
        for i in range(len(self.balls)):
            self.balls[i].update()

    def draw(self, g):
        g.background(1, 1, 1)
        for i in range(len(self.balls)):
            self.balls[i].draw(g, 600, 400)

Wave()
