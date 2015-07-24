import sys
sys.path.append("../../lib")

from sketchy import Sketchy
from ball import Ball
from vector import Vector
from physics import limit

class MyDrawing(Sketchy):

    def setup(self):
        width, height = [600, 400]
        self.balls = []
        for i in range(0,3):
            self.balls.append(Ball(width, height))
        self.size(width, height)

    def update(self):
        for i in range(len(self.balls)):
            self.balls[i].update(self.mouseX, self.mouseY)

    def draw(self, g):
        g.background(1, 1, 1)
        for i in range(len(self.balls)):
            self.balls[i].draw(g)

MyDrawing()
