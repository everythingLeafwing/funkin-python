import pygame
from CalcEngine import Modulo, Floor
from source.images import menuBG, Alphabet, menu

scr = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

def Screen(screen, frame):
    screen.fill((255, 210, 80))

    pygame.draw.rect(screen, (0, 0, 0), (0, 0, 1920, 50))
    pygame.draw.rect(screen, (0, 0, 0), (0, 450, 1920, 500))

    pygame.display.update()
