
class SignalCollection():
    """Class that generates a signal collection."""

    # Slots 
    __slots__ = ('collectionName','signalNames', 'data') 
    
    def __init__(self)->None:
        '''Initialize the SignalCollection object.'''

        self.collectionName = ''
        self.signalNames = ''
        self.data
        

    # def SetGearsProfile(self,g1x,g1y,g2x,g2y) -> None:
    #     """ Set the gear profiles for the original and modified configuration. """

    #     # Set the original configuration profile of the gear set 
    #     self.profile1.x = g1x
    #     self.profile1.y = g1y
    #     self.profile2.x = g2x
    #     self.profile2.y = g2y

    #     # Set the modified configuration profile of the gear set 
    #     self.profile1.xMod = g1x
    #     self.profile1.yMod = g1y
    #     self.profile2.xMod = g2x
    #     self.profile2.yMod = g2y

    #     self.SetAxisLimits()
        

    # def SetAxisLimits(self) -> None:
    #     """ Set the minimum and maximum values of the axis. """

    #     if self.profile1.IsEmpty():
    #         self.xMin = 0
    #         self.xMax = 1
    #         self.yMin = 0
    #         self.yMax = 1
    #     else:
    #         self.xMin = min(self.profile2.x)*self.axisScaleFactor
    #         self.xMax = max(self.profile2.x)*self.axisScaleFactor
    #         self.yMin = min(self.profile2.y)*self.axisScaleFactor
    #         self.yMax = max(self.profile2.y)*self.axisScaleFactor

