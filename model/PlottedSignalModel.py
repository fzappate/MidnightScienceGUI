from model.SignalModel import SignalModel

class PlottedSignalModel(SignalModel):
    def __init__(self,
                 width = 1,
                 style = '-',
                 marker = 'None',
                 color = '#000000',
                 label = '',
                 *args,
                 **kwargs)->None:
        '''
        Class that generates the model of a PlottedSignals object.
        The purpose of this class is to store all the signals
        and related information contained in a subplot.
        '''
        super().__init__(*args,**kwargs)
        
        self.objectName = 'PlottedSignal'
        self.width = width
        self.style = style
        self.marker = marker
        self.color = color
        self.label = label
        
    def CopySignalProperties(self,signal)->None:
        '''Take a signal of the Signal class, copy its properties into 
        a PlottedSignal instance.'''
        self.name = signal.name
        self.indexInResFile = signal.indexInResFile
        self.label = signal.name
        self.units = signal.units
        self.rawData = signal.rawData
        self.scaledData = signal.scaledData
        self.scalingFactor = signal.scalingFactor 
        self.quantity = signal.quantity
        