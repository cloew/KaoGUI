from kao_gui.pygame.pygame_helper import load_image
from kao_gui.pygame.pygame_widget import PygameWidget

import pygame

class Image(PygameWidget):
    """ Represents an image displayed via Pygame """
    
    def __init__(self, imageFilename, scaledSize=None):
        """ Initialize the Image by loading the Image File given """
        self.image = load_image(imageFilename)
        if scaledSize is not None:
            self.image = pygame.transform.scale(self.image, scaledSize)
        
    def buildSurface(self):
        """ Build the surface to display """
        return self.image