import os
import pygame

from . import config

images = {}
music = {}

def load_images(directory):
    for picture in os.listdir(directory):
        name, ext = os.path.splitext(picture)

        if ext.lower() == ".png":
            img = pygame.image.load(os.path.join(directory, picture))
            img = img.convert()
            #img = pygame.transform.scale(img, (config.SQUARE_SIZE, config.SQUARE_SIZE))

            images[name] = img

def get_image(name):
    if name in images:
        return images[name]
    else:
        return images["blank"]

def load_music(directory):
    pass

def get_music(name):
    return images[music]