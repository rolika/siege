"""The player in Siege! controlls a hero, who
- is placed on the bastion of his castle
- can move left and right, constrained by two towers on both ends of his bastion
- can pick up barrels at the towers, one at a time
- can toss barrels downwards at its enemies, again, one at a time"""


from pygame import sprite, Surface, key  # this way, IntelliSense works in VS Code
from pygame.locals import *


class Player(sprite.Sprite):
    def __init__(self, pos) -> None:
        super().__init__()
        self.image = Surface((20, 60))
        self.image.fill("white")
        self.rect = self.image.get_rect(midbottom=pos)
        self._speed = 5
        self._left_boundary = 200
        self._right_boundary = 600
    
    def _get_input(self):
        keys = key.get_pressed()

        if keys[K_RIGHT]:
            self.rect.x += self._speed
        elif keys[K_LEFT]:
            self.rect.x -= self._speed
    
    def _constrain(self):
        if self.rect.left <= self._left_boundary:
            self.rect.left = self._left_boundary
        elif self.rect.right >= self._right_boundary:
            self.rect.right = self._right_boundary
    
    def update(self):
        self._get_input()
        self._constrain()
