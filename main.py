import pygame
from constants import *

def main():
    pygame.init()
    print("Starting asteroids!")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Closing asteroids!")
                return
        screen.fill(0)
        pygame.display.flip()
    

if __name__ == "__main__":
    main()
