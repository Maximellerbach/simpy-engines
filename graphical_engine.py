import numpy as np
import numba
import cv2
import threading

import objects

class DrawThread(threading.Thread):
    def set_name(self, name):
        return

    def draw(self, object):
        return 