"""In Siege!, enemies are coming in at ground level, from left or right.
Once they reach the bastion, they start to climb up the walls. The wall is divided into 6 lanes.
The attacker randomly chooses a ladder."""


from pygame import sprite, image, time, transform, mixer
import random
from pathlib import Path
from itertools import cycle
from constant import BASTION_LEVEL, ENEMY_CLIMBING_SPEED, ENEMY_FALLING_SPEED, ENEMY_FRAME_COOLDOWN,\
                     ENEMY_NUMBER_OF_FRAMES, ENEMY_SCORE, ENEMY_SPAWN_DECREMENT, ENEMY_SPAWN_INTERVAL,\
                     ENEMY_SPEED_INCREMENT, ENEMY_WALKING_LEVEL, ENEMY_WALKING_SPEED, SCORE_LIMIT, SCREEN_WIDTH


class Enemy(sprite.Sprite):

    # class variables & methods
    walking_speed = ENEMY_WALKING_SPEED
    climbing_speed = ENEMY_CLIMBING_SPEED

    def increase_speed():
        Enemy.walking_speed += ENEMY_SPEED_INCREMENT
        Enemy.climbing_speed -= ENEMY_SPEED_INCREMENT

    def __init__(self, enemy_type, ladder) -> None:
        super().__init__()
        random.seed()
        self._frame = cycle(range(ENEMY_NUMBER_OF_FRAMES))
        self._enemy_type = enemy_type
        self._ladder = ladder
        self._falling = False
        self._spawn()

        self._land_sfx = mixer.Sound("sfx/land.wav")
        self._land_sfx.set_volume(0.8)

    @property
    def is_above_bastion(self):
        return self.rect.centery < BASTION_LEVEL

    @property
    def is_on_ground(self):
        return self.rect.bottom == ENEMY_WALKING_LEVEL

    @property
    def falling(self):
        return self._falling

    def _spawn(self):
        self._direction = random.choice((-1, 1))  # -1: right side, 1: left side
        side = SCREEN_WIDTH if self._direction == -1 else 0
        self.image = self._enemy_type[self._direction][0]
        self.rect = self.image.get_rect(midbottom=(side, ENEMY_WALKING_LEVEL))
        self._speed = (Enemy.walking_speed*self._direction, 0)
        self._reset_animation_timer()

    def _climb(self):
        self._direction = 0
        self._speed = (0, Enemy.climbing_speed)

    def fall(self):
        self._speed = (0, ENEMY_FALLING_SPEED)
        self._falling = True

    def _check_ladder(self):
        """Use enemy walking speed as a tolerance around the ladders vertical axis."""
        return not self._falling and self.rect.colliderect(self._ladder)

    def _is_ready_to_change_idle_frame(self):
        return time.get_ticks() - self._last_animation >= self._animation_cooldown

    def _reset_animation_timer(self):
        self._animation_cooldown = ENEMY_FRAME_COOLDOWN
        self._last_animation = time.get_ticks()

    def update(self, *args, **kwargs) -> None:

        self._animation_cooldown -= 1
        if self._is_ready_to_change_idle_frame():
            self.image = self._enemy_type[self._direction][next(self._frame)]
            self._reset_animation_timer()

        self.rect.x += self._speed[0]
        self.rect.y += self._speed[1]
        if self._check_ladder():
            self.rect.centerx = self._ladder.rect.centerx
            self._climb()
        if self.rect.y >= ENEMY_WALKING_LEVEL:
            self.kill()
            self._land_sfx.play()


class Enemies(sprite.Group):

    # class variables & methods

    spawn_interval = ENEMY_SPAWN_INTERVAL[:]

    def reset_spawn_interval():
        Enemies.spawn_interval = ENEMY_SPAWN_INTERVAL[:]  # create a new list, not just a reference

    def decrement_spawn_interval():
        Enemies.spawn_interval[0] -= ENEMY_SPAWN_DECREMENT
        Enemies.spawn_interval[1] -= ENEMY_SPAWN_DECREMENT // 2

    def __init__(self, ladders) -> None:
        super().__init__()
        self._ladders = tuple(ladders)
        self._spawn_interval = 0
        self._score = 0
        self._level_limit = SCORE_LIMIT
        self._level = 1
        self._enemy_types = dict()
        self._prep_animations()
        Enemies.reset_spawn_interval()

        self._hit_sfx = mixer.Sound("sfx/hit.wav")
        self._hit_sfx.set_volume(0.25)

    @property
    def conquer(self):
        return any([enemy.is_above_bastion for enemy in self.sprites()])

    @property
    def score(self):
        return self._score

    def _prep_animations(self):
        """Eenemies are stored in a dict:
        enemy names: [
            [idle phases], <- used for climbing and falling
            [run left phases], <- enemy direction: 1
            [run right phases] <- enemy direction: -1 [-1]
        ]"""
        p = Path("gfx/enemies/")
        for png in p.iterdir():  # itemdir yields in arbitrary order
            props = png.name.rstrip(".png").split("_")  # 0: enemy name, 2: run or climb, 3: phase
            # frame lists: 0: climb, 1: run right, 2: run left
            self._enemy_types[props[0]] = [[None, None, None, None], [None, None, None, None], [None, None, None, None]]

        # populate the frame lists
        for png in p.iterdir():
            img = image.load(png)  # source images face right, so they come from the left
            img = transform.scale2x(img)
            props = png.name.rstrip(".png").split("_")  # 0: enemy name, 2: run or climb, 3: frame
            direction = 1 if props[1] == "run" else 0
            i = int(props[3][-1])  # the ending number of f0-3 -> index in the phases list
            self._enemy_types[props[0]][direction][i] = img.convert_alpha()
            if direction:  # flip only the run phases
                img = transform.flip(img, True, False)
                self._enemy_types[props[0]][2][i] = img.convert_alpha()

    def _reset_timer(self):
        self._spawn_interval = random.randint(*Enemies.spawn_interval)

    def _ladder(self):
        return random.choice(self._ladders)

    def _enemy_name(self):
        return random.choice(list(self._enemy_types))

    def _spawn(self):
        self._spawn_interval -= 1
        if self._spawn_interval <= 0:
            self.add(Enemy(self._enemy_types[self._enemy_name()], self._ladder()))
            self._reset_timer()

    def _check_barrels(self, barrels):
        for barrel, enemies in sprite.groupcollide(barrels, self, False, False).items():
            for enemy in enemies:
                if not enemy.falling:
                    self._score += ENEMY_SCORE + barrel.bonus
                    if enemy.is_on_ground:
                        self._score += ENEMY_SCORE  # bonus for hitting an enemy on ground level
                    barrel.hit()
                    self._hit_sfx.play()
                    enemy.fall()

    def _challenge(self):
        if self._score >= self._level_limit and self._level == self._level_limit / SCORE_LIMIT:
            Enemies.decrement_spawn_interval()
            self._level += 1
            self._level_limit += SCORE_LIMIT

    def reset(self):
        self._score = 0
        self.empty()
        Enemies.reset_spawn_interval()

    def update(self, barrels):
        self._check_barrels(barrels)
        self._challenge()
        self._spawn()
        super().update()
