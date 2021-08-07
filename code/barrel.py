"""The barrel in Siege! is the player's weapon.
Barrels can be picked up at the towers.
When picked up, the player holds it above his head, and moves along with the player sprite.
When thrown away, the barrel starts to move downwards.
If the barrel hits an enemy, the player gets scored. If the barrel hits he ground, it breaks."""


from pygame import sprite, Surface
from constant import LOWER_BOUNDARY, BARREL_SPEED


class Barrel(sprite.Sprite):
    def __init__(self, pos) -> None:
        super().__init__()
        self.image = Surface((40, 20))
        self.image.fill("brown")
        self.rect = self.image.get_rect(midbottom=pos)
    
    def update(self, *args, **kwargs) -> None:
        player_pos = kwargs.get("player_pos", None)
        if player_pos:  # move along with the player
            self.rect.midbottom = player_pos
        else:  # barrel is thrown away, move down
            self.rect.y += BARREL_SPEED
            if self.rect.y >= LOWER_BOUNDARY:
                self.kill()