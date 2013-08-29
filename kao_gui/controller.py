import sys

class Controller:
    """ Represents a UI Controller """
    
    def __init__(self, screen, commands=None):
        """ Initialize the controller """
        self.screen = screen
        if commands is None:
            commands = {}
        self.commands = commands
        self.running = False
        self.parent = None
    
    def run(self):
        """  """
        self.running = True
        
        while self.isRunning():
            self.performGameCycle()
            
            if self.isRunning():
                window = self.getWindow()
                window.setScreen(self.screen)
                window.draw()
                
                self.handleInput()
                
    def getWindow(self):
        """ Returns the Window for the Controller to interact with """
        
    def getInputProcessor(self):
        """ Returns the Input Processor for the controller """
            
    def stopRunning(self, event=None):
        """ Stop running this controller """
        self.running = False
        
    def isRunning(self):
        """ Returns if the controller is still running """
        return self.running
        
    def performGameCycle(self):
        """ Perform a Game Cycle Event """
        
    def handleInput(self):
        """ Handle User Input """
        self.getInputProcessor().processInput(self.commands)
        
    def addCommand(self, event, command):
        """ Add the given command to happen on the given event """
        self.commands[event] = command
        
    def addCommands(self, events, command):
        """ Add the given command to happen on the given events """
        for event in events:
            self.commands[event] = command
            
    def runController(self, controller):
        """ Runs the next controller """
        if self.isRunning():
            controller.parent = self
            controller.run()
        
    def quitToDesktop(self, event=None):
        """ Quit the application entirely """
        self.stopRunning()
        if self.parent is not None:
            self.parent.quitToDesktop()