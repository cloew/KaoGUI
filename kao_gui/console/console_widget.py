from kao_gui.console.window import GetWindow

import sys

class ConsoleWidget:
    """ Represents a widget for the console """
    
    @property
    def terminal(self):
        """ Return the terminal """
        return self.window.terminal
    
    @property
    def window(self):
        """ Return the window """
        return GetWindow()
        
    def drawAtPosition(self, text, position):
        """ Draws the text to the window """
        column = int(position[0])
        lineNumber = int(position[1])
        
        for line in text:
            with self.terminal.location(column, lineNumber):
                # print line
                sys.stdout.write(line)
            lineNumber += 1
        
    def formatTerminalString(self, string):
        """ Return a formatted terminal string """
        return string.format(t=self.terminal)