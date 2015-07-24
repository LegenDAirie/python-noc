from sketchy import Sketchy
from ball import Ball
from vector import Vector
from physics import limit

class MyDrawing(Sketchy):

    def setup(self):
        width, height = [600, 400]
        self.ball = Ball(width, height)
        self.size(width, height)

    def update(self):

        self.ball.update(self.mouseX, self.mouseY)

    def draw(self, g):
        g.background(1, 1, 1)
        self.ball.draw(g)

MyDrawing()
