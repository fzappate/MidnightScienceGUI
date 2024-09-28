class PlotModel():
    """
    Class that generates the model of a Plot.
    The purpose of this class is to store all the information necessary to draw a series of subplots.
    """
    
    def __init__(self)->None:
        # Dictionary with signal names and values
        self.plotName = ''
        self.noOfSubplots = 0
        self.containedSubplots = []
        
    def AddSubplot(self,subplot):
        '''
        Add subplot model to the plot model.
        '''
        self.containedSubplots.append(subplot)
        self.noOfSubplots = len(self.containedSubplots)
        