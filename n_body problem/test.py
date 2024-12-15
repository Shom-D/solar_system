import time
import numpy as np
import math
import OpenGL
import vec

force = 0
force2= 0
forces= [0,0,0,0,0]

class Rect():
    def __init__(self, pos):
        self.starting_pos = vec.Vector2(pos)
        self.dimensions = vec.Vector2(dimensions)
        self.end_pos = self.starting_pos + self.dimensions
    
    def collidepoint(self, position):
        if self.starting_pos<position<self.dimensions:
            return True
        else:
            return False
        
class Vector():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def add(self, v2):
        return vec.Vector2(self.x+v2.x, self.y+v2.y)

    
v1 = Vector(1,0)
v2 = Vector(4,2)
print(v1.add(v2))
    


for x, f in enumerate(forces):
    for f2 in forces[x:]:
        force+=1
        forces[x]-=1
    forces[x]= force

print(forces)
        

