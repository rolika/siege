"""Siege
Siege is a game about a lonely hero who defends his castle from attackers by throwing barrels at them.
Code is loosely based on ClearCode's Space Invaders tutorial found here: https://www.youtube.com/watch?v=o-6pADy5Mdg
"""


import pygame
from pygame import sprite
import sys
from player import Player


class Siege:
    def __init__(self):
        self._hero = sprite.GroupSingle(Player((400, 200)))

    def run(self, screen):
        self._hero.update()
        self._hero.draw(screen)
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
        
        screen.fill((71, 93, 240))  # blue sky
        game.run(screen)

        pygame.display.flip()
        clock.tick(60)
