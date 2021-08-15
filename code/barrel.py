"""The barrel in Siege! is the player's weapon.
Barrels can be picked up at the towers.
When picked up, the player holds it above his head, and moves along with the player sprite.
When thrown away, the barrel starts to move downwards.
If the barrel hits an enemy, the player gets scored. If the barrel hits he ground, it breaks."""


import random
from pygame import sprite, image
from constant import BARREL_BONUS, GROUND_LEVEL, BARREL_SPEED


class Barrel(sprite.Sprite):

    barrel = image.load("gfx/barrel.png")
    chair = image.load("gfx/chair.png")
    rock = image.load("gfx/rock.png")
    trove = image.load("gfx/trove.png")
    throwables = (barrel, chair, rock, trove)

    def __init__(self, pos) -> None:
        super().__init__()
        self.image = random.choice(Barrel.throwables).convert_alpha()
        self.rect = self.image.get_rect(midbottom=pos)
        self._hit = 0
    
    @property
    def bonus(self):
        return self._hit * BARREL_BONUS
    
    def hit(self):
        self._hit += 1
    
    def update(self, *args, **kwargs) -> None:
        player_pos = kwargs.get("player_pos", None)
        if player_pos:  # move along with the player
            self.rect.midbottom = player_pos
        else:  # barrel is thrown away, move down
            self.rect.y += BARREL_SPEED
            if self.rect.y >= GROUND_LEVEL:
                self.kill()