from kao_gui.console.console_widget import ConsoleWidget

class ConsoleScreen(ConsoleWidget):
    """ Represents the view for a Consoel Screen """
    
    @property
    def width(self):
        """ Return the width of the window """
        return self.window.width
    
    @property
    def height(self):
        """ Return the height of the window """
        return self.window.height
        
    def drawCenteredText(self, text, size, xRatio, yRatio):
        """ Draws the given text so that it is centered at the given position """
        position = self.getCenteredPosition(size, xRatio, yRatio)
        self.drawAtPosition(text, position)

    def getCenteredPosition(self, size, xRatio, yRatio):
        """ Returns a position that centers the text on the given percentage of the screen """
        centerWidth = xRatio*self.width
        centerHeight = yRatio*self.height
        centerWidth -= size[0]/2
        centerHeight -= size[1]/2
        return centerWidth, centerHeight
        
    def drawAtPosition(self, text, position):
        """ Draws the text to the window """
        column = int(position[0])
        lineNumber = int(position[1])
        
        for line in text:
            with self.terminal.location(column, lineNumber):
                print line
            lineNumber += 1