"""The barrel in Siege! is the player's weapon.
Barrels can be picked up at the towers.
When picked up, the player holds it above his head, and moves along with the player sprite.
When thrown away, the barrel starts to move downwards.
If the barrel hits an enemy, the player gets scored. If the barrel hits he ground, it breaks."""


from pygame import sprite, Surface

class Barrel(sprite.Sprite):
    def __init__(self, pos) -> None:
        super().__init__()
        self.image = Surface((40, 20))
        self.image.fill("brown")
        self.rect = self.image.get_rect(midbottom=pos)
        self._held = True
    
    def update(self, *args, **kwargs) -> None:
        if self._held:
            pass  # move horizontally with the player
        else:
            pass  # move downwards