import sys
sys.path.append("../../../lib")

from sketchy import Sketchy
from vector import Vector
from object1 import Particle
from physics import *
# from object2 import Particle

class MyDrawing(Sketchy):

    def setup(self):
        width, height = [600, 400]
        self.balls = []
        # for i in range(0, 1):
        self.balls.append(Particle(width,height))
        self.size(width, height)

    def update(self):
        for i in range(len(self.balls) -1, -1 ,-1):
            print len(self.balls)
            self.balls[i].update()
            # print self.balls[i]
            if isDead(self.balls[i]):
                self.balls.remove(self.balls[i])
        self.balls.append(Particle(600, 400))


    def draw(self, g):
        g.background(1, 1, 1)
        for i in range(len(self.balls)):
            self.balls[i].draw(g)

MyDrawing()
