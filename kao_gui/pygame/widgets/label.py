from kao_gui.pygame.pygame_widget import PygameWidget

import pygame

class Label(PygameWidget):
    """ Represents a text label displayed via Pygame """
    
    def __init__(self, text, font="Times New Roman", size=36, bold=False, color=(10, 10, 10)):
        """ Initialize the Image by loading the Image File given """
        self.text = text
        self.font = pygame.font.SysFont(font, size)
        self.color = color
        self.setBold(bold)
        
    def buildSurface(self):
        """ Build the surface to display """
        return self.font.render(self.text, 1, self.color)
        
    def setBold(self, bold):
        """ Sets the Boldness of the entry """
        self.font.set_bold(bold)
        
    def setText(self, text):
        """ Set the current text """
        self.text = text