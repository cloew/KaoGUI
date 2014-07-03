from kao_gui.controller import Controller
from kao_gui.pygame.input_processor import InputProcessor
from kao_gui.pygame.quit_event_wrapper import QuitEventWrapper as QuitEvent
from kao_gui.pygame.window import GetWindow


class PygameController(Controller):
    """ Represents a Controller for the Pygame UI """
    
    def __init__(self, screen=None, commands=None, cancellable=False, noScreen=False):
        """ Initialize the controller """
        if commands is None:
            commands = {}
        commands[QuitEvent] = self.quitToDesktop
        Controller.__init__(self, screen, commands=commands, noScreen=noScreen)
        
    def getWindow(self):
        """ Return the Console Window """
        return GetWindow()
        
    def getInputProcessor(self):
        """ Return Input Processor """
        return InputProcessor