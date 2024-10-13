from model.SignalModel import Signal

class ResultFileModel():
    def __init__(self)->None:
        '''
        Class that generates the model of a ResultFile object.
        The purpose of this class is to store all the signals
        and related information contained in a result file.
        '''
        # Dictionary with signal names and values
        self.name = ''
        self.indx = 0
        self.absPath = ''
        self.signals = []
        self.signalNames = []
        self.selectedSignals = []
        
    def RemoveDataFromResultSignals(self)->None:
        '''Delete the data from singals.'''
        for sig in self.signals:
            sig.data = []
            
    def LoadResults(self,filePath)->None:
        '''Load results.'''       
        # Read results file
        file = open(filePath,'r')
        lines = file.readlines()
        file.close()
        
        # Create the list of signals
        headerTokens = lines[0].split(',')
        headerTokens = headerTokens[:-1]
        for i, headerToken in enumerate(headerTokens):
            headerToken = headerToken.strip() 
            sigTemp = Signal(headerToken, indx = i)
            self.signals.append(sigTemp)
            self.signalNames.append(headerToken)
        
        # Iterate on the lines - skip the first one
        for line in lines[1:]:
            valueTokens = line.split(',')
            valueTokens = valueTokens[:-1]
            for i, valueStr in enumerate(valueTokens):
                value = float(valueStr) 
                self.signals[i].AppendData(value)