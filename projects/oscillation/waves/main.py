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
        angleVel = 0.2
        amp = 100
        self.x = 10
        for i in range(0, 25):
            self.y = amp * math.sin(angle)
            self.balls.append(Ball(width, height, self.y, self.x))
            self.x += 25
            print self.x
            angle += angleVel
        self.size(width, height)

    def update(self):
        for i in range(len(self.balls)):
            self.balls[i].update()

    def draw(self, g):
        g.background(1, 1, 1)
        for i in range(len(self.balls)):
            self.balls[i].draw(g, 600, 400)

Wave()
