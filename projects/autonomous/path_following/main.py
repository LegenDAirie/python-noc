import sys
sys.path.append("../../../lib")

from sketchy import Sketchy
from vector import Vector
from object1 import Vehicle
from path import Path
class MyDrawing(Sketchy):

    def setup(self):
        width, height = [600, 400]
        self.path = Path(width, height)
        self.vehicles = []
        for i in range(0, 20):
            self.vehicles.append(Vehicle(width,height))
        self.size(width, height)

    def update(self):
        for i in range(len(self.vehicles)):
            self.vehicles[i].update(Vector(self.mouseX, self.mouseY), self.path)

    def draw(self, g):
        g.background(1, 1, 1)
        for i in range(len(self.vehicles)):
            self.vehicles[i].draw(g)
        self.path.draw(g)

MyDrawing()
