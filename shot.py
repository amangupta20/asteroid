from circleshape import CircleShape
from constants import SHOT_RADIUS,LINE_WIDTH
import pygame
class Shot(CircleShape):
    def __init__(self,other):
        super().__init__(other.position.x,other.position.y,SHOT_RADIUS)
    def draw(self,screen):
        pygame.draw.circle(screen,"white",self.position,self.radius ,LINE_WIDTH)
    def update(self,dt):
        self.position += dt * self.velocity

