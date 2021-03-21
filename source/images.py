import pygame
from source.spriteSheet import spriteSheet
from source.resourcePath import resource_path

scr = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

def listSprites(name, count, sprite_sheet):
    def numberStr(Value):
        if Value > 999:
            return str(Value)
        if Value > 99:
            return "0" + str(Value)
        if Value > 9:
            return "00" + str(Value)

        return "000" + str(Value)

    c = count
    final = []

    while c > 0:
        c -= 1
        final.append(sprite_sheet.parse_sprite(name + numberStr(c)))
    return final


gfDance = spriteSheet("assets\\images\\gfDancetitle.png")
gfDanceFrames = listSprites("gfDance", 30, gfDance)

titleEnter = spriteSheet("assets\\images\\titleEnter.png", True)
titleEnterFrames = listSprites("Press Enter to Begin", 45, titleEnter)

logoBumpin = spriteSheet("assets\\images\\logoBumpin.png")
logoBumpinFrames = listSprites("logo bumpin", 15, logoBumpin)

menuBG = pygame.transform.scale(pygame.image.load("assets\\images\\menuBG.png"), (1920, 1080))
menuBGBlue = pygame.transform.scale(pygame.image.load("assets\\images\\menuBGBlue.png"), (1920, 1080))
menuBGMagenta = pygame.transform.scale(pygame.image.load("assets\\images\\menuBGMagenta.png"), (1920, 1080))
menuDesat = pygame.transform.scale(pygame.image.load("assets\\images\\menuDesat.png"), (1920, 1080))

