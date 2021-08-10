"""In Siege!, enemies are coming in at ground level, from left or right.
Once they reach the bastion, they start to climb up the walls. The wall is divided into 7 lanes.
The attacker chooses the nearest ladder with the least other attackers already on it at spawn time."""


from pygame import sprite, Surface
import random
from constant import ENEMY_CLIMBING_SPEED, ENEMY_WALKING_SPEED, GROUND_LEVEL, SCREEN_WIDTH


class Enemy(sprite.Sprite):
    def __init__(self, ladders) -> None:
        super().__init__()
        random.seed()
        self.image = Surface((20, 50))
        self.image.fill("red")
        self._ladder = self._choose(ladders)
        self._spawn()

    def _spawn(self):
        direction = random.choice((-1, 1))  # -1: right side, 1: left side
        side = SCREEN_WIDTH if direction == -1 else 0
        self.rect = self.image.get_rect(midbottom=(side, GROUND_LEVEL))
        self._speed = (ENEMY_WALKING_SPEED*direction, 0)
    
    def _choose(self, ladders):
        return random.choice(list(ladders))

    def _climb(self):
        self._speed = (0, ENEMY_CLIMBING_SPEED)
    
    def _check_ladder(self):
        return self._ladder.rect.contains(self.rect)
    
    def update(self, *args, **kwargs) -> None:
        self.rect.x += self._speed[0]
        self.rect.y += self._speed[1]
        if self._check_ladder():
            self._climb()
