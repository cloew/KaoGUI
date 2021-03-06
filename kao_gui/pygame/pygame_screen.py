from kao_gui.pygame.pygame_widget import PygameWidget
from kao_gui.pygame.window import GetWindow

import pygame

class PygameScreen(PygameWidget):
    """ Represents a Screen in a Pygame based UI """
    
    def __init__(self):
        """ Initialize the Screen """
        PygameWidget.__init__(self)
        window = GetWindow()
        self.width = window.width
        self.height = window.height
        
    def update(self):
        """ Update the screen.
            Overridde in sub-class """
            
    def buildSurface(self):
        """ Build the surface to use when drawing """
        surface = pygame.Surface((self.width, self.height))
        surface.fill((255,255,255))
        return surface