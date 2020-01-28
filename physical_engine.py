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

        # print(obj.state[1])

        obj.dpos = np.multiply(obj.state[1], dt)

        obj.state[0][0] += obj.dpos[0]
        obj.state[0][1] += obj.dpos[1]

    def attraction(self, obj, attr_force = 9.87):
        return [0, -1*attr_force*obj.state[2]]

    def friction(self, obj, fric_res = 0.1, v = [0, 0]):
        return [1/2*obj.state[1][0]*fric_res*obj.size, 1/2*obj.state[1][1]*fric_res*obj.size]

    # TODO: collision + rigid bodys


    def simulate_gravity(self):
        while(True): # simulation Loop
            time.sleep(self.sleep_time)

            for obj in self.objects:

                F = np.zeros(2)
                F += self.attraction(obj, attr_force=self.gravity)
                F -= self.friction(obj, fric_res=0.1)

                self.apply_Force(obj, F, self.sleep_time)


if __name__ == "__main__":
    S = space(bounds=(-128, 256, 0, 768), scale=5)
    box = solid(S, pos=[60, 750], ini_v=[0, -20], size=5, mass=10, color=(254, 129, 12))
    box2 = solid(S, pos=[75, 750], ini_v=[0, 0], size=5, mass=100, color=(12, 129, 254))

    P = Physical(S, objects=[box, box2], gravity=9, dsleep=1E-3)
    G = Graphical(S, objects=P.objects)

    T = threading.Thread(target=P.simulate_gravity)
    T.start()
    while(True): # Display loop
        G.draw()
        G.display()
        
    G.display(0)
