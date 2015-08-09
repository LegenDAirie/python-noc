from random import randint, random
from vector import Vector
from object2 import ParticleSystem
import math

class SystemOfSystems(object):

    def __init__(self):

        self.particleSystems = []
        self.counter = 60

    def update(self, width, height, mouseX, mouseY):

        self.counter -= 1
        if self.counter <= 0:

            # places the particle system at the beginning of the list
            self.particleSystems.insert(0, ParticleSystem(width, height, mouseX, mouseY))
            self.counter = 60

        for i in range(len(self.particleSystems) -1, -1, -1):
            self.particleSystems[i].update(mouseX, mouseY)
            if len(self.particleSystems) > 4:
                self.particleSystems.remove(self.particleSystems[i])

    def applyforces(self, *arg):
        for i in range(len(self.particleSystems)):
            self.particleSystems[i].applyforces(arg)

    def draw(self, g):
        for i in range(len(self.particleSystems)):
            self.particleSystems[i].draw(g)
