from vector import *
import math
def limit(vector, topSpeed):
    """ limits a vectors magnitude """
    if vector.magnitude() > topSpeed:
        return vector.setMag(topSpeed)
    else:
        return vector

def applyForce(vector, *arg):
    """accumulates all the force vectors together before applying them"""
    for i in range(len(arg)):
        # checks to see if the first item is containing a tuple of forces or \
        # if it is just a force
        if type(arg[i]) == type((1,)):
            for force in arg[i]:
                vector.acceleration += force / vector.mass
        else:
            vector.acceleration += arg[i] / vector.mass
    return vector

def reflectEdges(vector, width, height):
    """keeps an vector inside the screen"""
    if vector.location.x > width:
        vector.location.x = width
        vector.velocity.x *= -1
    if vector.location.x < 0:
        vector.location.x = 0
        vector.velocity.x *= -1
    if vector.location.y > height:
        vector.location.y = height
        vector.velocity.y *= -1
    if vector.location.y < 0:
        vector.location.y = 0
        vector.velocity *= -1