class Alphabet:
    Sprites = spriteSheet("assets\\images\\alphabet.png", True)

    a = [Sprites.parse_sprite("a lowercase0000"), Sprites.parse_sprite("a lowercase0001"), Sprites.parse_sprite("a lowercase0002"), Sprites.parse_sprite("a lowercase0003")]
    A = [Sprites.parse_sprite("A bold0000"), Sprites.parse_sprite("A bold0001"), Sprites.parse_sprite("A bold0002"), Sprites.parse_sprite("A bold0003")]
    b = [Sprites.parse_sprite("b lowercase0000"), Sprites.parse_sprite("b lowercase0001"), Sprites.parse_sprite("b lowercase0002"), Sprites.parse_sprite("b lowercase0003")]
    B = [Sprites.parse_sprite("B bold0000"), Sprites.parse_sprite("B bold0001"), Sprites.parse_sprite("B bold0002"), Sprites.parse_sprite("B bold0003")]
    c = [Sprites.parse_sprite("c lowercase0000"), Sprites.parse_sprite("c lowercase0001"), Sprites.parse_sprite("c lowercase0002"), Sprites.parse_sprite("c lowercase0003")]
    C = [Sprites.parse_sprite("C bold0000"), Sprites.parse_sprite("C bold0001"), Sprites.parse_sprite("C bold0002"), Sprites.parse_sprite("C bold0003")]
    d = [Sprites.parse_sprite("d lowercase0000"), Sprites.parse_sprite("d lowercase0001"), Sprites.parse_sprite("d lowercase0002"), Sprites.parse_sprite("d lowercase0003")]
    D = [Sprites.parse_sprite("D bold0000"), Sprites.parse_sprite("D bold0001"), Sprites.parse_sprite("D bold0002"), Sprites.parse_sprite("D bold0003")]
    e = [Sprites.parse_sprite("e lowercase0000"), Sprites.parse_sprite("e lowercase0001"), Sprites.parse_sprite("e lowercase0002"), Sprites.parse_sprite("e lowercase0003")]
    E = [Sprites.parse_sprite("E bold0000"), Sprites.parse_sprite("E bold0001"), Sprites.parse_sprite("E bold0002"), Sprites.parse_sprite("E bold0003")]
    f = [Sprites.parse_sprite("f lowercase0000"), Sprites.parse_sprite("f lowercase0001"), Sprites.parse_sprite("f lowercase0002"), Sprites.parse_sprite("f lowercase0003")]
    F = [Sprites.parse_sprite("F bold0000"), Sprites.parse_sprite("F bold0001"), Sprites.parse_sprite("F bold0002"), Sprites.parse_sprite("F bold0003")]
    g = [Sprites.parse_sprite("g lowercase0000"), Sprites.parse_sprite("g lowercase0001"), Sprites.parse_sprite("g lowercase0002"), Sprites.parse_sprite("g lowercase0003")]
    G = [Sprites.parse_sprite("G bold0000"), Sprites.parse_sprite("G bold0001"), Sprites.parse_sprite("G bold0002"), Sprites.parse_sprite("G bold0003")]
    h = [Sprites.parse_sprite("h lowercase0000"), Sprites.parse_sprite("h lowercase0001"), Sprites.parse_sprite("h lowercase0002"), Sprites.parse_sprite("h lowercase0003")]
    H = [Sprites.parse_sprite("H bold0000"), Sprites.parse_sprite("H bold0001"), Sprites.parse_sprite("H bold0002"), Sprites.parse_sprite("H bold0003")]
    i = [Sprites.parse_sprite("i lowercase0000"), Sprites.parse_sprite("i lowercase0001"), Sprites.parse_sprite("i lowercase0002"), Sprites.parse_sprite("i lowercase0003")]
    I = [Sprites.parse_sprite("I bold0000"), Sprites.parse_sprite("I bold0001"), Sprites.parse_sprite("I bold0002"), Sprites.parse_sprite("I bold0003")]
    j = [Sprites.parse_sprite("j lowercase0000"), Sprites.parse_sprite("j lowercase0001"), Sprites.parse_sprite("j lowercase0002"), Sprites.parse_sprite("j lowercase0003")]
    J = [Sprites.parse_sprite("J bold0000"), Sprites.parse_sprite("J bold0001"), Sprites.parse_sprite("J bold0002"), Sprites.parse_sprite("J bold0003")]
    k = [Sprites.parse_sprite("k lowercase0000"), Sprites.parse_sprite("k lowercase0001"), Sprites.parse_sprite("k lowercase0002"), Sprites.parse_sprite("k lowercase0003")]
    K = [Sprites.parse_sprite("K bold0000"), Sprites.parse_sprite("K bold0001"), Sprites.parse_sprite("K bold0002"), Sprites.parse_sprite("K bold0003")]
    l = [Sprites.parse_sprite("l lowercase0000"), Sprites.parse_sprite("l lowercase0001"), Sprites.parse_sprite("l lowercase0002"), Sprites.parse_sprite("l lowercase0003")]
    L = [Sprites.parse_sprite("L bold0000"), Sprites.parse_sprite("L bold0001"), Sprites.parse_sprite("L bold0002"), Sprites.parse_sprite("L bold0003")]
    m = [Sprites.parse_sprite("m lowercase0000"), Sprites.parse_sprite("m lowercase0001"), Sprites.parse_sprite("m lowercase0002"), Sprites.parse_sprite("m lowercase0003")]
    M = [Sprites.parse_sprite("M bold0000"), Sprites.parse_sprite("M bold0001"), Sprites.parse_sprite("M bold0002"), Sprites.parse_sprite("M bold0003")]
    n = [Sprites.parse_sprite("n lowercase0000"), Sprites.parse_sprite("n lowercase0001"), Sprites.parse_sprite("n lowercase0002"), Sprites.parse_sprite("n lowercase0003")]
    N = [Sprites.parse_sprite("N bold0000"), Sprites.parse_sprite("N bold0001"), Sprites.parse_sprite("N bold0002"), Sprites.parse_sprite("N bold0003")]
    o = [Sprites.parse_sprite("o lowercase0000"), Sprites.parse_sprite("o lowercase0001"), Sprites.parse_sprite("o lowercase0002"), Sprites.parse_sprite("o lowercase0003")]
    O = [Sprites.parse_sprite("O bold0000"), Sprites.parse_sprite("O bold0001"), Sprites.parse_sprite("O bold0002"), Sprites.parse_sprite("O bold0003")]
    p = [Sprites.parse_sprite("p lowercase0000"), Sprites.parse_sprite("p lowercase0001"), Sprites.parse_sprite("p lowercase0002"), Sprites.parse_sprite("p lowercase0003")]
    P = [Sprites.parse_sprite("P bold0000"), Sprites.parse_sprite("P bold0001"), Sprites.parse_sprite("P bold0002"), Sprites.parse_sprite("P bold0003")]
    q = [Sprites.parse_sprite("q lowercase0000"), Sprites.parse_sprite("q lowercase0001"), Sprites.parse_sprite("q lowercase0002"), Sprites.parse_sprite("q lowercase0003")]
    Q = [Sprites.parse_sprite("Q bold0000"), Sprites.parse_sprite("Q bold0001"), Sprites.parse_sprite("Q bold0002"), Sprites.parse_sprite("Q bold0003")]
    r = [Sprites.parse_sprite("r lowercase0000"), Sprites.parse_sprite("r lowercase0001"), Sprites.parse_sprite("r lowercase0002"), Sprites.parse_sprite("r lowercase0003")]
    R = [Sprites.parse_sprite("R bold0000"), Sprites.parse_sprite("R bold0001"), Sprites.parse_sprite("R bold0002"), Sprites.parse_sprite("R bold0003")]
    s = [Sprites.parse_sprite("s lowercase0000"), Sprites.parse_sprite("s lowercase0001"), Sprites.parse_sprite("s lowercase0002"), Sprites.parse_sprite("s lowercase0003")]
    S = [Sprites.parse_sprite("S bold0000"), Sprites.parse_sprite("S bold0001"), Sprites.parse_sprite("S bold0002"), Sprites.parse_sprite("S bold0003")]
    t = [Sprites.parse_sprite("t lowercase0000"), Sprites.parse_sprite("t lowercase0001"), Sprites.parse_sprite("t lowercase0002"), Sprites.parse_sprite("t lowercase0003")]
    T = [Sprites.parse_sprite("T bold0000"), Sprites.parse_sprite("T bold0001"), Sprites.parse_sprite("T bold0002"), Sprites.parse_sprite("T bold0003")]
    u = [Sprites.parse_sprite("u lowercase0000"), Sprites.parse_sprite("u lowercase0001"), Sprites.parse_sprite("u lowercase0002"), Sprites.parse_sprite("u lowercase0003")]
    U = [Sprites.parse_sprite("U bold0000"), Sprites.parse_sprite("U bold0001"), Sprites.parse_sprite("U bold0002"), Sprites.parse_sprite("U bold0003")]
    v = [Sprites.parse_sprite("v lowercase0000"), Sprites.parse_sprite("v lowercase0001"), Sprites.parse_sprite("v lowercase0002"), Sprites.parse_sprite("v lowercase0003")]
    V = [Sprites.parse_sprite("V bold0000"), Sprites.parse_sprite("V bold0001"), Sprites.parse_sprite("V bold0002"), Sprites.parse_sprite("V bold0003")]
    w = [Sprites.parse_sprite("w lowercase0000"), Sprites.parse_sprite("w lowercase0001"), Sprites.parse_sprite("w lowercase0002"), Sprites.parse_sprite("w lowercase0003")]
    W = [Sprites.parse_sprite("W bold0000"), Sprites.parse_sprite("W bold0001"), Sprites.parse_sprite("W bold0002"), Sprites.parse_sprite("W bold0003")]
    x = [Sprites.parse_sprite("x lowercase0000"), Sprites.parse_sprite("x lowercase0001"), Sprites.parse_sprite("x lowercase0002"), Sprites.parse_sprite("x lowercase0003")]
    X = [Sprites.parse_sprite("X bold0000"), Sprites.parse_sprite("X bold0001"), Sprites.parse_sprite("X bold0002"), Sprites.parse_sprite("X bold0003")]
    y = [Sprites.parse_sprite("y lowercase0000"), Sprites.parse_sprite("y lowercase0001"), Sprites.parse_sprite("y lowercase0002"), Sprites.parse_sprite("y lowercase0003")]
    Y = [Sprites.parse_sprite("Y bold0000"), Sprites.parse_sprite("Y bold0001"), Sprites.parse_sprite("Y bold0002"), Sprites.parse_sprite("Y bold0003")]
    z = [Sprites.parse_sprite("z lowercase0000"), Sprites.parse_sprite("z lowercase0001"), Sprites.parse_sprite("z lowercase0002"), Sprites.parse_sprite("z lowercase0003")]
    Z = [Sprites.parse_sprite("Z bold0000"), Sprites.parse_sprite("Z bold0001"), Sprites.parse_sprite("Z bold0002"), Sprites.parse_sprite("Z bold0003")]

