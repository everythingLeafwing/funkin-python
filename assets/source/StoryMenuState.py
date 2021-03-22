import pygame as pygame
from assets.source.images import storyMenu

scr = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

def Screen(screen, frame, UIeffector, difficulty):
    screen.fill((0, 0, 0))

    weekSpacing = 155

    if difficulty == 0:
        screen.blit(storyMenu.StoryMenuUI.easy, (1135, 625))
    if difficulty == 1:
        screen.blit(storyMenu.StoryMenuUI.normal, (1105, 625))
    if difficulty == 2:
        screen.blit(storyMenu.StoryMenuUI.hard, (1135, 625))

    pygame.draw.rect(screen, (0, 0, 0), (0, 550, 1100, 500))
    pygame.draw.rect(screen, (0, 0, 0), (1435, 550, 190, 500))

    screen.blit(storyMenu.StoryMenuUI.arrowLeft[1], (1045, 625))
    screen.blit(storyMenu.StoryMenuUI.arrowRight[1], (1420, 625))

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
