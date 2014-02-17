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
        self.surface = pygame.Surface((window.width, window.height))
        self.surface.fill((255,255,255))
        self.drawSurface(self.surface)
        return self.surface
        
    def drawSurface(self, surface):
        """ Draw the screen on the given surface.
            Override in sub-class """
            
    def drawOnSurface(self, surface, left=None, right=None, centerx=None,
                                     top=None, bottom=None, centery=None):
        """ Draw the given surface onto this widget at the position specified """
        leftPosition = self.normalizeXCoordinate(surface, left, right, centerx)
        topPosition = self.normalizeYCoordinate(surface, top, bottom, centery)
        self.blit(surface, (leftPosition, topPosition))
        
    def normalizeXCoordinate(self, surface, left, right, centerx):
        """ Normalize and return the X Coordinate of the left of the surface """
        if left is not None:
            return left*self.width
        elif right is not None:
            return right*self.width - surface.get_width()
        elif centerx is not None:
            return centerx*self.width - surface.get_width()/2
        else:
            raise Exception("Must provide either left, right, or centerx argument")
            
    def normalizeYCoordinate(self, surface, top, bottom, centery):
        """ Normalize and return the Y Coordinate of the top of the surface """
        if top is not None:
            return top*self.height
        elif bottom is not None:
            return bottom*self.height - surface.get_height()
        elif centery is not None:
            return centery*self.height - surface.get_height()/2
        else:
            raise Exception("Must provide either top, bottom, or centery argument")
        
    def blit(self, surface, position):
        """ Blit the given surface onto the widget at the given position """
        self.surface.blit(surface, position)
        
    @property
    def width(self):
        """ Return the width of the screen """
        return self.surface.get_width()
        
    @property
    def height(self):
        """ Return the height of the screen """
        return self.surface.get_height()