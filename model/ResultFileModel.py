from model.PlottedSignalModel import PlottedSignalModel

class ResultFileModel():
    def __init__(self, name = 'Res File 0')->None:
        '''
        Class that generates the model of a ResultFile object.
        The purpose of this class is to store all the signals
        and related information contained in a result file.
        '''
        # Dictionary with signal names and values
        self.name = name
        self.objectName = 'ResultFileModel'
        
        self.absPath = ''
        self.signals = []
        self.signalNames = []
        self.selectedSignals = []
        
        self.xAxisSignal = PlottedSignalModel()
        
    def RemoveDataFromResultSignals(self)->None:
        '''Delete the data from singals.'''
        for sig in self.signals:
            sig.rawData = []
            sig.scaledData = []
            
    
                
    
        
        
        