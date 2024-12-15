import pygame
from pygame.locals import *
import vec
import math
import random

bodies = []
G = 6e-11
time_interval = 20e-4
HEIGHT = 700
WIDTH = 1000


class Body(pygame.sprite.Sprite):
    def __init__(self, velocity, mass, pos,radius, colour,name):
        super().__init__()
        self.surf = pygame.Surface((30, 30))
        self.surf.fill((128,255,40))
        self.rect = self.surf.get_rect(center = (10, 420))
        self.velocity = vec.Vector2(velocity)
        self.mass= mass
        self.pos = vec.Vector2(pos)
        self.radius = radius
        self.colour = colour
        self.next_pos = vec.Vector2(0,0)
        self.next_velocity = vec.Vector2(0,0)
        self.name = name
        self.force= vec.Vector2(0,0)
    
    def draw_circle(self,displaysurface):
        pygame.draw.circle(displaysurface, self.colour, self.pos, self.radius)

    def text_to_screen(self, size, displaysurface):
        if self.name == '':
            return 
        font = pygame.font.Font(pygame.font.get_default_font(), size)
        text = font.render(str(self.name), True, self.colour)
        displaysurface.blit(text, (self.pos[0]+self.radius, self.pos[1]+self.radius))
    
    def update_position(self):
        print(f"New position is {self.next_pos}")
        self.velocity = self.next_velocity
        self.pos = self.next_pos
        self.force = vec.Vector2(0,0)


def run_pygame(bodies,time_interval):
    pygame.init()
    vec = pygame.math.Vector2 
    
    FPS = 60
    FramePerSec = pygame.time.Clock()
    displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Simulation")
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                running = False
                break
        if not running:
            break

        displaysurface.fill((25,25,25))

        for counter, body in enumerate(bodies):
            body.draw_circle(displaysurface)
            body.text_to_screen(15,displaysurface)
            for second_body in bodies[counter:]:
                if body == second_body:
                    pass
                else:
                    force = find_force(G, body, second_body)
                    body.force += force
                    second_body.force -= force 
                    print(f"Force  on body {body.name} is {force}")
            acceleration = body.force/body.mass
            body.next_velocity = estimate(acceleration, body.velocity, time_interval)
            body.next_pos = estimate(body.next_velocity, body.pos, time_interval)
        
        for body in bodies:
            body.update_position()

        pygame.display.update()
        FramePerSec.tick(FPS)

def find_force(G, b1, b2):
    distance = b2.pos - b1.pos
    print(f"Distance is {distance}")
    print(f"Distance cubed is {abs(distance)**3}")
    print(G*b2.mass*b1.mass)
    return ((G*b2.mass*b1.mass)/abs(distance)**3)*distance

def estimate(initial_dt,initial, time_interval):
    return initial_dt*time_interval+initial

def abs(vector):
    return math.sqrt(vector.x**2+ vector.y**2)

#number_of_bodies = int(input("Enter the number of bodies: "))
planet = Body(velocity=(500,-500), mass=1, pos= (500,300), radius=10, colour= (255,255,255),name = '1')
bodies.append(planet) 
planet = Body(velocity=(0,0), mass=15.989e+17, pos=(WIDTH/2,HEIGHT/2), radius=25, colour= (255,255,0), name = 'Sun')     
bodies.append(planet)
planet = Body(velocity=(-500,300), mass = 100, pos= (700, 500), radius = 10, colour=(150,150,150), name = '2')
bodies.append(planet)

for x in range(4):
    planet = Body(velocity=(0,0), mass= 5, pos =(random.randint(0,800), random.randint(0,800)), radius=3, colour=(100,100,100), name = '')
    bodies.append(planet)


run_pygame(bodies, time_interval)


