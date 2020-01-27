import numpy as np
import numba

class space():
    def __init__(self, size=(128,128)):
        self.space_size = size