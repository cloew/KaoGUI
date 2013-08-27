from kao_gui.console.window import Window

class ConsoleWidget:
    """ Represents a widget for the console """
    
    @property
    def terminal(self):
        """ Return the terminal """
        return Window.terminal
    
    @property
    def window(self):
        """ Return the window """
        return Window
        
    def formatTerminalString(self, string):
        """ Return a formatted terminal string """
        return string.format(t=self.terminal)