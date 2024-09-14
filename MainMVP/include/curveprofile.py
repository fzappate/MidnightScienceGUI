import numpy as np


class CurveProfile():
    """Class of objects representing a 2 dimensional profile"""

    # Slots
    __slots__ = ('x','y','xMod','yMod','angDeg','angRad')
    
    def __init__(self,x = 0,y = 0)->None:
        self.x = x
        self.y = y
        self.xMod = x
        self.yMod = y
        self.angDeg = 0
        self.angRad = 0
    
    
    def IsEmpty(self) -> bool:
        """This function check if the curve profile is empty or not"""

        val = False 
        if (not self.x and not self.y):
            val = True
        return val