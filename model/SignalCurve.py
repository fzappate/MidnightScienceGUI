from model.Signal import Signal

class SignalCurve(Signal):
    def __init__(self)->None:
        '''
        Class that generates the model of a SignalCurve class.
        The purpose of this class is to store all the information 
        related to a signal and the info needed to properly plot it.
        '''
        # Dictionary with signal names and values
        self.color=[1,1,1]
        self.thickness=0
        self.marker=''
        self.linestyle=''