import pygame
from pygame import SurfaceType
from pygame.time import Clock
from player import Player

from constants import *

def main() -> None:
    pygame.init()
    screen: SurfaceType = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock: Clock = pygame.time.Clock()
    dt: float = 0.0

    x: int = SCREEN_WIDTH / 2
    y: int = SCREEN_HEIGHT / 2
    player: Player = Player(x, y)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(color=(0,0,0))
        player.draw(screen)
        player.update(dt)

        pygame.display.flip()

        clock.tick(60)
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()