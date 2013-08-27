from kao_console import getch
from kao_console.ascii import *

class InputProcessor:
    """ Class to process input from the Console and convert them to game commands """
    
    def __init__(self):
        """ Builds the input processor """
        
    def processInput(self, functions):
        """ Process inputs to functions """
        character = getch()
        
        if character in functions:
            functions[character](character)
        elif character < 256 and character > 0 and chr(character) in functions:
            functions[chr(character)](chr(character))
        
InputProcessor = InputProcessor()