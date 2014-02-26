from kao_gui.console.window import GetWindow

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
        
    def formatTerminalString(self, string):
        """ Return a formatted terminal string """
        return string.format(t=self.terminal)