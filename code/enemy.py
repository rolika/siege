"""In Siege!, enemies are coming in at ground level, from left or right.
Once they reach the bastion, they start to climb up the walls. The wall is divided into 7 lanes.
The attacker chooses the nearest ladder with the least other attackers already on it at spawn time."""


from pygame import sprite, Surface
import random
from constant import BASTION_LEVEL, ENEMY_CLIMBING_SPEED, ENEMY_FALLING_SPEED, ENEMY_SCORE, ENEMY_SPAWN_DECREMENT, ENEMY_SPAWN_INTERVAL, ENEMY_SPEED_INCREMENT, ENEMY_WALKING_SPEED, GROUND_LEVEL, SCORE_LIMIT_1, SCORE_LIMIT_2, SCORE_LIMIT_3, SCREEN_WIDTH


class Enemy(sprite.Sprite):

    # class variables & methods
    walking_speed = ENEMY_WALKING_SPEED
    climbing_speed = ENEMY_CLIMBING_SPEED
    
    def increase_speed():
        Enemy.walking_speed += ENEMY_SPEED_INCREMENT
        Enemy.climbing_speed -= ENEMY_SPEED_INCREMENT

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
    
    @property
    def is_on_ground(self):
        return self.rect.bottom == GROUND_LEVEL
    
    @property
    def falling(self):
        return self._falling

    def _spawn(self):
        direction = random.choice((-1, 1))  # -1: right side, 1: left side
        side = SCREEN_WIDTH if direction == -1 else 0
        self.rect = self.image.get_rect(midbottom=(side, GROUND_LEVEL))
        self._speed = (Enemy.walking_speed*direction, 0)

    def _climb(self):
        self._speed = (0, Enemy.climbing_speed)
    
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

    # class variables & methods
    spawn_interval = ENEMY_SPAWN_INTERVAL
    
    def decrement_spawn_interval():
        Enemies.spawn_interval[0] -= ENEMY_SPAWN_DECREMENT
        Enemies.spawn_interval[1] -= ENEMY_SPAWN_DECREMENT
    
    def __init__(self, ladders) -> None:
        super().__init__()
        self._ladders = tuple(ladders)
        self._spawn_interval = 0
        self._score = 0
        self._level = 1
    
    @property
    def conquer(self):
        return any([enemy.is_above_bastion for enemy in self.sprites()])
    
    @property
    def score(self):
        return self._score

    def _reset_timer(self):
        self._spawn_interval = random.randint(*Enemies.spawn_interval)

    def _ladder(self):
        return random.choice(self._ladders)
    
    def _spawn(self):
        self._spawn_interval -= 1
        if self._spawn_interval <= 0:
            self.add(Enemy(self._ladder()))
            self._reset_timer()
    
    def _check_barrels(self, barrels):
        for barrel, enemies in sprite.groupcollide(barrels, self, False, False).items():
            for enemy in enemies:
                if not enemy.falling:
                    self._score += ENEMY_SCORE + barrel.bonus
                    if enemy.is_on_ground:
                        self._score += ENEMY_SCORE  # bonus for hitting an enemy on ground level
                    barrel.hit()
                    enemy.fall()
    
    def _challenge(self):
        if self._score >= SCORE_LIMIT_1 and self._level == 1:
            #Enemy.increase_speed()
            self._level += 1
        elif self._score >= SCORE_LIMIT_2 and self._level == 2:
            Enemies.decrement_spawn_interval()
            self._level += 1
        elif self._score >= SCORE_LIMIT_3 and self._level == 3:
            self._level += 1
            #Enemy.increase_speed()
            Enemies.decrement_spawn_interval()

    def update(self, barrels):
        self._check_barrels(barrels)
        self._challenge()
        self._spawn()
        super().update()
