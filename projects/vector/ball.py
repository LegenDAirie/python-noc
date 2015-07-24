from random import randint, random
from vector import Vector
from sketchy import Sketchy
from physics import limit
import math

class Ball(object):
    def __init__(self, width, height):
         self.location = Vector(randint(0,width), randint(0,height))
         self.velocity = Vector(0, 0)


    def update(self,mouseX, mouseY):
        """ updates the objects """
        self.mouse = Vector(mouseX, mouseY)

        self.dir = self.mouse - self.location
        self.dir.normalize()
        self.dir * .5

        self.acceleration = self.dir
        self.velocity += self.acceleration
        # self.velocity.limit(13)
        limit(self.velocity, 13)
        self.location += self.velocity

    def draw(self, g):
        """ draws objects to the screen """

        # sets the color and opacity of the objects outline
        g.stroke(0, 0, 0, 1)

        # sets the thickness of the outline
        g.strokeWeight(1)

        # sets the color fill of the object
        g.fill(0, 1, 1, 0.75)

        # draws a cirlce
        g.circle(self.location.x, self.location.y, 20)
