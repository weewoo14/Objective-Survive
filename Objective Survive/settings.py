from random import *
screen_width = 1500
screen_height = 850

level_length = 8
level_width = 15

WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,255,0)
GRAY = (100,100,100)
LIGHT_GRAY = (160,160,160)
RED = (255,0,0)
ORANGE = (255,103,0)
BLUE = (0,0,255)

cooldown_movement = 0
magic_offset = 30

adj4 = [(0,-1),(0,1),(-1,0),(1,0),(-1,-1),(1,-1),(1,1),(-1,1)]

def is_valid_position(y,x):
    if y <= 0 or y >= level_length-1 or x <= 0 or x >= level_width-1:
        return False
    return True
def random_column():
    return randint(1,level_width-2)
def random_row():
    return randint(1,level_length-2)

