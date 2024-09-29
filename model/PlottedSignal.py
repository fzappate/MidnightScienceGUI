class PlottedSignals():
    def __init__(self)->None:
        '''
        Class that generates the model of a PlottedSignals object.
        The purpose of this class is to store all the signals
        and related information contained in a subplot.
        '''
        # Dictionary with signal names and values
        self.signals = {}