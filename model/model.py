from model.settings import Settings
from model.signalcollection import SignalCollection
from model.PlotModel import PlotModel

class Model():
    '''Model class containing all the submodel of the software.'''

    def __init__(self)->None:
        '''Initialize the model class.'''

        self.settings = Settings()
        self.results = {}
        self.plotData = SignalCollection()
        self.plotModel = PlotModel()
        
        



        