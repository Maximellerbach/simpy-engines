import numpy as np

def resize_poly(poly, size):
    return list(np.multiply(poly, size))
    
def adjust_pos(pos, mins):
    return list(np.subtract(pos, mins))

class solid():
    def __init__(self, space, poly=[[-0.5, -0.5], [-0.5, 0.5], [0.5, 0.5], [0.5, -0.5]], pos=[0,0], ini_v=[0, 0], mass=1, size=1, thrust=0, color=(255,255,255), rigid=False):
        self.space_bounds = space.bounds
        self.space_scale = space.scale
        

        if size!=[1,1]:
            poly = resize_poly(poly, [size[0]*self.space_scale, size[1]*self.space_scale])

        self.poly = poly
        self.size = size

        # pos = adjust_pos(pos, [self.space_bounds[0], self.space_bounds[2]])

        heading = [0, 1]
        self.state = [pos, ini_v, mass, heading] # [[x, y], [vx, vy], m]
        self.color = color
        self.rigid = rigid
        self.thrust = thrust

        self.dpos = [0, 0]
        self.minmax = (self.get_minp(), self.get_maxp())

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

    def check_overlap(self, objects):
        box_min, box_max = self.minmax
        for obj in objects:
            return

    def translate(self, iterable, coords):
        x, y = coords

        translated = []
        for pt in iterable:
            p = [int(pt[0]+x-self.space_bounds[0]), int(pt[1]+y-self.space_bounds[2])]
            translated.append(p)
        
        return np.array(translated)

    def translate_box(self):
        return self.translate(self.minmax, self.state[0])

    def translate_poly(self):
        return self.translate(self.poly, self.state[0])
