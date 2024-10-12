class PlotModel():    
    def __init__(self)->None:
        '''
        Class that generates the model of a Plot.
        The purpose of this class is to store all the 
        information necessary to draw a series of subplots.
        '''
        # Dictionary with signal names and values
        self.plotName = ''
        self.indx = 0
        self.noOfSubplots = 0
        self.containedSubplots = []
        self.areCollapsed = []
        
    def AddSubplot(self,subplot):
        '''
        Add subplot model to the plot model.
        '''
        self.containedSubplots.append(subplot)
        self.areCollapsed.append(True)
        self.noOfSubplots = len(self.containedSubplots)
        
    def DeleteSubplot(self,subplotPane):
        '''
        Remove a subplot from the sublpot list.
        '''
        # Remove subplot
        subplotNo = subplotPane.indx
        del self.containedSubplots[subplotNo]
        del self.areCollapsed[subplotNo]
        # Reassign subplot indx
        for ii, subplotTemp in enumerate(self.containedSubplots):
            subplotTemp.indx = ii
            
        self.noOfSubplots = len(self.containedSubplots)

        
        