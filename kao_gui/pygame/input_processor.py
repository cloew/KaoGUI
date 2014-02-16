from kao_gui.pygame.quit_event_wrapper import QuitEventWrapper as QuitEvent

class InputProcessor:
    """ Class to process input from Pygane and convert them to game commands """
    
    def __init__(self):
        """ Builds the input processor """
        self.bindings = None
        
    def processInputs(self, functions):
        """ Process inputs to functions """
        commands = self.convertEventToCommand()
        
        for command in commands:
            if command in functions:
                functions[command]()
            elif command[0] in functions and command[1] is PRESSED:
                functions[command[0]]()
        
    def convertEventToCommand(self):
        """ Converts PyGame Events to Game Commands """
        commands = []
        
        for event in pygame.event.get():
            if event.type == QUIT:
                commands.append(QuitEvent)
            elif event.type == KEYUP:
                self.addKeyEvent(commands, event, RELEASED)
            elif event.type == KEYDOWN:
                self.addKeyEvent(commands, event, PRESSED)
        
        return commands
        
    def addKeyEvent(self, commands, event, keyState):
        """ Adds a Key Event to the Commands list """
        if self.bindings is None:
            commands.append((event.key, keyState))
        elif event.key in self.bindings.keyBindings:
            gameAction = self.bindings.keyBindings[event.key]
            commands.append((gameAction, keyState))
        
inputProcessor = InputProcessor()