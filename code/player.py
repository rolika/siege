"""The player in Siege! controlls a hero, who
- is placed on the bastion of his castle
- can move left and right, constrained by two towers on both ends of his bastion
- can pick up barrels at the towers, one at a time
- can throw barrels downwards at its enemies, again, one at a time"""


from pygame import sprite, Surface, key  # this way, IntelliSense works in VS Code
from pygame.locals import *


class Player(sprite.Sprite):
    def __init__(self, pos) -> None:
        super().__init__()
        self.image = Surface((20, 60))
        self.image.fill("white")
        self.rect = self.image.get_rect(midbottom=pos)
        self._step = 5
        self._left_boundary = 200
        self._right_boundary = 600
        self._has_barrel = True
        self._can_throw = True
    
    def _get_input(self):
        keys = key.get_pressed()

        if keys[K_RIGHT]:
            self.rect.x += self._step
        elif keys[K_LEFT]:
            self.rect.x -= self._step
        
        if keys[K_SPACE] and self._has_barrel and self._can_throw:
            self._throw_barrel()
    
    def _constrain_movement(self):  # and pick up a new barrel
        if self.rect.left <= self._left_boundary:
            self.rect.left = self._left_boundary
            self._has_barrel = True
            self._can_throw = False
        elif self.rect.right >= self._right_boundary:
            self.rect.right = self._right_boundary
            self._has_barrel = True
            self._can_throw = False
    
    def _constrain_barrel_throw(self):
        if self.rect.left > self._left_boundary + self._step:
            self._can_throw = True
        elif self.rect.right < self._right_boundary - self._step:
            self._can_throw = True
    
    def _throw_barrel(self):
        print("barrel thrown")
        self._has_barrel = False
    
    def update(self):
        self._get_input()
        self._constrain_barrel_throw()  # this should be done before constraining the movement
        self._constrain_movement()