
class RelativePosition:
    """ Represents a relative position based on percentages """
    
    def __init__(self, value):
        """ Initialize the Relative Postiion """
        self.value = value
        
    def getPosition(self, surface, parent, lowEdge=False, highEdge=False, isCenter=False):
        """ Return the proper lowEdge position """
        if lowEdge is not None:
            return self.value
        elif right is not None:
            return right*self.width - surface.get_width()
        elif centerx is not None:
            return centerx*self.width - surface.get_width()/2
        else:
            raise Exception("Must provide either left, right, or centerx argument")
        
    def normalizeXCoordinate(self, surface, left, right, centerx):
        """ Normalize and return the X Coordinate of the left of the surface """
        if left is not None:
            return left*self.width
        elif right is not None:
            return right*self.width - surface.get_width()
        elif centerx is not None:
            return centerx*self.width - surface.get_width()/2
        else:
            raise Exception("Must provide either left, right, or centerx argument")
            
    def normalizeYCoordinate(self, surface, top, bottom, centery):
        """ Normalize and return the Y Coordinate of the top of the surface """
        if top is not None:
            return top*self.height
        elif bottom is not None:
            return bottom*self.height - surface.get_height()
        elif centery is not None:
            return centery*self.height - surface.get_height()/2
        else:
            raise Exception("Must provide either top, bottom, or centery argument")