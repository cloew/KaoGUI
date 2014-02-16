import pygame

from kao_gui.pygame.pygame_helper import load_image
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
        pygame.display.set_icon(self.getIcon(iconFilename))
        pygame.display.set_caption(caption)
        pygame.mouse.set_visible(0)
        return pygame.display.set_mode((self.width, self.height))
        
    def getIcon(self, iconFilename):
        """ Gets the icon """
        icon = pygame.Surface((32,32))
        rawicon = load_image(iconFilename) # must be 32x32, black is transparant
        icon.set_colorkey(rawicon.get_at((0,0)))
        
        for i in range(0,32):
            for j in range(0,32):
                icon.set_at((i,j), rawicon.get_at((i,j)))
        return icon
        
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