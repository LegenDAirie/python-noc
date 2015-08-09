from random import randint, random
from vector import Vector
from physics import *
import math

class Confetti(object):
    """docstring for Confetti"""
    def __init__(self):
        pass

    

    def isDead(self):
        if self.lifeSpan < 0:
            return True
        else:
            return False
