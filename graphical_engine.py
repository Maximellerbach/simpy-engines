import numpy as np
import numba
import cv2
import threading

from solid import *
from space import *

class Graphical():
    def __init__(self, space, objects=[]):
        self.space = space
        self.objects = objects
        self.img = np.zeros((self.space.size[1], self.space.size[0], 3), dtype=np.uint8)

    def draw(self):
        self.img = np.zeros((self.space.size[1], self.space.size[0], 3), dtype=np.uint8)
        for obj in self.objects:
            if obj.is_onscreen():
                npoly = obj.translate_poly()
                cv2.polylines(self.img, [npoly], True, obj.color, thickness=1)

    def display(self, n=1):
        cv2.imshow('img', cv2.flip(self.img, 0)) # show vertically flipped image
        cv2.waitKey(n)

if __name__ == "__main__":
    """
    test basic functions of the graphical engine
    """
    S = space()
    box = solid(S, pos=[64, 64], size=10, color=(254, 129, 12))
    G = Graphical(S, objects=[box])

    G.draw()
    G.display(n=0)