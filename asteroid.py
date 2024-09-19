import pygame
import random

from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(random.uniform(-1, 1), random.uniform(-1, 1))

    def draw(self, screen):
        pygame.draw.circle(screen, "blue", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def rotate(self, dt):
        self.rotation += ASTEROID_ROTATE_SPEED * dt

    def split(self):
        self.kill()

        random_angle = random.uniform(20, 50)
        velocity1 = self.velocity.rotate(random_angle)
        velocity2 = self.velocity.rotate(-random_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        if new_radius <= 0:
            return 
        
        velocity1 *= 1.2
        velocity2 *= 1.2
        asteroid1 = Asteroid(self.position, velocity1, new_radius)
        asteroid1.velocity = velocity1
        asteroid2 = Asteroid(self.position, velocity2, new_radius)
        asteroid2.velocity = velocity2
        return [asteroid1, asteroid2]