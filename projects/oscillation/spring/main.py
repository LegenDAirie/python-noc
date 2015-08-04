import sys
sys.path.append("../../../lib")

from sketchy import Sketchy
from vector import Vector
from object1 import Spring
from object2 import Ball
from physics import *

class MyDrawing(Sketchy):

    def setup(self):
        width, height = [600, 400]
        self.springs = []
        for i in range(0,1):
            self.springs.append(Spring(width, height))

        self.balls = []
        for i in range(0, 1):
            self.balls.append(Ball(width,height))
        self.size(width, height)

    def update(self):
        for i in range(len(self.balls)):
            self.balls[i].update()

        for i in range(len(self.springs)):
            self.springs[i].update()


    def draw(self, g):
        g.background(1, 1, 1)

        for i in range(len(self.balls)):
            self.balls[i].draw(g)

        for i in range(len(self.springs)):
            self.springs[i].draw(g, self.balls[i])

MyDrawing()
