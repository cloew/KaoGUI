from kao_gui.pygame.pygame_helper import load_image
from kao_gui.pygame.pygame_widget import PygameWidget

class Image(PygameWidget):
    """ Represents an image displayed via Pygame """
    
    def __init__(self, imageFilename):
        """ Initialize the Image by loading the Image File given """
        self.image = load_image(imageFilename)
        
    def buildSurface(self):
        """ Build the surface to display """
        return self.image