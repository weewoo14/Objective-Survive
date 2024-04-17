import pygame
from settings import *
pygame.init()

font = pygame.font.SysFont('Robus', 144)
integer_font = font = pygame.font.SysFont('javanesetext',80,bold=True)
time_message = font.render("You were alive for",True,WHITE)
time_rect = time_message.get_rect()
time_rect.center = (screen_width//2,100)

seconds_message = font.render("seconds",True,WHITE)
seconds_rect = time_message.get_rect()
seconds_rect.center = (925,350)

restart_font = pygame.font.SysFont('Robus', 70)
restart_button = pygame.Rect(600,700,300,100)
restart_color = LIGHT_GRAY
restart_text = restart_font.render("RESTART",True,BLACK)
restart_rect = (restart_text.get_rect())
restart_rect.center = (748,740)