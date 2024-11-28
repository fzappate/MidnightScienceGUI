class PlotModel():    
    def __init__(self, name = 'Plot 0')->None:
        '''
        Class that generates the model of a Plot.
        The purpose of this class is to store all the 
        information necessary to draw a series of subplots.
        '''
        # Dictionary with signal names and values
        self.name = name
        self.objectName = 'PlotModel'
        self.leftMargin = 0.1
        self.rightMargin = 0.9
        self.bottomMargin = 0.1
        self.topMargin = 0.9
        
        self.colorPalette = 0
        
        self.canvasColor = ["#ffffff","#666666","#666666"]
        self.plotColor =  ["#ffffff","#666666","#666666"]
        self.toolbarColor = ["#cccccc","#333333","#666666"]
        self.textColor = ["#000000","#ffffff","#6666ff"]
        
        self.noOfSubplots = 0
        self.containedSubplots = []
        
    def AddSubplot(self,subplot):
        '''
        Add subplot model to the plot model.
        '''
        self.containedSubplots.append(subplot)
        self.noOfSubplots = len(self.containedSubplots)
        
    def DeleteSubplot(self,subplotPane):
        '''
        Remove a subplot from the sublpot list.
        '''
        # Remove subplot
        subplotNo = subplotPane.indx
        del self.containedSubplots[subplotNo]
        # Reassign subplot indx
        for ii, subplotTemp in enumerate(self.containedSubplots):
            subplotTemp.indx = ii
            
        self.noOfSubplots = len(self.containedSubplots)

        
        