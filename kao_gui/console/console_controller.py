from kao_gui.controller import Controller
from kao_gui.console.input_processor import InputProcessor
from kao_gui.console.window import GetWindow

from kao_console.ascii import CTRL_Q, ESCAPE

class ConsoleController(Controller):
    """ Represents a Controller for the Console UI """
    
    def __init__(self, screen, commands=None, cancellable=False):
        """ Initialize the controller """
        if commands is None:
            commands = {}
        commands[CTRL_Q] = self.quitToDesktop
        if cancellable:
            commands[ESCAPE] = self.stopRunning
        Controller.__init__(self, screen, commands=commands)
        
    def getWindow(self):
        """ Return the Console Window """
        return GetWindow()
        
    def getInputProcessor(self):
        """ Return Input Processor """
        return InputProcessor