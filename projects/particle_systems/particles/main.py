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
        self.particles = []
        self.particles.append(Particle(width,height))
        self.size(width, height)

    def update(self):
        for i in range(len(self.particles) -1, -1 ,-1):
            self.particles[i].update()
            if self.particles[i].isDead():
                self.particles.remove(self.particles[i])
        self.particles.append(Particle(600, 400))



    def draw(self, g):
        g.background(1, 1, 1)
        for i in range(len(self.particles)):
            self.particles[i].draw(g)


MyDrawing()
