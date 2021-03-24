import pygame as pygame
import json
from assets.source.resourcePath import resource_path
from assets.source.images import notes

scr = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

def Screen(screen, eff):
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

    for key in data["song"]["notes"]:
        for keyPos in key["sectionNotes"]:
            if data["song"]["notes"][1]['mustHitSection']:
                print("mustHit")
                if keyPos[1] == 0:
                    screen.blit(notes.left, (800, (keyPos[0] / 2) - eff))
                if keyPos[1] == 1:
                    screen.blit(notes.down, (950, (keyPos[0] / 2) - eff))
                if keyPos[1] == 2:
                    screen.blit(notes.up, (1100, (keyPos[0] / 2) - eff))
                if keyPos[1] == 3:
                    screen.blit(notes.right, (1250, (keyPos[0] / 2) - eff))
            else:
                print("mustntHit")
                if keyPos[1] == 0:
                    screen.blit(notes.left, (100, (keyPos[0] / 2) - eff))
                if keyPos[1] == 1:
                    screen.blit(notes.down, (250, (keyPos[0] / 2) - eff))
                if keyPos[1] == 2:
                    screen.blit(notes.up, (400, (keyPos[0] / 2) - eff))
                if keyPos[1] == 3:
                    screen.blit(notes.right, (550, (keyPos[0] / 2) - eff))

    pygame.display.update()

    return data['song']['bpm']
