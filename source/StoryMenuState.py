import pygame
from CalcEngine import Modulo, Floor
from source.images import menuBG, Alphabet, menu

scr = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

def Screen(screen, frame, highlighted):

    screen.fill((0, 0, 0))
    

    pygame.display.update()
