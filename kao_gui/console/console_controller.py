from kao_gui.controller import Controller
from kao_gui.console.input_processor import InputProcessor
from kao_gui.console.window import Window

class ConsoleController(Controller):
    """ Represents a Controller for the Console UI """
        
    def getWindow(self):
        """ Return the Console Window """
        return Window
        
    def getInputProcessor(self):
        """ Return Input Processor """
        return InputProcessor