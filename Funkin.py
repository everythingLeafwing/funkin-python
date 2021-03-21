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

# while the game is running
while running:
    # for every event in the current events
    for event in pygame.event.get():

        # if the game was quit
        if event.type == pygame.QUIT:
            # make the game stop running
            running = False

        # if the event's type was a key being pressed
        if event.type == pygame.KEYDOWN:

            # if the event's key is enter or return
            if event.key == pygame.K_RETURN:

                # if the current screen is the title screen
                if currentScreen == "title":
                    # set the current screen to the main menu
                    currentScreen = "menu"
                    # "hover over" the story button
                    MainMenuHighlighted = "Story"

            # if the events key is down
            if event.key == pygame.K_DOWN and currentScreen == "menu":

                # if the story button is highlighted
                if MainMenuHighlighted == "Story":
                    # highlight the freeplay button
                    MainMenuHighlighted = "Freeplay"
                # if the freeplay button is highlighted
                elif MainMenuHighlighted == "Freeplay":
                    # highlight the donate button
                    MainMenuHighlighted = "Donate"
                # if the donate button is highlighted
                elif MainMenuHighlighted == "Donate":
                    # highlight the story button
                    MainMenuHighlighted = "Story"

            # if the up key is pressed
            if event.key == pygame.K_UP and currentScreen == "menu":
                # if the story button is highlighted
                if MainMenuHighlighted == "Story":
                    # highlight the donate button
                    MainMenuHighlighted = "Donate"
                # if the freeplay buttong is highlighted
                elif MainMenuHighlighted == "Freeplay":
                    # highlight the story button
                    MainMenuHighlighted = "Story"
                # if the donate button is highlighted
                elif MainMenuHighlighted == "Donate":
                    # highlight the freeplay button
                    MainMenuHighlighted = "Freeplay"

    # if you're on the title screen
    if currentScreen == "title":
        # display the title screen in the current screen and frame
        titleState.Screen(screen, frame)

    # if you're on the main menu screen
    if currentScreen == "menu":
        # display the main menu screen in the current screen and frame
        menuState.Screen(screen, frame, MainMenuHighlighted)

    # increase the current "frame"
    frame += 0.06