class SubplotModel():
    
    def __init__(self, name = '', subplotNo = 0)->None:
        """
        Class that generates the model of a Subplot.
        The purpose of this class is to store all the information necessary to draw a subplot.
        """
        # Dictionary with signal names and values
        self.subplotName = name
        self.subplotNo = subplotNo
        
        
        