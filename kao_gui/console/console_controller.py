from kao_gui.controller import Controller
from kao_gui.console.input_processor import InputProcessor
from kao_gui.console.window import Window

from kao_console.ascii import ESCAPE

class ConsoleController(Controller):
    """ Represents a Controller for the Console UI """
    
    def __init__(self, screen, commands=None):
        """ Initialize the controller """
        if commands is None:
            commands = {}
        commands[ESCAPE] = self.stopRunning
        Controller.__init__(self, screen, commands=commands)
        
    def getWindow(self):
        """ Return the Console Window """
        return Window
        
    def getInputProcessor(self):
        """ Return Input Processor """
        return InputProcessor