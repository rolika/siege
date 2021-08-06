"""Siege
Siege is a game about a lonely hero who defends his castle from attackers by hurling barrels at them.
Code is loosely based on ClearCode's Space Invaders tutorial found here: https://www.youtube.com/watch?v=o-6pADy5Mdg
"""


import pygame, sys


class Siege:
    def __init__(self):
        pass

    def run(self):
        pass
        # update all sprite groups
        # draw all sprite groups


if __name__ == "__main__":
    pygame.init()
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    game = Siege()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        screen.fill((30, 30, 30))
        game.run()

        pygame.display.flip()
        clock.tick(60)
