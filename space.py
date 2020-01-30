import numpy as np
import numba

class space():
    def __init__(self, bounds=(0, 128, 0, 128), scale=10, gravity=False):
        self.bounds = bounds
        self.size = (bounds[1]-bounds[0],bounds[3]-bounds[2])
        self.scale = scale
        self.gravity = gravity