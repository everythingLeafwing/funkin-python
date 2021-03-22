import pygame as pygame
from assets.source.resourcePath import resource_path
from assets.source import menuState, StoryMenuState, titleState

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

storyMenuEffector = 12
storyMenuWeek = 0
StoryMenuDifficulty = 1

StoryMenuPressArrow = "none"
StoryMenuFramesSincePressArrow = -1

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

                # if the current screen is the main menu and you're hovering on story mode
                elif currentScreen == "menu" and MainMenuHighlighted == "Story":
                    # switch to story mode
                    pygame.mixer.stop()
                    pygame.mixer.music.load(resource_path("assets\\music\\Tutorial_Inst.ogg"))
                    pygame.mixer.music.play()
                    currentScreen = "story menu"

            # if the events key is down
            if event.key == pygame.K_DOWN:
                # if the current screen is the main menu
                if currentScreen == "menu":
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

                # if the current screen is the story menu
                if currentScreen == "story menu":
                    if storyMenuWeek != 6:
                        storyMenuEffector -= 156
                        storyMenuWeek += 1

            # if the up key is pressed
            if event.key == pygame.K_UP:
                if currentScreen == "menu":
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

                # if the current screen is the story menu:
                if storyMenuWeek != 0:
                    storyMenuEffector += 156
                    storyMenuWeek -= 1

            if currentScreen == "story menu":
                StoryMenuFramesSincePressArrow = 0
                if event.key == pygame.K_LEFT:
                    StoryMenuPressArrow = "left"
                    if StoryMenuDifficulty != 0:
                        StoryMenuDifficulty -= 1
                    elif StoryMenuDifficulty == 0:
                        StoryMenuDifficulty = 2
                if event.key == pygame.K_RIGHT:
                    StoryMenuPressArrow = "right"
                    if StoryMenuDifficulty != 2:
                        StoryMenuDifficulty += 1
                    elif StoryMenuDifficulty == 2:
                        StoryMenuDifficulty = 0
    # if you're on the title screen
    if currentScreen == "title":
        # display the title screen in the current screen and frame
        titleState.Screen(screen, frame)

    # if you're on the main menu screen
    if currentScreen == "menu":
        # display the main menu screen in the current screen and frame
        menuState.Screen(screen, frame, MainMenuHighlighted)
    # if you're on the main menu screen

    if currentScreen == "story menu":
        # display the main menu screen in the current screen and frame
        StoryMenuState.Screen(screen, frame, storyMenuEffector, StoryMenuDifficulty, StoryMenuPressArrow)
        if StoryMenuFramesSincePressArrow != -1 and StoryMenuFramesSincePressArrow != 35:
            StoryMenuFramesSincePressArrow += 1
        elif StoryMenuFramesSincePressArrow == 35:
            StoryMenuFramesSincePressArrow == -1
            StoryMenuPressArrow = "none"


    # increase the current "frame"
    frame += 0.06
