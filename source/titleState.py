import pygame
from CalcEngine import Modulo, Floor
from source.images import gfDanceFrames, titleEnterFrames, logoBumpinFrames

scr = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

pygame.init()
pygame.font.init()
pygame.mixer.init()

def Screen(screen, frame):

    screen.fill((0, 0, 0))

    screen.blit(gfDanceFrames[Floor(Modulo(frame, 27))], (1920 - 1080, 250))
    screen.blit(titleEnterFrames[Floor(Modulo(frame, 42))], (115, 758))
    screen.blit(logoBumpinFrames[Floor(Modulo(frame, 12))], (-35, -35))

    frame += 0.06

    pygame.display.update()
