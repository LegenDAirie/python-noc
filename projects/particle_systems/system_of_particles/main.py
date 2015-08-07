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
        self.system = ParticleSystem(width, height, self.mouseX, self.mouseY)
        self.size(width, height)

    def update(self):

        # all that needs to be
        self.system.update(self.mouseX, self.mouseY)

    def draw(self, g):

        # all that needs to be
        self.system.draw(g)








MyDrawing()
