class SignalModel():
    def __init__(self,
                 name = '',
                 units = '',
                 quantity = '',
                 indexInResFile = 0,
                 scalingFactor = 1)->None:
        '''
        Class that generates the model of a Signal class.
        The purpose of this class is to store all the information 
        related to a signal.
        '''
        # Dictionary with signal names and values
        self.name = name
        self.quantity = quantity
        self.units = units
        self.rawData = []
        self.scaledData = []
        self.indexInResFile = indexInResFile
        self.scalingFactor = scalingFactor
        
    def AddData(self,data)->None:
        '''Add a full list of data to the signal overwriting the data already present.'''
        
    def AppendData(self,data)->None:
        '''Append data to the data already stored in the Signal object.'''
        self.rawData.append(data)
        self.scaledData.append(data*self.scalingFactor)