import sys
sys.path.append("../../lib")

from sketchy import Sketchy
from vector import Vector
from ball import Ball

class MyDrawing(Sketchy):

    def setup(self):
        width, height = [600, 400]
        self.balls = []
        for i in range(0, 10):
            self.balls.append(Ball(width,height))
        self.size(width, height)
        print len(self.balls)

    def update(self,):
        width, height = [600, 400]
        for i in range(len(self.balls)):
            self.balls[i].update(width, height)

    def draw(self, g):
        g.background(1, 1, 1)
        for i in range(len(self.balls)):
            self.balls[i].draw(g)

MyDrawing()
