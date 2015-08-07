import sys
sys.path.append("../../../lib")

from sketchy import Sketchy
from vector import Vector
from object1 import Particle
from physics import *
from object2 import ParticleSystem

class MyDrawing(Sketchy):

    def setup(self):

        # all that needs to be
        width, height = [600, 400]
        self.system = ParticleSystem()
        self.size(width, height)







        self.particles = []
        self.particles.append(Particle(width,height))

    def update(self):

        # all that needs to be
        self.system.update()





        # Particle update stuff
        for i in range(len(self.particles) -1, -1 ,-1):
            self.particles[i].update()
            if self.particles[i].isDead():
                self.particles.remove(self.particles[i])
        self.particles.append(Particle(600, 400))



    def draw(self, g):

        # all that needs to be
        self.system.draw(g)






        g.background(1, 1, 1)
        for i in range(len(self.particles)):
            self.particles[i].draw(g)


MyDrawing()
