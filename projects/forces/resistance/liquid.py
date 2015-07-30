import sys
sys.path.append("../../../lib")

class Liquid(object):
    """representing liquid"""
    def __init__(self, x, y, w, h):
        self.x, self.y, self.w, self.h = x, y, w, h
        drag = -.01

    def draw(self, g):
        g.fill(0, 0, 0, .75)
        g.rect(self.x, self.y, self.w, self.h)
