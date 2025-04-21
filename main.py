import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        #set background color to black
        screen.fill("black")

        #REFRESH
        pygame.display.flip()

        #Pause gameloop until 1/60th of a second has passed, devided that output with 1000 and save it in dt variable
        dt = game_clock.tick(60) / 1000


if __name__ == "__main__":
    main()