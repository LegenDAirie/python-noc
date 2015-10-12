import sys
sys.path.append("../../../lib")

from sketchy import Sketchy
from vector import Vector
from vehicle import Vehicle
from ball import Ball
from random import randint

class MyDrawing(Sketchy):

    def setup(self):
        self.width, self.height = [600, 400]
        self.ball = Ball(self.width, self.height)
        self.vehicles = []
        self.k = 1
        self.size(self.width, self.height)

    def update(self):
        self.mouse = Vector(self.mouseX, self.mouseY)
        self.ball.update(self.mouse)
        if self.k == 90:
            self.k = 1
            for i in range(0, 1):
                self.vehicles.append(Vehicle(self.width, self.width))
        if self.vehicles != []:
            for i in range(len(self.vehicles) -1, -1, -1):
                self.vehicles[i].update(self.mouse)
                if self.vehicles[i].isDead(self.ball):
                    self.vehicles.remove(self.vehicles[i])
        self.k += 1


    def draw(self, g):
        g.background(1, 1, 1)
        self.ball.draw(g)
        for i in range(len(self.vehicles)):
            self.vehicles[i].draw(g)

MyDrawing()
