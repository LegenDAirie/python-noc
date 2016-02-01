import sys
sys.path.append("../../../lib")

from sketchy import Sketchy
from vector import Vector
from object1 import Square
from object2 import Rectangle
from object3 import Oscillator

class MyDrawing(Sketchy):

    def setup(self):
        width, height = [600, 400]
        self.line = Rectangle(width, height)

        self.oscillations = []
        for i in range(0,7):
            self.oscillations.append(Oscillator(width, height))

        self.balls = []
        for i in range(0, 1):
            self.balls.append(Square(width,height))

        self.size(width, height)

    def update(self):
        for i in range(len(self.oscillations)):
            self.oscillations[i].update()

        for i in range(len(self.balls)):
            self.balls[i].update()
        self.line.update()

    def draw(self, g):
        g.background(1, 1, 1)

        for i in range(len(self.oscillations)):
            self.oscillations[i].draw(g, 600, 400)

        for i in range(len(self.balls)):
            self.balls[i].draw(g, 600, 400)

        self.line.draw(g, 600, 400)
MyDrawing()
