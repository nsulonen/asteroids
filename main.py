import pygame
from pygame import SurfaceType
from pygame.time import Clock

from constants import *

def main() -> None:
    pygame.init()
    screen: SurfaceType = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock: Clock = pygame.time.Clock()
    dt: float = 0.0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(color=(0,0,0))

        pygame.display.flip()

        clock.tick(60)
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()