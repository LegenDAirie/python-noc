from random import randint, random
from vector import Vector
from circles import Circles
from squares import Squares
import math

class ParticleSystem(object):

    def __init__(self, width, height, mouseX, mouseY):

        self.width = width
        self.height = height
        self.origin = Vector(mouseX, mouseY)
        self.particles = []
        self.particles.append(Circles(width, height, self.origin))

    def update(self, mouseX, mouseY):
        """updates the objects"""

        # Circles update stuff by iterating backwards
        for i in range(len(self.particles) -1, -1 ,-1):
            self.particles[i].update()

            # becks to see if the particle is dead
            if self.particles[i].isDead():

                # removes particle
                self.particles.remove(self.particles[i])
        k = randint(0,1)
        if k == 0:
            self.particles.append(Circles(self.width, self.height, self.origin))
        else:
            self.particles.append(Squares(self.width, self.height, self.origin))

    def applyforces(self, forces):
        for i in range(len(self.particles)):
            self.particles[i].applyforces(forces)


    def draw(self, g):
        """ draws objects to the screen """
        g.background(1, 1, 1)

        for i in range(len(self.particles)):
            self.particles[i].draw(g)
