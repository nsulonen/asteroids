import pygame.draw
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x: int, y: int, radius: int) -> None:
        super().__init__(self, x, y)
        self.radius = radius
        self.position: tuple = (x, y)
        self.velocity = super().velocity

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt