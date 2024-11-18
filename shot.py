import pygame
from circleshape import CircleShape
from constants import PLAYER_TURN_SPEED, SHOOT_RADIUS

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOOT_RADIUS)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)