import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    print("Starting asteroids!")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable

    bullet = pygame.sprite.Group()
    Shot.containers = (bullet, updatable, drawable)

    dt = 0
    triangle = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Closing asteroids!")
                return
        screen.fill(0)
        for obj in updatable:
            obj.update(dt)
        for obj in drawable:
            obj.draw(screen)
        for obj in asteroids:
            if triangle.collision(obj):
                print("Game over!")
                return
            for shot in bullet:
                if obj.collision(shot):
                    shot.kill()
                    obj.split()

        pygame.display.flip()
        dt = pygame.time.Clock().tick(60) / 1000
    

if __name__ == "__main__":
    main()
