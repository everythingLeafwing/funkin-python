import pygame as pygame
import xml.dom.minidom as xmldom
from assets.source.resourcePath import resource_path


class spriteSheet:
    def __init__(self, filename, trans=False):
        self.filename = resource_path(filename)
        self.sprite_sheet = pygame.image.load(filename).convert_alpha()
        self.meta_data = self.filename.replace("png", "xml")

        self.trans = trans

        self.data = xmldom.parse(self.meta_data)

    def get_sprite(self, x, y, w, h):
        sprite = "";
        if self.trans:
            sprite = pygame.Surface((w, h), pygame.SRCALPHA)
        else:
            sprite = pygame.Surface((w, h))
            sprite.set_colorkey((0, 0, 0, 0))
        sprite.blit(self.sprite_sheet, (0, 0), (x, y, w, h))
        return sprite

    def parse_sprite(self, name):
        textures = self.data.getElementsByTagName("SubTexture")
        x, y, w, h = 0, 0, 0, 0
        for texture in textures:
            if texture.getAttribute("name") == name:
                x, y, w, h = int(texture.getAttribute("x")), int(texture.getAttribute("y")), int(texture.getAttribute("width")), int(texture.getAttribute("height"))

        image = self.get_sprite(x, y, w, h)
        return image