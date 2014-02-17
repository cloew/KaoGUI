from kao_gui.pygame.window import GetWindow

import pygame

class PygameScreen:
    """ Represents a Screen in a Pygame based UI """
    
    def __init__(self):
        """ Initialize the Screen """
        
    def update(self):
        """ Update the screen.
            Overridde in sub-class """
        
    def draw(self):
        """ Draws the screen to the Window provided """
        window = GetWindow()
        surface = pygame.Surface((window.width, window.height))
        self.drawSurface(surface)
        return surface
        
    def drawSurface(self, surface):
        """ Draw the screen on the given surface.
            Override in sub-class """
    
    def getCenteredPostition(self, surface, xRatio, yRatio, parentSurface=None):
        """ Returns a rect for the surface centered at a x, y ratio of the window """
        if parentSurface is None:
            parentSurface = GetWindow().window
        
        x = parentSurface.get_width()*xRatio
        y = parentSurface.get_height()*yRatio
        return surface.get_rect(centerx = x, centery= y)