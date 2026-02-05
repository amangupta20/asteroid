import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state,log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys
from shot import Shot
def main():
    pygame.init()
def main():
    shots=pygame.sprite.Group()
    updatable=pygame.sprite.Group()
    drawable=pygame.sprite.Group()
    Player.containers=(updatable,drawable)
    asteroids=pygame.sprite.Group()
    Asteroid.containers=(asteroids,drawable,updatable)
    AsteroidField.containers=(updatable)
    Shot.containers=(shots,drawable,updatable            )
    astero=AsteroidField()
    pygame.init()
    clk=pygame.time.Clock()
    dt=0
    ver = pygame.version.ver
    play=Player(SCREEN_WIDTH//2, SCREEN_HEIGHT//2)
    print("Starting Asteroids with pygame version:", ver)
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collides_with(play):
                log_event("player_hit")
                print("Game Over!")
                sys.exit()

        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        pygame.display.flip()
        dt=clk.tick(60)/1000.0
if __name__ == "__main__":
    main()
