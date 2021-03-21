import pygame
from CalcEngine import Modulo, Floor
from source.spriteSheet import spriteSheet
from source.resourcePath import resource_path
from source import titleState, menuState

pygame.init()
pygame.font.init()
pygame.mixer.init()

black = 0, 0, 0
screenSize = width, height = 1920, 1080

screen = pygame.display.set_mode(screenSize, pygame.FULLSCREEN)

running = True

frame = 0

currentScreen = "title"

pygame.mixer.music.load(resource_path("assets\\music\\freakyMenu.ogg"))
pygame.mixer.music.play()

songPlating = "none"

MainMenuHighlighted = "Story"

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if currentScreen == "title":
                    currentScreen = "menu"
                    MainMenuHighlighted = "Story"
            if event.key == pygame.K_DOWN and currentScreen == "menu":
                if MainMenuHighlighted == "Story":
                    MainMenuHighlighted = "Freeplay"
                elif MainMenuHighlighted == "Freeplay":
                    MainMenuHighlighted = "Donate"
                elif MainMenuHighlighted == "Donate":
                    MainMenuHighlighted = "Story"
            if event.key == pygame.K_UP and currentScreen == "menu":
                if MainMenuHighlighted == "Story":
                    MainMenuHighlighted = "Donate"
                elif MainMenuHighlighted == "Freeplay":
                    MainMenuHighlighted = "Story"
                elif MainMenuHighlighted == "Donate":
                    MainMenuHighlighted = "Freeplay"


    if currentScreen == "title":
        titleState.Screen(screen, frame)
    if currentScreen == "menu":
        menuState.Screen(screen, frame, MainMenuHighlighted)

    frame += 0.06
