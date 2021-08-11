"""Siege!
Siege! is a game about a lonely hero who defends his castle from attackers by throwing barrels at them.
Code is loosely based on ClearCode's Space Invaders tutorial found here: https://www.youtube.com/watch?v=o-6pADy5Mdg
"""


from random import random
import pygame
from pygame import sprite
import sys
from player import Player
from scenery import Field, Bastion, Roof, LeftTower, RightTower, Road
from enemy import Enemies
from ladder import Ladders
from constant import SCREEN_SIZE, BLUE_SKY


class Siege:
    def __init__(self):
        left_tower = LeftTower()
        right_tower = RightTower()
        self._scenery = sprite.Group(Field(), Bastion(), left_tower, right_tower, Roof(left_tower.rect.midtop), Roof(right_tower.rect.midtop), Road())
        self._ladders = Ladders()
        self._enemies = Enemies(self._ladders)
        self._hero = sprite.GroupSingle(Player())

    def run(self, screen):
        # update sprites
        self._hero.update()
        self._enemies.update()

        if self._enemies.conquer:
            pygame.quit()
            sys.exit("Your castle has been conquered!")
        
        # draw sprites
        self._scenery.draw(screen)
        self._hero.draw(screen)
        self._hero.sprite.held_barrel.draw(screen)
        self._ladders.draw(screen)
        self._enemies.draw(screen)
        self._hero.sprite.thrown_barrels.draw(screen)


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
