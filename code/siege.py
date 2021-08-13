"""Siege!
Siege! is a game about a lonely hero who defends his castle from attackers by throwing barrels at them.
Code is loosely based on ClearCode's Space Invaders tutorial found here: https://www.youtube.com/watch?v=o-6pADy5Mdg
"""


import pygame
from pygame import sprite, key
from pygame.locals import *
import sys
import shelve
from player import Player
from scenery import Sky, Field, Bastion, Roof, LeftTower, RightTower, Road
from enemy import Enemies
from ladder import Ladders
from text import HiScore, Score, Text
from constant import BASTION_HEIGHT, GROUND_LEVEL, HISCORE_FILENAME, SCREEN_SIZE, BLUE_SKY, SCREEN_WIDTH, State


class Siege:
    def __init__(self):
        self._restore_hiscore()
        left_tower = LeftTower()
        right_tower = RightTower()
        self._scenery = sprite.Group(Sky(), Field(), Bastion(), left_tower, right_tower, Roof(left_tower.rect.midtop), Roof(right_tower.rect.midtop), Road())
        self._ladders = Ladders()
        self._enemies = Enemies(self._ladders)
        self._hero = sprite.GroupSingle(Player())
        self._title = sprite.GroupSingle(Text("Siege!", "font/RubikMonoOne-Regular.ttf", 24, "darkslategrey", (SCREEN_WIDTH//2, 0)))
        self._score = sprite.GroupSingle(Score("font/Monofett-Regular.ttf", 24, "darkslategrey", (0, 0)))
        self._hiscore = sprite.GroupSingle(HiScore("font/Monofett-Regular.ttf", 24, "darkslategrey", (SCREEN_WIDTH, 0)))
        self._game_over = sprite.GroupSingle(Text("Game Over", "font/RubikMonoOne-Regular.ttf", 40, "darkslategrey", (SCREEN_WIDTH//2, GROUND_LEVEL - BASTION_HEIGHT//2)))
        self._press_space = sprite.GroupSingle(Text("Press space!", "font/RubikMonoOne-Regular.ttf", 24, "darkslategrey", (SCREEN_WIDTH//2, GROUND_LEVEL+10)))
    
    def _restore_hiscore(self):
        with shelve.open(HISCORE_FILENAME) as hs:
            self._hiscore_value = hs.get("hiscore", 0)
    
    def _save_hiscore(self):
        with shelve.open(HISCORE_FILENAME) as hs:
            hs["hiscore"] = self._hiscore_value
    
    def _draw_general_sprites(self, screen):
        self._scenery.draw(screen)
        self._hero.draw(screen)
        self._ladders.draw(screen)
        self._title.draw(screen)
        self._score.draw(screen)
        self._hiscore.draw(screen)
    
    def _draw_run_sprites(self, screen):
        self._hero.sprite.held_barrel.draw(screen)
        self._enemies.draw(screen)
        self._hero.sprite.thrown_barrels.draw(screen)
    
    def title(self, screen):
        self._enemies.reset()
        self._hero.sprite.reset()
        self._draw_general_sprites(screen)
        self._press_space.draw(screen)
        return State.TITLE

    def run(self, screen):
        # update sprites
        self._hero.update()
        self._enemies.update(self._hero.sprite.thrown_barrels)
        self._score.update(self._enemies.score)
        if self._enemies.score > self._hiscore_value:
            self._hiscore_value = self._enemies.score
        self._hiscore.update(self._hiscore_value)

        if self._enemies.conquer:
            self._save_hiscore()
            return State.OVER
        
        # draw sprites
        self._draw_general_sprites(screen)
        self._draw_run_sprites(screen)

        return State.RUN
    
    def over(self, screen):
        self._draw_general_sprites(screen)
        self._game_over.draw(screen)
        self._press_space.draw(screen)
        return State.OVER


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    clock = pygame.time.Clock()
    game = Siege()
    state = State.TITLE

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    if state == State.TITLE:
                        state = State.RUN
                    elif state == State.OVER:
                        state = State.TITLE
        
        screen.fill(BLUE_SKY)

        if state == State.TITLE:
            state = game.title(screen)

        if state == State.RUN:
            state = game.run(screen)
        
        if state == State.OVER:
            state = game.over(screen)

        pygame.display.flip()
        clock.tick(60)
