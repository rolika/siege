"""Scenery sprites are visual background items which do not interact with the player."""


from constant import BASTION_HEIGHT, BASTION_WIDTH, BLUE_SKY, GROUND_LEVEL, LEFT_TOWER, RIGHT_TOWER, ROAD_HEIGHT, ROOF_HEIGHT, ROOF_WIDTH, SCREEN_HEIGHT, SCREEN_WIDTH, TOWER_HEIGHT, TOWER_WIDTH
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
        self.image = image.load("gfx/tower.png").convert()
        self.rect = self.image.get_rect(bottomright=(LEFT_TOWER, GROUND_LEVEL))


class RightTower(sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image = image.load("gfx/tower.png").convert()
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