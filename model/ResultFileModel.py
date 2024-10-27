from model.SignalModel import SignalModel

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
        self.objectName = 'ResultFileModel'
        
        self.absPath = ''
        self.signals = []
        self.signalNames = []
        self.selectedSignals = []
        self.selectedSignalsIndx = []
        
    def RemoveDataFromResultSignals(self)->None:
        '''Delete the data from singals.'''
        for sig in self.signals:
            sig.rawData = []
            sig.scaledData = []
            
    
                
    
        
        
        