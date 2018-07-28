import os
import pygame

from . import config

images = {}

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
    music = []

    for song in os.listdir(directory):
        name, ext = os.path.splitext(song)

        if ext.lower() == ".mp3":
            music.append(directory + song)

    return music

            
