import pygame
from CalcEngine import Modulo, Floor
from source.images import menuBG, Alphabet, menu

scr = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

def Screen(screen, frame, highlighted):

    screen.fill((0, 0, 0))
    menuBgUp = 0
    if highlighted == "Story":
        menuBgUp = 0
    if highlighted == "Freeplay":
        menuBgUp = -40
    if highlighted == "Donate":
        menuBgUp = -80
    screen.blit(menuBG, (0, menuBgUp))

    if highlighted == "Story":
        screen.blit(menu.StoryWhite[Modulo(Floor(frame), 2)], (530, 170))
    else:
        screen.blit(menu.Story[0], (530, 170))

    if highlighted == "Freeplay":
        screen.blit(menu.FreeplayWhite[Modulo(Floor(frame), 2)], (530, 340))
    else:
        screen.blit(menu.Freeplay[0], (530, 340))

    if highlighted == "Donate":
        screen.blit(menu.DonateWhite[Modulo(Floor(frame), 2)], (530, 510))
    else:
        screen.blit(menu.Donate[0], (530, 510))

    pygame.display.update()
