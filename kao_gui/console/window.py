from blessings import Terminal

class ConsoleWindow(object):
    """ Represents the Console Window displayed to the user """
    
    def __init__(self):
        """ Build the window """
        self.screen = None
        self.terminal = Terminal()
        
        print self.terminal.enter_fullscreen()
        print self.terminal.hide_cursor()
        
    def close(self):
        print self.terminal.exit_fullscreen()
        print self.terminal.normal_cursor()

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
        #print self.terminal.clear()
        
Window = ConsoleWindow()