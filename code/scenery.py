"""Scenery sprites are visual background items which do not interact with the player."""


from constant import GROUND_LEVEL, LEFT_TOWER, RIGHT_TOWER, SCREEN_HEIGHT
from pygame import sprite, Surface, image


class Sky(sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image = image.load("gfx/sky.png").convert()
        self.rect = self.image.get_rect(topleft=(0, 0))


class Field(sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image = image.load("gfx/field.png").convert()
        self.rect = self.image.get_rect(bottomleft=(0, SCREEN_HEIGHT))


class Bastion(sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image = image.load("gfx/bastion.png").convert_alpha()
        self.rect = self.image.get_rect(bottomleft=(LEFT_TOWER, GROUND_LEVEL))


class LeftTower(sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image = image.load("gfx/tower_left.png").convert()
        self.rect = self.image.get_rect(bottomright=(LEFT_TOWER, GROUND_LEVEL))


class RightTower(sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image = image.load("gfx/tower_right.png").convert()
        self.rect = self.image.get_rect(bottomleft=(RIGHT_TOWER, GROUND_LEVEL))


class Roof(sprite.Sprite):
    def __init__(self, midbottom) -> None:
        super().__init__()
        self.image = image.load("gfx/roof.png").convert_alpha()
        self.rect = self.image.get_rect(midbottom=midbottom)


class Road(sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image = image.load("gfx/road.png").convert()
        self.rect = self.image.get_rect(topleft=(0, GROUND_LEVEL))