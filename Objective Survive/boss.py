from settings import *

boss_laser_on = False
boss_row_on = False
def boss_laser(row,col):
    return ((RED,((100*(col))+magic_offset,(100*row)+magic_offset,35,35)))
def boss_octagon(already_hit,laser_settings,current_row,current_column):
    check = 0
    damage_taken = 0
    boss_laser_storage = []
    hit_set = set()
    for i in range(laser_direction):
        if laser_settings[i][0] == current_row and laser_settings[i][1] == current_column and i not in already_hit:
            check += 1
            damage_taken += 10
            hit_set.add(i)
            continue
        if is_valid_position(laser_settings[i][0]+adj4[i][0],laser_settings[i][1]+adj4[i][1]):
            laser_settings[i][0] += adj4[i][0]
            laser_settings[i][1] += adj4[i][1]
            colour,rect = boss_laser(laser_settings[i][0],laser_settings[i][1])
            boss_laser_storage.append([colour,rect])
        else:
            check += 1
    return boss_laser_storage,check,damage_taken,hit_set

octagon_length = 3
boss_cooldown = 10
boss_laser_storage = [[] for j in range(octagon_length)]
boss_animation_cooldown = 5
laser_direction = 8
laser_settings = [[[0,0] for i in range(laser_direction)] for j in range(octagon_length)]
