
class AbsolutePosition:
    """ Represents an Absolute Positioning based on Pixels """
    
    def __init__(self, surface, left=None, right=None, centerx=None,
                                top=None, bottom=None, centery=None):
        """ Initialize the Absolute position """
        self.surface = surface
        self.left = self.normalizeXCoordinate(surface, left, right, centerx)
        self.top = self.normalizeYCoordinate(surface, top, bottom, centery)
        
    def normalizeXCoordinate(self, surface, left, right, centerx):
        """ Normalize and return the X Coordinate of the left of the surface """
        if left is not None:
            return left
        elif right is not None:
            return right - surface.get_width()
        elif centerx is not None:
            return centerx - surface.get_width()/2
        else:
            raise Exception("Must provide either left, right, or centerx argument")
            
    def normalizeYCoordinate(self, surface, top, bottom, centery):
        """ Normalize and return the Y Coordinate of the top of the surface """
        if top is not None:
            return top
        elif bottom is not None:
            return bottom - surface.get_height()
        elif centery is not None:
            return centery - surface.get_height()/2
        else:
            raise Exception("Must provide either top, bottom, or centery argument")