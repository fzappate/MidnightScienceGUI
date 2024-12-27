class SubplotModel():
    def __init__(self)->None:
        '''
        Class that generates the model of a Subplot.
        The purpose of this class is to store all the 
        information necessary to draw a subplot.
        '''
        # Dictionary with signal names and values
        self.name = ''
        self.indx = 0
        self.noOfResFile = 0
        self.isCollapsed = 1
        self.containedResultFiles = []
        
        self.xLabel = ''
        self.yLabel = ''
        self.xLim = [0.0, 1.0]
        self.yLim = [0.0, 1.0]
        self.xLimUser = [0.0, 1.0]
        self.yLimUser = [0.0, 1.0]
        self.useUserLim = 0
        self.xTick = 0.2
        self.yTick = 0.2
        self.xTickUser = 0.2
        self.yTickUser = 0.2
        self.useUserTicks = 0
        self.setGrid = 1
        
        self.colorCounter = 0
        
    def AddResultFile(self,resultFileModel):
        '''Add ResultFileModel to SubplotModel.'''
        self.containedResultFiles.append(resultFileModel)
        self.noOfResFile = len(self.containedResultFiles)
        
    def DeleteResultFile(self,resultFilePane):
        '''Remove a ResultFileModel from SubplotModel.'''
        # Remove result file
        resultFileNo = resultFilePane.index
        del self.containedResultFiles[resultFileNo]
        
        # Reassign result files indx
        for ii, resFileTemp in enumerate(self.containedResultFiles):
            resFileTemp.index = ii
            
        self.noOfResFile = len(self.containedResultFiles)
        
        
        
        