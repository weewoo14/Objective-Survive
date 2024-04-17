import pygame
from settings import *
from level1 import *
from character import *
from boss import *

pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()

current_level = 1
levels = {1:level1_map}

running = True
while running:
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.scancode == 44:
                if not current_fireball and fireball_cooldown >= 30:
                    fireball_cooldown = 0
                    current_fireball = True
                    for idx in range(fireball_direction):
                        fireball_settings[idx][0],fireball_settings[idx][1] = current_row,current_column

            if cooldown_movement >= 3:
                if event.scancode == 80:
                    if current_column-1 >= 1 and levels[current_level][current_row][current_column-1][0] != GRAY:
                        current_column -= 1
                if event.scancode == 79:
                    if current_column+1 <= 13 and levels[current_level][current_row][current_column+1][0] != GRAY:
                        current_column += 1
                if event.scancode == 82:
                    if current_row-1 >= 1 and levels[current_level][current_row-1][current_column][0] != GRAY:
                        current_row -= 1
                if event.scancode == 81:
                    if current_row+1 <= 6 and levels[current_level][current_row+1][current_column][0] != GRAY:
                        current_row += 1
                cooldown_movement = 0

    screen.fill(BLACK)

    if redbar_x <= greenbar_x:
        running = False

    for row in levels[current_level]:
        for column in row:
            pygame.draw.rect(screen,column[0],column[1])

    if current_fireball and fireball_animation_cooldown >= 5:
        check = 0
        fireball_storage = []
        for i in range(fireball_direction):
            if levels[current_level][fireball_settings[i][0]][fireball_settings[i][1]][0] == GRAY:
                check += 1
                continue
            if is_valid_position(fireball_settings[i][0]+adj4[i][0],fireball_settings[i][1]+adj4[i][1]):
                fireball_settings[i][0] += adj4[i][0]
                fireball_settings[i][1] += adj4[i][1]
                colour,rect = fireball(fireball_settings[i][0],fireball_settings[i][1])
                fireball_storage.append([colour,rect])
            else:
                check += 1
        if check == 8:
            current_fireball = False
            fireball_storage = []
        fireball_animation_cooldown = 0

    if boss_cooldown >= 30 and not boss_laser_on:
            already_hit = set()
            temp_col = random_column()
            temp_row = random_row()
            for i in range(laser_direction):
                laser_settings[i][0],laser_settings[i][1] = temp_row,temp_col
            boss_laser_on = True
            boss_cooldown = 0

    player_y = (100*current_row) + player_offset
    player_x = (100*current_column) + player_offset
    player_rect = (player_x,player_y,player_height,player_width)

    if boss_laser_on and boss_animation_cooldown >= 7:
        check = 0
        boss_laser_storage = []
        for i in range(laser_direction):
            if laser_settings[i][0] == current_row and laser_settings[i][1] == current_column and i not in already_hit:
                check += 1
                redbar_x -= 10
                already_hit.add(i)
                continue
            if is_valid_position(laser_settings[i][0]+adj4[i][0],laser_settings[i][1]+adj4[i][1]):
                laser_settings[i][0] += adj4[i][0]
                laser_settings[i][1] += adj4[i][1]
                colour,rect = boss_laser(laser_settings[i][0],laser_settings[i][1])
                boss_laser_storage.append([colour,rect])
            else:
                check += 1
        if check == 8:
            boss_laser_on = False
            boss_laser_storage = []
        boss_animation_cooldown = 0


    for colour,rect in fireball_storage:
        pygame.draw.rect(screen,colour,rect)
    for colour,rect in boss_laser_storage:
        pygame.draw.rect(screen,colour,rect)

    pygame.draw.rect(screen,GREEN,player_rect)
    pygame.draw.rect(screen,GREEN,(greenbar_x,greenbar_y,greenbar_length,bar_width))
    pygame.draw.rect(screen,RED,(redbar_x,redbar_y,500-redbar_x,bar_width))

    cooldown_movement += 1
    fireball_cooldown += 1
    fireball_animation_cooldown += 1
    boss_cooldown += 1
    boss_animation_cooldown += 1

    pygame.display.flip()
    clock.tick(60)
pygame.quit()
