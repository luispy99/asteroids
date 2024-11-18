import pygame
from constants import *

def main():
    pygame.init()
    print("Starting asteroids!")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Closing asteroids!")
                return
        screen.fill(0)
        pygame.display.flip()
        dt = pygame.time.Clock().tick(60) / 1000
    

if __name__ == "__main__":
    main()
