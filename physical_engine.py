import numpy as np
import numba
import threading
import time

from solid import solid
from space import space
from graphical_engine import Graphical

class Physical():
    def __init__(self, space, objects=[], gravity=False, dsleep=0.1):
        self.objects = objects
        self.rigids = []
        self.gravity = gravity
        self.sleep_time = dsleep
        self.space = space

    def process_Force(self, obj, F, dt):
        mass = obj.state[2]
        dvx = F[0]*dt/mass*self.space.scale
        dvy = F[1]*dt/mass*self.space.scale
                    
        obj.state[1][0] += dvx
        obj.state[1][1] += dvy
        obj.state[0][0] += obj.state[1][0]*dt
        obj.state[0][1] += obj.state[1][1]*dt

    def process_gravity(self):
        while(True): # simulation Loop
            st = time.time()
            time.sleep(self.sleep_time)

            for obj in self.objects:
            
                if obj.state[0][1]>10:
                    dt = time.time()-st

                    fx = 0
                    fy = -self.gravity*obj.state[2]

                    self.process_Force(obj, [fx,fy], dt)




if __name__ == "__main__":
    S = space(size=(128, 512))
    box = solid(pos=[64, 500], ini_v=[0, 0], size=10, mass=100, color=(254, 129, 12))
    box2 = solid(pos=[64, 500], ini_v=[7, 10], size=10, mass=1, color=(12, 129, 254))

    P = Physical(S, objects=[box, box2], gravity=9, dsleep=1E-3)
    G = Graphical(S, objects=P.objects)

    T = threading.Thread(target=P.process_gravity)
    T.start()
    while(True): # Display loop
        G.draw()
        G.display()
        
    G.display(0)
