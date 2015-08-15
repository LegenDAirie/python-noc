import sys
sys.path.append("../../../lib")

from sketchy import Sketchy
from vector import Vector
from vehicle import Vehicle

class MyDrawing(Sketchy):

    def setup(self):
        width, height = [600, 400]
        self.vehicles = []
        for i in range(0, 1):
            self.vehicles.append(Vehicle(width, height))
        self.size(width, height)

    def update(self):
        self.mouse = Vector(self.mouseX, self.mouseY)
        for i in range(len(self.vehicles)):
            self.vehicles[i].update(self.mouse)

    def draw(self, g):
        g.background(1, 1, 1)
        for i in range(len(self.vehicles)):
            self.vehicles[i].draw(g)

MyDrawing()
