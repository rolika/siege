"""Scenery sprites are visual background items which do not interact with the player."""


from constant import BASTION_HEIGHT, BASTION_WIDTH, BLUE_SKY, GROUND_LEVEL, LEFT_TOWER, RIGHT_TOWER, ROAD_HEIGHT, ROOF_HEIGHT, ROOF_WIDTH, SCREEN_HEIGHT, SCREEN_WIDTH, TOWER_HEIGHT, TOWER_WIDTH
from pygame import sprite, Surface


class Sky(sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image = Surface((SCREEN_WIDTH, SCREEN_HEIGHT//2))
        self.image.fill(BLUE_SKY)
        self.rect = self.image.get_rect(topleft=(0, 0))


class Field(sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image = Surface((SCREEN_WIDTH, SCREEN_HEIGHT//2))
        self.image.fill("forestgreen")
        self.rect = self.image.get_rect(bottomleft=(0, SCREEN_HEIGHT))


class Bastion(sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image = Surface((BASTION_WIDTH, BASTION_HEIGHT))
        self.image.fill("sienna")
        self.rect = self.image.get_rect(bottomleft=(LEFT_TOWER, GROUND_LEVEL))


class LeftTower(sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image = Surface((TOWER_WIDTH, TOWER_HEIGHT))
        self.image.fill("salmon")
        self.rect = self.image.get_rect(bottomright=(LEFT_TOWER, GROUND_LEVEL))


class RightTower(sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image = Surface((TOWER_WIDTH, TOWER_HEIGHT))
        self.image.fill("salmon")
        self.rect = self.image.get_rect(bottomleft=(RIGHT_TOWER, GROUND_LEVEL))


class Roof(sprite.Sprite):
    def __init__(self, midbottom) -> None:
        super().__init__()
        self.image = Surface((ROOF_WIDTH, ROOF_HEIGHT))
        self.image.fill("bisque")
        self.rect = self.image.get_rect(midbottom=midbottom)


class Road(sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image = Surface((SCREEN_WIDTH, ROAD_HEIGHT))
        self.image.fill("sandybrown")
        self.rect = self.image.get_rect(topleft=(0, GROUND_LEVEL))