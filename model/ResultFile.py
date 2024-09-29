class ResultFile():
    def __init__(self)->None:
        '''
        Class that generates the model of a ResultFile object.
        The purpose of this class is to store all the signals
        and related information contained in a result file.
        '''
        # Dictionary with signal names and values
        self.name = ''
        self.resultNo = 0
        self.absPath = ''
        self.signals = {}