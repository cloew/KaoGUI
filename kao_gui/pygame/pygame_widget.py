
class PygameWidget:
    """ Represents a Widgetrendered using Pygame """
    
    def __init__(self):
        """ Initialize the Pygame Widget """
        
    def update(self):
        """ Update the screen.
            Overridde in sub-class """
        
    def buildSurface(self):
        """ Build the surface to use when drawing """
        return None
        
    def draw(self):
        """ Draw the widget and return the surface """
        self.update()
        self.surface = self.buildSurface()
        self.drawSurface()
        return self.surface
        
    def drawSurface(self):
        """ Draw the screen on the given surface.
            Override in sub-class """
        
    def drawOnSurface(self, surface, left=None, right=None, centerx=None,
                                     top=None, bottom=None, centery=None, isRelative=True):
        """ Draw the given surface onto this widget at the position specified """
        leftPosition = self.normalizeXCoordinate(surface, left, right, centerx, isRelative)
        topPosition = self.normalizeYCoordinate(surface, top, bottom, centery, isRelative)
        self.blit(surface, (leftPosition, topPosition))
        
    def normalizeXCoordinate(self, surface, left, right, centerx, isRelative):
        """ Normalize and return the X Coordinate of the left of the surface """
        if left is not None:
            return self.transfromRelativeValue(left, self.width, isRelative)
        elif right is not None:
            return self.transfromRelativeValue(right, self.width, isRelative) - surface.get_width()
        elif centerx is not None:
            return self.transfromRelativeValue(centerx, self.width, isRelative) - surface.get_width()/2
        else:
            raise Exception("Must provide either left, right, or centerx argument")
            
    def normalizeYCoordinate(self, surface, top, bottom, centery, isRelative):
        """ Normalize and return the Y Coordinate of the top of the surface """
        if top is not None:
            return self.transfromRelativeValue(top, self.height, isRelative)
        elif bottom is not None:
            return self.transfromRelativeValue(bottom, self.height, isRelative) - surface.get_height()
        elif centery is not None:
            return self.transfromRelativeValue(centery, self.height, isRelative) - surface.get_height()/2
        else:
            raise Exception("Must provide either top, bottom, or centery argument")
            
    def transfromRelativeValue(self, value, modifier, isRelative):
        """ Transform a relative percent value into a pixel value, if needed """
        newValue = value
        if isRelative:
            newValue = value*modifier
        return newValue
        
    def blit(self, surface, position):
        """ Blit the given surface onto the widget at the given position """
        self.surface.blit(surface, position)
        
    @property
    def width(self):
        """ Return the width of the screen """
        return self.surface.get_width()
        
    @property
    def height(self):
        """ Return the height of the screen """
        return self.surface.get_height()