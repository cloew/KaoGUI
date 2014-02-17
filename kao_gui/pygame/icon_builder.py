from kao_gui.pygame.pygame_helper import load_image

import pygame

class IconBuilder:
    """ Class to aid in construction of valid Icons """
    
    def __init__(self, iconFilename):
        """ Initialie the Builder with the filename to load from """
        self.iconFilename = iconFilename
        
    def buildIcon(self):
        """ Build and return the Icon Surface """
        iconSurface = pygame.Surface((32, 32))
        rawIconSurface = load_image(self.iconFilename)
        self.setTransparency(iconSurface, rawIconSurface)
        
        return iconSurface
        
    def setTransparency(self, iconSurface, rawIcon):
        """ Set the transparency on the icon surface """
        iconSurface.set_colorkey(rawIcon.get_at((0, 0)))
        
        for i in range(0, 32):
            for j in range(0, 32):
                iconSurface.set_at((i,j), rawIcon.get_at((i,j)))