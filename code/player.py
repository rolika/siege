"""The player in Siege! controlls a hero, who
- is placed on the bastion of his castle
- can move left and right, constrained by two towers on both ends of his bastion
- can pick up barrels at the towers, one at a time
- can throw barrels downwards at its enemies, again, one at a time"""


from pygame import sprite, image, key, transform, time  # this way, IntelliSense works in VS Code
from pygame.locals import *
from itertools import cycle
from barrel import Barrel
from constant import PLAYER_IDLE_FRAME_COOLDOWN, PLAYER_NUMBER_OF_FRAMES, PLAYER_STEP, PLAYER_START_POS, LEFT_TOWER, PLAYER_STEP_HOLDING_BARREL, RIGHT_TOWER


class Player(sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self._frame = cycle(range(PLAYER_NUMBER_OF_FRAMES))
        self._prep_animation_frames(PLAYER_NUMBER_OF_FRAMES)
        self.image = self._idle[0]

        self._can_throw = True
        self._held_barrel = sprite.GroupSingle()
        self._thrown_barrels = sprite.Group()
        
        self.reset()
    
    @property
    def held_barrel(self):
        return self._held_barrel
    
    @property
    def thrown_barrels(self):
        return self._thrown_barrels
    
    def _prep_animation_frames(self, num_of_frames):
        self._run_right = []
        self._run_left = []
        self._idle = []
        for i in range(num_of_frames):
            frame = image.load("gfx/hero/knight_m_run_anim_f" + str(i) + ".png")
            frame = transform.scale2x(frame)
            self._run_right.append(frame.convert_alpha())
            frame = transform.flip(frame, True, False)
            self._run_left.append(frame.convert_alpha())
            frame = image.load("gfx/hero/knight_m_idle_anim_f" + str(i) + ".png")
            frame = transform.scale2x(frame)
            self._idle.append(frame)
    
    def _get_input(self):
        keys = key.get_pressed()

        self._idle_animation_cooldown -= 1
        if self._is_ready_to_change_idle_frame():
            self.image = self._idle[next(self._frame)]
            self._reset_idle_animation_timer()

        if keys[K_RIGHT]:
            self.rect.x += PLAYER_STEP_HOLDING_BARREL if self._held_barrel.sprite else PLAYER_STEP
            self.image = self._run_right[next(self._frame)]
        elif keys[K_LEFT]:
            self.rect.x -= PLAYER_STEP_HOLDING_BARREL if self._held_barrel.sprite else PLAYER_STEP
            self.image = self._run_left[next(self._frame)]
        if keys[K_SPACE] and self._held_barrel.sprite and self._can_throw:
            self._throw_barrel()
    
    def _is_ready_to_change_idle_frame(self):
        return time.get_ticks() - self._last_idle_animation >= self._idle_animation_cooldown
    
    def _reset_idle_animation_timer(self):
        self._idle_animation_cooldown = PLAYER_IDLE_FRAME_COOLDOWN
        self._last_idle_animation = time.get_ticks()
    
    def _constrain_movement(self):  # and pick up a new barrel
        if self.rect.left <= LEFT_TOWER:
            self.rect.left = LEFT_TOWER
            self._pick_up_barrel()
        elif self.rect.right >= RIGHT_TOWER:
            self.rect.right = RIGHT_TOWER
            self._pick_up_barrel()
    
    def _constrain_barrel_throw(self):
        if self.rect.left > LEFT_TOWER + PLAYER_STEP and self.rect.right < RIGHT_TOWER - PLAYER_STEP:
            self._can_throw = True
    
    def _pick_up_barrel(self):
        if not self._held_barrel:
            self._barrel = Barrel(self.rect.midtop)
            self._held_barrel.add(self._barrel)
            self._can_throw = False
    
    def _throw_barrel(self):
        self._held_barrel.empty()
        self._thrown_barrels.add(self._barrel)
    
    def reset(self):
        self.rect = self.image.get_rect(midbottom=PLAYER_START_POS)
        self._held_barrel.empty()
        self._reset_idle_animation_timer()
    
    def update(self):
        self._get_input()
        self._constrain_barrel_throw()  # this should be done before constraining the movement
        self._constrain_movement()
        self._held_barrel.update(player_pos=self.rect.midtop)
        self._thrown_barrels.update()
