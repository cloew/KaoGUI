import pygame

from kao_gui.pygame.icon_builder import IconBuilder
from pygame.locals import *

class PygameWindow:
    """ Represents the Pygame window displayed to the user """
    GAME_SPEED = 60
    
    def __init__(self, width=640, height=480, caption='Pokemon', iconFilename='resources/images/pokeball3.bmp'):
        """ Build the window """
        self.width = width
        self.height = height
        self.screen = None
        
        self.window = self.getWindow(caption, iconFilename)
        self.clock = pygame.time.Clock()
        
    def setScreen(self, screen):
        """ Sets the current Screen Display """
        self.screen = screen
        
    def getWindow(self, caption, iconFilename):
        """ Gets the GUI Window """
        pygame.init()
        builder = IconBuilder(iconFilename)
        pygame.display.set_icon(builder.buildIcon())
        pygame.display.set_caption(caption)
        pygame.mouse.set_visible(0)
        return pygame.display.set_mode((self.width, self.height))
        
    def update(self):
        """ Update the screen """
        self.clock.tick(self.GAME_SPEED)
        self.screen.update()
        self.screen.draw(self)
        self.redraw()
        
    def draw(self, surface, pos):
        """ Draws the surface to the window """
        self.window.blit(surface, pos)
            
    def redraw(self):
        pygame.display.flip()
        
    def clear(self):
        """ Clears the window """
        self.window.fill((255,255,255))
        
    def close(self):
        """ Close the window...? """
   
Window = PygameWindow()