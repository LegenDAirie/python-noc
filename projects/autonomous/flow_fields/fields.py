import sys
sys.path.append("../../../lib")

# from random import randint, random
from vector import Vector
import math
import random

class Field(object):

    def __init__(self, width, height):
        """2D array holding a grid of vectors"""
        self.width = width
        self.height = height

        # self.field_vector = Vector(1, 1)
        self.resolution = 50
        # need to take the floor and convert to int
        self.rows = width / self.resolution
        # need to take the floor and convert to int
        self.cols = height / self.resolution
        # range only takes ints
        self.field = [[Vector(random.uniform(-1, 1), random.uniform(-1, 1)) for x in range(self.rows)] for x in range(self.cols)]

    def update(self, mouse):
        # row horizontal x-axis
        for row in range(len(self.field)):
            # row horizontal x-axis
            for col in range(len(self.field[row])):
                self.field[row][col] = mouse - Vector((col * self.resolution + self.resolution / 2), (row * self.resolution + self.resolution / 2))

    def draw(self, g):
        gridY1 = 0
        gridX1 = 0


        # row horizontal x-axis
        for row in range(len(self.field)):
            # row horizontal x-axis
            for col in range(len(self.field[row])):
                self.arrow_len = self.field[row][col].normalize() * self.resolution * .8

                g.push()
                # places dots at the center of spaces on the grid
                g.translate(col * self.resolution + self.resolution / 2, row \
                 * self.resolution + self.resolution / 2)

                g.stroke(0, 0, 0, .25)
                g.strokeWeight(1)
                g.line(-self.arrow_len.x / 2, - self.arrow_len.y / 2, self.arrow_len.x / 2, self.arrow_len.y / 2)

                g.stroke(0, 0, 0, 1)
                g.strokeWeight(3)
                g.point(self.arrow_len.x / 2, self.arrow_len.y / 2)

                g.pop()

        g.stroke(0, 0, 0, 1)
        g.strokeWeight(1)
        # a grid of lines
        for x in range(0, self.cols):
            gridY1 += self.resolution
            g.line(0, gridY1, self.width, gridY1)
        for x in range(0, self.rows):
            gridX1 += self.resolution
            g.line(gridX1, 0, gridX1, self.height)
