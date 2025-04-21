import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        #update player movement
        player.update(dt)

        #set background color to black
        screen.fill("black")

        #draw the player
        player.draw(screen)

        #REFRESH
        pygame.display.flip()

        #Pause gameloop until 1/60th of a second has passed, devided that output with 1000 and save it in dt variable
        dt = game_clock.tick(60) / 1000


if __name__ == "__main__":
    main()