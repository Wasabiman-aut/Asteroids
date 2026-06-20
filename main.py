from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state, log_event
from player import *
from asteroid import *
from asteroidfield import AsteroidField
import pygame
import sys


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0.0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Shot.containers= (shots, updatable, drawable)
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = updatable
    Asteroid_Field = AsteroidField()

    y = SCREEN_HEIGHT / 2
    x = SCREEN_WIDTH /2
    player_instance = Player(x,y)


    while True:
        
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)
        for thing in drawable:
            thing.draw(screen)
        for asteroid_hit in asteroids:
            if player_instance.collides_with(asteroid_hit):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            for shot in shots:
                if asteroid_hit.collides_with(shot):
                    asteroid_hit.kill()
                    shot.kill()
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        
        



if __name__ == "__main__":
    main()
