from blessings import Terminal
from contextlib import contextmanager

import sys

class ConsoleWindow(object):
    """ Represents the Console Window displayed to the user """
    
    def __init__(self):
        """ Build the window """
        self.screen = None
        self.terminal = Terminal()
        
        self.write(self.terminal.enter_fullscreen())
        self.write(self.terminal.hide_cursor())
        
    def close(self):
        self.write(self.terminal.exit_fullscreen())
        self.write(self.terminal.normal_cursor())

    @property
    def width(self):
        """ Return the width of the window """
        return self.terminal.width
    
    @property
    def height(self):
        """ Return the height of the window """
        return self.terminal.height
        
    def setScreen(self, screen):
        """ Sets the current Screen Display """
        self.screen = screen
        self.clear()
        
    def update(self):
        """ Update the screen """
        self.screen.update()
        self.screen.draw(self)
        
    def draw(self):
        """ Draw the Screen """
        self.screen.draw()
        
    # def draw(self, text, pos):
        # """ Draws the text to the window """
        # lineNum = pos[1]
        # for line in text:
            # with self.terminal.location(int(pos[0]), int(lineNum)):
                # print line
            # lineNum += 1
        
    def clear(self):
        """ Clears the window """
        print self.terminal.clear()
        
    def write(self, string):
        """ Write the string directly to stdout """
        sys.stdout.write(string)
        
    @contextmanager
    def window(self):
        """ Returns the window """
        yield Window
        Window.close()
        
Window = ConsoleWindow()