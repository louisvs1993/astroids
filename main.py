import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        #update player movement
        updatable.update(dt)

        for obj in asteroids:
            if obj.collision(player):
                print("Game over!")
                sys.exit()

        #set background color to black
        screen.fill("black")

        #draw the player
        for obj in drawable:
            obj.draw(screen)

        #REFRESH SCREEN
        pygame.display.flip()

        #Pause gameloop until 1/60th of a second has passed, devided that output with 1000 and save it in dt variable
        dt = game_clock.tick(60) / 1000


if __name__ == "__main__":
    main()