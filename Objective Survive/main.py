import pygame
from settings import *
from level1 import *
from character import *
from boss import *
from startingscreen import *
from deathscreen import *
from math import floor
from time import *

pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Objective: Survive")
clock = pygame.time.Clock()

current_level = 1
levels = {1:level1_map}

pygame.mixer.init()
pygame.mixer.music.load('menumusic.mp3')
pygame.mixer.music.play(-1,0.0)

main = True
death = False
while main:
    running = False
    game_check = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            main = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if start_button.collidepoint(event.pos):
                start_time = time()
                boss_cooldown = 10
                boss_laser_storage = [[] for j in range(octagon_length)]
                boss_animation_cooldown = 5
                laser_direction = 8
                laser_settings = [[[0,0] for i in range(laser_direction)] for j in range(octagon_length)]
                redbar_x = greenbar_x + greenbar_length
                redbar_y = greenbar_y
                current_row = 4
                current_column = 13
                death = False
                running = True
    cursor_x,cursor_y = pygame.mouse.get_pos()
    screen.fill(BLACK)
    if not death:
        if cursor_x >= 600 and cursor_x <= 900 and cursor_y >= 700 and cursor_y <= 800:
            start_color = WHITE
        else:
            start_color = LIGHT_GRAY
        screen.blit(start,start_rect)
        pygame.draw.rect(screen,start_color,start_button)
        screen.blit(button_text,button_rect)
    while running:
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                main = False
            if event.type == pygame.KEYDOWN:
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
            time_alive = floor(time()-start_time)
            death = True
        for row in levels[current_level]:
            for column in row:
                pygame.draw.rect(screen,column[0],column[1])

        if boss_cooldown >= 30 and not boss_laser_on:
            hit_check = [set() for i in range(octagon_length)]
            for j in range(octagon_length):
                temp_col = random_column()
                temp_row = random_row()
                for i in range(laser_direction):
                    laser_settings[j][i][0],laser_settings[j][i][1] = temp_row,temp_col
            boss_laser_on = True
            boss_cooldown = 0
        player_y = (100*current_row) + player_offset
        player_x = (100*current_column) + player_offset
        player_rect = (player_x,player_y,player_height,player_width)

        if boss_laser_on and boss_animation_cooldown >= 7:
            for i in range(octagon_length):
                boss_laser_storage[i],check,damage,new_hits = boss_octagon(hit_check[i],laser_settings[i],current_row,current_column)
                hit_check[i] = hit_check[i] | new_hits
                redbar_x -= damage
                if check == 8:
                    boss_laser_on = False
                    boss_laser_storage[i] = []
            boss_animation_cooldown = 0
            
        for i in range(octagon_length):
            for colour,rect in boss_laser_storage[i]:
                pygame.draw.rect(screen,colour,rect)

        pygame.draw.rect(screen,GREEN,player_rect)
        pygame.draw.rect(screen,GREEN,(greenbar_x,greenbar_y,greenbar_length,bar_width))
        pygame.draw.rect(screen,RED,(redbar_x,redbar_y,500-redbar_x,bar_width))

        cooldown_movement += 1
        boss_cooldown += 1
        boss_animation_cooldown += 1
        pygame.display.flip()
        clock.tick(60)
    if death:
        amount_message = integer_font.render(str(time_alive),True,WHITE)
        amount_rect = amount_message.get_rect()
        amount_rect.center = (screen_width//2,235)
        if cursor_x >= 600 and cursor_x <= 900 and cursor_y >= 700 and cursor_y <= 800:
            restart_color = WHITE
        else:
            restart_color = LIGHT_GRAY
        screen.blit(time_message,time_rect)
        screen.blit(amount_message,amount_rect)
        screen.blit(seconds_message,seconds_rect)
        pygame.draw.rect(screen, restart_color,restart_button)
        screen.blit(restart_text,restart_rect)
    pygame.display.flip()
pygame.quit()
