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

        # print self.mouse.x
        self.dir = self.mouse - self.location
        self.dir.norm()
        self.dir * .5
        self.acceleration = self.dir

        # print self.dir.get_mag()
        # self.mult(10)
        # print self.dir.x

        # self.dir = self.mouse.sub(self.center)
        # print self.mouse.x
        # self.dir.norm()
        # print(math.sqrt((self.dir.x ** 2) + (self.dir.y ** 2)))
        # print self.dir.x
        # self.dir.mult(1)
        # self.velocity = Vector(1, 1)


        # self.acceleration = self.dir
        # print self.acceleration.x
        # print self.acceleration
        # self.velocity.add(self.acceleration)
        # print self.velocity.x
        # print(math.sqrt((self.velocity.x ** 2) + (self.velocity.y ** 2)))
        # print(math.sqrt((self.velocity.x ** 2) + (self.velocity.y ** 2)))
        # if self.velocity.x < 5 and self.velocity.x > -5 and self.velocity.y < 5 and self.velocity.y > -5:
            # print "k"
        # else:
            # return Vector(0, 0)
        # self.velocity += self.acceleration
        # self. velocity = self.velocity.limit(10)
        self.velocity += self.acceleration
        self.velocity.limit(13)
        self.location += self.velocity
        # print self.acceleration.y

        # self.velocity.limit(20)

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