class menu:
    mainMenu = spriteSheet("assets\\images\\FNF_main_menu_assets.png", True)

    Donate = [mainMenu.parse_sprite("donate basic0000"), mainMenu.parse_sprite("donate basic0003"), mainMenu.parse_sprite("donate basic0006")]
    DonateWhite = [mainMenu.parse_sprite("donate white0000"), mainMenu.parse_sprite("donate white0001"), mainMenu.parse_sprite("donate white0002")]
    Freeplay = [mainMenu.parse_sprite("freeplay basic0000"), mainMenu.parse_sprite("freeplay basic0003"), mainMenu.parse_sprite("freeplay basic0006")]
    FreeplayWhite = [mainMenu.parse_sprite("freeplay white0000"), mainMenu.parse_sprite("freeplay white0001"), mainMenu.parse_sprite("freeplay white0002")]
    Options = [mainMenu.parse_sprite("options basic0000"), mainMenu.parse_sprite("options basic0003"), mainMenu.parse_sprite("options basic0006")]
    OptionsWhite = [mainMenu.parse_sprite("options white0000"), mainMenu.parse_sprite("options white0001"), mainMenu.parse_sprite("options white0002")]
    Story = [mainMenu.parse_sprite("story mode basic0000"), mainMenu.parse_sprite("story mode basic0003"), mainMenu.parse_sprite("story mode basic0006")]
    StoryWhite = [mainMenu.parse_sprite("story mode white0000"), mainMenu.parse_sprite("story mode white0001"), mainMenu.parse_sprite("story mode white0002")]

