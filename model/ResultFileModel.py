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
            sig.rawData = []
            sig.scaledData = []
            
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
            signalTokens = headerToken.split(':')
            name = signalTokens[:-1]
            name = ":".join(name)
            units = signalTokens[-1]
            sigQuantity = self.DetermineSignalQuantity(name,units)
            sigTemp = Signal(name=name,units=units,quantity=sigQuantity,indx = i)
            self.signals.append(sigTemp)
            self.signalNames.append(name)
        
        # Iterate on the lines - skip the first one
        for line in lines[1:]:
            valueTokens = line.split(',')
            valueTokens = valueTokens[:-1]
            for i, valueStr in enumerate(valueTokens):
                value = float(valueStr) 
                self.signals[i].AppendData(value)
                
    def DetermineSignalQuantity(self,name,units)->str:
        '''Take the unit of the signal, and determine its quantity.'''
        if units == 's':
            return 'Time'
        
        elif units == 'm':
            return 'Length'
        
        elif units == 'm^2':
            return 'Area'
        
        elif units == 'm^3':
            return 'Volume'
        
        elif units == 'm^3/s':
            return 'Flow'
        
        elif units == 'Pa':
            return 'Pressure'
        
        elif units == 'Pa*s':
            return 'BulkModulus'
        
        elif units == '-':
            return 'Ratio'        
        
        else:
            print('Units of signal ' + name + ' not found.')
        
        
        