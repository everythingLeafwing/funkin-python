import pygame as pygame
import json
from assets.source.resourcePath import resource_path
from assets.source.images import notes

scr = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

def Screen(screen):
    screen.fill((0, 0, 0))

    with open(resource_path("assets\\data\\tutorial\\tutorial.json")) as f:
        data = json.load(f)

    screen.blit(notes.left, (100, 25))
    screen.blit(notes.down, (250, 25))
    screen.blit(notes.up, (400, 25))
    screen.blit(notes.right, (550, 25))

    screen.blit(notes.left, (800, 25))
    screen.blit(notes.down, (950, 25))
    screen.blit(notes.up, (1100, 25))
    screen.blit(notes.right, (1250, 25))

    for key in data

    pygame.display.update()
