import numpy as np
import numba

def resize_poly(poly, size):
    npoly = []
    for pt in poly:
        npoly.append([pt[0]*size, pt[1]*size])

    return np.array(npoly)
    
class solid():
    def __init__(self, poly=[[-0.5, -0.5], [-0.5, 0.5], [0.5, 0.5], [0.5, -0.5]], pos=[0,0], ini_v=[0, 0], mass=1, size=1, color=(255,255,255), rigid=False):
        if size!=1:
            poly = resize_poly(poly, size)
        self.poly = poly
        self.state = [pos, ini_v, mass] # [[x, y], [vx, vy], m]
        self.color = color
        self.rigid = rigid