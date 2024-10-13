class Signal():
    def __init__(self,
                 name = '',
                 units = '',
                 quantity = '',
                 indx = 0)->None:
        '''
        Class that generates the model of a Signal class.
        The purpose of this class is to store all the information 
        related to a signal.
        '''
        # Dictionary with signal names and values
        self.name = name
        self.indx = indx
        self.quantity = quantity
        self.unit = units
        self.rawData = []
        self.scalingFactor = 1
        self.scaledData = []
        
    def AddData(self,data)->None:
        '''Add a full list of data to the signal overwriting the data already present.'''
        
    def AppendData(self,data)->None:
        '''Append data to the data already stored in the Signal object.'''
        self.rawData.append(data)
        self.scaledData.append(data*self.scalingFactor)