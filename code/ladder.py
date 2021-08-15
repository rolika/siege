"""Enemies use ladders to climb the bastion. The ladders are evenly distributed over the bastion."""


from pygame import sprite, image
from constant import FIRST_LADDER_LEFT_POS, GROUND_LEVEL, LADDERS, LADDER_HEIGHT, LADDER_WIDTH, SPACE_BETWEEN_LADDERS


class Ladder(sprite.Sprite):
    def __init__(self, x) -> None:
        super().__init__()
        self.image = image.load("gfx/ladder.png").convert_alpha()
        self.rect = self.image.get_rect(midbottom=(x, GROUND_LEVEL))


class Ladders(sprite.Group):
    def __init__(self):
        super().__init__()
        for n in range(LADDERS):
            self.add(Ladder(FIRST_LADDER_LEFT_POS + SPACE_BETWEEN_LADDERS*n))
    
    def least_populated(self, enemies):
        ladders = list(self)
        ladders.sort(key=lambda ladder: ladder.rect.collidelist(enemies))