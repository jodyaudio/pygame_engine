import pygame
import os


# graphics = {}
#
#
# def load_graphics(root_path, colorkey=(255, 0, 255)):
#     for file in os.listdir(root_path):
#         file_name, ext = os.path.splitext(file)
#         img = pygame.image.load(os.path.join(root_path, file))
#         if img.get_alpha():
#             img = img.convert_alpha()
#         else:
#             img = img.convert()
#             img.set_colorkey(colorkey)
#         graphics[file_name] = img
#     return graphics
