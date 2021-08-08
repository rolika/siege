"""Enemies use ladders to climb the bastion. The ladders are evenly distributed over the bastion."""


from pygame import sprite, Surface
from constant import FIRST_LADDER_LEFT_POS, GROUND_LEVEL, LADDERS, LADDER_HEIGHT, LADDER_WIDTH


class Ladder(sprite.Sprite):
    def __init__(self, x) -> None:
        super().__init__()
        self.image = Surface((LADDER_WIDTH, LADDER_HEIGHT))
        self.image.fill("grey")
        self.rect = self.image.get_rect(midbottom=(x, GROUND_LEVEL))


class Ladders(sprite.Group):
    def __init__(self):
        super().__init__()
        for n in range(LADDERS):
            self.add(Ladder(FIRST_LADDER_LEFT_POS + (LADDER_WIDTH+10)*n))