from circleshape import CircleShape
import pygame
from constants import LINE_WIDTH,ASTEROID_MIN_RADIUS
from logger import log_event
import random
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    def draw(self,screen):
        pygame.draw.circle(screen,"white",self.position,self.radius ,LINE_WIDTH)
    def update(self,dt):
        self.position += dt * self.velocity
    def split(self):
        self.kill()
        if self.radius <=ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        random.uniform(0,1)
