import pygame
from asteroid import Asteroid
from constants import *
from player import *
from asteroidfield import *
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0,0,0))
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game over!")
                exit()

        for d in drawable:
            d.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000.0

if __name__ == "__main__":
    main()
