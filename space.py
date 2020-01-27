import numpy as np
import numba

class space():
    def __init__(self, size=(128,128), scale=10):
        self.size = size
        self.scale = scale