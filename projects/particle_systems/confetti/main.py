import sys
sys.path.append("../../../lib")

from sketchy import Sketchy
from object3 import SystemOfSystems

class MyDrawing(Sketchy):

    def setup(self):

        # all that needs to be
        self.width, self.height = [600, 400]
        self.systems = SystemOfSystems()
        self.size(self.width, self.height)

    def update(self):

        # all that needs to be
        self.systems.update(self.width, self.height, self.mouseX, self.mouseY)


    def draw(self, g):

        # all that needs to be
        self.systems.draw(g)
MyDrawing()
