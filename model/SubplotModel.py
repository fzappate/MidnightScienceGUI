class SubplotModel():
    def __init__(self, name = '', subplotNo = 0)->None:
        '''
        Class that generates the model of a Subplot.
        The purpose of this class is to store all the 
        information necessary to draw a subplot.
        '''
        # Dictionary with signal names and values
        self.name = name
        self.subplotNo = subplotNo
        self.xLabel = ''
        self.yLabel = ''
        self.xTick = 0
        self.yTick = 0
        self.grid = 1
        self.xAxis = ''
        self.resultFiles = {}
        self.plottedSignal = {}
        
        
        