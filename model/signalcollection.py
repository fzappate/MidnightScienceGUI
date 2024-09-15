
class SignalCollection():
    """Class that generates a signal collection."""

    # Slots 
    __slots__ = ('results','units') 
    
    def __init__(self)->None:
        '''Initialize the SignalCollection object.'''

        # Dictionary with signal names and values
        self.results = {}
        # List of units
        self.units = []
        