class storyMenu:
    class StoryMenuUI:
        storyMenuUI = spriteSheet("assets\\images\\campaign_menu_UI_assets.png")

        easy, normal, hard = storyMenuUI.parse_sprite("EASY0000"), storyMenuUI.parse_sprite("NORMAL0000"), storyMenuUI.parse_sprite("HARD0000")

        tutorial = [storyMenuUI.parse_sprite("tutorial selected0000"), storyMenuUI.parse_sprite("tutorial selected0001")]
        week1 = [storyMenuUI.parse_sprite("WEEK1 select0000"), storyMenuUI.parse_sprite("WEEK1 select0001")]
        week2 = [storyMenuUI.parse_sprite("week2 select0000"), storyMenuUI.parse_sprite("week2 select0001")]
        week3 = [storyMenuUI.parse_sprite("Week3 select0000"), storyMenuUI.parse_sprite("Week3 select0001")]
        week4 = [storyMenuUI.parse_sprite("Week4 select0000"), storyMenuUI.parse_sprite("Week4 select0001")]
        week5 = [storyMenuUI.parse_sprite("week2 select0000"), storyMenuUI.parse_sprite("week2 select0001")]
        week6 = [storyMenuUI.parse_sprite("week2 select0000"), storyMenuUI.parse_sprite("week2 select0001")]

        arrowLeft = [storyMenuUI.parse_sprite("arrow left0000"), storyMenuUI.parse_sprite("arrow push left0000")]
        arrowRight = [storyMenuUI.parse_sprite("arrow right0000"), storyMenuUI.parse_sprite("arrow push right0000")]
