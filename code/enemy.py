"""In Siege!, enemies are coming in at ground level, from left or right.
Once they reach the bastion, they start to climb up the walls. The wall is divided into 7 lanes.
The attacker chooses the nearest ladder with the least other attackers already on it at spawn time."""


from pygame import sprite, Surface
import random
from constant import BASTION_LEVEL, ENEMY_CLIMBING_SPEED, ENEMY_FALLING_SPEED, ENEMY_SPAWN_INTERVAL, ENEMY_WALKING_SPEED, GROUND_LEVEL, SCREEN_WIDTH


class Enemy(sprite.Sprite):
    def __init__(self, ladder) -> None:
        super().__init__()
        random.seed()
        self.image = Surface((20, 50))
        self.image.fill(random.choice(("red", "green", "blue", "orange")))
        self._ladder = ladder
        self._falling = False
        self._spawn()
    
    @property
    def is_above_bastion(self):
        return self.rect.centery < BASTION_LEVEL

    def _spawn(self):
        direction = random.choice((-1, 1))  # -1: right side, 1: left side
        side = SCREEN_WIDTH if direction == -1 else 0
        self.rect = self.image.get_rect(midbottom=(side, GROUND_LEVEL))
        self._speed = (ENEMY_WALKING_SPEED*direction, 0)

    def _climb(self):
        self._speed = (0, ENEMY_CLIMBING_SPEED)
    
    def fall(self):
        self._speed = (0, ENEMY_FALLING_SPEED)
        self._falling = True

    def _check_ladder(self):
        return not self._falling and self._ladder.rect.contains(self.rect)

    def update(self, *args, **kwargs) -> None:
        self.rect.x += self._speed[0]
        self.rect.y += self._speed[1]
        if self._check_ladder():
            self._climb()
        if self.rect.y >= GROUND_LEVEL:
            self.kill()


class Enemies(sprite.Group):
    def __init__(self, ladders) -> None:
        super().__init__()
        self._ladders = tuple(ladders)
        self._spawn_interval = 0
    
    @property
    def conquer(self):
        return any([enemy.is_above_bastion for enemy in self.sprites()])

    def _reset_timer(self):
        self._spawn_interval = random.randint(*ENEMY_SPAWN_INTERVAL)

    def _ladder(self):
        return random.choice(self._ladders)
    
    def _spawn(self):
        self._spawn_interval -= 1
        if self._spawn_interval <= 0:
            self.add(Enemy(self._ladder()))
            self._reset_timer()
    
    def _check_barrels(self, barrels):
        for enemies in sprite.groupcollide(barrels, self, False, False).values():
            for enemy in enemies:
                enemy.fall()

    def update(self, barrels):
        self._check_barrels(barrels)
        self._spawn()
        super().update()
