import pygame as pygame
from CalcEngine import Modulo, Floor
from assets.source.images import gfDanceFrames, titleEnterFrames, logoBumpinFrames

scr = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

pygame.init()
pygame.font.init()
pygame.mixer.init()

def Screen(screen, frame):

    screen.fill((0, 0, 0))

    w, h = screen.get_size()

    screen.blit(gfDanceFrames[Floor(Modulo(frame, 27))], (1920 - 1080, 250))

    size = (Floor(w * 0.9), Floor(h * 0.1))
    titleEnter = pygame.transform.scale(titleEnterFrames[Floor(Modulo(frame, 42))], size)

    screen.blit(titleEnter, ((w / 2) - Floor(w * 0.45), h - (h * 0.15)))

    screen.blit(logoBumpinFrames[Floor(Modulo(frame, 12))], (-35, -35))

    frame += 0.06

    pygame.display.update()
