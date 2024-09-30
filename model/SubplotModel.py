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
        self.resultFiles = []
        self.plottedSignal = []
        
        self.xLabel = ''
        self.yLabel = ''
        self.xTick = 0
        self.yTick = 0
        self.grid = 1
        self.xAxis = ''
        
    def AddResultFile(self,resultFileModel):
        '''Add ResultFileModel to SubplotModel.'''
        self.resultFiles.append(resultFileModel)
        self.noOfResFile = len(self.resultFiles)
        
        
        