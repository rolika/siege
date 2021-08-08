"""Constants gathered in one place"""

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

PLAYER_START_POS =(SCREEN_WIDTH // 2, BASTION_LEVEL)
PLAYER_STEP = 5

BARREL_SPEED = 6
