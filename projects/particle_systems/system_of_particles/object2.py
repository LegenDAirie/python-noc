import sys
sys.path.append("../../../lib")

from random import randint, random
from vector import Vector
from sketchy import Sketchy
from physics import limit
from object1 import Particle
import math

class ParticleSystem(object):
    def __init__(self, width, height, mouseX, mouseY):

        self.width = width
        self.height = height
        self.origin = Vector(mouseX, mouseY)
        self.particles = []
        self.particles.append(Particle(width, height, self.origin))

    def update(self, mouseX, mouseY):
        """updates the objects"""
        self.origin = Vector(mouseX, mouseY)

        # Particle update stuff by iterating backwards
        for i in range(len(self.particles) -1, -1 ,-1):
            self.particles[i].update()

            # becks to see if the particle is dead
            if self.particles[i].isDead():

                # removes particle
                self.particles.remove(self.particles[i])
        self.particles.append(Particle(self.width, self.height, self.origin))

    def draw(self, g):
        """ draws objects to the screen """
        g.background(1, 1, 1)

        for i in range(len(self.particles)):
            self.particles[i].draw(g)
