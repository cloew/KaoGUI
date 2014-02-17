import pygame
from pygame.locals import *

def load_image(imageFilename, colorkey=None):
    try:
        image = pygame.image.load(imageFilename)
    except pygame.error, message:
        print 'Cannot load image:', imageFilename
        raise SystemExit, message
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image
    
def GetTransparentSurface(width, height):
    """ Constructs a transparent pygame surface """
    surface = pygame.Surface((width, height), flags=pygame.SRCALPHA)
    return surface