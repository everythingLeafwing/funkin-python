import pygame
from CalcEngine import Modulo, Floor
from source.images import menuBG, Alphabet, menu, storyMenu

scr = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

def Screen(screen, frame, UIeffector):
    screen.fill((0, 0, 0))

    weekSpacing = 155

    screen.blit(storyMenu.StoryMenuUI.easy, (1150, 625))

    pygame.draw.rect(screen, (0, 0, 0), (0, 550, 1100, 500))
    pygame.draw.rect(screen, (0, 0, 0), (1370, 550, 190, 500))

    screen.blit(storyMenu.StoryMenuUI.arrowLeft[1], (1045, 625))
    screen.blit(storyMenu.StoryMenuUI.arrowRight[1], (1375, 625))

    screen.blit(storyMenu.StoryMenuUI.tutorial[0], (525, 600 + UIeffector))
    screen.blit(storyMenu.StoryMenuUI.week1[0], (525, 600 + UIeffector + (weekSpacing * 1)))
    screen.blit(storyMenu.StoryMenuUI.week2[0], (525, 600 + UIeffector + (weekSpacing * 2)))
    screen.blit(storyMenu.StoryMenuUI.week3[0], (525, 600 + UIeffector + (weekSpacing * 3)))
    screen.blit(storyMenu.StoryMenuUI.week4[0], (525, 600 + UIeffector + (weekSpacing * 4)))
    screen.blit(storyMenu.StoryMenuUI.week5[0], (525, 600 + UIeffector + (weekSpacing * 5)))
    screen.blit(storyMenu.StoryMenuUI.week6[0], (525, 600 + UIeffector + (weekSpacing * 6)))

    pygame.draw.rect(screen, (0, 0, 0), (0, 0, 1920, 50))
    pygame.draw.rect(screen, (255, 210, 80), (0, 50, 1920, 500))

    pygame.display.update()
