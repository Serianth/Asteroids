import pygame
from constants import *

def main():
    pygame.init()
    print("Starting Asteroids!")
    print("Screen width: 1280")
    print("Screen height: 720")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    while True:
        # Event handling (makes close button work)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Fill screen with black
        screen.fill("black")
        # Refresh the display
        pygame.display.flip()
        
if __name__ == "__main__":
    main()
