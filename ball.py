from random import randint, random
from vector import Vector
from sketchy import Sketchy
import math

class Ball(object):
    def __init__(self, width, height):
         self.location = Vector(width/2, height/2)
         self.velocity = Vector(0, 0)
        #  self.center = Vector(width/2, height/2)
        #  topSpeed = 10
        #  self.acceleration = Vector(0, 0.1)


    def update(self,mouseX, mouseY):
        self.mouse = Vector(mouseX, mouseY)

        self.dir = self.mouse - self.location
        self.dir.norm()
        self.dir * .5
        self.acceleration = self.dir


        self.velocity += self.acceleration
        self.velocity.limit(13)
        self.location += self.velocity
        
    def draw(self, g):
        g.fill(1, 0, 1, 0.75)
        g.circle(self.mouse.x, self.mouse.y, 20)

        g.fill(0, 1, 1, 0.75)
        g.circle(self.location.x, self.location.y, 20)

        # # mouse vector
        # g.stroke(0, 0, 0, 1)
        # g.strokeWeight(1)
        # g.line(0, 0, self.mouse.x, self.mouse.y)
        #
        # # center vector
        # g.stroke(0, 0, 0, 1)
        # g.strokeWeight(1)
        # g.line(0, 0, self.center.x, self.center.y)
        #
        # mouse - center vector
        g.stroke(0, 0, 0, 1)
        g.strokeWeight(1)
        # g.line(self.center.x, self.center.y, self.center.x + self.dir.x, self.center.y + self.dir.y)
