import random
import pygame.draw
from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius) -> None:
        super().__init__(x, y, radius)
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        rand_angle = random.uniform(20, 50)
        vector1 = self.velocity.rotate(rand_angle)
        vector2 = self.velocity.rotate(-rand_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        split1 = Asteroid(self.position, self.position, new_radius)
        split2 = Asteroid(self.position, self.position, new_radius)

        split1.velocity = vector1 * 1.2
        split2.velocity = vector2 * 1.2