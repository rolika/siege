"""The player in Siege! controlls a hero, who
- is placed on the bastion of his castle
- can move left and right, constrained by two towers on both ends of his bastion
- can pick up barrels at the towers, one at a time
- can throw barrels downwards at its enemies, again, one at a time"""


from pygame import sprite, Surface, key  # this way, IntelliSense works in VS Code
from pygame.locals import *
from barrel import Barrel
from constant import PLAYER_STEP, PLAYER_START_POS, LEFT_TOWER, RIGHT_TOWER


class Player(sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image = Surface((20, 60))
        self.image.fill("white")
        self.rect = self.image.get_rect(midbottom=PLAYER_START_POS)

        self._can_throw = True
        self._held_barrel = sprite.GroupSingle()
        self._thrown_barrels = sprite.Group()
    
    @property
    def held_barrel(self):
        return self._held_barrel
    
    @property
    def thrown_barrels(self):
        return self._thrown_barrels
    
    def _get_input(self):
        keys = key.get_pressed()

        if keys[K_RIGHT]:
            self.rect.x += PLAYER_STEP
        elif keys[K_LEFT]:
            self.rect.x -= PLAYER_STEP
        
        if keys[K_SPACE] and self._held_barrel.sprite and self._can_throw:
            self._throw_barrel()
    
    def _constrain_movement(self):  # and pick up a new barrel
        if self.rect.left <= LEFT_TOWER:
            self.rect.left = LEFT_TOWER
            self._pick_up_barrel()
        elif self.rect.right >= RIGHT_TOWER:
            self.rect.right = RIGHT_TOWER
            self._pick_up_barrel()
    
    def _constrain_barrel_throw(self):
        if self.rect.left > LEFT_TOWER + PLAYER_STEP and self.rect.right < RIGHT_TOWER - PLAYER_STEP:
            self._can_throw = True
    
    def _pick_up_barrel(self):
        self._barrel = Barrel(self.rect.midtop)
        self._held_barrel.add(self._barrel)
        self._can_throw = False
    
    def _throw_barrel(self):
        self._held_barrel.empty()
        self._thrown_barrels.add(self._barrel)
    
    def update(self):
        self._get_input()
        self._constrain_barrel_throw()  # this should be done before constraining the movement
        self._constrain_movement()
        self._held_barrel.update(player_pos=self.rect.midtop)
        self._thrown_barrels.update()
