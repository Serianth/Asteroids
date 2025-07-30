import sys
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    pygame.init()
    print("Starting Asteroids!")
    print("Screen width: 1280")
    print("Screen height: 720")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    Shot.containers =(updatable,drawable,bullets)
    AsteroidField.containers = (updatable,)
    Asteroid.containers = (updatable,drawable,asteroids)
    Player.containers = (updatable,drawable)
    player = Player(SCREEN_WIDTH / 2,SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

    while True:
        # Event handling (makes close button work)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)
        for asteroid in asteroids:
            if player.collision_detection(asteroid):
                sys.exit(print(f"Game over!"))
        for asteroid in asteroids:
            for bullet in bullets:
                if bullet.collision_detection(asteroid):
                    bullet.kill()
                    asteroid.split()
        # Fill screen with black
        screen.fill("black")
        for object in drawable:
            object.draw(screen)
        # Refresh the display
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
