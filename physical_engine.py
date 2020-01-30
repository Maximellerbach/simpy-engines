import numpy as np
import numba
import threading
import time

from solid import *
from space import *
from graphical_engine import Graphical

class Physical():
    def __init__(self, space, objects=[], dsleep=0.1):
        self.objects = objects
        self.rigids = []
        self.sleep_time = dsleep
        self.space = space
        self.gravity = self.space.gravity

    def apply_Force(self, obj, F, dt):
        mass = obj.state[2]
        dvx = 1/2*F[0]*dt/mass
        dvy = 1/2*F[1]*dt/mass
                    
        obj.state[1][0] += dvx
        obj.state[1][1] += dvy


        obj.dpos = [obj.state[1][0]*dt*self.space.scale, obj.state[1][1]*dt*self.space.scale]

        obj.state[0][0] = obj.state[0][0]+obj.dpos[0]
        obj.state[0][1] = obj.state[0][1]+obj.dpos[1]


    def attraction(self, obj, attr_force = 9.87):
        return [0, -1*attr_force*obj.state[2]]

    def friction(self, obj, fric_res = 0.1, v = [0, 0]):
        return [1/2*obj.state[1][0]**2*fric_res*obj.size[1], 1/2*obj.state[1][1]**2*fric_res*obj.size[0]]

    def thrust(self, obj):
        return [0, obj.thrust]

    # TODO: collision + rigid bodys

    def simulate_gravity(self):
        while(True): # simulation Loop
            time.sleep(self.sleep_time)        
            for obj in self.objects:

                if obj.rigid==False:
                    F = np.zeros(2)
                    F += self.attraction(obj, attr_force=self.gravity)
                    F += self.thrust(obj)
                    F += self.friction(obj, fric_res=0.1)
                    
                    self.apply_Force(obj, F, self.sleep_time)
                else:
                    obj.check_overlap(self.objects)



if __name__ == "__main__":
    S = space(bounds=(-128, 128, 0, 768), scale=5, gravity=9)
    box = solid(S, pos=[-5, 750], ini_v=[0, 0], size=[0.07, 0.05], mass=0.040, color=(254, 129, 12))
    box2 = solid(S, pos=[5, 750], ini_v=[0, 0], size=[1.7, 0.4], mass=80, color=(12, 129, 254))

    P = Physical(S, objects=[box, box2], dsleep=0.02)
    G = Graphical(S, objects=P.objects)

    T = threading.Thread(target=P.simulate_gravity)
    T.start()
    while(True): # Display loop
        G.draw()
        G.display(n=33)
        
    G.display(0)
