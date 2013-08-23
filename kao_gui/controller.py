
class Controller:
    """ Represents a UI Controller """
    
    def __init__(self, screen, commands={}):
        """ Initialize the controller """
        self.screen = screen
        self.commands = commands
        self.running = False
    
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
            
    def stopRunning(self):
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
        
    def addCommand(self, character, command):
        """ Add the given command to happen on the given character """
        self.commands[character] = command
        