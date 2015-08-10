import sys
sys.path.append("../../../lib")

from sketchy import Sketchy
from object3 import SystemOfSystems
from repeller import Repeller
from vector import Vector

class MyDrawing(Sketchy):

    gravity = Vector(0, .1)
    wind = Vector(.2, 0)
    def setup(self):
        # all that needs to be
        self.width, self.height = [600, 400]
        self.systems = SystemOfSystems()
        self.repeller = Repeller(self.width, self.height)
        self.size(self.width, self.height)

    def update(self):
        # all that needs to be
        self.systems.addParticle()

        self.systems.applyforces(self.gravity, self.wind)
        self.systems.update(self.width, self.height, self.mouseX, self.mouseY, self.repeller)


    def draw(self, g):
        # all that needs to be
        self.systems.draw(g)
        self.repeller.draw(g)
MyDrawing()
