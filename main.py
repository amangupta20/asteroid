import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player
def main():
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
        play.update(dt)
        screen.fill("black")
        play.draw(screen)
        pygame.display.flip()
        pygame.display.flip()
        dt=clk.tick(60)/1000.0
if __name__ == "__main__":
    main()
