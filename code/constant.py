"""Constants gathered in one place"""


import enum

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

BLUE_SKY = (71, 93, 240)  # background color

BASTION_LEVEL = 200
LEFT_TOWER = 200  # right edge of left tower
RIGHT_TOWER = 600  # left edge of right tower
GROUND_LEVEL = 500  # incoming enemies and where the barrel breaks

BASTION_WIDTH = RIGHT_TOWER - LEFT_TOWER
BASTION_HEIGHT = GROUND_LEVEL - BASTION_LEVEL
TOWER_WIDTH = 150
TOWER_HEIGHT = BASTION_HEIGHT + 70
ROOF_WIDTH = 200
ROOF_HEIGHT = 100
ROAD_HEIGHT = 70  # actually this is road width for human beings

PLAYER_START_POS =(SCREEN_WIDTH // 2, BASTION_LEVEL + 20)
PLAYER_STEP = 6
PLAYER_STEP_HOLDING_BARREL = 4
PLAYER_NUMBER_OF_FRAMES = 4
PLAYER_IDLE_FRAME_COOLDOWN = 100

BARREL_SPEED = 6
BARREL_BONUS = 500  # if one barrel hits multiple enemies

ENEMY_WALKING_LEVEL = GROUND_LEVEL + 20
ENEMY_WALKING_SPEED = 2
ENEMY_CLIMBING_SPEED = -1
ENEMY_FALLING_SPEED = 4
ENEMY_SPAWN_INTERVAL = [50, 200]
ENEMY_SCORE = 1000
ENEMY_SPEED_INCREMENT = 0.1
ENEMY_SPAWN_DECREMENT = 10
SCORE_LIMIT = 10000
ENEMY_FRAME_COOLDOWN = 100
ENEMY_NUMBER_OF_FRAMES = 4

LADDERS = 6
SPACE_BETWEEN_LADDERS = BASTION_WIDTH // LADDERS
FIRST_LADDER_LEFT_POS = LEFT_TOWER + SPACE_BETWEEN_LADDERS // 2

HISCORE_FILENAME = "hiscore"


class State(enum.Enum):
    TITLE = enum.auto()
    RUN = enum.auto()
    OVER = enum.auto()
