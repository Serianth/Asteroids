import pygame
from constants import *
from player import *

def main():
    pygame.init()
    print("Starting Asteroids!")
    print("Screen width: 1280")
    print("Screen height: 720")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH / 2,SCREEN_HEIGHT / 2)

    while True:
        # Event handling (makes close button work)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        
        # Fill screen with black
        screen.fill("black")
        player.draw(screen)
        # Refresh the display
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
