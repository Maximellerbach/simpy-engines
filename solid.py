import numpy as np

def resize_poly(poly, size):
    return list(np.multiply(poly, size))
    
def adjust_pos(pos, mins):
    return list(np.add(pos, mins))

class solid():
    def __init__(self, space, poly=[[-0.5, -0.5], [-0.5, 0.5], [0.5, 0.5], [0.5, -0.5]], pos=[0,0], ini_v=[0, 0], mass=1, size=1, color=(255,255,255), rigid=False):
        self.space_bounds = space.bounds

        if size!=1:
            poly = resize_poly(poly, size)

        self.poly = poly
        self.prev_npoly = self.translate_poly

        pos = adjust_pos(pos, [-self.space_bounds[0], -self.space_bounds[2]])
        self.state = [pos, ini_v, mass] # [[x, y], [vx, vy], m]
        self.color = color
        self.rigid = rigid

    def get_maxp(self):
        return np.max(self.poly, axis=0)

    def get_minp(self):
        return np.min(self.poly, axis=0)
        
    def is_onscreen(self):
        x, y = self.state[0]
        minx, maxx, miny, maxy = self.space_bounds
        if minx<=x<=maxx and miny<=y<=maxy:
            return True
        else:
            False
    
    def translate_poly(self):
        x, y = self.state[0]

        npoly = []
        for pt in self.poly:
            p = [int(pt[0]+x), int(pt[1]+y)]
            npoly.append(p)
        
        return np.array(npoly)