"""Siege!
Siege! is a game about a lonely hero who defends his castle from attackers by throwing barrels at them.
Code is loosely based on ClearCode's Space Invaders tutorial found here: https://www.youtube.com/watch?v=o-6pADy5Mdg
"""


import pygame
from pygame import sprite
import sys
from player import Player
from enemy import Enemy
from constant import SCREEN_SIZE, BLUE_SKY


class Siege:
    def __init__(self):
        self._hero = sprite.GroupSingle(Player())
        self._enemies = sprite.Group(Enemy())

    def run(self, screen):
        # update sprites
        self._hero.update()
        self._enemies.update()

        # draw sprites
        self._hero.sprite.held_barrel.draw(screen)
        self._hero.sprite.thrown_barrels.draw(screen)
        self._hero.draw(screen)
        self._enemies.draw(screen)


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    clock = pygame.time.Clock()
    game = Siege()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        screen.fill(BLUE_SKY)
        game.run(screen)

        pygame.display.flip()
        clock.tick(60)
