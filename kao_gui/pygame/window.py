from kao_gui.pygame.icon_builder import IconBuilder
from kao_gui.pygame.input_processor import InputProcessor

from pygame.locals import *
import pygame

class PygameWindow:
    """ Represents the Pygame window displayed to the user """
    GAME_SPEED = 60
    
    def __init__(self, width=640, height=480, caption='KaoGUI Pygame Window', iconFilename=None):
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
        if iconFilename is not None:
            self.setIcon(iconFilename)
        pygame.display.set_caption(caption)
        pygame.mouse.set_visible(0)
        return pygame.display.set_mode((self.width, self.height))
        
    def setIcon(self, iconFilename):
        """ Set the Window Icon """
        builder = IconBuilder(iconFilename)
        pygame.display.set_icon(builder.buildIcon())
        
    def draw(self):
        """ Draw the screen """
        self.clock.tick(self.GAME_SPEED)
        self.screen.update()
        surface = self.screen.draw()
        self.window.blit(surface, (0,0))
        self.redraw()
        
    # def draw(self, surface, pos):
        # """ Draws the surface to the window """
        # self.window.blit(surface, pos)
            
    def redraw(self):
        pygame.display.flip()
        
    def clear(self):
        """ Clears the window """
        self.window.fill((255,255,255))
        
    def close(self):
        """ Close the window...? """
   
Window = None

def BuildWindow(width=640, height=480, caption='KaoGUI Pygame Window', iconFilename=None, bindings=None):
    global Window
    Window = PygameWindow(width=width, height=height, caption=caption, iconFilename=iconFilename)
    InputProcessor.bindings = bindings
    return Window
    
def GetWindow():
    """ Return the current window """
    global Window
    return Window