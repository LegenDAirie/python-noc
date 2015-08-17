import sys
sys.path.append("../../../lib")

from random import *
from vector import Vector
from sketchy import Sketchy
from physics import *
import math

class Vehicle(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.location = Vector(randint(0, width), randint(0, height))
        self.velocity = Vector(0, 0)
        self.acceleration = Vector(0, 0)
        self.maxSpeed = 4
        self.maxForce = .1
        self.mass = 1
        self.circleRad = 20
        self.future = Vector(0, 0)
        self.circlePoint = Vector(0, 0)
        self.counter = 0
        self.angle = 0

    def update(self, target):
        """updates the objects"""
        self.counter += 1
        if self.counter == 15:
            self.angle = random() * 6.28
            self.counter = 0

        # its future location if no change to acceleration
        self.future = (self.velocity.normalize() * 100) + self.location

        self.circlePoint = Vector(self.circleRad * math.sin(self.angle), self.circleRad * math.cos(self.angle))
        self.circlePoint += self.future


        self.seek(self.circlePoint)
        self.velocity += self.acceleration
        limit(self.velocity, self.maxSpeed)
        self.location += self.velocity

        if self.location.x > self.width:
            self.location.x = 0
        if self.location.x < 0:
            self.location.x = self.width
        if self.location.y > self.height:
            self.location.y = 0
        if self.location.y < 0:
            self.location.y = self.height

        # resetting acceleration back to 0 so it doesnt accumulate
        self.acceleration *= 0

    def seek(self, target):
        # calculates the vector that vehicle wants
        self.desired = target - self.location
        d = self.desired.magnitude()

        # apparently just self.disired.normalize() doesnt work
        self.desired = self.desired.normalize()

        if d < 100:
            k = self.maxSpeed * d / 100
            self.desired *= k
        else:
            self.desired *= self.maxSpeed

        # changing velocity to desired
        self.steer = self.desired - self.velocity

        # limits the max force, controles how sharp it turns
        limit(self.steer, self.maxForce)
        applyForce(self, self.steer)


    def draw(self, g):
        """ draws objects to the screen """

        # sets the color and opacity of the objects outline
        g.stroke(0, 0, 0, 1)

        # sets the thickness of the outline
        g.strokeWeight(1)

        # sets the color fill of the object
        g.fill(1, 1, 0, 0.75)

        theda = math.atan2(self.velocity.y, self.velocity.x)
        g.push()
        g.translate(self.location.x + 10, self.location.y + 2.5)
        g.rotate(theda)

        # draws a cirlce
        g.rect(-10, -2.5, 20, 5)
        g.pop()

        # toggle on to know where its destination is
        # g.circle(self.future.x, self.future.y, 20)
        # g.circle(self.circlePoint.x, self.circlePoint.y, 1)