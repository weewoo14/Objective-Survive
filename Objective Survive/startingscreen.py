import pygame
from settings import *
pygame.init()

font = pygame.font.SysFont('Robus', 144)
start = font.render("Objective: Survive", True, WHITE,BLACK)
start_rect = start.get_rect()
start_rect.center = (screen_width//2,200)

start_font = pygame.font.SysFont('Robus', 100)
start_button = pygame.Rect(600,700,300,100)
start_color = LIGHT_GRAY
button_text = start_font.render("START",True,BLACK)
button_rect = (button_text.get_rect())
button_rect.center = (748,740)
