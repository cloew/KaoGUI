from kao_gui.pygame.pygame_helper import GetTransparentSurface
from kao_gui.pygame.pygame_widget import PygameWidget

class SizedWidget(PygameWidget):
    """ Represents a fixed size widget """
    
    def __init__(self, width, height):
        """ Initialize the sized widget """
        self.width = width
        self.height = height
        
    def buildSurface(self):
        """ Return the surface for the widget """
        return GetTransparentSurface(self.width, self.height)