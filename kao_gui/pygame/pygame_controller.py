from kao_gui.controller import Controller
from kao_gui.pygame.input_processor import InputProcessor
from kao_gui.pygame.quit_event_wrapper import QuitEventWrapper as QuitEvent
from kao_gui.pygame.window import Window


class PygameController(Controller):
    """ Represents a Controller for the Pygame UI """
    
    def __init__(self, screen, commands=None, cancellable=False):
        """ Initialize the controller """
        if commands is None:
            commands = {}
        commands[QuitEvent] = self.quitToDesktop
        Controller.__init__(self, screen, commands=commands)
        
    def getWindow(self):
        """ Return the Console Window """
        return Window
        
    def getInputProcessor(self):
        """ Return Input Processor """
        return InputProcessor