import pygame
import constants as c
import os
import ultracolors as color


# Graphics dictionary that will store all surfaces to be used by all classes that require images
graphics = {}


# Graphics class that will be used by gamestates to control the graphics layering system on the display
class GFX:
    def __init__(self):
        self.layer_0 = pygame.sprite.Group()        # BG2
        self.layer_1 = pygame.sprite.Group()        # BG1
        self.layer_2 = pygame.sprite.Group()        # Enemies
        self.layer_3 = pygame.sprite.Group()        # Player
        self.layer_4 = pygame.sprite.Group()        # Projectiles / Items
        self.layer_5 = pygame.sprite.Group()        # Platforms Tiles
        self.layer_6 = pygame.sprite.Group()        # FG
        self.layer_7 = pygame.sprite.Group()        # HUD
        self.layer_8 = pygame.sprite.Group()        # Screen Fade
        self.layers = [self.layer_0,
                       self.layer_1,
                       self.layer_2,
                       self.layer_3,
                       self.layer_4,
                       self.layer_5,
                       self.layer_6,
                       self.layer_7,
                       self.layer_8]
        # Native resolution canvas. After drawing to the canvas, it will be scaled to proper display resolution.
        # This ensures that base game resolution is maintained even while scaling the game window.
        self.canvas = pygame.Surface(c.NATIVE_SIZE)

    def update(self):
        for l in self.layers:
            l.update()

    def render(self, display):
        self.canvas.fill(color.BLACK)

        for l in self.layers:
            l.draw(self.canvas)
        if c.SCALE >= 1:
            pygame.transform.scale(self.canvas, c.DISPLAY_SIZE, display)
        else:
            display.blit(self.canvas, c.DISPLAY_TOP_LEFT)
        pygame.display.update()

    def add_sprite(self, sprite, layer):
        self.layers[layer].add(sprite)


def load_graphics(root_path, colorkey=(255, 0, 255)):
    for file in os.listdir(root_path):
        file_name, ext = os.path.splitext(file)
        img = pygame.image.load(os.path.join(root_path, file))
        if img.get_alpha():
            img = img.convert_alpha()
        else:
            img = img.convert()
            img.set_colorkey(colorkey)
        graphics[file_name] = img
    return graphics
