import numpy as np
import numba
import threading
import time

from solid import *
from space import *
from graphical_engine import Graphical

class Physical():
    def __init__(self, space, objects=[], gravity=False, dsleep=0.1):
        self.objects = objects
        self.rigids = []
        self.gravity = gravity
        self.sleep_time = dsleep
        self.space = space

    def apply_Force(self, obj, F, dt):
        mass = obj.state[2]
        dvx = F[0]*dt/mass*self.space.scale
        dvy = F[1]*dt/mass*self.space.scale
                    
        obj.state[1][0] += dvx
        obj.state[1][1] += dvy
        obj.state[0][0] += obj.state[1][0]*dt
        obj.state[0][1] += obj.state[1][1]*dt

    def attraction(self, obj, attr_force = 9.87, u=[0, -1]):
        return np.multiply(u, attr_force*obj.state[2])


    def simulate_gravity(self):
        while(True): # simulation Loop
            st = time.time()
            time.sleep(self.sleep_time)

            for obj in self.objects:
                dt = time.time()-st

                F = self.attraction(obj, attr_force=self.gravity)
                self.apply_Force(obj, F, dt)


if __name__ == "__main__":
    S = space(bounds=(-128, 256, 0, 512))
    box = solid(S, pos=[64, 500], ini_v=[0, 0], size=10, mass=100, color=(254, 129, 12))
    box2 = solid(S, pos=[64, 500], ini_v=[7, -1], size=10, mass=1, color=(12, 129, 254))

    P = Physical(S, objects=[box, box2], gravity=9, dsleep=1E-5)
    G = Graphical(S, objects=P.objects)

    T = threading.Thread(target=P.simulate_gravity)
    T.start()
    while(True): # Display loop
        G.draw()
        G.display()
        
    G.display(0)
